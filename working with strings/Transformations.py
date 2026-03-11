#Transformations on Strings
    #replace()
price = "12234,32"
print(price.replace(",", "-"))

phone = "123-456-7890"
print(phone.replace("-", " "))

price = "$1,299.99"
print(price.replace("$", " ").replace(",", " "))

    #concatination
first_name = "john"
last_name = "doe"
last_name = first_name + " " + last_name
print(last_name)

folder = "C:/Users/JOSH"
file = "report.csv"
full_file_path = folder + "/" + file
print(full_file_path)

    #f-strings formatting
name = "john"
age = 30
is_student = False
print("my name is " + name + ", i am " + str(age) + " years old, and student status is " + str(is_student) + ".")
print(f"my name is {name}, i am {age} years old, and student status is {is_student}.")
print(f"2 + 3 = {2 + 3}")