from multiprocessing import Process, Queue, Pipe
import os

# 프로세스 간 통신에는 큐와 파이프가 사용된다. 큐는 thread-safe, process-safe하며 파이프는 큐보다 빠르지만 thread-safe하지 않다.


def f(x):
    print('{0} - 프로세스 ID: {1} (부모 프로세스 IDL {2})'.format(x, os.getpid(), os.getppid()))


def sender(q, n):
    # 큐에 메시지를 송신.
    q.put('{0}회째의 Hello World!'.format(n))


def pipe_sender(conn):
    # 송신측.
    conn.send('Hello World!')
    conn.close()


def pipe_receiver(conn):
    # 수신측.
    msg = conn.recv()
    print('메시지 수신: {0}'.format(msg))
    conn.close()


def main():

    q = Queue()

    # 메시지를 송수신하는 파이프 생성.
    parent_conn, child_conn = Pipe()

    for i in range(3):
        p = Process(target=f, args=(i, ))
        p.start()

        p2 = Process(target=sender, args=(q, i))
        p2.start()

    p.join()
    print(p.is_alive())

    # 큐로 보낸 메시지를 수신.
    print(q.get())
    print(q.get())

    p2.join()

    # 메시지 송신
    p3 = Process(target=pipe_sender, args=(child_conn,))
    p3.start()

    # 메시지 수신
    p3 = Process(target=pipe_receiver, args=(parent_conn,))
    p3.start()

    p3.join()


if __name__ == '__main__':
    main()
