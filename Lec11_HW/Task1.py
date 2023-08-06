import requests

resp = requests.get("https://api.monobank.ua/bank/currency")
print(resp.status_code)
my_currencies = {
    980: "🇺🇦",
    840: "🇺🇸",
    978: "🇪🇺",
}

my_rates = []
for obj in resp.json():
    if obj["currencyCodeA"] in my_currencies:
        my_rates.append(obj)

print(my_rates)
