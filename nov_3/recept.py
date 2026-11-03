file = open("order.csv")
# for line in file:
#     print(line, end="")
# file.close()
# file = open("order.csv")
# first_line = file.readline()
# print(first_line)
# file.close()

# for i,line in enumerate(file):
#   if line != "" and i != 0 :
#     print(i, line)

# file.close()
total = 0
for i, line in enumerate(file):
  if i!=0:
    name, planet, quantity, price = line.strip().split(",")
    int_quantity=int(quantity)
    float_price = float(price)
    product = int_quantity*float_price
    total += product
    # print(name)
    # print(planet)
    # print(int(quantity))
    # print(f"{float(price):.2f}")
    print(f"{name}: {product:.2f}")

print(f"Total: {total:.2f}")
