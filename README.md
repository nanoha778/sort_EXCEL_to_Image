## Excel集計ツール

- Excelファイルを入力として読み込み
- 日付またはカテゴリごとに合計・平均を算出
- 結果をPNG画像として出力

### 実行例
python main.py --input data.xlsx --output result.png --sort-type date

### 実行引数
--input 入力元エクセルファイル
--output 出力先画像ファイル
--sort-type ソートする対象(date, category)