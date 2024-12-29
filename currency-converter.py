exchange_rates = {
    "USD": 1,
    "INR": 82.5,
    "EUR": 0.9
}

def convert(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates:
        return amount * (exchange_rates[to_currency] / exchange_rates[from_currency])
    return None

amount = float(input("Enter amount: "))
from_currency = input("Enter from currency (USD, INR, EUR): ").upper()
to_currency = input("Enter to currency (USD, INR, EUR): ").upper()

converted = convert(amount, from_currency, to_currency)
if converted:
    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
else:
    print("Invalid currency!")
