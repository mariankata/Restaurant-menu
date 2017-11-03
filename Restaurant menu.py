#Our daily menu
print "\nPlease enter the meals and prices\nthat you would like to have in your MENU!"
meal_list = {}
while True:
    question = raw_input("\nWould you like to enter a new meal to your MENU? (yes/no): ")
    if question == "yes":
        meal = raw_input("\nPlease enter a name for a meal: ")
        price = float(raw_input("\nPlease enter a price for the above given meal: "))
        meal_list[meal] = price
    elif question == "no":
        print "Thank you for using our program!"
        break
    else:
        print "\nUse just 'yes' or 'no' as an answer, please!"
with open("menu_list.txt", "w+") as menu_list_file:
    print "This is the list of meals for our MENU :\n"
    menu_list_file.write("This is the list of meals for our MENU :\n")
    for meal in meal_list:
        menu_list_file.write(meal + " - " + str(price) + ";\n")