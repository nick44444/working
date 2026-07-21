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
office = "Time for work!"
for i in range(4):
    office += " WORK!"
print(office)
prac = "Practise!"
print(prac)
endo = prac[-1]
prac = prac[:-1].replace("s", "c")
perfo_sent = prac + " makes perfect" + endo
print(perfo_sent)
almanac = "It's my Autumn Almanac."
for i in range(3):
    print("YES!")
print(almanac)
hoy = "hoy"
hoy = hoy.title() + "nors"
print(hoy)
count = "Count"
face = ["e", "c", "a", "f", "n", "i", "b"]
face_comp = ""
for i in range(len(face)):
    face_comp += face[(i + 1) * -1]
print(count + " " + face_comp.title() + " must win!")
middo = "Mid"
culd = "Mudi"
middo = (middo + " " + culd).replace("M", "K")
print(middo + "?")
gasso = "bye"
mike = ["m", "i", "c", "h", "a", "e", "l"]
gasso2 = gasso.title() + " " + gasso + " " + "".join(mike).title() + "!"
print(gasso2)
tolby = "Tol"
bius = ["b", "I", "U", "S"]
print(tolby, bius)
for i in range(len(bius)):
    tolby += bius[i].lower()
print(tolby + "!")
print("Token check!")
bale = "Bale"
ful = ["f", "u", "p"]
for i in ful:
    bale += i
print(bale.replace("p", "l") + ".")
great = "Great"
great += " "
gus = "gusso"
for index, i in enumerate(gus):
    if index < len(gus) - 2:
        great += i
print(great.replace("s", "y!"))
new_pm = ["A", "n", "d", "y", " "]
new_pm = "".join(new_pm) + "Burnham"
print(new_pm)
tom = "Tommy"
more = ["Robinson", "is", "an", "idiot"]
print(tom + " " + " ".join(more) + ".")