# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#variable used to create an infinte loop
infinite_loop = 1

#list with all the items in the store [item, size]
full_list_of_items = []

#Tuple with user options
user_option = ("restock", "display", "sell_last_item", "sell_any_item")

#Function that initializes the store with the standard stock
def populate_the_store():
    list_of_item_types = ['shirt', 'scarf', 'glove', 'hat']
    list_of_sizes = ['S', 'M', 'L', 'XL', 'XXL']
    multiply_factor = 20
    #list of lists (items combined with sizes)
    for types in list_of_item_types:
        for sizes in list_of_sizes:
            for factor in range(multiply_factor):
                full_list_of_items.append([types, sizes])  # 4 item types * 5 sizes * 20 = 400 items


#Function that allows to restock the store
def restock_the_store():
    no_of_items = input("How manny items would you like to add?\n")
    for item in range(int(no_of_items)):
        print(f"Item number" + str(item+1)  +" :\n")
        new_item = input("Please enter the type of item:\n")
        new_item_size = input("Please enter the size of the new item:\n")
        full_list_of_items.append([new_item, new_item_size])


#Function to display all the items in the store
def display_all_items():
    print('This is a list of all the items.')
    print(full_list_of_items)


#Function to sell the last item added to store
def sell_last_item():
    sold_item = full_list_of_items.pop(-1)
    print("The sold item is: " + str(sold_item[0]) + ",size " + str(sold_item[1]) + ".\n")


#Function that allows to sell any item based on customer search
def sell_by_search():
    searched_item = input("Please enter the item you would like to sell:\n")
    searched_item_size = input("Please enter the size of the item:\n")
    purchase_flag = 0
    for item in range(len(full_list_of_items)):
        if ((full_list_of_items[item][0] == searched_item) and (full_list_of_items[item][1] ==searched_item_size)):
            print(f"You sold the item: ", {full_list_of_items[item][0]}, ", size", {full_list_of_items[item][1]}, ".\n")
            full_list_of_items.pop(item)
            purchase_flag = 1
            break
    if(purchase_flag == 0):
        print("Unfortunately the requested item is not in stock.\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ("restock", "display", "sell_last_item", "sell_any_item")

    print("Hello and welcome to THE STORE!\n What would you like to do next?\n")
    print("Please select one of the following options:\n")
    print("restock - to restock with new items\n")
    print("display - to display the entire stock\n")
    print("sell_last_item - to sell the last item added to stock\n")
    print("sell_any_item - to sell any item based on a customer search\n")

    #Add initial items to the store
    populate_the_store()

    while(infinite_loop):
        command = input("Your command is:")
        if(command == "restock"):
            restock_the_store()
        elif(command == "display"):
            display_all_items()
        elif(command == "sell_last_item"):
            sell_last_item()
        elif(command == "sell_any_item"):
            sell_by_search()
        else:
            print("No valid command was introduced. Please try one of the following:\n")
            print("|    restock     |       display     |      sell_last_item       |        sell_any_item      |\n")


    populate_the_store()
    restock_the_store()
    display_all_items()
    sell_last_item()
    display_all_items()
    sell_by_search()
    display_all_items()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
