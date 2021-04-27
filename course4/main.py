# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def id_type_value():
    #everything is an object
    #every object has an ID, type and value
    a=5
    print(type(a))
    print(id(a))
    # is operator(id comparison) if x=y =>vor avea acelas id (wtf?)
    x = 5
    y = 5
    print(x is y)
    print("-------")
    print(isinstance(5, float))
    print("-------")
    #value
    #mutable - value can change - lists dict
    #imutable - value does not change - numbers strings, tuples



    # mutable vs immutable int >immutable; list> imutable


def lists_comprehensions_tuples():
    #list mutable
    #tuple imutable
    print("lists")
    colors=['red','green','yellow']
    print(colors)
    color = 'blue'
    print(color in colors)
    print(color not in colors)
    shirt1=['alb','verde']
    shirt2=['rosu']
    print(shirt1+shirt2)
    print(shirt1*10)
    print(shirt1[1])
    #slice-


    print("tuples")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    id_type_value()
    lists_comprehensions_tuples()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
