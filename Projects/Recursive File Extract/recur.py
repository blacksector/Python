
import os
import time

# Recursive File Scan
# Wayne Kenney (Pythogen) - 2016
# Extract all files on a drive of a specific format.

def rget(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

# Recursive listing
def rscan(path, prefix = ""):
    # Directory List
    dirlist = rget(path)
    # Loop directories/files
    for f in dirlist:
        # Print 'f' for File
        # Print 'path' for Directory

        # Text File format specified
        if f.find(".txt") != -1:
            print("%s/%s") % (path, f)
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            rscan(fullname, prefix + "| ")
            # Delay Results for Debug
            #time.sleep(0.1)

print ("\nThis script will scan your harddrive recursively.\n\n\n"

    "Application:\n"
    " - File Search\n"
    " - Mass-Data Injection\n"
    " - Infection/Modification\n")

x = raw_input("Press Enter to Start Scan...\n")

forWindows = "C:"
rscan("/home/developer/Desktop")


print ("\nOperation Complete!\n\n"
        "Results: All extracted from your drive.\n")