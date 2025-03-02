import sys
import markdown

def convert_markdown_to_html(input_file, output_file):
    """Markdown を HTML に変換"""
    try:
        print(f"📂 入力ファイル: {input_file}")  # デバッグ用
        print(f"📂 出力ファイル: {output_file}")  # デバッグ用
        
        with open(input_file, 'r', encoding='utf-8') as infile:
            md_content = infile.read()
            print(f"📜 読み込んだ Markdown: {md_content}")  # デバッグ用
        
        html_content = markdown.markdown(md_content)
        print(f"🌐 変換後の HTML: {html_content}")  # デバッグ用

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(html_content)
        
        print(f"✅ {output_file} に HTML を出力しました！")
    
    except FileNotFoundError:
        print("❌ 入力ファイルが見つかりません！")
    except Exception as e:
        print(f"❌ エラー: {e}")

# コマンドライン引数の処理
if len(sys.argv) != 4 or sys.argv[1] != "markdown":
    print("❌ 正しいコマンドを指定してください！（例: python3 file_converter.py markdown input.md output.html）")
    print("sys.argv の内容:", sys.argv)
    
    sys.exit(1)

input_path = sys.argv[2]
output_path = sys.argv[3]

convert_markdown_to_html(input_path, output_path)
