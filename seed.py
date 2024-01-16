from app import app




from models import db, User, Supplier, Sales, Product, ProductOrder, Profile 



users = [{
  "id": 1,
  "name": "Elysia",
  "email": "Lindenman"
}, {
  "id": 2,
  "name": "Cosmo",
  "email": "Lesper"
}, {
  "id": 3,
  "name": "Carlin",
  "email": "Oakinfold"
}, {
  "id": 4,
  "name": "Mallory",
  "email": "Bayford"
}, {
  "id": 5,
  "name": "Vivia",
  "email": "Gullane"
}, {
  "id": 6,
  "name": "Gallagher",
  "email": "Fenty"
}, {
  "id": 7,
  "name": "Dael",
  "email": "Braker"
}, {
  "id": 8,
  "name": "Addy",
  "email": "Dirkin"
}, {
  "id": 9,
  "name": "Padgett",
  "email": "Weald"
}, {
  "id": 10,
  "name": "Cary",
  "email": "McFetrich"
}]




Profiles= [{
  "id": 1,
  "firstname": "Brandice",
  "lastname": "Wheelton",
  "user_id": 1,
  "photo_url": "http://dummyimage.com/189x100.png/ff4444/ffffff"
}, {
  "id": 2,
  "firstname": "Bernadene",
  "lastname": "Chesworth",
  "user_id": 2,
  "photo_url": "http://dummyimage.com/104x100.png/5fa2dd/ffffff"
}, {
  "id": 3,
  "firstname": "Debra",
  "lastname": "Nunns",
  "user_id": 3,
  "photo_url": "http://dummyimage.com/229x100.png/ff4444/ffffff"
}, {
  "id": 4,
  "firstname": "Lauraine",
  "lastname": "MacCosto",
  "user_id": 4,
  "photo_url": "http://dummyimage.com/232x100.png/cc0000/ffffff"
}, {
  "id": 5,
  "firstname": "Elnar",
  "lastname": "Bellham",
  "user_id": 5,
  "photo_url": "http://dummyimage.com/231x100.png/cc0000/ffffff"
}, {
  "id": 6,
  "firstname": "Wayland",
  "lastname": "Klaassens",
  "user_id": 6,
  "photo_url": "http://dummyimage.com/107x100.png/dddddd/000000"
}, {
  "id": 7,
  "firstname": "Johnette",
  "lastname": "Entres",
  "user_id": 7,
  "photo_url": "http://dummyimage.com/106x100.png/cc0000/ffffff"
}, {
  "id": 8,
  "firstname": "Jaquenetta",
  "lastname": "Sneyd",
  "user_id": 8,
  "photo_url": "http://dummyimage.com/135x100.png/cc0000/ffffff"
}, {
  "id": 9,
  "firstname": "Patrizius",
  "lastname": "Gilogly",
  "user_id": 9,
  "photo_url": "http://dummyimage.com/242x100.png/ff4444/ffffff"
}, {
  "id": 10,
  "firstname": "Rosemaria",
  "lastname": "Bytheway",
  "user_id": 10,
  "photo_url": "http://dummyimage.com/227x100.png/dddddd/000000"
}]

