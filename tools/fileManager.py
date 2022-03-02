import os


def init_files():
    create_folder("output")
    create_folder("input")
    create_file("input/ssh-credentials.txt")
    create_file("output/status.json")


def create_file(name):
    try:
        from pathlib import Path
        p = Path(name)
        if p.is_file():
            print(name + " file exist")
        else:
            print(name + " file does not exist")
            with p.open("w", encoding="utf-8") as f:
                f.write("")
                f.close()
                print(name + " file created successfully")
    except FileNotFoundError:
        print("File cannot be created")


def create_folder(name):
    myDir = name
    CHECK_FOLDER = os.path.isdir(myDir)

    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(myDir)
        print("created folder : ", myDir)

    else:
        print(myDir, "folder already exists.")
