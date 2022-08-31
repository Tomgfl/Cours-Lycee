from classe_palindrome import Palindrome

continuer = True

while continuer:
    print("*** Bienvenue dans le programme de test de palindromme ***")
    ch = input("Veuillez saisir une chaine de caractere : ")
    
    pal = Palindrome(ch.lower())
    
    if pal.estPalindrome():
        print(f"la chaine '{ch}' est un palindrome \n")
    else:
        print(f"la chaine '{ch}' n'est pas un palindrome \n")

    if input("Souhaitez-vous tester une nouvelle chaine ?(O/N)\n") == "N":
        continuer = False
