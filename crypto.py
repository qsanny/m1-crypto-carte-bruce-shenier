

def encode(message, cle):
    message=message.upper()
    cle=cle.upper()
    encoded_msg = ""
    for i, m in enumerate(message):
        nm = ord(m) - 65 + 1
        nc = ord(cle[i]) - 65 + 1

        ne = (nm + nc)
        if ne > 26:
            ne = ne - 26
        # print(ne)
        encoded_msg+=chr(ne + 65 - 1)
    return encoded_msg

def generatekey(n):
    return "acrpm"
