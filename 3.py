import re

txt_file = open("input.txt", "r").read()

def solution1(input):
	total = 0
	calls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)
	for call in calls:
		nums = [ re.sub(r"[^0-9]*", "", n) for n in call.split(',')]
		total += int(nums[0]) * int(nums[1])
	return total

TEST_INPUT = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''
TEST_OUTPUT = 161

# print(f"expected output: {TEST_OUTPUT} - actual output: {solution1(TEST_INPUT)}")
print(f"answer: {solution1(txt_file)}")