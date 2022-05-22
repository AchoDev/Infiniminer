import os
import time, random
from termcolor import colored
from simple_term_menu import TerminalMenu


# VARIABLES
keys = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
currency = "ETH"
addressLength = 30
addressCount = 25000
probability = 1000
waitTime = 0.015

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear") 

def distraction():

    uuid = ["uuid"]

    class Model:
        def __init__(self) -> None:
            pass
        def UUIDField(self, one, two, three):
            pass
        


    models = Model()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.addressField (("BTS address"), unique=True)
    is_staff = models.BooleanField( ("ETH status"), default=False)
    is_superuser = models.BooleanField(("superuser status"), default=False)
    is_active = models.BooleanField(("active"),default=True)

    activation_key = models.UUIDField(unique=True,default=uuid.uuld4)
    confirmed_email = models.BooleanField(default=False)
    
    USERNAME_FIELD = "jf29r9ciafol"

def main():

    clear()
    start()

    time.sleep(0.5)

    print(colored("[/-/] Loading configuration file\n", "yellow"))

    time.sleep(3)
    
    input(colored("[/-/] Config file is ready. Press enter to start mining  ", "green"))

    clear()

    for i in range(addressCount):
        
        currStr = list("[-] bc1p")

        for j in range(addressLength):
            currStr.append(keys[random.randint(0, len(keys) - 1)])

        try:
            if(1 == random.randint(1, probability)):
                walletFound(currStr)
        except:
            print("")


        print(colored("".join(currStr) + f" 0.00 {currency}", "red"))
        time.sleep(waitTime)

def start():
    print(colored(
        """ 
         ____  _  _  ____  ____  _  _  ____  __  __  ____  _  _  ____  ____ 
        (_  _)( \( )( ___)(_  _)( \( )(_  _)(  \/  )(_  _)( \( )( ___)(  _ \ 
         _)(_  )  (  )__)  _)(_  )  (  _)(_  )    (  _)(_  )  (  )__)  )   /
        (____)(_)\_)(__)  (____)(_)\_)(____)(_/\/\_)(____)(_)\_)(____)(_)\_)
        """
        , "magenta"))
    

    options = ["Start mining for wallets", "Information", "Change configurations"]

    termMenu = TerminalMenu(options)
    index = termMenu.show()
    
    match index:
        case 0:
            return
        case 1:
            return
        case 2:
            return

    

def walletFound(str):
    print(colored("".join(str) + f"[+] 0.022 {currency}", "green") + " ~ 45.23 USD\n")
    print(colored(colored("Connecting to wallet through server EU 1 ->", "cyan")))

    for i in range(100):
        print(colored(f"%{i}{i%4}", "blue"), end=' ')
        if i%10 == 0:
            time.sleep(0.2)

    print("\n")
    
    time.sleep(1)
    print(colored(f"successfully claimed wallet" + "".join(str), "green"))
    time.sleep(0.5)
    print(colored("see ADDRESS.txt for more info about this address", "green"))
    input("")


    clear()
    print(colored("restarting...", "yellow"))
    time.sleep(2)
    clear()

if __name__ == "__main__":
    main()