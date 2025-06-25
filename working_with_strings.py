#string creation and manipulation
first_name = "cristiano"
second_name = "ronaldo"

#string concatenation
full_name = first_name + " " + second_name
print(full_name)

#string formatting
age=40
msg = f"hello, i'm {full_name} and i'm {age} year old."
print(msg)

#string methods
text =" Python Programming "
print(text.strip()) #remove whitespace
print(text.lower()) #lowercase
print(text.upper()) #uppercase
print(text.replace("Python","Java"))