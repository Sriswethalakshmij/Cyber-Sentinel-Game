from colorama import Fore, init
import time

init(autoreset=True)

score = 0

print(Fore.YELLOW + "Initializing Cyber Security System...")
time.sleep(2)

print(Fore.CYAN + "===== CYBER SENTINEL =====")

name = input("Enter Agent Name: ")

print(Fore.GREEN + f"Welcome Agent {name}")

answer1 = input("Block suspicious IP? (yes/no): ")

if answer1.lower() == "yes":
    print(Fore.GREEN + "Mission Successful")
    score += 10
else:
    print(Fore.RED + "Security Breach")

answer2 = input("Allow unknown hacker access? (yes/no): ")

if answer2.lower() == "no":
    print(Fore.GREEN + "Correct Decision")
    score += 10
else:
    print(Fore.RED + "System Hacked")

answer3 = input("Quarantine infected file? (yes/no): ")

if answer3.lower() == "yes":
    print(Fore.GREEN + "Threat Neutralized")
    score += 10
else:
    print(Fore.RED + "Virus Spread Detected")

print(Fore.CYAN + f"Final Score: {score}")

if score == 30:
    print(Fore.GREEN + "Rank: Elite Cyber Agent")

elif score >= 20:
    print(Fore.YELLOW + "Rank: Security Specialist")

else:
    print(Fore.RED + "Rank: Trainee")

file = open("scores.txt", "a")
file.write(name + " : " + str(score) + "\n")
file.close()