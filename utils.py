
import time
def stop_time(f):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        print(f"solution: {res} \n completed in {(time.time() - start_time)} seconds")
        return res

    return wrapper


def split_input(string=None, splitter = "\n"):
    if string:
        return string.split(splitter)
    return open("input.txt", 'r').read().split(splitter)
