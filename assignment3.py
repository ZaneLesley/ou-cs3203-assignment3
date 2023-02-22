def main():
    list = []
    n = int(input("size of list: "))

    for i in range(0, n):
        element = int(input("Enter elements: "))
        list.append(element)

    print(sum(list))
    print(mulitplication(list))

def sum(list):
    sum = 0 
    for x in list:
        sum = sum + x
    return sum

def mulitplication(list):
    product = 1
    for x in list:
        product = product * x
    return product


if __name__ == "__main__":
    main()