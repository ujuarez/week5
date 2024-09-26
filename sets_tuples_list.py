# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates
#   Set = {} unordered and immutable, but Add/Remove OK. NO Duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. Faster

fruits = ["apple", "orange", "banana", "coconut"]
# print(fruits[])
# print(dir(fruits)) 
# print(help(fruits)) #Gives help 
# print(len(fruits)) #
# print("pineapple" is fruits) # Tells if it is in the list (True or False)


# fruits[0] = "pineapple" # Can REASSIGN values in list
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
print(fruits.index("coconut"))


print(fruits)


# for fruit in fruits:
  #  print(fruits)