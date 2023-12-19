
import time
def stop_time(f):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        print(f"solution: {res} \n completed in {(time.time() - start_time)} seconds")
        return res

    return wrapper


def split_input(string=None, splitter = "\n", remove_empty=False):
    if string:
        return string.split(splitter)
    if remove_empty:
        return [x for x in open('input.txt', 'r').read().split(splitter) if x!='']
    else:
        return open('input.txt', 'r').read().split(splitter)
     

def print_matrix(matrix):
    for row in matrix:
        print(' '.join([str(element) for element in row]))

