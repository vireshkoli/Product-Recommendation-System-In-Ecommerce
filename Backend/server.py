from flask import Flask, request
import datetime

from scrapper import amazon, flipkart, reliance
  
x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)

# variable to know if data is passes
amazon_data = None
flipkart_data = None
reliance_data = None
  
  
# Route for seeing a data
@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    # y = amazon()
    # print(y)
    if amazon_data == None and flipkart_data == None and reliance_data == None:
        return {
            "ProductName": 'No value',
            "ProductPrice": 0,
            "ProductRating": 0.0,
            "ProductSRC": ''
        }
    return [
    {
        'SiteName': amazon_data['SiteName'],
        'ProductLink': amazon_data['ProductLink'],
        'ProductName': amazon_data["ProductTitle"], 
        'ProductPrice': amazon_data["ProductPrice"],
        'ProductRating': amazon_data["ProductRating"],
        'ProductSRC': amazon_data["ProductSRC"]
    },
    {
        'SiteName': flipkart_data['SiteName'],
        'ProductLink': flipkart_data['ProductLink'],
        'ProductName': flipkart_data["ProductTitle"], 
        'ProductPrice': flipkart_data["ProductPrice"],
        'ProductRating': flipkart_data["ProductRating"],
        'ProductSRC': flipkart_data["ProductSRC"]
    },
    {
        'SiteName': reliance_data['SiteName'],
        'ProductLink': reliance_data['ProductLink'],
        'ProductName': reliance_data["ProductTitle"], 
        'ProductPrice': reliance_data["ProductPrice"],
        'ProductRating': reliance_data["ProductRating"],
        'ProductSRC': reliance_data["ProductSRC"]
    }
    ]

@app.route('/GetInput', methods=['POST'])
def get_input():
    global amazon_data, flipkart_data, reliance_data
    # getting the data of input field
    data = request.get_json()
    print("Hello there")
    # getting all data for the 3 websites
    amazon_data = amazon(data['ProductName'])
    flipkart_data = flipkart(data['ProductName'])
    reliance_data = reliance(data['ProductName'])
    print(amazon_data)
    print(flipkart_data)
    print(reliance_data)
    print(data)
    return data
  
      
# Running app
if __name__ == '__main__':
    print("Server Started")
    app.run(debug=True)