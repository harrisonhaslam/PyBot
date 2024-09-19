
###VARIABLES###
soda_flavors = ["Coke", "Coke Zero", "Sprite", "Dr. Pepper", "Ginger Ale", "Lemonade", "Root Beer"]
shake_flavors = ["Vanilla", "Strawberry", "Chocolate", "Oreo", "Mint"]

###FUNCTIONS###
def find_drink(name, menu):
  return name if name in menu else None
  
def select_drink(name, drink_type):
  if drink_type == "Soda":
    return find_drink(name, soda_flavors)
  elif drink_type == "Shake":
    return find_drink(name, shake_flavors)
  else:
    None

###AVAILABLE MEALS###
def display_available_meals(drink_type):
  drink_type = type_input

  # Soda #
  if drink_type == "Soda":
    print("Available Soda Meals:")
    for flavor in soda_flavors:
      print(flavor)
 
    # Shake # 
  elif drink_type == "Shake":
    print("Available Shakes:")
    for flavor in shake_flavors:
      print(flavor)

    # Else #  
  else:
    return "Invalid drink type"   

###SUMMARY###
def create_summary(name, amount, drink_type):
  order = select_drink(name, drink_type)
  drink_type = type_input
  if order:
    return f"You ordered {amount} glass(es) of {name}"
  else:
    return "Invalid drink type"
  
###RUN###
print("Welcome to the Drink Order System!")
type_input = input("Would you like order a *Soda* or a *Shake*? " )

display_available_meals(type_input)

name_input = input("What flavor would you like? ")
amount_input = input("How many glasses of that would you like? ")

result = create_summary(name_input, amount_input, type_input)
print(result)










