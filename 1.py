from collections import Counter

txt = open("input.txt", "r").read()

def solution1(input):
	list1, list2 = [], []
	for n, row in enumerate(input.split('\n')):
		if row:
			vals = row.split()
			list1.append((int(vals[0]), n))
			list2.append((int(vals[1]), n))

	list1.sort(key= lambda e: e[0])
	list2.sort(key= lambda e: e[0])

	total_dist = 0
	for i in range(len(list1)):
		i_1 = list1[i][0]
		i_2 = list2[i][0]
		total_dist += max(i_1 - i_2, i_2 - i_1)

	return total_dist

def solution2(input):
	list1, list2 = [], []
	for n, row in enumerate(input.split('\n')):
		if row:
			vals = row.split()
			list1.append(int(vals[0]))
			list2.append(int(vals[1]))

	counter = Counter(list2)

	total_similarity = 0

	for n in list1:
		total_similarity += (n * counter[n])

	return total_similarity

TEST_DATA = '''3   4
4   3
2   5
1   3
3   9
3   3'''
TEST_ANSWER = 11

print(f"Task1 answer: {solution1(txt)}")
print(f"Task2 answer: {solution2(txt)}")