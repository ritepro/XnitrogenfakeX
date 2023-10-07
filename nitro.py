import random
from colorama import Fore, Style
from multiprocessing import Pool

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

def generate_random_code(_):
    code = "https://discord.gift/"
    code += ''.join(random.choice(characters) for _ in range(11))
    return code

def main():
    try:
        reps = int(input("Enter the number of times to repeat: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    print(Fore.RED + "WARNING: BEFORE THIS WILL START, THIS IS FAKE" + Style.RESET_ALL)
    input("Press Enter to start...")

    pool = Pool()  

  
    codes = pool.map(generate_random_code, range(reps))

    pool.close()
    pool.join()

    for code in codes:
        print(code)

    input("Press Enter to close the script.")

if __name__ == "__main__":
    main()
