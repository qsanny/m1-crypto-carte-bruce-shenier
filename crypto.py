

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


def decode(message):
    # to decode we need the init state of the cards
    pass

def generatekey(n):
    # key must have same lenth as the message. 
    # n is the size of the key we want to generate

    return "acrpm"
