from shlex import join
fals_text = input("text:")
textlist = fals_text.split(" ")

print(textlist)

stempel_vokale = "aeiouAEIOU"

Gestempelte_worte = {}
for index, wort in enumerate(textlist) :
    schlüssel = f"wort{index}"
    Gestempelte_worte[schlüssel] = wort

print(Gestempelte_worte)

beringte_text = {}

for schlüssel, wert in Gestempelte_worte.items():
    sauberer_string = "".join([char for char in wert  if char in stempel_vokale])




    beringte_text[schlüssel] = (wert, sauberer_string) #+ Gestempelte_worte



    print(beringte_text)

#in einzelde wörter umwandeln und jeweils in stempel verwandeln