import random

n = int(input("最小値 n を入力: "))
m = int(input("最大値 m を入力: "))

if n > m:
    print("エラー: n は m 以下でなければなりません")
else:
    target = random.randint(n, m)
    attempts = m - n + 1  # 試行回数の上限

    print(f"{n} から {m} の間の数字を当ててください！")

    for i in range(attempts):
        guess = int(input(f"{i+1} 回目の予想: "))

        if guess < target:
            print("もっと大きいです！")
        elif guess > target:
            print("もっと小さいです！")
        else:
            print("正解！🎉")
            break
    else:
        print(f"残念！正解は {target} でした。")
