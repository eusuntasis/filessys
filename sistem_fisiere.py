import os

def show_menu():
    print("\nComenzi disponibile:")
    print("1. Afișează conținutul directorului curent")
    print("2. Intră într-un folder")
    print("3. Creează un fișier")
    print("4. Creează un folder")
    print("5. Șterge un fișier")
    print("6. Șterge un folder")
    print("7. Ieși din program\n")

def list_directory():
    print("\nConținutul directorului curent:")
    for item in os.listdir():
        print(f"  - {item}")

def change_directory():
    folder = input("Introdu numele folderului în care vrei să intri: ")
    try:
        os.chdir(folder)
        print(f"Acum ești în: {os.getcwd()}")
    except FileNotFoundError:
        print("Folderul nu există.")
    except NotADirectoryError:
        print("Nu este un folder valid.")

def create_file():
    filename = input("Introdu numele fișierului: ")
    with open(filename, 'w') as f:
        f.write("")  # Crează un fișier gol
    print(f"Fișierul '{filename}' a fost creat.")

def create_folder():
    foldername = input("Introdu numele folderului: ")
    try:
        os.mkdir(foldername)
        print(f"Folderul '{foldername}' a fost creat.")
    except FileExistsError:
        print("Folderul există deja.")

def delete_file():
    filename = input("Introdu numele fișierului pe care vrei să-l ștergi: ")
    try:
        os.remove(filename)
        print(f"Fișierul '{filename}' a fost șters.")
    except FileNotFoundError:
        print("Fișierul nu a fost găsit.")
    except IsADirectoryError:
        print("Nu poți șterge un folder folosind această comandă.")

def delete_folder():
    foldername = input("Introdu numele folderului pe care vrei să-l ștergi: ")
    try:
        os.rmdir(foldername)
        print(f"Folderul '{foldername}' a fost șters.")
    except FileNotFoundError:
        print("Folderul nu a fost găsit.")
    except OSError:
        print("Folderul nu este gol. Nu poți șterge foldere care conțin fișiere.")

def main():
    while True:
        show_menu()
        choice = input("Alege o opțiune: ")

        if choice == "1":
            list_directory()
        elif choice == "2":
            change_directory()
        elif choice == "3":
            create_file()
        elif choice == "4":
            create_folder()
        elif choice == "5":
            delete_file()
        elif choice == "6":
            delete_folder()
        elif choice == "7":
            print("Ieșire din program.")
            break
        else:
            print("Comandă necunoscută. Încearcă din nou.")

if __name__ == "__main__":
    main()
