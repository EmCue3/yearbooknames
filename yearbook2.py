#With great assistance from Simon Zeng
#Alphabetizes a list of names by full last name, then by first name
print(', '.join(sorted((x.strip().split(', ')[1] + ' ' + x.strip().split(', ')[0] for x in open('input1.txt', 'r').readlines()), key=lambda k: k.split()[1] + k.split()[0])))
