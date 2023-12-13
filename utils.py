
import time
def stop_time(argument):
    def stop_time_decorator(f):

        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = f(*args, **kwargs)
            print(f"solution part{argument}: {res} \n completed in {(time.time() - start_time)} seconds")
            return res

        return wrapper

    return stop_time_decorator

def input(string=None, splitter = "\n"):
    if string:
        return string.split(splitter)
    return open("input.txt", 'r').read().split(splitter)
