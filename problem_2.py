def get_name():
    Name = input('Your Good Name:')
    return Name

def get_tshirt(brand_name,Size):
    name = get_name()
    Available=["spykar" , "levis", "us polo", "adidas"]
    size=["s" , "m" , "l" , "xl"]
    if brand_name in Available and Size in size:
        print("Hi", {name} , ",the brand and size you are looking for is available in our store.")
    else:
       print("Hi", {name} , ",Unfortunately the brand or size you are looking for is not available in our store.")

get_tshirt("adidas","xxl")
