# 1. Real-World Python Dictionary Applications
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
# I'm assuming you'd like me to update the menu with commands, rather than directly editing the text.
# For the record, directly editing the text would be faster. I would do that if I were doing this in real life.
restaurant_menu.update({"Beverages" : {"Fountain drinks": 1.99, "Coffee": 5.99, "Water": 0}})
restaurant_menu["Main Course"]["Steak"] = 17.99
restaurant_menu["Starters"].pop("Bruschetta")
print(restaurant_menu)