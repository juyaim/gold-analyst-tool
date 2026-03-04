import webbrowser

# 1. 市場報價與技術面
market_links = {
    "Investing_Gold": "https://www.investing.com/currencies/xau-usd",
    "TradingView_Chart": "https://www.tradingview.com/symbols/XAUUSD/",
    "Market_Focus": "重點：技術摘要、情緒指標與趨勢線"
}

# 2. 總體經濟與聯準會
macro_links = {
    "CME_FedWatch": "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html",
    "FRED_TIPS": "https://fred.stlouisfed.org/series/REAINTRATREARAT10Y",
    "Macro_Focus": "重點：聯準會降息預期與 10 年期實際利率"
}

# 3. 權威報告與數據指標 (包含金銀比、比特幣黃金比)
data_links = {
    "World_Gold_Council": "https://www.gold.org/goldhub",
    "Kitco_News": "https://www.kitco.com/news/",
    "Report_Focus": "重點：央行動態、實體供需與交易所庫存",
    "Gold_WTI_Ratio": "https://www.macromicro.me/series/3830/wti-gold-ratio",
    "Gold_Silver_Ratio": "https://www.macromicro.me/charts/17565/Gold-Silver-Ratio",
    "BTC_Gold_Ratio": "https://milkroad.com/bitcoin-gold-ratio/",
    "Ratio_Focus": "重點：資金在能源、貴金屬與虛擬資產間的移動"
}

def open_all_analysis():
    print("正在為『gold分析師』開啟所有關鍵數據網頁，包含最新的比特幣/黃金比例...")
    # 合併所有字典進行顯示
    all_links = {**market_links, **macro_links, **data_links}
    for name, content in all_links.items():
        print(f"分析項目: {name} -> {content}")

if __name__ == "__main__":
    open_all_analysis()