products = [{
  "id": 1,
  "name": "Muffins - Assorted",
  "perishable": True,
  "quantity": 15,
  "price": 67.36
}, {
  "id": 2,
  "name": "Yogurt - Banana, 175 Gr",
  "perishable": True,
  "quantity": 13,
  "price": 56.78
}, {
  "id": 3,
  "name": "Beer - Muskoka Cream Ale",
  "perishable": False,
  "quantity": 10,
  "price": 148.62
}, {
  "id": 4,
  "name": "Veal - Loin",
  "perishable": True,
  "quantity": 25,
  "price": 81.92
}, {
  "id": 5,
  "name": "Mince Meat - Filling",
  "perishable": True,
  "quantity": 90,
  "price": 158.11
}, {
  "id": 6,
  "name": "Tea - Honey Green Tea",
  "perishable": False,
  "quantity": 83,
  "price": 147.55
}, {
  "id": 7,
  "name": "Wine - Chablis J Moreau Et Fils",
  "perishable": False,
  "quantity": 92,
  "price": 172.09
}, {
  "id": 8,
  "name": "Chocolate - Sugar Free Semi Choc",
  "perishable": True,
  "quantity": 34,
  "price": 66.01
}, {
  "id": 9,
  "name": "Cape Capensis - Fillet",
  "perishable": False,
  "quantity": 28,
  "price": 145.49
}, {
  "id": 10,
  "name": "Cake Circle, Foil, Scallop",
  "perishable": False,
  "quantity": 58,
  "price": 53.69
}, {
  "id": 11,
  "name": "Oil - Sunflower",
  "perishable": True,
  "quantity": 89,
  "price": 156.3
}, {
  "id": 12,
  "name": "Soup - Campbells Pasta Fagioli",
  "perishable": True,
  "quantity": 81,
  "price": 197.94
}, {
  "id": 13,
  "name": "Pepper - Red Chili",
  "perishable": False,
  "quantity": 77,
  "price": 139.74
}, {
  "id": 14,
  "name": "Table Cloth 120 Round White",
  "perishable": False,
  "quantity": 42,
  "price": 77.07
}, {
  "id": 15,
  "name": "Sambuca - Opal Nera",
  "perishable": True,
  "quantity": 54,
  "price": 110.06
}, {
  "id": 16,
  "name": "Potatoes - Fingerling 4 Oz",
  "perishable": True,
  "quantity": 36,
  "price": 118.32
}, {
  "id": 17,
  "name": "Berry Brulee",
  "perishable": False,
  "quantity": 13,
  "price": 90.62
}, {
  "id": 18,
  "name": "Cheese - Roquefort Pappillon",
  "perishable": False,
  "quantity": 34,
  "price": 182.42
}, {
  "id": 19,
  "name": "Sage Ground Wiberg",
  "perishable": False,
  "quantity": 94,
  "price": 125.35
}, {
  "id": 20,
  "name": "Cake - Lemon Chiffon",
  "perishable": False,
  "quantity": 69,
  "price": 61.64
}, {
  "id": 21,
  "name": "Cheese - Stilton",
  "perishable": False,
  "quantity": 34,
  "price": 130.87
}, {
  "id": 22,
  "name": "Bay Leaf",
  "perishable": False,
  "quantity": 11,
  "price": 196.63
}, {
  "id": 23,
  "name": "Pumpkin",
  "perishable": True,
  "quantity": 87,
  "price": 187.07
}, {
  "id": 24,
  "name": "Sweet Pea Sprouts",
  "perishable": False,
  "quantity": 43,
  "price": 66.4
}, {
  "id": 25,
  "name": "Port - 74 Brights",
  "perishable": True,
  "quantity": 78,
  "price": 184.61
}, {
  "id": 26,
  "name": "V8 - Vegetable Cocktail",
  "perishable": True,
  "quantity": 51,
  "price": 117.23
}, {
  "id": 27,
  "name": "Wine - Rioja Campo Viejo",
  "perishable": True,
  "quantity": 68,
  "price": 67.35
}, {
  "id": 28,
  "name": "Cheese - Stilton",
  "perishable": False,
  "quantity": 43,
  "price": 68.5
}, {
  "id": 29,
  "name": "Juice - Mango",
  "perishable": True,
  "quantity": 95,
  "price": 187.14
}, {
  "id": 30,
  "name": "Baking Soda",
  "perishable": True,
  "quantity": 47,
  "price": 53.14
}]

sales = [{
  "id": 1,
  "quantity": 10,
  "user_id": 1,
  "product_id": 28
}, {
  "id": 2,
  "quantity": 10,
  "user_id": 2,
  "product_id": 21
}, {
  "id": 3,
  "quantity": 2,
  "user_id": 3,
  "product_id": 12
}, {
  "id": 4,
  "quantity": 1,
  "user_id": 4,
  "product_id": 21
}, {
  "id": 5,
  "quantity": 1,
  "user_id": 5,
  "product_id": 7
}, {
  "id": 6,
  "quantity": 9,
  "user_id": 6,
  "product_id": 12
}, {
  "id": 7,
  "quantity": 3,
  "user_id": 7,
  "product_id": 27
}, {
  "id": 8,
  "quantity": 1,
  "user_id": 8,
  "product_id": 20
}, {
  "id": 9,
  "quantity": 2,
  "user_id": 9,
  "product_id": 22
}, {
  "id": 10,
  "quantity": 5,
  "user_id": 10,
  "product_id": 25
}, {
  "id": 11,
  "quantity": 8,
  "user_id": 11,
  "product_id": 3
}, {
  "id": 12,
  "quantity": 5,
  "user_id": 12,
  "product_id": 19
}, {
  "id": 13,
  "quantity": 3,
  "user_id": 13,
  "product_id": 1
}, {
  "id": 14,
  "quantity": 1,
  "user_id": 14,
  "product_id": 3
}, {
  "id": 15,
  "quantity": 2,
  "user_id": 15,
  "product_id": 7
}, {
  "id": 16,
  "quantity": 6,
  "user_id": 16,
  "product_id": 16
}, {
  "id": 17,
  "quantity": 6,
  "user_id": 17,
  "product_id": 15
}, {
  "id": 18,
  "quantity": 6,
  "user_id": 18,
  "product_id": 13
}, {
  "id": 19,
  "quantity": 2,
  "user_id": 19,
  "product_id": 4
}, {
  "id": 20,
  "quantity": 2,
  "user_id": 20,
  "product_id": 19
}]
 


with app.app_context():
    # db.session.add_all(User(**user) for user in users)
    # db.session.commit()

    # db.session.add_all(Profile(**profile) for profile in Profiles)
    # db.session.commit()

    # db.session.add_all(Product(**product) for product in products)
    # db.session.commit()

    db.session.add_all(Sales(**sale) for sale in sales)
    db.session.commit()