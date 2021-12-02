#loading input
input_file = open("data/day2.txt","r")
navigation = {'up' : 0,
              'down': 0,
              'forward' : 0}
instructions = input_file.read().split('\n')[:-1]
instructions = [i.split(' ') for i in instructions]
for i in instructions:
    navigation[i[0]] += int(i[1])
print(navigation['forward']*(navigation['down'] - navigation['up']))
