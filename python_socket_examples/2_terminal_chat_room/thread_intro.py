import threading
# threading allows us to speed up programs by executing multiple tasks at the same time.
# each task will run on its own thread
# each thread can run simultaneously and share data with each other

# every thread when you start it must do SOMETHING, which we can define with a function
# our threads will then target these functions
# when we start the threads, the target functions will be run

def function1():
    for i in range(10):
        print("ONE ")
def function2():
    for i in range(10):
        print("TWO ")

def function3():
    for i in range(10):
        print("THREE ")

# if we call these functions we see the first function call MUST complete before the next
# they are executed linearly
function1()
function2()
function3()