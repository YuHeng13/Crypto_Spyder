

from finlab_crypto import crawler
import pandas as pd
import os

# 定義貨幣對列表
# 一次爬不同的貨幣種類  可增加
symbols = ['BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'LTCUSDT']  # 這裡可以根據需要修改

# 設定主儲存路徑  路徑自行設定
folder_path = r"C:\Users\"
os.makedirs(folder_path, exist_ok=True)  # 如果目錄不存在，則自動建立

# 迴圈處理每一個貨幣  新增分類子目錄
for symbol in symbols:
    # 為每個貨幣對建立子資料夾
    symbol_folder_path = os.path.join(folder_path, symbol)
    os.makedirs(symbol_folder_path, exist_ok=True)  # 如果該子資料夾不存在，則自動建立

    # 爬取資料
    data = crawler.get_all_binance(symbol, '1d')

    # 建立 DataFrame
    df = pd.DataFrame(data)

    # 確保 index 是日期格式
    df.index = pd.to_datetime(df.index)

    # 取得起始日期和結束日期
    start = df.index.min().strftime('%Y%m%d')
    end = df.index.max().strftime('%Y%m%d')

    # 設定檔案名稱
    filename = f"{symbol}_{start}-{end}.csv"

    # 建立完整的檔案路徑，將檔案儲存到該貨幣對的子資料夾
    file_path = os.path.join(symbol_folder_path, filename)

    # 將 DataFrame 存成 CSV 檔案
    df.to_csv(file_path, index=True)

    print(f"{symbol} 的 CSV 檔案已成功儲存於 {symbol_folder_path}！")
