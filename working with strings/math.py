#math
    #length of a string
password="1234dfghjkjha"
password = input("enter your password: ")
#print(len(password))

if len(password) < 8:
    print("password must be at least 8 characters long")

    #count
text = """
python is easy to learn. 
python is a great language. 
python is used in many fields.
"""
print(text.count("python"))