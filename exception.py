try:
    x = int(input("Input a number: "))
    print(x)
except ValueError:
    print("Something went wrong")   
finally:
    print("finished")    