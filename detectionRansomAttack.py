import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import enchant
import re

'''
Checks whether the words within the file are normal English words
'''
def checkEnglish(line):
    dr = enchant.Dict("en_US")
    line = line.replace('!', '').replace('?', '').replace('.', '').replace(',', '') #Removes valid characters
    words = line.split()  # split the line by words

    for word in words:
        if not dr.check(word):  # if the word contains garbage value
            return False
    return True

'''
A function that passes the contents of the file and checks whether it is valid
'''
def scanFile(file):
    f = open(file, "r")
    clear = True
    try:
        lines = f.read().splitlines()  # make a list from the file
    except:
        print(" * Encrypted content found in " + f.name + "\n")
        clear = False
    for line in lines:
        # print line
        if (re.sub('[ -~]', '', line)) != "":  # check content without ascii characters
            print(" * Encrypted content found in " + f.name + "\n")
            clear = False
            break
        if not checkEnglish(line):
            print(" * Encrypted content found in " + f.name + "\n")
            clear = False
            break
    if clear:
        print(" * The file " + f.name + " is clear!\n")

'''
When changes are made to files, this function works to check that the change is valid
'''
def on_modified(event):
    scanFile(event.src_path)

if __name__ == "__main__":
    #Create the handler event
    patterns = "*.txt" #The patterns we look for are .txt
    ignore_patterns = ""
    ignore_directories = True #is just a boolean that we can set to True if we want to be notified just for regular files (not for directories)
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_modified = on_modified

    # Create Observer
    path = "." #The path to be monitored (in my case is “.”, that’s the current directory)
    not_go_recursively = False
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=not_go_recursively)

    #Scane tge dir
    my_observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
