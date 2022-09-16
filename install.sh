echo 'Welcome to the spammer installer!'
echo 'This program was made by Ubuntufanboy'
echo 'This program is licenced under the GPLv3'
echo 'Would you like a quick tour or would you like to jump right into the installation? (t/j)'
read answer
if [ $answer == 'j' ]; then
    echo 'installing...'
    pip3 install pyautogui
    pip3 install termcolor
    echo 'Finished installing!'
    echo 'launching app'
    cd src
    python3 spam3.0.py
fi

if [ $answer == 't' ]; then
    echo 'Starting tour'
    echo 'Tour started'
    echo 'Press enter to continue throughout the tour'
    read
    echo 'Make sure you read the README script for some extra info'
    read
    echo 'This program will simulate keystrokes on the keyboard to enter some text and then press enter to send it'
    read
    echo 'This program makes pyautogui do all the heavy lifting'
    read
    echo 'This program has been tested on discord and works very well'
    read
    echo 'To support me star this repo or check out my other projects!'
    read
    echo 'Starting instalation'
    pip3 install pyautogui
    pip3 install termcolor
    echo 'Starting program'
    cd src
    python3 spam3.0.py
fi
