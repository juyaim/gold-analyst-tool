import webbrowser

# 1. 市場報價與技術面
market_links = {
    "Investing_Gold": "https://www.investing.com/currencies/xau-usd",
    "TradingView_Chart": "https://www.tradingview.com/symbols/XAUUSD/"
}

# 2. 總體經濟與聯準會
macro_links = {
    "CME_FedWatch": "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html",
    "FRED_TIPS": "https://fred.stlouisfed.org/series/REAINTRATREARAT10Y"
}

# 3. 權威報告與數據指標
data_links = {
    "World_Gold_Council": "https://www.gold.org/goldhub",
    "Kitco_News": "https://www.kitco.com/news/",
    "Gold_WTI_Ratio": "https://www.macromicro.me/series/3830/wti-gold-ratio",
    "Gold_Silver_Ratio": "https://www.macromicro.me/charts/17565/Gold-Silver-Ratio"
}

def open_all_analysis():
    print("正在為『gold分析師』開啟所有關鍵數據網頁...")
    # 這裡可以根據需要執行網頁開啟或後續的數據抓取邏輯
    for name, url in {**market_links, **macro_links, **data_links}.items():
        print(f"準備分析: {name}")

if __name__ == "__main__":
    open_all_analysis()
