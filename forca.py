palavra_secreta = ["f","u","t","e","b","o","l"]
letras_descobertas = []


print('***Bem vindo ao jogo da forca!***')
print('*********************************')

for i in range(0, len(palavra_secreta)) :
    letras_descobertas.append("-") 
    acertou = False 

while acertou == False :
  letra =str(input("digite a letra: "))
for i in range(0, len (palavra_secreta)) :

    if letra == palavra_secreta[1] :
       letras_descobertas[i] = letra
    print(letras_descobertas[i])
acertou = True 

for x in range(0, len (letras_descobertas)) :
   if  letras_descobertas[x] == "-" :
       acertou = False
for x in range(0, len (letras_descobertas)) :
   if  letras_descobertas[x] == "-" :
       acertou = False



       class Imprimir:
    def desenharNaTela(self, nErros):
        self.nErros = nErros

        if self.nErros == 0:
            print("""
              |||||||||||||
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
             ++++
            ++++++
            """)



            elif self.nErros == 1:
            print("""
              |||||||||||||
              ++         ***
              ++        *   *
              ++         ***
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
             ++++
            ++++++
            """)



            elif self.nErros == 2:
            print("""
              |||||||||||||
              ++         ***
              ++        *   *
              ++         ***
              ++          |
              ++          |
              ++          |
              ++          |
              ++
              ++
              ++
              ++
              ++
             ++++
            ++++++
            """)

             elif self.nErros == 3:
            print("""
              |||||||||||||
              ++         ***
              ++        *   *
              ++         ***
              ++         /|
              ++        / |
              ++          |
              ++          |
              ++
              ++
              ++
              ++
              ++
             ++++
            ++++++
            """)


            elif self.nErros == 4:
            print("""
              |||||||||||||
              ++         ***
              ++        *   *
              ++         ***
              ++         /|\ 
              ++        / | \ 
              ++          |
              ++          |
              ++
              ++
              ++
              ++
              ++
             ++++
            ++++++
            """)



elif self.nErros == 5:
            print("""
              |||||||||||||
              ++         ***
              ++        *   *
              ++         ***
              ++         /|\ 
              ++        / | \ 
              ++          |
              ++          |
              ++         /
              ++        /
              ++
              ++
              ++
             ++++
            ++++++
            """)



            else:
            print("""
              |||||||||||||
              ++         ***
              ++        *   *
              ++         ***
              ++         /|\ 
              ++        / | \ 
              ++          |
              ++          |
              ++         / \ 
              ++        /   \ 
              ++
              ++
              ++
             ++++
            ++++++
            """)



