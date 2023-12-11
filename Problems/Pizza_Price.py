print("Welcome to Pizza")
size=input("what size pizza do you want?S,M,L?")
addpep=input("add pep?Y,N")
addcheese=input("add cheese?Y,N")

price=0

if size=="S":
    price+=100
elif size=="M":
    price+=200
else:
    price+=300
if addpep=="Y":
    if size=="S":
        price+=5
    else:
        price+=7
if addcheese=="Y":
    price+10
print(f"Your final bill is {price} rs")