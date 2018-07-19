import time, threading


balance = 0
lock = threading.Lock()


def change(n):
    global balance
    balance = balance + n
    print('add to %d' % balance)

    balance = balance - n
    print('minus to %d' % balance)


def run_thread(n):
    for i in range(10000000):
        # change(n)
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)