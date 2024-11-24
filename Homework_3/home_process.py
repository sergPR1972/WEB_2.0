from multiprocessing import Pool, cpu_count
from time import time

def factorize(number):
    result = [i for i in range(1, number+1) if number % i == 0]
    print(result)


if __name__ == '__main__':
    with Pool(cpu_count()) as p:
        start_time = time()
        p.map(factorize, [128, 255, 99999, 10651060],)
        p.close()
        p.join()
        stop_time = time()
    print(f"time: {stop_time - start_time} sec.")