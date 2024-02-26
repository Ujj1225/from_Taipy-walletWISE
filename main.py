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
message = ""

path = "wallet_calc.gif"

source_of_income = ["salary", "dividend", "business_revenue", "tax_rebate", "others"]
source_of_expenses = [
    "Fooding",
    "Clothing",
    "Education",
    "Health",
    "Misc",
]


# loading Gemini Pro model
model = genai.GenerativeModel("gemini-pro")


# Generating content using the model
def generate(state):
    state.message = "Please wait while we analyze your INCOME AND EXPENDITURE"
    response = model.generate_content(["Create a financial Saving plan for the month"])
    print(response.text)
    state.message = response.text


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


def clear_income(state):
    state.income_sector = ""
    state.income = ""


def clear_expenses(state):
    state.expenses_sector = ""
    state.expenses = ""


page = """

<style>

.button_row{
    display: flex;
}

.fullwidth{
width:100% !important;
}

.form{
 display:flex;
 flex-direction:column;
 justify-content:space-evenly;
 padding:2rem;
 margin-top:2rem;
}

.middleSection{
 display:flex;
  flex-wrap: wrap;
 justify-content:center;
 gap:2rem;
 padding:"2rem"
 
}

.fullCenter{
 display:flex;
 justify-content:center;
 align-items:center;
  flex-direction:column;
}
</style>

<|text-right|toggle|theme|>\n<center>\n<|navbar|>\n</center>
<|text-center |
<|{title}|hover_text="{hover_text}"|text|>
|>
<|middleSection| 
<|fullCenter|  
 <|{path}|image|>
 |>
<||

<|form| 

<|1 1|layout|
### Income **Amount & Sector**{: .color-primary}!    
TOTAL INCOME: <|{income}|input|>
<|{income_sector}|selector|lov={source_of_income}|dropdown|label=sources of income|> 
|>
<|class_name = button_row|
<|Add to Income!|button|on_action=generate_income|>
<|Clear|button|on_action=clear_income|>
|>
<|1 1|layout|
### Expenses **Amount & Sector**{: .color-primary}!    
EXPENDITURE: <|{expenses}|input|>
<|{expenses_sector}|selector|lov={source_of_expenses}|dropdown|label=sources of expense|> 
|>
<|class_name=button_row|
<|Add to Expense|button|on_action=generate_expenses|>
<|Clear|button|on_action=clear_expenses|>
|>
|>

<|text-center|
<|Get Insights|button|on_action=generate|>
|>
|>
|>
<|part|class_name=card|
<|{message}|input|multiline|not active|label= your message will appear here...|class_name=fullwidth|>
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
