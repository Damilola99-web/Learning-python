# while loop
i = 1
while i < 100:
    print(i)
    i += 1


# for loop
list = ["ac","ab","agg"]
for morpheme in list:
    print(morpheme)

for x in range(200, 500):
    print(x)    
else:
    print("loop done")    


twod = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]   

for arr in twod:
    for number in arr:
        print(number)