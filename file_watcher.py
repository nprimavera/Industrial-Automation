import sys
import time
from os.path import getmtime

# A class to build an object from a full path of a file and watch whenever it's changed through has_changed() method.
class FileWatcher:
    def __init__(self, path):
        self.path = path
        self.last_mtime = None
    def has_changed(self):
        mtime = getmtime(self.path)     # t1: time from epoch now 
        last_mtime = self.last_mtime    # t0: last time
        self.last_mtime = mtime         # update the current time
        return (mtime != last_mtime)    # report if there's a difference

def main():
    path = sys.argv[1]
    print('path:', path)
    watcher = FileWatcher(path)
    # check every 10 ms, for a total of 2000 times
    for i in range(2000):
        print(i, watcher.has_changed())
        time.sleep(0.1)

if __name__ == "__main__":
    main()