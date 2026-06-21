# words = ["apple", "banana", "cherry"]

# # Get the length of every string
# lengths = map(len, words)

# print(list(lengths))  # Output: [5, 6, 6]

# # Convert all text to uppercase
# # shouting = map(str.upper, words)
# print(list(shouting))  # Output: ['APPLE', 'BANANA', 'CHERRY']

customer_demand = input("Enter the food you want...")

customer_demand = customer_demand.lower()

if customer_demand == "springroll":
  print("Price : 40$ ")
elif customer_demand == "chicken":
  print("Price : 50$")
elif customer_demand == "paneer":
  print("Price : 50$")
else:
  print("Food not available")

