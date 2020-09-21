'''
def my_decorator(func):
    def wrapper():
        print("something is happenning before")
        func()
        print("after")
    return wrapper()

def say_whee():
    print("say WHEE!!")

abc = my_decorator(say_whee)
print(abc)
'''
from datetime import datetime

def not_during_night(func):
    def wrapper():
        if 1==1: #7 <= datetime.now().hour < 22:
            func()
        else:
            pass
        return 1
    return wrapper

@not_during_night
def say_whee():
    print("say WHEE!!")


print(say_whee())