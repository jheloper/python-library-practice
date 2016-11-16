from multiprocessing import Process, Lock, Pool


def f(lock, i):
    # lock이 unlock 상태가 될 떄까지 block.
    lock.acquire()
    # 처리 순번 출력.
    print('{0}번째 프로세스 실행 중'.format(i))
    # lock 해제.
    lock.release()


def f2(x):
    return x * x


def main():
    # lock 객체.
    lock = Lock()

    for i in range(3):
        p = Process(target=f, args=(lock,i))
        p.start()

    p.join()

    # 프로세스 수 상한을 4개로 설정.
    pool = Pool(processes=4)
    # 비동기 처리.
    result = pool.apply_async(f2, [10])
    print(result.get())

    with Pool(5) as p:
        print(p.map(f2, [1, 2, 3]))


if __name__ == '__main__':
    main()
