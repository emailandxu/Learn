"""
overview:
    threading 模块提供基于面向对象的线程框架. 

before:
    可以通过_thread模块的start_new_thread方法创造并且运行新线程.

after:
    1. 由threading模块生成的线程不会随主线程退出.
    2. 可以通过继承threading模块的Thread类 (并且实现run方法), 实例化之后调用start方法开始线程.
    3. join方法阻塞调用它的线程, 一直到它所属的线程退出为止.
"""
import threading

class MyThread(threading.Thread):
    
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count
        self.mutex = mutex
        super(MyThread, self).__init__()

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print(self.myId, '=>', i)


stdoutmutex = threading.Lock()

threads = []

for i in range(3):
    thread = MyThread(i, 5, stdoutmutex)
    thread.start()    # doubt
    threads.append(thread)

for thread in threads:
    thread.join()

print('Main thread exiting.')
