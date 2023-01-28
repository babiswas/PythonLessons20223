import re
pattern="^[A-Za-z0-9]+@[A-Za-z]+\.(com|in|net)$"
email=input("Enter an email:")
if re.search(pattern,email):
   print(email)
else:
   print("Invalid email")
