#Long Code
def find_missing_letter(chars):
    import string
    valsLower = [item.lower() for item in chars]
    valsUpper = [item.upper() for item in chars]
    alphabet = [*string.ascii_lowercase]
    alphabetUpper = [*string.ascii_uppercase]
    if chars[0] in alphabetUpper:
        first = valsLower[0]
        last = valsLower[-1]
        firstLetterAlphabet = alphabet.index(first)
        lastLetterAlphabet = alphabet.index(last)+1
        realList = []
        for i in range(firstLetterAlphabet,lastLetterAlphabet):
            realList.append(alphabet[i])
        for i in range(len(realList)-1):
            if realList[i] != valsLower[i]:
                return realList[i].upper()
    else:
        first = valsLower[0]
        last = valsLower[-1]
        firstLetterAlphabet = alphabet.index(first)
        lastLetterAlphabet = alphabet.index(last)+1
        realList = []
        for i in range(firstLetterAlphabet,lastLetterAlphabet):
            realList.append(alphabet[i])
        for i in range(len(realList)-1):
            if realList[i] != valsLower[i]:
                return realList[i]
    
    
#But if we use ord()


#Short Code
def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if ord(chars[i]) != ord(chars[i + 1]) - 1:
            return chr(ord(chars[i]) + 1)


        


