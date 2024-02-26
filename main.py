from taipy import Gui
from dotenv import load_dotenv

load_dotenv()

import os
import google.generativeai as genai

# Configuration for GenAI
genai.configure(api_key=os.getenv("API_KEY"))

title = "walletWISE 🤑"

hover_text = """🚀 Track, Thrive, Triumph. #MoneyMastery"""

income = ""
expenses = ""

income_sector = ""
expenses_sector = ""

path = "wallet_calc.gif"

source_of_income = ["salary", "dividend", "business_revenue", "tax_rebate", "others"]
source_of_expenses = ["Fooding", "Clothing", "Education", "Health", "Entertainment", "Misc"]


# loading Gemini Pro model
model = genai.GenerativeModel("gemini-pro")


# Generating content using the model
def generate():
    response = model.generate_content(["Create a financial Saving plan for the month"])
    print(response.text)


def generate_income(state):
    print(state.income)
    if state.income != "" and state.income_sector != "":
        with open("income.txt", "a") as f:
            f.write(f"{state.income_sector}:{state.income},")


def generate_expenses(state):
    print(state.expenses)
    if state.expenses != "" and state.expenses_sector != "":
        with open("expenses.txt", "a") as f:
            f.write(f"{state.expenses_sector}:{state.expenses},")


page = """
<|text-center |
<|{title}|hover_text="{hover_text}"|text|>
|>

<|text-right|toggle|theme|>\n<center>\n<|navbar|>\n</center>

<|text-center|
<|{path}|image|>


INCOME: <|{income}|input|>
<|text-center|

<|1 1|layout|

### Choose **Sector**{: .color-primary}!    

<|{income_sector}|selector|lov={source_of_income}|dropdown|on_change=update_income|>

|>
<br />
<|Add to Income!|button|on_action=generate_income|>


EXPENDITURE: <|{expenses}|input|>
<|text-center|

<|1 1|layout|

### Choose **Sector**{: .color-primary}!    

<|{expenses_sector}|selector|lov={source_of_expenses}|dropdown|on_change=update_expenses|>

|>
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
        watermark="""Balance your revenue and expenses! Copyright @Ujj1225""",
        favicon="wallet_wise.gif",
        use_reloader=True,
    )
