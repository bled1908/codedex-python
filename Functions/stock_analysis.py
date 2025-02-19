# Scope determines where in the program a variable is visible and can be used.
# local variable that belongs to the local scope
# ariable created outside of a function is called a global variable and belongs to the global scope, meaning that they can be used by every function.

# Write code below 💖

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
  return stock_prices[x - 1]

def max_price(a, b):
  new_stock_price = []
  for num in range(a - 1, b - 1):
    new_stock_price.append(stock_prices[num])
  return max(new_stock_price)

def min_price(a, b):
  new_stock_price = []
  for num in range(a - 1, b - 1):
    new_stock_price.append(stock_prices[num])
  return min(new_stock_price)

print(price_at(2))
print(min_price(2, 5))
print(max_price(2, 5))

'''# Stonks 📈
# Codédex

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(i):
  return stock_prices[i-1]

def max_price(a, b):
  mx = 0
  for i in range(a, b + 1):
    mx = max(mx, price_at(i))
  return mx

def min_price(a, b):
  mn = price_at(a)
  for i in range(a, b + 1):
    mn = min(mn, price_at(i))
  return mn

print(max_price(1, 15))
print(min_price(5, 10))
print(price_at(3))'''