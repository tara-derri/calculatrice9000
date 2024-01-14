def addition(a, b):
    return a + b 

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
         return a / b  
    else:
        raise ValueError("Erreur : Division par zero")

historique = []

while True:
    try:

        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))
        operation = (input("Entrez l'operation(+, -, *, /):"))        
                
        
        if operation == '+':
            resultat = addition(num1, num2) 
        elif operation == "-":
             resultat = soustraction(num1, num2)    
        elif operation == '*':
            resultat = multiplication(num1, num2)
        elif operation == '/':
             resultat = division(num1, num2)

        else:
            print("Erreur: Operation non valide")
            continue

        historique.append(f"{num1} {operation} {num2} = {resultat}")

        print("Resultat:" , resultat)

        continuer = input ("voulez-vous effectuer une autre opération ? (o/n) : ")
        if continuer.lower() != 'o':
           break 

    except ValueError as ve:
        print(f"Erreur : {ve}") 
    except Exception as e:
        print (f"Erreur inattendue : {e}")


if historique:
    print("\nHistorique des calculs :")
    for calcul in historique:
        print(calcul)

else:
    print("\nHistorique vide.")

effacer_historique = input("\nVoulez-vous effacer l'historique (o/n) : ")

if effacer_historique.lower() == 'o':
    historique.clear()
    print("Historique effacé.")
else: 
    print("Historique non effacé.")

