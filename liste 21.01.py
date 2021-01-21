"""Se citesc elementele unei liste, care reprezintă numere întregi (pozitive și negative). Să se afișeze la ecran:
	a) conținutul (elementele) listei /lista1
	b) lista sortată în ordine crescătoare / lista2
	c) lista sortată în ordine descrescătoare / lista3
	d) numărul de elemente din listă
	e) elementul MAX
	f) elementul MIN
	g) să se adauge la coadă în lista inițială elementul – 111. 
	    Să se afișeze lista nou-formată. / lista4
	h) să se adauge pe poziția a doua din lista inițială elementul – 222. 
	    Să se afișeze lista nou-formată. / lista5
2. Rezolvați problema de mai sus citind datele inițiale din fisierul input.txt."""

with open('input.txt','r') as f:
    a=f.readline()
print("lista initiala:",a)

a=a.split(',')

l2=list(a)
l2.sort()
print("lista 2:",(l2))

l3=list(a)
l3.sort(reverse=True)
print("lista 3:",(l3))

n=len(a)
print("in lista sunt ",(n),"elemente")

ma=max(a)
print("elementul maxim: ",(ma))

mi=min(a)
print("elementul minim: ",(mi))

l4=a
l4.extend([111])
print("lista 4:",(l4))

with open('input.txt','r') as f:
    a=f.readline()
a=a.split(',')

l5=a
l5[2]=222
print("lista 5:",(l5))
