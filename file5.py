belper = "Belper"
print(belper + "?")
nope = f"No, not {belper}: " + "-".join(list(belper.upper())) + ". " + belper.upper() + "!"
print(nope)
att = ["A","T"]
att2 = att[0] +  "".join(att)
print(att2)
booh = ["Heck", "of", "out", "Bat"]
heb = ""
for i in range(len(booh)):
    heb += booh[(i + 1) * -1] + " "
print(heb[:-1] + "!")
tobbu = ["g", "y", "t", "u", "s"]
tobbu2 = "".join([tobbu[0], tobbu[3], tobbu[-1], tobbu[2], tobbu[1]]).title()
print(tobbu2 + "!")
