def checkFile():
    from pathlib import Path
    p = Path('input/ssh-credentials.txt')
    if p.is_file():
        return True
    else:
        print("File does not exist")
        with p.open("w", encoding="utf-8") as f:
            f.write("")
            f.close()
            print("File created successfully")
            return False


def checkFile_verbose():
    from pathlib import Path
    p = Path('input/ssh-credentials.txt')
    if p.is_file():
        print("File exist")
    else:
        print("File does not exist")
        with p.open("w", encoding="utf-8") as f:
            f.write("")
            f.close()
            print("File created successfully")



