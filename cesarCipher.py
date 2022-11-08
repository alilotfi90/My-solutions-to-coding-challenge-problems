def caesarCipherEncryptor(string, key):
    lis=list(string)
    for index in range(len(string)):
        lis[index]=chr( ( ord(string[index])-97+key )%26 +97 )
    string="".join(lis)
    return string
string="abz"
key=1
print(caesarCipherEncryptor(string, key))