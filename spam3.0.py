"""
This program is not ment to be used for anything malicious.
It is ment to be used for educational purposes.
Do not use this program for illegal purposes.
This is just for fun.
"""

try:
    import termcolor
    print(termcolor.colored("----- Welcome to the Spammer script! -----", 'yellow'))
except ImportError:
    print("----- Welcome to the Spammer script! -----")

try:
    import pyautogui
except ImportError:
    print("pyautogui is not installed")
    exit(1)
import time

#modes
def very_slow_simple(word, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(20)

def slow_simple(word, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(8)

def normal_simple(word, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(3)

def fast_simple(word, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(1)

def very_fast_simple(word, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(0.25)


def very_slow_double(word,word2, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(20)
        pyautogui.write(word2)
        pyautogui.press("enter")
        time.sleep(20)


def slow_double(word,word2, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(8)
        pyautogui.write(word2)
        pyautogui.press("enter")
        time.sleep(8)

def normal_double(word,word2, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.write(word2)
        pyautogui.press("enter")
        time.sleep(3)

def fast_double(word,word2, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.write(word2)
        pyautogui.press("enter")
        time.sleep(1)

def very_fast_double(word,word2, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(.25)
        pyautogui.write(word2)
        pyautogui.press("enter")
        time.sleep(.25)

def very_slow_triple(word,word2,word3, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(20)
        pyautogui.write(word2)
        pyautogui.press("enter")
        time.sleep(20)
        pyautogui.write(word3)
        pyautogui.press("enter")
        time.sleep(20)

def slow_triple(word,word2,word3, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(8)
        pyautogui.write(word2)
        pyautogui.press("enter")
        time.sleep(8)
        pyautogui.write(word3)
        pyautogui.press("enter")
        time.sleep(8)

def normal_triple(word,word2,word3, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.write(word2)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.write(word3)
        pyautogui.press("enter")
        time.sleep(3)

def fast_triple(word,word2,word3, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.write(word2)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.write(word3)
        pyautogui.press("enter")
        time.sleep(1)
def very_fast_triple(word,word2,word3, amount):
    for i in range(10):
        print(10-i)
        time.sleep(1)
    for i in range(amount):    
        pyautogui.write(word)
        pyautogui.press("enter")
        time.sleep(.25)
        pyautogui.write(word2)
        pyautogui.press("enter")
        time.sleep(.25)
        pyautogui.write(word3)
        pyautogui.press("enter")
        time.sleep(.25)


print("Welcome to the spam script")
print("Select a mode")

main_mode = input("1. Preset\n2. Custom\n")

if main_mode == "1":
    print("Select a preset")
    preset = int(input("1. Very slow basic\n2. Slow basic\n3. Normal basic\n4. Fast Basic\n5. Very fast basic\n6. Very slow double\n7. Slow double\n8. Normal double\n9. Fast double\n10. Very fast double\n11. Very slow triple\n12. Slow triple\n13. Normal triple\n14. Fast triple\n15. Very fast triple\n"))
    if preset < 6:
        word = input("Enter a messege: ")
        amount = int(input("Enter amount of messages: "))
        if preset == 1:
            very_slow_simple(word, amount)
        elif preset == 2:
            slow_simple(word, amount)
        elif preset == 3:
            normal_simple(word, amount)
        elif preset == 4:
            fast_simple(word, amount)
        elif preset == 5:
            very_fast_simple(word, amount)        
    elif preset < 11:
        word = input("Enter a messege: ")
        word2 = input("Enter a messege: ")
        amount = int(input("Enter amount that these sets will be sent: "))
        if preset == 6:
            very_slow_double(word, word2, amount)
        elif preset == 7:
            slow_double(word, word2, amount)
        elif preset == 8:
            normal_double(word, word2, amount)
        elif preset == 9:
            fast_double(word, word2, amount)
        elif preset == 10:
            very_fast_double(word, word2, amount)

    elif preset < 16:
        word = input("Enter a messege: ")
        word2 = input("Enter a messege: ")
        word3 = input("Enter a messege: ")
        amount = int(input("Enter amount that these sets will be sent: "))
            
        if preset == 11:
            very_slow_triple(word, word2, word3, amount)
        elif preset == 12:
            slow_triple(word, word2, word3, amount)
        elif preset == 13:
            normal_triple(word, word2, word3, amount)
        elif preset == 14:
            fast_triple(word, word2, word3, amount)
        elif preset == 15:
            very_fast_triple(word, word2, word3, amount)
    else:
        print("Invalid input")
    
elif main_mode == "2":
    print("Select a mode")
        
    customs = input("1. Single message\n2. Double message\n3. Triple message\n4. Quadruple message\n5. Quintuple message\n")

    if customs == "1":
        word = input("Enter a messege: ")
        amount = int(input("Enter amount of messages:"))
        cooldown = float(input("Enter cooldown in seconds: "))
        prep = int(input("How many seconds do you need to prepare: "))

        for i in range(prep):
            print(prep-i)
            time.sleep(1)
        for i in range(amount):
            pyautogui.write(word)
            pyautogui.press("enter")
            time.sleep(cooldown)
    elif customs == "2":
        word = input("Enter a messege: ")
        word2 = input("Enter a messege: ")
        amount = int(input("Enter amount of messages:"))
        cooldown = float(input("Enter cooldown in seconds: "))
        prep = int(input("How many seconds do you need to prepare: "))

        for i in range(prep):
            print(prep-i)
            time.sleep(1)
        for i in range(amount):
            pyautogui.write(word)
            pyautogui.press("enter")
            time.sleep(cooldown)
            pyautogui.write(word2)
            pyautogui.press("enter")
            time.sleep(cooldown)
    elif customs == "3":
        word = input("Enter a messege: ")
        word2 = input("Enter a messege: ")
        word3 = input("Enter a messege: ")
        amount = int(input("Enter amount of messages:"))
        cooldown = float(input("Enter cooldown in seconds: "))
        prep = int(input("How many seconds do you need to prepare: "))

        for i in range(prep):
            print(prep-i)
            time.sleep(1)
        for i in range(amount):
            pyautogui.write(word)
            pyautogui.press("enter")
            time.sleep(cooldown)
            pyautogui.write(word2)
            pyautogui.press("enter")
            time.sleep(cooldown)
            pyautogui.write(word3)
            pyautogui.press("enter")
            time.sleep(cooldown)
    elif customs == "4":
        word = input("Enter a messege: ")
        word2 = input("Enter a messege: ")
        word3 = input("Enter a messege: ")
        word4 = input("Enter a messege: ")
        amount = int(input("Enter amount of messages:"))
        cooldown = float(input("Enter cooldown in seconds: "))
        prep = int(input("How many seconds do you need to prepare: "))

        for i in range(prep):
                print(prep-i)
                time.sleep(1)
        for i in range(amount):
            pyautogui.write(word)
            pyautogui.press("enter")
            time.sleep(cooldown)
            pyautogui.write(word2)
            pyautogui.press("enter")
            time.sleep(cooldown)
            pyautogui.write(word3)
            pyautogui.press("enter")
            time.sleep(cooldown)
            pyautogui.write(word4)
            pyautogui.press("enter")
            time.sleep(cooldown)
    elif customs == "5":
        word = input("Enter a messege: ")
        word2 = input("Enter a messege: ")
        word3 = input("Enter a messege: ")
        word4 = input("Enter a messege: ")
        word5 = input("Enter a messege: ")
        amount = int(input("Enter amount of messages:"))
        cooldown = float(input("Enter cooldown in seconds: "))
        prep = int(input("How many seconds do you need to prepare: "))
        for i in range(prep):
            print(prep-i)
            time.sleep(1)
        for i in range(amount):
            pyautogui.write(word)
            pyautogui.press("enter")
            time.sleep(cooldown)
            pyautogui.write(word2)
            pyautogui.press("enter")
            time.sleep(cooldown)
            pyautogui.write(word3)
            pyautogui.press("enter")
            time.sleep(cooldown)
            pyautogui.write(word4)
            pyautogui.press("enter")
            time.sleep(cooldown)
            pyautogui.write(word5)
            pyautogui.press("enter")
            time.sleep(cooldown)

    else:
        print("Invalid input")
    
    
else:
    print("Invalid input")

 