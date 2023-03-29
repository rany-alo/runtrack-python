input = input("Veuillez saisir du texte : ")
with open("output.txt", "w") as fichier:
    fichier.write(input)
print("Le text a été sauvegardé dans le fichier output.txt.")