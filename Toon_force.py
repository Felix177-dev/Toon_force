#!/usar/bin/python3
import os
import time
senha = input("Qual a senha?:  ")
if senha < "67":
    print("Acesso não liberado")
    exit ()
elif senha == "68":
    print("Acesso liberado")
    time.sleep(3)
    os.system("clear")
else:
    print("Bem vindo a meu script")
print("LOADING")
time.sleep(2)
os.system("clear")
time.sleep(3)
print(" _____ _____ _     _____  __  _____ _   _ _____    ____    _  _____")
print("|  ___| ____| |   |_ _\ \/ / |_   _| | | | ____|  / ___|  / \|_   _|")
print("| |_  |  _| | |    | | \  /    | | | |_| |  _|   | |     / _ \ | |")
print("|  _| | |___| |___ | | /  \    | | |  _  | |___  | |___ / ___ \| |")
print("|_|   |_____|_____|___/_/\_\   |_| |_| |_|_____|  \____/_/   \_\_|")
print("")
print("1: ATUALIZAR TERMUX")
print("2: MPV MUSIC 0-11")
print("3: INICIAR PARDUS FELIX OS")
print("4: EXIT")

escolha = False

while escolha == False:
        nivel =  int(input("Qual a opção: "))
        if (nivel == 1):
            os.system("pkg update && pkg upgrade")
     
        elif (nivel == 2):
            os.system("cd && mpv storage/shared/Download/'Fyzer Music'/FNAF.mp3 && cd && cd storage/shared/Music && mpv music0.mp3 music1.mp3 music.2-5.mp3 music.2-6 music2.mp3 music3.mp3 music4.mp3 music5.mp3 music6.mp3 music7.mp3 music8.mp3 music9.mp3 music10.mp3")
        elif (nivel == 3): 
            os.system("pardus.desktop")
        elif (nivel == 4):
            os.system("exit")    
            