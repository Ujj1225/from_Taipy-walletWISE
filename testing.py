# Importing data for Chart
from income_pi_data import income_pi_data

# Access the data
income_sources = income_pi_data["Income_Source"]
amounts = income_pi_data["Amount"]

# Example: Print income sources and amounts
for source, amount in zip(income_sources, amounts):
    print(f"Source: {source}, Amount: {amount}")
