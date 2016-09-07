from random import randrange
# The built-in exceptions are in inheritance hierarchy (just like C#) and the most base class is BaseException though in practice custom exceptions should derive from Exception class.

# It's recommended that custom exception class only takes a single string as the payload so that it's consistent with other exceptions when exception payload is retrieved.

def median(seq):
    length = len(seq)
    if length == 0:
        raise ValueError("median() arg is an empty sequence")
    items = sort(seq)
    if length & 1 == 0: # even length
        middleIndex = length / 2
        return (items[middleIndex] + items[middleIndex + 1])/2.0
    else:
        return items[length//2]
    


def main():
    number = randrange(100)
    while True:
        try:
            guess = int(input())
            # always specify the exception type; handling all exception is generally bad; this is similar to not catch Exception in C#
        except ValueError: 
            continue
        if guess == number:
            print("you win!")
            break

if __name__ == '__main__':
    main()

print(median([2, 4, 5]))