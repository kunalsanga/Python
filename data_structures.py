#list
fruits=["apple","mango","orange","grapes"]
numbers=[1,2,3,4,5]

#accessing elements of the list
print(fruits[-1])

#modifying the list
fruits.append("pineapple")
fruits.insert(2,"banana")
fruits.remove("banana")
fruits.pop()
print(fruits)

#list slicing
print(numbers[1:5])
print(numbers[:3])
print(numbers[2:])

#list comprehension
squares = [x**2 for x in range(5)]
print(squares)