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

## 使用技術

- Python 3.x
- pandas
- dataframe_image

---

## インストール

```bash
pip install pandas dataframe_image
```

---

## 使い方

基本実行（日付ごとに集計）
python main.py --input data.xlsx --output result.png

カテゴリごとに集計
python main.py --input data.xlsx --output result.png --sort-type category

---

## 入力データ形式（例）

```
date	category	amount
2026-01-01	A	1200
2026-01-02	B	700
```
date : 日付

category : カテゴリ名

amount : 数値データ（集計対象）

---

## 出力例

出力される画像には以下の情報が含まれます。

日付	合計	平均
2026-01-01	2200	733.33
2026-01-02	2900	966.67

※ 実際の出力は PNG 画像です。

---

## 想定ユースケース

Excel 手作業集計の自動化

レポート用画像の生成

定期業務（売上・ログ・計測値など）の可視化

Python を使った業務効率化のサンプル

---

## 注意事項

入力 Excel の列名は固定です
(date, category, amount)

数値以外が amount 列に含まれる場合、正しく集計されない可能性があります

---

## ライセンス

MIT License