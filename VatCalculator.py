
def vatcalculation(x):
    totalPrice = x+(x*7/100)
    return totalPrice
price = int(input("What is your price ? : "))
print(vatcalculation(price))