# Review 1

def add_to_list(value, my_list=[]):
    """add value to list
    check:correct

    Parameters
    ----------
    value : any
    my_list : list, optional
        by default []

    Returns
    -------
    type : list
    """
    my_list.append(value)
    return my_list

# Review 2

def format_greeting(name, age):
    """ format_greeting
    check: incorrect
    Parameters
    ----------
    name : any
        name to greeting
    age : any
        age

    Returns
    -------
    string
    """
    return f"Hello, my name is {name} and I am {age} years old." # return should be f-string to autofill the parameters into it.

 

# Review 3
class Counter():
    """counter 
    check : incorrect

    """
    def __init__(self):
        """ this part initialize the Counter for using
        """
        self.count = 0

    def get_count(self):
        """ once this method called return the times it be called
        """
        self.count += 1
        return self.count

 

# Review 4

import threading

class SafeCounter:
    """ counter in thread
    check : correct
    """
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = SafeCounter()
threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()


# Review 5

def count_occurrences(lst):
    """count occurrences in a list
    check : incorrect
    Parameters
    ----------
    lst : list

    Returns
    -------
    dict for count
        use name for key and occurrence times as value
    """
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1 # here should be += not =+ typo thing.
        else:
            counts[item] = 1

    return counts

 