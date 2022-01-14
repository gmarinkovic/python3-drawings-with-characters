# За дато n исписати елементе низа 1, 2, 4, 5, 7, 9, 10, 12, 14, 16, 17, … који се формира тако што се полазећи
# од броја 1 – приказује један непаран природни број, затим следећа два парна – 2, 4; па следећа 3 непарна –
# 5, 7, 9; следећа 4 парна – 10, 12, 14, 16, … итд. Последња серија садржи n елемената.
#
# Улаз: Са стандардног улаза се учитава природан број n у границама од 1 до 40.
#
# Излаз: На стандардни излаз исписати елементе траженог низа, сваку подсерију у посебном реду, при чему
# се иза сваког броја исписује један размак.
#
# Пример
# Улаз
# 5
# Излаз
# 1
# 2 4
# 5 7 9
# 10 12 14 16
# 17 19 21 23 25

def niz(pocetni,n):
    for i in range (pocetni,pocetni+n*2,2):
        print(i," ",sep="",end="")
    print()

n = int(input("Uneti broj n za grupu parnih i neparnih elemneata: "))
k=1
for i in range (1,n+1):
    if i//2 != 0 :
        niz(k,i)
        k=k+i*2
    else:
        niz(k,i)
        k = k + i * 2
    k=k-1
