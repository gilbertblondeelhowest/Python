getal1 = 100
getal2 = 300
product = -1


def geef_product():
    product = getal1 * getal2
    print(f"product is hier {product}")

getal1 = int(input("Geef een getal1 op:> "))
getal2 = int(input("Geef een getal2 op:> "))
geef_product()
print(product)

# correctie:
# def geef_product(getal1: int, getal2: int) -> int:
#     product = getal1 * getal2
#     return product


# x = int(input("Geef een getal1 op:> "))
# y = int(input("Geef een getal2 op:> "))
# print(f"Het product is {geef_product(x,y)}")
