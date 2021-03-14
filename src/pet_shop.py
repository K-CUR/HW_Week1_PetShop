# WRITE YOUR FUNCTIONS HERE
# 1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# 2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# 3
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

# 4
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# 5
def increase_pets_sold(pet_shop, qty_sold):
    pet_shop["admin"]["pets_sold"] += qty_sold

# 6
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# 7
def get_pets_by_breed(pet_shop, breed_name):
    selected_breed_list = []
    for breed in pet_shop["pets"]:
        if breed["breed"] == breed_name:
            selected_breed_list.append(breed["breed"])
    return selected_breed_list

# 8
def find_pet_by_name(pet_shop, pet_name):
    for name in pet_shop["pets"]:
        if name["name"] == pet_name:
            return(name)

# 9
def remove_pet_by_name(pet_shop, pet_name):
    for name in pet_shop["pets"]:
        if name["name"] == pet_name:
            pet_shop["pets"].remove(name)

# 10
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

# 11
def get_customer_cash(customers):
    return customers["cash"]

# 12
def remove_customer_cash(customer, cash_to_remove):
    customer["cash"] -= cash_to_remove

# 13
def get_customer_pet_count(customer):
    if customer["pets"] == []:
        return 0
    else:
        return len(customer["pets"])
# 14
def add_pet_to_customer(customers, add_pet):
    customers["pets"].append(add_pet)

# END OF MVP