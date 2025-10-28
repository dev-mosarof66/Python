course = 'Python\'s for beginners'
print(course)

long_str = '''
Hi
I am
Mosarof Hossain.


'''
print(long_str)

# accessing the string index by forward method
print(course[0])
#accessing the string index by backward method => negative index
print(course[-1])


# javascript slice method
print(course[0:5]) # going to print 0 to 5 index
print(course[:5]) #going to print 0 to 5 again but the starting index not defined . so compiler assumes it as 0
print(course[0:]) #going to print whole string as no end index provided.
print(course[:]) #going to print whole string but no start or end index is provided.

# assignment 04

name= 'Mosarof Hossain'
print(name[0:-1])
#what is going to be the output.
# by providing negative index , it excludes those index say  => -4 => so it is going to exclude 4 characters from right
print(name[-15:-1]) # same as the name[0:-1]