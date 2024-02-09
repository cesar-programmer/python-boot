def about_me():
  me = {
    'first' : 'cesar',
    'last' : 'cordova',
    'age' : 21,
    'address' : {
      'street' : '123 main st',
      'city' : 'anytown',
      'state' : 'NY',
      'zip' : '12345'
    }
  }
  print(me)

# read the values
  print(me['first'] + ' ' + me['last'])
  print(f'im {me["age"]} years old')

# read the address
  print(me['address']['street'])
  adress = me['address']
  print(adress['street'])

# a) street #number, city, zip.
  print(f'{me["address"]["street"]}, {me["address"]["city"]}, {me["address"]["zip"]}.')


def computer_store():
  catalog = [
    {"title": "Keyboard", "price": 45.33},
    {"title": "Mouse", "price": 20.00},
    {"title": "4K Monitor", "price": 195.93},
    {"title": "Ultrawide Monitor", "price": 425.16},
    {"title": "Webcam", "price": 42.50},
  ]
  for item in catalog:
    print(f'{item["title"]}')

  total = 0
  for item in catalog:
    print(f'{item["title"]}: {item["price"]}')
    total += item['price']
  print(f'Total: {total}')


def school():
  students = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "age": 34,
            "grade": "A",
            "due_balance": 325.00,
        },
        {
            "first_name": "Carlos",
            "last_name": "Rodriguez",
            "age": 56,
            "grade": "B",
            "due_balance": 30.00,
        },
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "age": 37,
            "grade": "B",
            "due_balance": 0.00,
        },
        {
            "first_name": "Carlos",
            "last_name": "Rodriguez",
            "age": 56,
            "grade": "B",
            "due_balance": 30.00,
        },
{
            "first_name": "Emma",
            "last_name": "Smith",
            "age": 22,
            "grade": "B",
            "due_balance": 150.00,
        },
        {
            "first_name": "Liam",
            "last_name": "Johnson",
            "age": 20,
            "grade": "A",
            "due_balance": 200.00,
        },
        {
            "first_name": "Olivia",
            "last_name": "Williams",
            "age": 23,
            "grade": "C",
            "due_balance": 220.00,
        },
        {
            "first_name": "Noah",
            "last_name": "Brown",
            "age": 21,
            "grade": "B",
            "due_balance": 180.00,
        },
        {
            "first_name": "Ava",
            "last_name": "Jones",
            "age": 24,
            "grade": "A",
            "due_balance": 300.00,
        },
{
            "first_name": "Ethan",
            "last_name": "Garcia",
            "age": 25,
            "grade": "C",
            "due_balance": 100.00,
        },
        {
            "first_name": "Sophia",
            "last_name": "Miller",
            "age": 26,
            "grade": "B",
            "due_balance": 250.00,
        },
    ]

  # a) print the first and last name of each student
  for student in students:
    print(f'{student["first_name"]} {student["last_name"]}')
  print('---')
  # b) print the first and last name for students with A grade
  for student in students:
    if student['grade'] == 'A':
      print(f'{student["first_name"]} {student["last_name"]}')
  #c print the total due balance for all students
  total = 0
  for student in students:
    total += student['due_balance']
  print(f'Total due balance: {total}')

# fn calls
# about_me()
computer_store()
school()
