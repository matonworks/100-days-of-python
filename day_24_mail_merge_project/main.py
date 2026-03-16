PLACEHOLDER = "[name]"

with open("input/names/invited_names.txt") as n:
    names = n.readlines()

with open("input/letters/starting_letter.txt") as l:
    letter = l.read()

for name in names:
    name = name.strip() 
    new_letter = letter.replace(PLACEHOLDER, name)
    
    with open(f"output/readytosend/{name}.txt", "w") as w:
        w.write(new_letter)





