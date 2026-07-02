lib = "Lib"
rary = ["r", "a", "r", "y"]
print(lib)
for i in range(len(rary)):
    lib += rary[i]
lib += "!"
print(lib)
printo = "Message"
print(printo + ":")
for i in range(3):
    if i == 1:
        print("FOILED!")
    else:
        print("FAILED!")
tob = "To Tobby"
print(tob)
tob += ", so Bobby."
print(tob)
gant = "Goose"
print(gant)
for index, i in enumerate(gant):
    print(f"{gant} #{index + 1}!")
fors = "Forsa!"
print(fors)
fors = fors.replace("r", "o")
print("No! " + fors)
belief = "Moral uplift?"
print(belief + " No:")
for i in belief.replace("?", "").split(" "):
    print(i.upper() + "!")
sir = "Sir"
print(f"Hello {gant}!")
new_gant= "That's " + sir.upper() + f" {gant} to you!"
print(new_gant)