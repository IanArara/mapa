###Como definir as dimensões do mapa
quadrado = "0"
altura = int(input("Qual altura?")) 
largura = int(input("Qual largura?"))
Grade = [[quadrado]*largura for i in range(altura)]

###Onde começa o "P" personagem
x = int(input("Qual altura do início?")) -1
y = int(input("Qual largura do início?")) -1
Grade[x][y]="P"

###Como definir o final do jogo
fim_a = int(input("Qual altura do final?")) 
fim_l = int(input("Qual largura do final?"))
Grade[fim_a - 1][fim_l - 1] = "#"

###Como se movimenta o personagem "P" no mapa
def andar(): 
    global x
    global y
    movimento = input("Use WASD para se movimentar\n")
    if movimento == ("w"):
        x -= 1
        Grade[x + 1][y]=quadrado
    if movimento == ("s"):
        x += 1
        Grade[x - 1][y]=quadrado
    if movimento == ("d"):
        y += 1
        Grade[x][y - 1]=quadrado
    if movimento == ("a"):
        y -= 1
        Grade[x][y + 1]=quadrado
    Grade[x][y]="P"

###Evitar que o personagem "P" saia da matrix desejada, chegue nas bordas e dar uma mensagem de aviso

###Fazer uma parede que rodeie o mapa 
#Alguma coisa assim: 
#Grade = [[qudrado]*largura+1 for i in range(altura+1)]
#Grade toda a primeira linha  = "_"
#Grade toda a primeira coluna = "|"
#Grade toda a última linha = "_"
#Grade[largura] toda a última coluna = "|"

###Fazer uma visão do personagem que vai acompanhar ele em um raio de tantos quadrados



for l in Grade:
    print(l) 

while Grade[x][y] != Grade[fim_a-1][fim_l-1]:
    andar()
    for l in Grade:
        print(l)


print("Acabou")
