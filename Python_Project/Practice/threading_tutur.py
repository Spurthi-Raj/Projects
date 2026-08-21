import threading
import time

# def task():
#     for i in range(3):
#         print("Running task.....")
#         time.sleep(2)

# t1 = threading.Thread(target=task)
# t1.start()
# # t1.join()
# # t1.run()
# print("Main thread continues..")

# *************************************************************************************************************************

# Lock mechanism
# lock = threading.Lock()
# def print_message(name):
#     lock.acquire()
#     print(f"{name} entered")
#     time.sleep(2)
#     print(f"{name} leaving")
#     lock.release()

# t1 = threading.Thread(target = print_message,args=("Thread-1",))
# t2 = threading.Thread(target = print_message,args=("Thread-2",))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# *************************************************************************************************************************

# lock = threading.Lock()
# def print_message(name):
#     with lock:              # automatically handle acquire and release
#         print(f"{name} entered")
#         time.sleep(2)
#         print(f"{name} leaving")

# t1 = threading.Thread(target = print_message,args=("Thread-1",))
# t2 = threading.Thread(target = print_message,args=("Thread-2",))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# *************************************************************************************************************************


def task1(message):
    for i in range(3):
        print(f"{message} task is running..........")
        time.sleep(2)

def task2(message):
    for i in range(3):
        print(f"{message} task is running..........")
        time.sleep(2)

t1 = threading.Thread(target=task1,args=('Thread-1',))
t2 = threading.Thread(target=task2,args=('Thread-2',))
t1.start()
t2.start()
t1.join()
t2.join()
print("Main thread finished")