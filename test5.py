def products_test():
    products = [
        {
            "title": "Smartphone",
            "image": "smartphone.jpg",
            "price": 299.99,
            "category": "Electronics",
        },
        {
            "title": "Running Shoes",
            "image": "running_shoes.jpg",
            "price": 89.99,
            "category": "Footwear",
        },
        {
            "title": "Backpack",
            "image": "backpack.jpg",
            "price": 49.99,
            "category": "Accessories",
        },
        {
            "title": "Coffee Maker",
            "image": "coffee_maker.jpg",
            "price": 119.99,
            "category": "Home Appliances",
        },
        {
            "title": "Wireless Headphones",
            "image": "wireless_headphones.jpg",
            "price": 159.99,
            "category": "Electronics",
        },
        {
            "title": "Fitness Tracker",
            "image": "fitness_tracker.jpg",
            "price": 59.99,
            "category": "Wearables",
        },
        {
            "title": "Digital Camera",
            "image": "digital_camera.jpg",
            "price": 349.99,
            "category": "Electronics",
        },
        {
            "title": "Yoga Mat",
            "image": "yoga_mat.jpg",
            "price": 25.99,
            "category": "Fitness",
        },
        {
            "title": "Novel - 'Mystery of the Old Manor'",
            "image": "novel.jpg",
            "price": 14.99,
            "category": "Books",
        },
        {
            "title": "Portable Charger",
            "image": "portable_charger.jpg",
            "price": 39.99,
            "category": "Electronics",
        },
    ]


    # a) print the total of products
    total = 0
    for product in products:
      print(f'{product["title"]} ${product["price"]}')
      total += product['price']
    print(f'Total: {total}')
    # c) print the cheapest product
    products.sort(key=lambda x: x['price'])
    print(products[0])

    actual = 0
    cheaper = 999999

    for product in products:
      actual = product['price']
      if(actual <= cheaper):
        cheaper = actual
    print(cheaper)

    # B) What is the total of Electronics?
    counter = 0
    for product in products:
      if(product['category'] == 'Electronics'):
        counter += 1
    print(f'the total of Electronics are {counter}')

    #D) list of unique categories

    categories = []
    for product in products:
      if product['category'] not in categories:
        categories.append(product['category'])
    print(categories)
products_test()