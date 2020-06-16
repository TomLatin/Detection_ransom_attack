import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import enchant
import re

def checkEng(line):
    dr = enchant.Dict("en_US")

    line = line.replace('!', '').replace('?', '').replace('.', '').replace(',', '')
    # remove accepted signs (!?.,)
    words = line.split()  # split the line by words

    for word in words:
        if dr.check(word) == False:  # if the word contains garbage value
            # print (word + " - ENCRYPTED WORD")
            return False
    return True


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
        if not checkEng(line):
            print(" * Encrypted content found in " + f.name + "\n")
            clear = False
            break
    if clear:
        print(" * The file " + f.name + " is clear!\n")

def on_modified(event):
    scanFile(event.src_path)

if __name__ == "__main__":
    patterns = "*.txt"
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_modified = on_modified
    path = "."
    not_go_recursively = False
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=not_go_recursively)
    my_observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
