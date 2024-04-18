def add_toppings(scoop_size , toppings):
    scoopsize = ["s" ,"m" ,"l"]
    topping = ["sprinkles" , "hot fudge" , "whipped cream"]
    if scoop_size in scoopsize and toppings in topping:
        print("wohoo! your icecream is being ready.")
    else:
        print( "oops! unfortunately we don't have your picked sccopsize or topping try something else.")


def make_shake(choice):
    flavour = ["nuts" , "fruits"]
    if choice in flavour:
        print("Great choice! you're shake will be prepared soon.")
    else:
        print("This flavour is unavailable, kindly choose another one.")    


import ice_cream 
ice_cream.add_toppings("m", "hot fudge")
ice_cream.make_shake("nuts")
