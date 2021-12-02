#loading input
input_file = open("data/day1.txt","r")
numbers = input_file.read().split('\n')[:-1]
trios = [int(numbers[index]) + int(numbers[index-1]) + int(numbers[index-2]) for index in range(2,len(numbers))]
positive_changes = [int(trios[index]) - int(trios[index-1]) > 0 for index in range(1,len(trios))]
print('number of measurements', len(numbers))
print('number of triplets', len(trios))
print('number of increases in triplets',sum(positive_changes))
