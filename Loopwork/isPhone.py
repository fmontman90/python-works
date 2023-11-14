def isPhonenum(text):
    if len(text) != 12: #checks for 12 chars 1st
        return False
    
    for i in range(0,3): #checks area code
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7): #checks first three digits
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return  False
    return True

print('312-333-4456 is a phone number:')
print(isPhonenum('312-333-4456'))
print('Garbageshoot is a phone number')
print(isPhonenum('Garbageshoot'))
    