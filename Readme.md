# File Synchronization Program

A Python program that automatically copies new files and removes files that no longer exist in the source directory


# Features
    
    - Copies new files from source folder to replica folder
    - Removes files from replica folder if they no longer exist in source files
    - Creates a log file with the program activity

## Usage

    python main.py <source> <replica> <interval> <cycles> <log_file>

    source -> folder where the original files are
    replica -> folder where the files are copied
    interval -> time between synchronizations in seconds
    cycles -> number of cycles
    log_file -> file where the program logs all operations

## What I learned

    - Learned how to manipulate files and directories using Pathlib
    - Learned how to use command-line arguments using sys.argv to pass inputs to the program and allow the user to
      control how it runs
  
## Technologies Used  

    - Python  3.10+
    - pathlib
    - shutil
    - os
    - sys