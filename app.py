course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
# this will give back the letter at the very end of the string, all negative numbers will start at the end of the string


print(course[0:3])
# this will return the indexs until the 3 index so it returns Pyt
print(course[:3])  # Python will automatically start at the 0 index

print(course[0:])
# if you do not define the end index Python will stop at the end of the string
