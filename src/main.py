# main.py
import sys
import pandas as pd
import dataframe_image as dfi

# データファイルのパスを指定
path = './data.xlsx'

if '--input' in sys.argv:
    path = sys.argv[sys.argv.index('--input') + 1]

out_path = './output.png'
if '--output' in sys.argv:
    out_path = sys.argv[sys.argv.index('--output') + 1]




# データファイルを読み込み
df = pd.read_excel(path)


df = df.reset_index(drop=True)

# カテゴリ別にソートする
group = ["date"]
if '--sort-type' in sys.argv:
    group = [sys.argv[sys.argv.index("--sort-type") + 1]]

mean_df = df.groupby(group, as_index=False)["amount"].mean()
sum_df = df.groupby(group, as_index=False)["amount"].sum()

df.drop(df.index, inplace=True)

df["sum"] = sum_df["amount"]
df["average"] = mean_df["amount"].round(2)


output_df = df[[]]

if group == ["date"]:
    df["date"] = sum_df["date"]
    output_df = df[["date", "sum", "average"]]
else:
    df["category"] = sum_df["category"]
    output_df = df[["category", "sum", "average"]]




centences = output_df.head()


# データファイルを出力
print(centences)


dfi.export(
    output_df,
    out_path,
    fontsize=14,
    table_conversion="matplotlib"
    )