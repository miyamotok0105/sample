import threading

def worker(num):
    print(num)

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

#argsに引数を入れた