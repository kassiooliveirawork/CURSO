lista01= ["john", "mary", "luke", "zoe"]
lista01.append("mark")
lista01.sort()
qtd= lista01.count("mark")
lista01.insert(5, "pedro")
lista01.insert(3, "joão")

lista02= []
for i in range(1,21):
    lista02.append(i)
lista02.reverse()
pos= lista02.index(13)
lista02.remove(10)
lista02.remove(13)

lista03= lista01+lista02

print(lista01)
print(qtd)
print(lista02)
print(lista02[pos])
print(lista03)