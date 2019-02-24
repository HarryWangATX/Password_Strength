import getpass


while True:
  x = getpass.getpass("Enter your password: ")

  y =  len(x)

  if y < 5 or x == "1234567890" or x == "123456789" or x == "12345678" or x == "1234567" or x == "123456" or x == "12345" or x == "1234" :
    print("Your Password Will Be Cracked Instantly.")
  elif y < 10:
    print("Your Password Will Take A While To Crack")
  elif y < 15:
    print("Your Password Will Take a Computer 15 Years To Crack")
  else:
    print("Your Password is Impossible To Crack")

  print("Is you password: "+ str(x))

  z = input("Would You Like to Test Out Another Password?")

  if z == "Yes" or z == "yes":
    a = 0
  elif z =="No" or z == "no":
    break
