fruits = ["apples", "bananas", "mango's", "watermelons", "kiwis", "peaches", "apples"]
years = [1985, "2000", 3, 6.5, 120]

fruits.append("oranges")
print(fruits)

fruits.extend(years)
print(fruits)

fruits.remove("oranges")
print(fruits)

years.pop(0)
print(years)

fruits.pop(-1)
print(fruits)

numbers = [67, 12, 0, 1, 2]
numbers.sort()
print(numbers)

# check the membership of item in the list
print("apples" in fruits)  # true
print("apple" in fruits)  # false

# counts how many items with the given name exist in the list
print(fruits.count("apples"))

