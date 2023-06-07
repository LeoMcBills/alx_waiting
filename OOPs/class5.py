# class attributes

class Q:

    count = 0

    def __init__(self):
        type(self).count += 1

    def __del__(self):
        type(self).count -= 1

if __name__ == "__main__":
    x = Q()
    print(Q.count)
    print()
    t = Q()
    print(t.count)
    print()
    y = Q()
    print(Q.count)
    print()

    del y
    print(Q.count)
    print()