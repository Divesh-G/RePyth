import random
import string

# print(string.ascii_letters)
# print(string.punctuation)
# print(string.digits)

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)

# list comprehension for above code: [function for i in range(n)]
password = "".join([random.choice(charValues) for i in range(pass_len)])

print("Your random password is:", password)