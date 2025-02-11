# JP2pdf

JP2pdf は JP2/JPEG 2000 画像ファイルをPDFに変換するシンプルな Python ツールです。単一のJP2ファイルまたはディレクトリ内の複数のJP2ファイルを処理できます。

## 特徴

- 単一のJP2ファイルまたはディレクトリ内の全JP2ファイルを処理
- JP2からPDFへの直接変換による高品質な出力
- シンプルなコマンドライン操作
- 詳細なログ出力

## インストール

依存パッケージのインストール：
```bash
pip install -r requirements.txt
```

## 使用方法

### 基本的な使用方法

単一のJP2ファイルを変換：
```bash
python jp2pdf.py path/to/image.jp2
```

ディレクトリ内の全JP2ファイルを変換：
```bash
python jp2pdf.py path/to/directory
```

出力ファイルを指定して変換：
```bash
python jp2pdf.py path/to/image.jp2 -o output.pdf
```

### コマンドラインオプション

- `input_path`: JP2ファイルまたはJP2ファイルが存在するディレクトリのパス（必須）
- `-o, --output`: 出力するPDFファイルのパス（オプション、デフォルト：input_path.pdf）

## 動作要件

- Python 3.6以上
- PyMuPDF (fitz)

## ライセンス

MIT License

## 作者

wabisuke
