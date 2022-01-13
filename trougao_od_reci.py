# Напиши програм који исцртава троугао чије су ивице састављене од карактера дате речи. Реч се добија читањем слова са леве и десне ивице троугла наниже, док се на доњој ивици налази палиндром чија је десна
# половина та дата реч.
#
# Улаз: Са стандардног улаза се учитава реч дужине између 3 и 20 карактера.
#
# Излаз: На стандардни излаз исписати тражени троугао.
#
# Пример
# Улаз
# bravo
# Излаз
#     b
#    r r
#   a   a
#  v     v
# ovarbravo


def ispisi_n_puta(c, n):
    for i in range(n):
        print(c, sep="", end="")

s = input("Unesi rec: ")
n = len(s)                          # broji duzinu reci

ispisi_n_puta(" ", n-1)             # ispisuje prazno
print(s[0])                         # ispisuje prvo slovo unete reci za prvi red

for i in range(1, n-1):             # ispis po dva karaktera
    ispisi_n_puta(" ", n-1-i)       # ispis prvih praznina
    print(s[i], sep="", end="")     # ispis prvog karaktera
    ispisi_n_puta(" ", 2*i-1)       # ispis praznina do sledeceg karaktera
    print(s[i])                     # ispis drugog karaktera u istom redu

print(s[n-1:0:-1] + s[0:n])         # ispis poslednjeg reda
