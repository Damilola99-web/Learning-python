# def greet(name = "rasheed"):
#     print("welcome", name)

# greet("korede")

# def addNum(*numbers):
#     total = sum(numbers)
#     return total

# print(addNum(1,2,3,4,5,6))

def oddOrEven(number):
    num = int(number)
    if num > 0:
        oddoev = num % 2
        if oddoev == 0:
            return "even"
        else:
            return "odd"
    else:
        return "Enter a valid number greater than 0"


print(oddOrEven(1))

