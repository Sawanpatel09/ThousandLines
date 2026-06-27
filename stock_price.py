stock_price = [345,656,643,534,685]
for i in range(len(stock_price)):
    if stock_price[i] == 534:
        print(i)
stock_price.insert(1,777)
print(stock_price[1])
stock_price.remove(656)
print(stock_price)