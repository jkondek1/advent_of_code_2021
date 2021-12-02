#loading input
input_file = open("data/day2.txt","r")
navigation = {'aim' : 0,
              'forward' : 0,
              'depth': 0}
instructions = input_file.read().split('\n')[:-1]
instructions = [i.split(' ') for i in instructions]

for i in instructions:
    cmd = i[0]
    if cmd == 'forward':
        navigation['forward'] += int(i[1])
        navigation['depth'] += (int(i[1]) * navigation['aim'])
    elif cmd == 'up':
        navigation['aim'] -= int(i[1])
    else:
        navigation['aim'] += int(i[1])

print(navigation['forward']*navigation['depth'])
