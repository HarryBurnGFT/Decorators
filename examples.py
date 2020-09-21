from decorators import *
import math
@do_twice
def say_whee():
    print("Whee!")

@timer
def waist_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}"
    else:
        return f"Whoa {name}! {age} already! You are growing up!"

math.factorial = debug(math.factorial)
def approx_e(terms=18):
    return sum(1/math.factorial(n) for n in range(terms))

@slow_down
def countdown(fromno):
    if fromno < 1:
        print("Lift off!!")
    else:
        print(fromno)
        countdown(fromno-1)



