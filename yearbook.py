#With great assistance from Simon Zeng
print(', '.join(y[:y.index(' ') + 2] for y in sorted((x.strip().split(', ')[1] + ' ' + x.strip().split(', ')[0][0] for x in open('yes.txt', 'r').readlines()), key=lambda k: k.split()[1] + k.split()[0])))
