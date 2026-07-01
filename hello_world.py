# 1. Import the Flask class
from flask import Flask

# 2. Create an instance of the Flask class
app = Flask(__name__)

# 3. Define a route and the function to handle it
@app.route('/', methods=['GET'])
def home():
   return "Hello World!"
@app.route('/name')
def get_name():
   return "Rahul"

# 4. Run the application server
if __name__ == '__main__':
    app.run(debug=True)