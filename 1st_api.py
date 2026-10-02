import requests
import ast 

API_key = "FwKTdnFCjVecR4w3mmnz6aY5UqK7VfNO"
base_url = "https://api.currencybeacon.com/v1"

def get_info():
    from_country_name = input("Enter From country name: ").capitalize()
    to_country_name = input("Enter TO country name: ").capitalize()

    with open ("currency_code.txt","r") as file:
        content = file.read()
        currency_codes = ast.literal_eval(content)

        from_code =(currency_codes[from_country_name])
        to_code  =(currency_codes[to_country_name])
        url = f"{base_url}/convert"
    
        _amount_ =int(input("enter them amount to conver: "))
    
        params = {
        "api_key": API_key
        ,"from" : from_code
        ,"to" :to_code
        ,"amount" : _amount_
        }
        response = requests.get(url,params = params)
        data = response.json()
    
    
        value = data["response"]["value"]
        print(f"{_amount_} {from_code} = {value} {to_code}")
    
get_info()
