#loading input
input_file = open("data/day1.txt","r")
numbers = input_file.read().split('\n')[:-1]
positive_changes = [int(numbers[index]) - int(numbers[index-1]) > 0 for index in range(1,len(numbers))]
print('number of measurements', len(numbers))
print('number of increases',sum(positive_changes))
