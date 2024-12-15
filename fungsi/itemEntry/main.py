import json
import datetime
import sys
import os
import uuid
import sys

# Otak saat ini 🔥🔥🔥
def menu():
    print("Menu Lisensi:")
    print("1.Mengkontrak lisensi ")
    print("2.Cek Aktivasi lisensi ")
    print("3.Menonaktifkan lisensi ")
    print("4.Search")
    print("5.Sort")
def choice():
        choice=int(input('Enter menu choice: '))
        os.system('cls')
        return choice
def option1():
    import sys
    sys.path.insert(0, "..")
    from itemEntry.berlangganan import main
    
    main()
    
def option2():
    search =str(input("Masukkan tokenmu:"))
    with open('license.json', 'r') as file:
        data = json.load(file)
        wow=data['license_data']
        
    for aktivasi_data in wow: 
        kadaluarsa = datetime.datetime.strptime(aktivasi_data['expires_at'], "%Y-%m-%d %H:%M:%S")
        sekarang = datetime.datetime.now() 
        if aktivasi_data['aktivasi_token'] == search:
            if sekarang > kadaluarsa:
                aktivasi_data['active'] = False
                name =aktivasi_data['name']
                print(f"{name} trial has expired. Deactivating account.")
            else:
                name =aktivasi_data['name']
                print(f"{name} trial is still active.") 
            break
def option3():
    sys.path.insert(0,"..")
    from expired.deque import  hapus_aktivasi
    hapus_aktivasi()
def option4():
    sys.path.insert(0,"..")
    from itemSearch.search2 import  main
    main()
def option5():
    sys.path.insert(0,"..")
    from itemSorting.sorting2 import  main
    main()
def option6():
    print()
def main():
    menu()
    pilihan= choice()
    if pilihan == 1:
        option1()
    elif pilihan ==2:
        option2()
    elif pilihan == 3:  
        option3()
    elif pilihan == 4:
        option4()
    elif pilihan == 5:
        option5()
    else :
        "Diluar pilihan"
if __name__=='__main__':
    pilihan2=""
    while pilihan2 != 'quit':
        main()
        pilihan2=str(input('Uwes rung?: '))
        if pilihan2=='ws' or pilihan2=='uws'or pilihan2=='wes' or pilihan2=='uwes':
            pilihan2='quit'
        elif pilihan2== 'rung' or pilihan2=='urung':
            pass