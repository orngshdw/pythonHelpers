filename="Darkside.reg"


def reg_to_mintty():
    mintty={}
    mintty["Colour21"]="BoldWhite"
    mintty["Colour20"]="White"
    mintty["Colour19"]="BoldCyan"
    mintty["Colour18"]="Cyan"
    mintty["Colour17"]="BoldMagenta"
    mintty["Colour16"]="Magenta"
    mintty["Colour15"]="BoldBlue"
    mintty["Colour14"]="Blue"
    mintty["Colour13"]="BoldYellow"
    mintty["Colour12"]="Yellow"
    mintty["Colour11"]="BoldGreen"
    mintty["Colour9"]="BoldRed"
    mintty["Colour8"]="Red"
    mintty["Colour7"]="BoldBlack"
    mintty["Colour6"]="Black"
    mintty["Colour5"]="Black"
    mintty["Colour0"]="ForegroundColour"
    mintty["Colour2"]="BackgroundColour"
    return mintty

mintty = reg_to_mintty()
converted = open("convertedmintty", "w+")
with open(filename, "r") as file:
    line = file.readline()
    while line:
        print(line)
        index = line.find('=')
        indexstart = index + 2 if index != -1 else None
        reg_color = line[1:index-1] if index != -1 else None
        
        mintty_color = mintty[reg_color] if reg_color in mintty else None
        indexstart = None if index == -1 else index + 2
        
        if indexstart and mintty_color:
            value = line[indexstart:-2]
            converted.write(f"{mintty_color}={value}\n")
        line = file.readline()
    file.close()

converted.close()

