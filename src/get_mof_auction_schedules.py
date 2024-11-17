import requests
from bs4 import BeautifulSoup
import pandas as pd

# 11月のページURL
url = "https://www.mof.go.jp/jgbs/auction/calendar/2411.htm"

# ページを取得
response = requests.get(url)
response.encoding = response.apparent_encoding  # 文字エンコーディングを自動検出

# BeautifulSoupでHTML解析
soup = BeautifulSoup(response.text, 'html.parser')

# テーブルを取得
table = soup.find("table")

# テーブルが見つからない場合の処理
if not table:
    print("テーブルが見つかりませんでした。")
else:
    # テーブルデータの抽出
    schedule = []
    rows = table.find_all("tr")

    for row in rows[1:]:  # ヘッダー行をスキップ
        columns = row.find_all("td")
        if len(columns) >= 2:
            date_str = columns[0].get_text(strip=True)
            bond_type = columns[1].get_text(strip=True)
            schedule.append([date_str, bond_type])

    # DataFrameに格納
    df = pd.DataFrame(schedule, columns=["日付", "入札対象"])

    # DataFrameの表示
    print(df)