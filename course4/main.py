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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    id_type_value()

    #is operator(id comparison) if x=y =>vor avea acelas id (wtf?)
    x=5
    y=5
    print(x is y)

    #mutable vs immutable int >immutable; list> imutable

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
