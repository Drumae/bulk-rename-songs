import os

def rensng(path, pref):  
    try:  
        for file in os.listdir(path):
            if file.startswith(pref) and file.endswith('.mp3') and os.path.isfile(path + file):
                renfile = ''
                for c in range(5, len(file)):
                    renfile += file[c]
                os.rename(path + file, path + renfile)
                print(f'Renaming "{file}" to "{renfile}"...')
        print('\nDone.')
    except Exception as e:
        print(f"An error has occured: {e}")
        return

path = input('Insert the target folder path here: ')
pref = input('Type the prefix to be removed from file name: ')
confirm = input(f'\n↓ Confirm the options below ↓\nTarget folder path: "{path}"\nRemove "{pref}" from file names\nConfirm? (Y/N): ')

if (confirm.lower() == 'y'):
    if not path.endswith('/'):
        path += '/'
    rensng(path, pref)