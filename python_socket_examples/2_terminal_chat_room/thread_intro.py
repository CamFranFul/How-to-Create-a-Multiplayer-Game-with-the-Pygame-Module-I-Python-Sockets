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

# WE can execute these functions concurrently using threads! We must have a target for a thread.
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function3)

t1.start()
t2.start()
t3.start()

# threads can only be run once. If you want to reuse, you must redefine.
t1 = threading.Thread(target=function1)
t1.start()

# if you want to 'pause' the main program until a thread is done you can
t1 = threading.Thread(target=function1)
t1.start()
t1.join() # this pauses the main program until the thread is complete
print("Threading rules!")

