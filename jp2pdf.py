"""JP2画像ファイルをPDFに変換するモジュール（PyMuPDF使用）"""
import fitz
from pathlib import Path
import sys
import traceback
import argparse

def create_pdf_from_jp2_files(input_path, output_pdf_path=None):
    """JP2ファイルを読み込んでPDFファイルにまとめる.

    Args:
        input_path (str): JP2ファイルまたはJP2ファイルが存在するディレクトリのパス
        output_pdf_path (str, optional): 出力するPDFファイルのパス。
            Noneの場合は入力パスに基づいて生成

    Returns:
        None
    """
    print(f"システムのファイルシステムエンコーディング: {sys.getfilesystemencoding()}")

    try:
        input_path = Path(input_path).resolve()

        # 入力パスの処理
        if input_path.is_file():
            if input_path.suffix.lower() != '.jp2':
                print("エラー: 指定されたファイルはJP2形式ではありません。")
                return
            jp2_files = [input_path]
            if output_pdf_path is None:
                output_pdf_path = f"{input_path}.pdf"
        else:
            jp2_files = sorted(input_path.glob('*.jp2'))
            if output_pdf_path is None:
                output_pdf_path = f"{input_path.name}.pdf"

        print(f"処理するパス: {input_path}")
        print(f"出力PDFファイル: {output_pdf_path}")

        if not jp2_files:
            print("JP2ファイルが見つかりませんでした。")
            return

        print(f"見つかったJP2ファイル数: {len(jp2_files)}")

        # 新しいPDFドキュメントを作成
        pdf_doc = fitz.open()

        for jp2_file in jp2_files:
            try:
                print(f"\n{'='*50}")
                print(f"処理中のファイル: {jp2_file.name}")

                if not jp2_file.exists():
                    print(f"エラー: ファイルが存在しません: {jp2_file}")
                    continue

                # JP2画像からPDFページを作成
                img_doc = fitz.open(jp2_file)
                pdfbytes = img_doc.convert_to_pdf()
                img_pdf = fitz.open("pdf", pdfbytes)
                
                # PDFドキュメントにページを追加
                pdf_doc.insert_pdf(img_pdf)
                
                # 一時的なPDFをクローズ
                img_pdf.close()
                img_doc.close()

                print(f"ファイル {jp2_file.name} を正常に処理しました。")

            except Exception as e:
                print(f"エラー: {jp2_file.name} の処理中にエラーが発生しました。")
                print(f"エラー種類: {type(e).__name__}")
                print(f"エラー内容: {str(e)}")
                print("詳細なエラー情報:")
                traceback.print_exc()
                continue

        # PDFを保存
        pdf_doc.save(output_pdf_path)
        pdf_doc.close()
        print(f"\nPDFファイルを保存しました: {output_pdf_path}")

    except Exception as e:
        print("処理中に予期せぬエラーが発生しました。")
        print(f"エラー種類: {type(e).__name__}")
        print(f"エラー内容: {str(e)}")
        traceback.print_exc()

def main():
    """メイン関数."""
    parser = argparse.ArgumentParser(description='JP2ファイルをPDFに変換するプログラム')
    parser.add_argument(
        'input_path',
        help='JP2ファイルまたはJP2ファイルが存在するディレクトリのパス'
    )
    parser.add_argument(
        '-o',
        '--output',
        help='出力するPDFファイルのパス (デフォルト: 入力名.pdf)'
    )

    args = parser.parse_args()
    create_pdf_from_jp2_files(args.input_path, args.output)

if __name__ == "__main__":
    main()