input_file = open("input.txt", "r").read()

def solution1(input):
	count = 0
	for row in input.split("\n"):
		row_list = [int(n) for n in row.split()]
		if len(row_list) < 2:
			continue
		is_positive_diff = row_list[1] - row_list[0] > 0
		flag = True
		for i in range(1, len(row_list)):
			diff = row_list[i] - row_list[i-1]
			if ((diff > 0) == is_positive_diff) and (-3 <= diff <= 3 and diff != 0):
				continue
			else:
				flag = False
				break
		if flag:
			count += 1
	return count

def solution2(input):
	count = 0
	# i am fully aware this is not a good way to approach this - short on time today

	def is_safe(arr):
		is_positive_diff = arr[1] - arr[0] > 0
		flag = True
		for i in range(1, len(arr)):
			diff = arr[i] - arr[i - 1]
			if ((diff > 0) == is_positive_diff) and (-3 <= diff <= 3 and diff != 0):
				continue
			else:
				flag = False
				break
		return flag

	for row in input.split("\n"):
		row_list = [int(n) for n in row.split()]
		if len(row_list) < 2:
			continue
		if is_safe(row_list):
			count += 1
		else:
			for i in range(len(row_list)):
				copy = [int(n) for n in row.split()]
				copy.pop(i)
				if is_safe(copy):
					count += 1
					break
	
	return count

TEST_INPUT = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

TEST_OUTPUT = 4

# print(f"expected output: {TEST_OUTPUT} - actual output: {solution2(TEST_INPUT)}")
print(f"answer: {solution2(input_file)}")