# Soal keluarkan hasil bilang prima seperti ini "2,3,5,7,11,13,17"

for i in range(2, 18):
  prima = True

  for j in range(2, i):
    if (i % j == 0):
      prima = False

  if prima:
    print(i)
