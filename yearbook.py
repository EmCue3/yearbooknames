#With great assistance from Simon Zeng
#Alphabetizes a list of names by first initial of last name and first name
print(', '.join(y[:y.index(' ') + 2] for y in sorted((x.strip().split(', ')[1] + ' ' + x.strip().split(', ')[0][0] for x in open('input1.txt', 'r').readlines()), key=lambda k: k.split()[1] + k.split()[0])))
