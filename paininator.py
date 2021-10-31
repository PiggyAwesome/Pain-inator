import string

def main(code, independant=False):

    red = code
    rit = []
    total_ = 0
    for letter in string.ascii_letters + string.digits + " " + "\".?'!():=+-,":
        total_ += 1
        if independant == True:
            writ = f'{"_"* total_} = "{letter}"\n'
            writ2 = f'{"_"* total_} = "\{letter}\"\n'
            if letter == "\"":
                rit.append(writ2)
            else:
                rit.append(writ)
        if independant == False:
            red = red.replace(letter, "{"+"______________________________________________________________________________{}{}"+"_"* total_+"}")
        if independant == True:
            red = red.replace(letter, "{"+"_"* total_+"}")

    if independant == False:
        rit.append("import pain as ______________________________________________________________________________\n")

    total_ += 1
    if independant == True:
        rit.append(f'{"_"* total_} = exec\n')
        red = red.replace("exec", "{"+"_"* total_+"}")
    elif independant == False:
        red = red.replace("exec", "{"+"______________________________________________________________________________{}{}"+"_"* (total_- 1)+"}")
    
    total_ += 1

    if independant == True:
        rit.append(f'{"_"* total_} = eval\n')
        red = red.replace("eval", "{"+"_"* total_+"}")
    elif independant == False:
        red = red.replace("eval", "{"+"______________________________________________________________________________{}{}"+"_"* total_+"}")

    total_ -= 1
    if independant == False:
        rit.append(f"\n{'______________________________________________________________________________.'+'_'* total_}(f\"\"\"")
    elif independant == True:
        rit.append(f"\n{'_'* total_}(f\"\"\"")

    red = red.replace("{}{}", ".")
    bru = []
    reddet = red.splitlines()
    for r in reddet:
        bru.append(r.split("#")[-1])

    red = "\n".join(bru)

    rit.append(red)
    rit.append("\"\"\")")

    return "".join(rit)
