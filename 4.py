import numpy as np

# read text file into 2 dimensional char array
with open("input.txt", 'r') as file:
	lines = file.readlines()
	array = np.array([list(line.rstrip()) for line in lines])


# part 1
def get_all_diagonals(arr):
	diagonals = []
	rows, cols = arr.shape

	for offset in range(-rows + 1, cols):
		diag = arr.diagonal(offset=offset)
		diag = ''.join(diag.astype(str))
		diagonals.append(diag)

	return diagonals


horizontal = 0
for line in array:
	line = ''.join(line.astype(str))
	horizontal += line.count("XMAS")
	horizontal += line.count("SAMX")

vertical = 0
for line in array.T:
	line = ''.join(line.astype(str))
	vertical += line.count("XMAS")
	vertical += line.count("SAMX")

diagonal1 = 0
diagonals1 = get_all_diagonals(array)
for line in diagonals1:
	diagonal1 += line.count("XMAS")
	diagonal1 += line.count("SAMX")

diagonal2 = 0
diagonals2 = get_all_diagonals(np.flip(array, 0))
for line in diagonals2:
	diagonal2 += line.count("XMAS")
	diagonal2 += line.count("SAMX")

print(f"Total XMAS count: {horizontal + vertical + diagonal1 + diagonal2}")