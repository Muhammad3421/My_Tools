import requests

def currency_converter():
    currencies = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()["rates"]

    source = input("Enter the currency to converter from(USD, JPY, GBP, EUR): ").upper()
    target = input("Enter the currency to converter to(USD, JPY, GBP, EUR): ").upper()
    amount = float(input("Enter the amount: "))

    result = amount * currencies[target]/currencies[source]

    print(f"{amount} {source} = {result} {target}")


if __name__ == "__main__":
    currency_converter()