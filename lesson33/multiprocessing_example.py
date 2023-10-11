from multiprocessing import Process, Pool, Queue, Lock
import time

def f(x):
    print(f'hello,{x}')

def fx(x):
    return x*x

def other_ord_func(q):
    q.put([42, None, 'mr hello'])

def func_to_test_lock(l,x):
    l.acquire()
    try:
        print(f'hello mr{x}, welcome again')
    finally:
        l.release()

if __name__ == '__main__':
    '''
    proc = Process(target=f, args=('Jhonatan',))
    proc.start()
    proc.join()
    q = Queue()
    p = Process(target=other_ord_func, args=(q,))
    p.start()
    print(q.get())
    p.join()
    with Pool(3)as p:
        print(p.map(fx,[1,2,3]))'''
    lock = Lock()
    for numb in range(15):
        pr = Process(target=func_to_test_lock, args=(lock, numb))
        pr.start()
