import ast 
country_name = input("Enter country name: ").capitalize()
with open ("currency_code.txt","r") as file:
    content = file.read()
    currency_codes = ast.literal_eval(content)
    from_code =(currency_codes[country_name])
