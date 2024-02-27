import re


def convert_to_dict(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Extract income sources and amounts using regular expression
    matches = re.findall(r"(\w+):(\d+)", content)

    # Create a dictionary with "Income_Source" and "Amount" keys
    data = {"Income_Source": [], "Amount": []}

    income_dict = {}

    for match in matches:
        income_source, amount = match
        income_dict.setdefault(income_source, 0)
        income_dict[income_source] += float(amount)

    data["Income_Source"] = list(income_dict.keys())
    data["Amount"] = list(income_dict.values())

    return data


# Example usage for income.txt
income_file_path = "income.txt"
income_data = convert_to_dict(income_file_path)

# Save the result in another Python file
with open("income_pi_data.py", "w") as output_file:
    output_file.write(f"income_pi_data = {income_data}\n")

# Example usage for expenses.txt
expenses_file_path = "expenses.txt"
expenses_data = convert_to_dict(expenses_file_path)

# Save the result in another Python file
with open("expenses_pi_data.py", "w") as output_file:
    output_file.write(f"expenses_pi_data = {expenses_data}\n")
