print(', '.join(sorted((x.strip().split(', ')[1] + ' ' + x.strip().split(', ')[0] for x in open('yes2.txt', 'r').readlines()), key=lambda k: k.split()[1] + k.split()[0])))
