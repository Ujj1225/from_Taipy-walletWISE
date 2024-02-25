from taipy import Gui

title = "walletWISE"


hover_text = "Your savvy sidekick in the finance game.\n🚀 Track, Thrive, Triumph.\n#MoneyMastery"

page = """
<|text-center |
<|{title}|hover_text="{hover_text}"|>
|>
"""

if __name__ == "__main__":
    app = Gui(page)
    app.run(use_reloader=True)
