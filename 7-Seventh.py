# Convert to Roman Number to Decimal


def rom_to_dec(rom) :
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}  
    x = 0
    num = 0
    while x < len(rom):
        if x+1<len(rom) and rom[x:x+2] in roman:
            num+=roman[rom[x:x+2]]
            x += 2
        else:
            num+=roman[rom[x]]
            x+=1
    return num

roman = input("Enter roman number..")
print(rom_to_dec(roman))