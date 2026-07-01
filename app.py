from flask import Flask

app = Flask(__name__)

# Sample product data
products = [
   {"id": 1, "name": "Chopping Board", "price": 360},
   {"id": 2, "name": "Sketch Pens", "price": 30},
   {"id": 3, "name": "Shoes", "price": 519}
]

if __name__ == '__main__':
    app.run(debug=True)