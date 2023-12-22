import threading

def funA():
    for i in range(1000):
        print("Calling function A!")

def funB():
    for i in range(1000):
        print("Calling function B!")

t1 = threading.Thread(target=funA)
t2 = threading.Thread(target=funB)

t1.start()
t1.join()
t2.start()
