row_num = int(input())
for i in range(row_num):
  line = " " * (row_num - i - 1)
  line += "*" * (i+1)
  print(line)