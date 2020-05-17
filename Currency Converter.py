with open(r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\Currency.txt") as f:
    lines = f.readlines()

print(lines)
curr_dict = {}
for line in lines:
    split = line.split("\t")
    curr_dict[split[0]] = split[1]

print(curr_dict)
amount = int(input("Enter the amount: "))
print("Enter Conversion Currency:  \nAvailable Options:\n")
[print(item) for item in curr_dict.keys()]

currency = input("Enter one of these values:")
print(f"{amount} INR is equal to {amount * float(curr_dict[currency])} {currency}")

print("------------------------------------------------------------------------------------------------")

from forex_python.converter import CurrencyRates, CurrencyCodes
c = CurrencyRates()
print(c.get_rate('INR','USD'))
print(c.convert("INR","USD",500))

curr = CurrencyCodes()
print(curr.get_symbol("INR"))
print(curr.get_currency_name("INR"))

from forex_python.bitcoin import BtcConverter
bt = BtcConverter()
print(bt.get_latest_price("INR"))
