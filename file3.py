print("Hello!")
print("How are you?")
for i in range(2):
    print("Same old.")
narrow = ["town",  "street", "people"]
for i in narrow:
    print(f"Narrow {i}.")
tilp = "Tiny Liberal Party"
print(tilp)
for i in tilp.split(" "):
    print(i[0] + i[-1] + "!")
print("Mo-lec-u-lo!")
for i in range(2):
    print("The Molecular Man!")
bobbi = ("Bpobbi")
print(bobbi)
bobbi = bobbi.replace("p", "") + "?"
print(bobbi)
print("Babbi Burns?")
for i in range(2):
    print("NO!")
print("RABBI Burns.")
refrain = "Hey hey, come out tonight."
for i in range(2):
    print(refrain)
popscene = ["PO","PSC","EN","E"]
print("".join(popscene) + "!")
print("Grin! I said:")
toops = tilp.split(" ")
for index, i in enumerate(toops):
    print(toops[index - len(toops) + 1] + "!")
