rows = int(input())
init_set = [0]
operations = []
for i in range(rows):
	line = input()
	temp_row = line.split(' ')
	for i in range(0, len(temp_row)):
		temp_row[i] = int(temp_row[i])
	operations.append(temp_row)

for i in operations:
	if i[0] == 1:
		init_set.append(i[1])
	if i[0] == 2:
		for j in range(len(init_set)):
			init_set[j] = init_set[j] ^ i[1]
	if i[0] == 3:
		print(max(init_set))


