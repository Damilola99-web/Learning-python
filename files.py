country_file = open("countries.txt", "r")
for country in country_file.readlines():
    print(country)
# r read
# r+ read and write
# w write
# a append

# .readline() print first line then next line

open("new.txt", "w").write("this is overwritten")
# overite
