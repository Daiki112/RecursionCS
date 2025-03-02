import sys
import os

print(f"sys.argv: {sys.argv}")

def reverse(inputpath, outputpath):
    """ ファイルの内容を逆順にして保存 """
    try:
        with open(inputpath, 'r', encoding='utf-8') as infile:
            content = infile.read()[::-1]  # 文字列を反転
        with open(outputpath, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        print(f"✅ {outputpath} に内容を反転して保存しました！")
    except FileNotFoundError:
        print("❌ 入力ファイルが見つかりません！")
    except Exception as e:
        print(f"❌ エラー: {e}")

def copy(inputpath, outputpath):
    """ ファイルをコピー """
    try:
        with open(inputpath, 'r', encoding='utf-8') as infile:
            content = infile.read()
        with open(outputpath, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        print(f"✅ {outputpath} にコピーしました！")
    except FileNotFoundError:
        print("❌ 入力ファイルが見つかりません！")
    except Exception as e:
        print(f"❌ エラー: {e}")

def duplicate_contents(inputpath, n):
    """ ファイルの内容を n 回繰り返して書き込む """
    try:
        n = int(n)
        with open(inputpath, 'r+', encoding='utf-8') as file:
            content = file.read()
            file.write(content * n)
        print(f"✅ {inputpath} に内容を {n} 回複製しました！")
    except ValueError:
        print("❌ n は整数で入力してください！")
    except FileNotFoundError:
        print("❌ 入力ファイルが見つかりません！")
    except Exception as e:
        print(f"❌ エラー: {e}")

def replace_string(inputpath, needle, newstring):
    """ ファイル内の特定の文字列を置き換える """
    try:
        with open(inputpath, 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace(needle, newstring)
        with open(inputpath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✅ {inputpath} 内の '{needle}' を '{newstring}' に置き換えました！")
    except FileNotFoundError:
        print("❌ 入力ファイルが見つかりません！")
    except Exception as e:
        print(f"❌ エラー: {e}")

# コマンドライン引数の処理
if len(sys.argv) < 2:
    print("❌ コマンドを指定してください！（reverse, copy, duplicate-contents, replace-string）")
    sys.exit(1)

command = sys.argv[1]

if command == "reverse" and len(sys.argv) == 4:
    reverse(sys.argv[2], sys.argv[3])
elif command == "copy" and len(sys.argv) == 4:
    copy(sys.argv[2], sys.argv[3])
elif command == "duplicate-contents" and len(sys.argv) == 4:
    duplicate_contents(sys.argv[2], sys.argv[3])
elif command == "replace-string" and len(sys.argv) == 5:
    replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
else:
    print("❌ 無効なコマンドまたは引数の数が間違っています！")
