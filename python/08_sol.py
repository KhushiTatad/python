password = "Khushiowe@2190"

if len(password) < 6:
    strength = "Weak Password"
elif len(password) <= 10:
    strength = "Medium Password"
else:
    strength = "Strong Password"

 print(strength)




 Password = "kasljakjdaskd"
password_len = len(password)

if password_len < 6:
      strength = "Weak Password"
elif password_len <= 10:
     strength = "Medium Password"
 else:
     strength = "Strong Password"

 print(strength)
