import os

# list of file names to run
file_names = ["yora.py", "AI.py"]

# loop through each file and run them one at a time
for file_name in file_names:
    os.system("python " + file_name)
