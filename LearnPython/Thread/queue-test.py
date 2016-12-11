"""
overview:
    只要队列同步对自身的访问, 线程间的交互 (数据传递) 将自动同步.

before:
    可以通过锁机制同步线程对象间的数据传递.

after:
    1. queue的get和put方法有阻塞选项参数block, 默认为True, 队列空的时候调用get方法的线程阻塞, 队列满的时候调用put方法的线程阻塞.
"""

import threading, queue, time

numconsumers = 2
numproducers = 4
nummessages = 5

safeprint = threading.Lock()

dataQueue = queue.Queue(maxsize=3)

def producer(idnum):
	for msg in range(nummessages):
		dataQueue.put("producer[%s] => %s"%(idnum, msg))
		with safeprint:
			print('produce', msg)

def consumer(idnum):
	while True:
		try:
			data = dataQueue.get(block=True)
		except queue.Empty as e:
			pass
		else:
			with safeprint:
				print('consumer[%s] got %s'%(idnum, data))


p_t = threading.Thread(target=producer, args=(1,))
c_t = threading.Thread(target=consumer, args=(1,))

c_t.daemon = True

p_t.start()
c_t.start()

p_t.join()

print('Main exiting')
