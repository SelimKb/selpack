def try_me():
    name = input ("what's your name?")
    if 'jean ' in name.lower() or 'jean-' in name.lower():
        print ('Salut fil de fer')
    elif name.lower() == 'morgan':
        print("File t'entrainer! Louis t'attend à la salle")
    else:
        print (f'Bonjour {name}, bienvenu!!!')
