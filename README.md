### Welcome to our README 
In this project we built a tool to protect against ransom attacks.
The tool should be run inside a particular folder, making sure that no file is encrypted or changed in an unwanted way.

#### Base assumptions:
We assumed that the folder will only find text files (.txt) containing ascii characters.

We assumed that encryption does not necessarily occur on all folder files together, or on an entire file

In addition, encryption is not, Necessarily, the content of the file becomes "gibberish".

#### Open source we used in our project:
##### watchdog:
for learn more: https://pypi.org/project/watchdog/ , https://github.com/gorakhargosh/watchdog

##### enchant:
for learn more: https://pypi.org/project/pyenchant/

#### How to Run in linux:
python3 detectionRansomAttack.py
