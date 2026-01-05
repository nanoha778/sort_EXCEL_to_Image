# sort_EXCEL_to_Image

Excel ファイルを読み込み、指定した条件で集計し、  
結果を **画像（PNG）として出力**する Python ツールです。

業務でよくある  
「Excel を集計して、見やすい形で共有したい」  
という用途を想定しています。

---

## 機能

- Excel（.xlsx）ファイルの読み込み
- 日付 or カテゴリごとの集計
- 合計・平均の算出
- 集計結果を PNG 画像として出力
- CLI（コマンドライン）操作対応

---

## 使用引数

- --input
入力元のエクセルファイルパス

- --output
出力先の画像ファイルパス

- --sort-type
category または date
---

## 使用技術

- Python 3.x
- pandas
- dataframe_image

---

## インストール

```bash
pip install pandas dataframe_image
