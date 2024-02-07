def student_names():
  names = ["Dave", "Jazper",  "Andy", "Corey", "Samuel", "Cesar", "Darius", "Demetri", "Janaye", "Donald", "Marco"]
  print(names)

  # add a name to the list
  names.append("sergio")

  # travel the list
  for name in names:
    print(name)

  # count the number of names
  print(len(names))

def products():
  prices = [23, 234, 34, 672, 77, 214, 756, 76, 500, 479, 629, 325, 389, 29, 101, 50, 67, 800, 54]

  total = 0
  for price in prices:
    total += price

  print(total)
  print(sum(prices))

  counter = 0
  counter2 = 0
  for price in prices:
    if price < 500:
      counter += 1
    if price >= 500:
      counter2 += 1
  print(counter)
  print(counter2)

  actual = 0
  greater = 0

  for price in prices:
    actual = price
    if(actual >= greater):
      greater = actual
  
  print(max(prices))

  print(greater)

def art():
  colors = ["red", "blue", "pink", "blue", "white", "black", "green", "black", "red", "white", "blue", "yellow"]

  print(len(colors))

  counter = 0
  counter2 = 0
  for color in colors:
    if color == 'blue':
      counter += 1
    if color == 'white' or color == 'black':
      counter2 += 1

  print('amount of blue: ' + str(counter))
  print('amount of white and black: ' + str(counter2))

# function calls
# student_names()
# products()
art()