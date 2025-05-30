#!/usr/bin/env python3

import shutil

def free_space():
    total, used, free = shutil.disk_usage("C:\\")
    return f"{int(free / (1024 ** 3))}G\n"  # Include newline exactly as the test expects

if __name__ == "__main__":
    print(free_space().strip())  # Strip to avoid double newlines during print
