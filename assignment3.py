def main():
    list = []
    n = int(input("size of list: "))

    for i in range(0, n):
        element = int(input("Enter elements: "))
        list.append(element)

    #call to print function
    print(sum(list))
    print(mulitplication(list))
    print(reverse_list(list))

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

def reverse_list(list):
    list.reverse()
    return list

if __name__ == "__main__":
    main()