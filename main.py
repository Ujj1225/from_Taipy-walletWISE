from taipy import Gui

title = "walletWISE 🤑"

hover_text = """🚀 Track, Thrive, Triumph. #MoneyMastery"""

income = ""
expenses = ""

path = "wallet_calc.gif"


def generate():
    print("Good Work!")


def generate_income(state):
    print(state.income)
    with open("income.txt", "a") as f:
        f.write(f"{state.income},")


def generate_expenses(state):
    print(state.expenses)
    with open("expenses.txt", "a") as f:
        f.write(f"{state.expenses,}")


page = """
<|text-center |
<|{title}|hover_text="{hover_text}"|text|>
|>

<|text-right|toggle|theme|>\n<center>\n<|navbar|>\n</center>

<|text-center|
<|{path}|image|>
INCOME: <|{income}|input|>
<|Add to Income!|button|on_action=generate_income|>
EXPENDITURE: <|{expenses}|input|>
<|Add to Expenses!|button|on_action=generate_expenses|>
|>

<|text-center|
<|Get Insights|button|on_action=generate|>
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
