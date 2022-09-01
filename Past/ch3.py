
def gugudan(num):
    for i in range(2, 10):
        print("\n\n%d Dan is printed" % i)
        for j in range(1, 10):
            print(i, "X", j, "=", i*j, end="\t")
        print()


if __name__ == "__main__":
    gugudan(1)
    