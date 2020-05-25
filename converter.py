## Convert Minutes, Hours, Days to seconds
import time
import sys
from colorama import Fore, Back, Style 

#Menu to choose what do you wish to transform to 
# seconds --> Min, Hours, Days // 1
# Min ---> Hours, Days, Seconds // 2
# Hours ---> Days, Seconds, Minutes // 3
# Days ---> Seonds, Minutes, Hours // 4
choice = 0
convto = 0
def menu():
    print(Fore.WHITE + "1: Convert to seconds")

    print(Fore.CYAN + "2: Convert to minutes")

    print(Fore.BLUE + "3: Convert to hours")

    print(Fore.GREEN + "4: Convert to Days")

    print(Fore.RED + "5: Exit")

    choice = int(input(Fore.WHITE + "Please pick an option"))
    time.sleep(1)
    if choice == 1:
        tosec()
    elif choice == 2: 
        tomin()
    elif choice == 3:
        tohour()
    elif choice == 4:
        today()
    else:
        choice ==5
        sys.exit()
def returntomenu(): 
        time.sleep(0.5)
        print("You will be brought back to the Main Menu")    
        time.sleep(1)
def mintosec():
    min1 = float(input(Fore.WHITE + "Enter the ammount of minutes you want in seconds: "))
    mintosec = float(min1) * 60
    print(str(min1) + " Minutes = " + str(mintosec) + " Seconds")
def hourtosec():
    hour1 = float(input(Fore.WHITE + "Enter the amount of hours you want in seconds: "))
    hourtosec = float(hour1) * 3600
    print(str(hour1) + " Hours =  " + str(hourtosec) + " Seconds")
def daytosec():
    day1 = float(input(Fore.WHITE + "Enter the ammount of days you want in seconds: "))
    daytosec = float(day1) * 86400
    print(str(day1) + " Days = " + str(daytosec) + " Seconds")
def tosec():
    print(Fore.RED + "1: Min ---> Sec")
    time.sleep(0.5)
    print(Fore.GREEN +   "2: Hours --> Seconds")
    time.sleep(0.5)
    print(Fore.YELLOW +  "3: Days ---> Seconds")
    time.sleep(0.5)
    print(Fore.BLUE + "4: GO BACK ")
    convto = int(input('Enter your choice:'))
    time.sleep(0.5)

    if convto == 1:
        time.sleep(0.5)
        mintosec()
        time.sleep(1.5)
    elif convto == 2: 
        time.sleep(0.5)
        hourtosec()
        time.sleep(1.5)
    elif convto == 3: 
        time.sleep(0.5)
        daytosec()
        time.sleep(1.5)
    else:
        convto == 4
        returntomenu()
def sectomin():
    sec1 = float(input("Enter the amount of seconds you would like to transform to minutes: "))
    sectomin = float(sec1) / 60
    print(str(sec1) + " Seconds = " + str(sectomin) + " Minutes ")
def hourtomin():
    hour1 = float(input("Enter the amount of hours you would like to transform onto Minutes: "))
    hourtomin = float(hour1) * 60
    print(str(hour1) + " Hours = " + str(hourtomin) + " Minutes")
def daytomin():
    day1 = float(input("Enter the amount of days you would like to transform to Minutes: "))
    daytomin = float(day1) * 1440
    print(str(day1) + " Days = " + str(daytomin) + " Minutes ")
def tomin():
    print(Fore.RED + "1: Sec ---> Min")
    time.sleep(0.5)
    print(Fore.GREEN +   "2: Hours --> Min")
    time.sleep(0.5)
    print(Fore.YELLOW +  "3: Days ---> Min")
    time.sleep(0.5)
    print(Fore.BLUE + "4: GO BACK ")
    convto = int(input('Enter your choice:'))
    if convto == 1:
        sectomin()
    elif convto == 2: 
        hourtomin()
    elif convto == 3:
        daytomin()
    else:
        convto == 4
        returntomenu()
def mintohour():
    min1 = float(input("Enter the amount of minutes you would like to transform to Minutes: "))
    mintohour = float(min1) / 60
    print(str(min1) + " Minutes = " + str(mintohour) + " Hours ")
def sectohour():
    sec1 = float(input("Enter the amount of seconds you would like to transfom to hours: "))
    sectohour = float(sec1) / 3600
    print(str(sec1) + " Seconds = " + str(sectohour) + " Hours ")
def daytohour():
    day1 = float(input("Enter the amount of days you would like to transfom to hours: "))
    daytohour = float(day1) * 24
    print(str(day1) + " Days = " + str(daytohour) + " Hours ")
def tohour():
    print(Fore.RED + "1: Sec ---> Hour")
    time.sleep(0.5)
    print(Fore.GREEN +   "2: Min --> Hour")
    time.sleep(0.5)
    print(Fore.YELLOW +  "3: Days ---> Min")
    time.sleep(0.5)
    print(Fore.BLUE + "4: GO BACK ")
    convto = int(input('Enter your choice:'))
    
    if convto == 1: 
        sectohour()
        time.sleep(0.5)
    elif convto == 2:
        mintohour()
        time.sleep(0.5)
    elif convto == 3:
        daytohour()
        time.sleep(0.5)
    
    else:
        convto == 4
        returntomenu()
def sectoday():
    sec1 = float(input("Enter the amount of Seconds you would like to transfom to Days: "))
    sectoday = float(sec1) / 86400
    print(str(sec1) + " Seconds = " + str(sectoday) + " Days ")
def mintoday():
    min1 = float(input("Enter the amount of Minutes you would like to transfom to Days: "))
    mintoday = float(min1) / 1440
    print(str(min1) + " Minutes = " + str(mintoday) + " Days ")
def hourtoday():
    hour1 = float(input("Enter the amount of Hours you would like to transfom to Days: "))
    hourtoday = float(hour1) / 24
    print(str(hour1) + " Hours = " + str(hourtoday) + " Days ")
def today():
    print(Fore.RED + "1: Sec ---> Day")
    time.sleep(0.5)
    print(Fore.GREEN +   "2: Min --> Day")
    time.sleep(0.5)
    print(Fore.YELLOW +  "3: Hour ---> Day")
    time.sleep(0.5)
    print(Fore.BLUE + "4: GO BACK ")

    convto = int(input('Enter your choice:'))    
    if convto == 1: 
        sectoday()
        time.sleep(0.5)
    elif convto == 2:
        mintoday()
        time.sleep(0.5)
    elif convto == 3:
        hourtoday()
        time.sleep(0.5)
    
    else:
        convto == 4
        returntomenu()
while choice == 0:
    menu()  

