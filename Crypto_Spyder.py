# Crypto_Spyder
Crypto_Spyder


from finlab_crypto import crawler
import pandas as pd
import os

# 獲取BTC數據
#  修改貨幣種類 貨幣幣種：“1m”、“5m”、“15m”、“30m”、“1h”、“2h”、“4h”、“1d”）  6h,8h,3d,1w無法使用
BTC = crawler.get_all_binance('BTCUSDT', '1d')

# 設定儲存路徑和檔案名稱
folder_path = r"C:\Users\j_171\OneDrive\Desktop\Crypto_data"

os.makedirs(folder_path, exist_ok=True)  # 如果目錄不存在，則自動建立

# 建立一個 DataFrame
data = BTC
df = pd.DataFrame(data)

# 確保index是日期格式
df.index = pd.to_datetime(df.index)

# 取得起始日期和結束日期
symbol = 'BTCUSDT'  # 這裡應該是加密貨幣的名稱
start = df.index.min().strftime('%Y%m%d')
end = df.index.max().strftime('%Y%m%d')

# 設定檔案名稱
filename = f"{symbol}_{start}-{end}.csv"

# 建立完整的檔案路徑
file_path = os.path.join(folder_path, filename)

# 將 DataFrame 存成 CSV 檔案
df.to_csv(file_path, index=True)

print(f"CSV 檔案已成功儲存！")
