input_notes = input("Saisir les notes de la liste séparés par un espace ")
current_notes = []
notes_list = input_notes.split()
for i in range(len(notes_list)):
    note = int(notes_list[i])
    current_notes.append(note)
print('La liste des notes sans arrondi: ', current_notes)

def notes_arrondies(current_notes):
    notes = []
    for note in current_notes:
        if note < 40:
            notes.append(note)
        elif note % 5 >= 3:
            notes.append(note + (5 - note % 5))
        else:
            notes.append(note)
    print('La liste des notes arrondies: ', notes)
    
notes_arrondies(current_notes)


