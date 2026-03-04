import re

f = open('TPC3/dicionario_medico.txt', 'r', encoding='utf8')
text=f.read()


text=re.sub(r'\n\n','\n\n@',text)

text=re.sub(r'\f','\n',text)

text=re.sub(r'\n\n@\n([A-ZÀ-Ú])',r'\n\1',text) 

text = re.sub(r'([a-zà-ú])\s*\n\n@\n\s*([a-zà-ú])',r'\1 \2',text)

text=re.sub(r'@','',text)
print(text)

f2=open("dicionario_medico_tratado.txt", "w", encoding="utf-8")
f2.write(text)


texto = text.split("\n\n")
print(len(texto))