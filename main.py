from taipy import Gui

title = "walletWISE 🤑"

hover_text = """
🚀 Track, Thrive, Triumph.
#MoneyMastery"""

page = """
<|text-center |
<|{title}|hover_text="{hover_text}"|text|>
|>
"""

if __name__ == "__main__":
    app = Gui(page)
    app.run(
        title="walletWISE",
        watermark="Balance your revenue and expenses!",
        favicon="wallet_wise.gif",
        use_reloader=True,
    )
