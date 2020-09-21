# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

def say_hello(name):
    return f"Hello {name}"
print(say_hello("Harry"))
print(say_hello)

def parent(num):
    def first_child():
        print("Hi, I am Emma")
    def second_child():
        print("My name is Liam")
    if num ==1:
        return first_child
    else:
        return second_child
first = parent(1)
second = parent(2)
print(first())
print(second)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
