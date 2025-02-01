#Funções para definir em que módulo entrar:

def variaveis():
    #Variáveis

    print("Hello world! God bless you!")
    age = 25
    name = 'Gabriel'
    hasChildren = True

    print(f"I'm {name}!")

def inputs():

    #Inputs
    book = input("Tell me a book: ")
    print(book)

def listas():
    #Listas
    books = ['Bible', 'Harry Potter and the Philosopher Stone', 'Python for Dummies', 'Design Patterns']

    print(books[0])
    print(books[1].title())

    #Insere um livro na lista
    newBook = input("Insira um novo livro na lista:")
    books.append(newBook)
    print(books[-1])

#Functions

def someFunction():
    print("Hellooo! This function is working!")

someFunction()

#For loops

def forLoops():
    for i in books:
        print(i)

#While loops

def whileLoops():
    counter = 0
    
opcao = int(input("Escolha uma opção: \n1-Variáveis\n2-Inputs\n3-Listas\n4-Loop For\n5-Loop While"))

if(opcao == 1):
    variaveis()
elif(opcao == 2):
    inputs()
elif(opcao == 3):
    listas()

   
