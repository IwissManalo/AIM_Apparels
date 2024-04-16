import time

print("""
Welcome to AIM Apparels! Where we aim to show off our styles
Input your name to continue shopping
""")
name = input()
print("Greetings Ms/Mr " + name + '!' + " Below are some of our newest collection. Enjoy Shopping!")

time.sleep(5)

shoe_collection = {
    "Amanda": 20,
    "Sophie": 35,
    "Lana": 50
}

top_collection = {
    "Hailey": 40,
    "Poopy": 95,
    "Wanda": 70
}

bottom_collection = {
    "Darry": 20,
    "Quin": 25,
    "Sierra": 80
}

shopping_cart = {}


def display_collections():
    items_description = {
        "Amanda": "Casual sneakers",
        "Sophie": "Classic pumps",
        "Lana": "Stylish boots",
        "Hailey": "Striped blouse",
        "Poopy": "Embroidered jacket",
        "Wanda": "Denim skirt",
        "Darry": "Cargo pants",
        "Quin": "Slim-fit jeans",
        "Sierra": "High-waisted trousers"
    }

    print("""\n-----Shoe Collection----- 
Amanda [$20] - """ + items_description["Amanda"] + """
Sophie [$35] - """ + items_description["Sophie"] + """
Lana [$50] - """ + items_description["Lana"] + """

-----Top Collection----- 
Hailey [$40] - """ + items_description["Hailey"] + """
Poopy [$95] - """ + items_description["Poopy"] + """
Wanda [$70] - """ + items_description["Wanda"] + """

-----Bottom Collection----- 
Darry [$20] - """ + items_description["Darry"] + """
Quin [$25] - """ + items_description["Quin"] + """
Sierra [$80] - """ + items_description["Sierra"])


display_collections()


def add_to_cart(category, item, quantity):
    if category == 'shoe':
        price = shoe_collection[item] * quantity
    elif category == 'top':
        price = top_collection[item] * quantity
    elif category == 'bottom':
        price = bottom_collection[item] * quantity
    else:
        print("Invalid category. Please try again")
        time.sleep(3)
        return

    if item in shopping_cart:
        shopping_cart[item] += quantity
    else:
        shopping_cart[item] = quantity

    print(f"{quantity} {item}(s) added to your cart.")


def calculate_total():
    total = 0
    for item, quantity in shopping_cart.items():
        if item in shoe_collection:
            total += shoe_collection[item] * quantity
        elif item in top_collection:
            total += top_collection[item] * quantity
        elif item in bottom_collection:
            total += bottom_collection[item] * quantity
    return total