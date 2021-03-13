# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, qty_sold):
    pet_shop["admin"]["pets_sold"] += qty_sold


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed_name):
    selected_breed_list = []
    for breed in pet_shop["pets"]:
        if breed["breed"] == breed_name:
            selected_breed_list.append(breed["breed"])
    return selected_breed_list
    

def find_pet_by_name(pet_shop, pet_name):
    for name in pet_shop["pets"]:
        if name["name"] == pet_name:
            return(name)



            
