data_list = [3, 9, 4, 5]

data_length = len(data_list)

for i in range(data_length):
  for j in range(0, data_length-i-1):
    if data_list[j] > data_list[j + 1]:
      data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]

print(data_list)
