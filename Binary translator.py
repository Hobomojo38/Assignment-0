String = "sophie"

out = ""
for i in String:
    value = ord(i)
    count = 128
    
    while count > 0:
        if value > count:
            out += "1"
            value -= count
        else:
            out += "0"
        count = count / 2 if count != 1 else 0

print(out)