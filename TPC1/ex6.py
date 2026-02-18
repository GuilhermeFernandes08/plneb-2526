def capicua(s):
    invertedstring=''
    for i in range(len(s)-1,-1,-1):
        invertedstring+=s[i]
    if invertedstring==s:
        return True
    else:
        return False

print(capicua('1991'))
print(capicua('aldeia'))


