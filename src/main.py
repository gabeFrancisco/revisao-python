#Variáveis

books = ['Bible', 'Harry Potter and the Philosopher Stone', 'Python for Dummies', 'Design Patterns']

def variaveis():

    print("Hello world! God bless you!")
    age = 25
    name = 'Gabriel'
    hasChildren = True

    print(f"I'm {name}!")

    opcoes()

#Inputs
def inputs():
    book = input("Tell me a book: ")
    print(book)
    
    opcoes()

#Listas
def listas():

    print(books[0])
    print(books[1].title())

    #Insere um livro na lista
    newBook = input("Insira um novo livro na lista:")
    books.append(newBook)
    print(books[-1])

    opcoes()

#Functions

def someFunction():
    print("Hellooo! This function is working!")

    someFunction()

#For loops

def forLoops():
    for i in books:
        print(i)

    opcoes()

#While loops

def whileLoops():
    counter = 0
    while counter < 12:
        print(f'Valor de counter é: {counter}')
        counter += 1

def pesquisaBinaria(lista, numero):
    low = lista[0],
    high = len(lista)
    guess = 0

#Opções de módulos
def opcoes():
    try:
        opcao = int(input("\n\nEscolha uma opção: \n1-Variáveis\n2-Inputs\n3-Listas\n4-Loop For\n5-Loop While\n\nNúmero #: "))
    except:
        print('\nDigite apenas números!')
        opcoes()
    print("\n")
    if(opcao == 1):
        variaveis()
    elif(opcao == 2):
        inputs()
    elif(opcao == 3):
        listas()
    elif(opcao == 4):
        forLoops()
    elif(opcao == 5):
        whileLoops()
opcoes()
