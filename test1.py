def sayHello():
  print("Hello, World!")


def sayHi(name):
  print("Hi, " + name)

def give_me_a_beer(age):
  if age >= 21:
    print("You can drink")
  elif age >= 90:
    print("Enjoy this one is on the house!")
  else:
    print("You can't drink")


# function calls
sayHello()
sayHi("Cesar")
give_me_a_beer(21)