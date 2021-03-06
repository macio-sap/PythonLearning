#!/usr/bin/python3
# 多线程与非多线程时间对比
# 测试多线程是否适合I/O密集型，用时间加减来检测多线程与非多线程
import time
from queue import Queue    # 用队列来保存线程的结果，先进先出
from threading import Thread

q_result = Queue()  # 新建一个队列对象
str_list = ['1', '3', '6', '8']

def str_to_int(arg, queue):
    result = int(arg)
    queue.put({arg: result})

def with_thread():
    thread_list = []
    start_time = time.time()
    for s in str_list:
        t = Thread(target=str_to_int, args=(s, q_result))
        t.start()
        thread_list.append(t)

    for i in thread_list:
        i.join()
    print('with thread:', (time.time() - start_time) * 1000)   # 显示毫秒
    return [q_result.get() for _ in range(len(str_list))]

def no_thread():
    start_time = time.time()
    q = Queue()
    for s in str_list:
        str_to_int(s, q)

    print('no thread:', (time.time() - start_time) * 1000)   #  显示毫秒
    return [q.get() for _ in range(len(str_list))]

def main():
    no_thread()
    with_thread()

if __name__ == '__main__':
    main() 