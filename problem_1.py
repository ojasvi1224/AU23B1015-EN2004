def get_name():
    Name = input('Your Good Name:')
    return Name

def get_tshirt(brand_name):
    name = get_name()
    Available=["spykar" , "levis", "us polo", "adidas"]
    if brand_name in Available:
        print("Hi", {name} , ",the brand you are looking for is available in our store.")
    else:
       print("Hi", {name} , ",Unfortunately the brand you are looking for is not available in our store.")
get_tshirt("levis")
