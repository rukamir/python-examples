from multiprocessing import Pool, Semaphore, cpu_count
import sys

sem = Semaphore(value=3)

def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


def mycallback(param):
    print(param)


if __name__ == "__main__":
    print("hello world")
    workers = cpu_count() - 1
    results = []

    with Pool(processes=workers) as pool:
        for x in range(0, 25):
            results.append(pool.apply_async(recur_fibo, (32,), callback=mycallback))

        pool.close()
        pool.join()

    sum = 0
    for result in results:
        sum += result.get()

    print(sum)
