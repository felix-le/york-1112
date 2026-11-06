file = open("results.csv")

for i, line in enumerate(file):
  print(line)
  # if i > 0:
  #   print(line, end="")