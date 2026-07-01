from flask import Flask
from flask import Flask, request
app = Flask(__name__)

# Sample product data
products = [
 {
   "id": 1,
   "name": "Chopping Board",
   "price": 360,
   "description": "A durable wooden chopping board for daily kitchen use.",
   "image": "https://bit.ly/3XCmlH5"
 },
 {
   "id": 2,
   "name": "Sketch Pens",
   "price": 30,
   "description": "12 bright colors perfect for school and art projects.",
   "image": "https://bit.ly/3X8Tb2d"
 },
 {
   "id": 3,
   "name": "Shoes",
   "price": 519,
   "description": "Comfortable running shoes with breathable mesh.",
   "image": "https://bit.ly/4r5FnTX"
 },
 {
   "id": 4,
   "name": "Water Bottle",
   "price": 199,
   "description": "1-litre stainless steel insulated bottle.",
   "image": "https://bit.ly/48oQWy3"
 },
 {
   "id": 5,
   "name": "Notebook",
   "price": 85,
   "description": "200-page ruled notebook for study & office use.",
   "image": "https://images.unsplash.com/photo-1519682337058-a94d519337bc"
 },
 {
   "id": 6,
   "name": "Earphones",
   "price": 299,
   "description": "High-quality wired earphones with mic.",
   "image": "https://bit.ly/4i705i2"
 },
 {
   "id": 7,
   "name": "Backpack",
   "price": 899,
   "description": "Lightweight waterproof backpack with 3 compartments.",
   "image": "https://bit.ly/4ocvZuZ"
 },
 {
   "id": 8,
   "name": "LED Bulb",
   "price": 120,
   "description": "9W energy-efficient LED bulb.",
   "image": "https://bit.ly/49oKyI9"
 },
 {
   "id": 9,
   "name": "Coffee Mug",
   "price": 250,
   "description": "Ceramic mug with heat insulation and stylish print.",
   "image": "https://bit.ly/48uDdov"
 },
 {
   "id": 10,
   "name": "Keyboard",
   "price": 750,
   "description": "USB keyboard with smooth keys and long durability.",
   "image": "https://bit.ly/3X6DtEU"
 }
]
@app.route('/products', methods=['GET'])
def get_products():
  return products
# ... (previous code remains the same)

# Route to get a single product by ID
@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
  product_id = int(product_id)
  for product in products:
    if product['id'] == product_id:
      return product
  # Return an error if the product is not found
  return {"error": "Product not found"}, 404

    
  # Return an error if the product is not found
  #adding post method to add product
@app.route('/products', methods=['POST'])
def add_product():
   new_product = request.get_json()
   
   # Generate a new ID (in a real app, a database would handle this)
   new_product['id'] = len(products) + 1
   products.append(new_product)
   
   return {"message": "Product added!", "product": new_product}, 201
    
if __name__ == '__main__':
    app.run(debug=True)