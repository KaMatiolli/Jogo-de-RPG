class personagem:

  def __init__(self, nome, vida, forca):
    self.nome = nome
    self.vida = vida
    self.forca = 0

  def mostrainfo(self):
    print("-- Status --")
    print(self.nome)
    print(self.vida)
    print(self.forca)
    print("-"*12)

  def setnome(self, nome):
    self.nome = nome
  
  def setvida(self, vida):
    self.vida = vida
  
  def setforca(self, forca):
    self.forca = forca

class mago(personagem):

  def __init__(self, nome, vida, forca):
    super().__init__(nome, vida, forca)
    self.forca = forca*0.5
    
class cavaleiro(personagem):

  def __init__(self, nome, vida, forca):
    super().__init__(nome, vida, forca)
    self.forca = forca*0.75

class arqueiro(personagem):

  def __init__(self, nome, vida, forca):
    super().__init__(nome, vida, forca)
    self.forca = forca*0.6

#programa
print("-- Mago --")
nome = input("nome: ")
vida = int(input ("vida: "))
forca = int(input ("forca: "))

objMago = mago(nome, vida, forca)
objMago.mostrainfo()

print("-- Cavaleiro --")
nome = input("nome: ")
vida = int(input ("vida: "))
forca = int(input ("forca: "))

objCavaleiro = cavaleiro(nome, vida, forca)
objCavaleiro.mostrainfo()

print("-- Arqueiro --")
nome = input("nome: ")
vida = int(input ("vida: "))
forca = int(input ("forca: "))

objArqueiro = arqueiro(nome, vida, forca)
objArqueiro.mostrainfo()

