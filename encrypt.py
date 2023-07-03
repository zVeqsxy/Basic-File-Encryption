import os
from cryptography.fernet import Fernet
import bcrypt

current_path = os.path.dirname(os.path.abspath(__file__))

def get_files(path):
    if path == current_path or os.path.dirname(path) == current_path:
        raise PermissionError("You can't encrypt files from this directory.")

    if os.path.isfile(path):
        return [path]
    
    if os.path.isdir(path):
        files = [os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
        return files
    
    raise FileNotFoundError("The file or directory you entered doesn't exist.")

def generate_key():
    key = Fernet.generate_key()

    key_path = os.path.join(current_path, "thekey.key")
    with open(key_path, "wb") as thekey:
        thekey.write(key)

    return key

def innitialize_password():
    password = input("innitialize the password: ")
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    pw_path = os.path.join(current_path, "pw.key")
    with open(pw_path, "wb") as thepw:
        thepw.write(hashed_pw)

def encrypt_files(files, key):
    for file in files:
        try:
            with open(file, "rb") as thefile:
                content = thefile.read()
            encrypted_content = Fernet(key).encrypt(content)
            with open(file, "wb") as thefile:
                thefile.write(encrypted_content)
        except Exception as e:
            print(f"Couldn't encrypt the file '{os.path.basename(file)}'.")

def main():
    try:
        path = input("Enter path: ")
        innitialize_password()
        files = get_files(path)
        key = generate_key()
        encrypt_files(files, key)
        
        if os.path.isfile(path):
            filename = os.path.basename(path)
            print(f"\nThe file '{filename}' has been encrypted.")

        elif os.path.isdir(path):
            dirname = os.path.basename(path)
            print(f"\nThe files in the directory '{dirname}' have been encrypted.")

    except Exception as e:
        print(f"A problem occured: {e}")

if __name__ == "__main__":
    main()