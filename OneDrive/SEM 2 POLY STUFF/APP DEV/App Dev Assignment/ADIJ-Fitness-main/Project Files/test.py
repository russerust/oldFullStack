def main():
    print(sum(10))


def sum(x):
    if (x >= 1):
        return (x + sum(x-1))
    else:
        return x


main()
