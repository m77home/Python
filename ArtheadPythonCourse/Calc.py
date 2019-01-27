
def main():
    x = 10
    y = x
    print(id(x))
    print(id(y))
    x += 1
    print(id(x))
    print(id(y))
    print(x)


if __name__ == '__main__':
    main()

