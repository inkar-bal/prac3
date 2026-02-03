# List of prices in USD
usd_prices = [10, 25, 40, 100]
# Convert to KZT (example rate: 1 USD = 470 KZT)
kzt_prices = list(map(lambda x: x * 470, usd_prices))
print(kzt_prices)


numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)


numbers = ["1", "2", "3", "4"]
ints = list(map(lambda x: int(x), numbers))
print(ints)

