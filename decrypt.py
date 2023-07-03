import os
from cryptography.fernet import Fernet
import bcrypt

current_path = os.path.dirname(os.path.abspath(__file__))

def get_files(path):
	if path == current_path or os.path.dirname(path) == current_path:
		raise PermissionError("You can't encrypt or decrypt files from this directory.")

	if os.path.isfile(path):
		return [path]

	if os.path.isdir(path):
		files = [os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
		return files
	
	raise FileNotFoundError("The file or directory you entered doesn't exist.")

def get_key():	
	key_path = os.path.join(current_path, "thekey.key")
	with open(key_path, "rb") as thekey:
		key = thekey.read()
	
	if not key:
		raise Exception("No key found.")
	
	return key

def get_password():
	pw_path = os.path.join(current_path, "pw.key")
	with open(pw_path, "rb") as thepw:
		hashed_pw = thepw.read()
	
	if not hashed_pw:
		raise Exception("No password found.")
	
	return hashed_pw

def decrypt_files(files, hashed_pw, key):		
	user = input("Enter the password: ")

	if not bcrypt.checkpw(user.encode(), hashed_pw):
		raise Exception("Incorrect password.")

	for file in files:
		with open(file, "rb") as thefile:
			content = thefile.read()

		try:
			decrypted_content = Fernet(key).decrypt(content)
		except Exception as e:
			raise Exception(f"Couldn't decrypt the file '{os.path.basename(file)}'. It may not be encrypted.")

		with open(file, "wb") as thefile:
			thefile.write(decrypted_content)

def main():
	try:
		path = input("Enter path: ")
		hashed_pw = get_password()
		files = get_files(path)
		key = get_key()
		decrypt_files(files, hashed_pw, key)
		
		if os.path.isfile(path):
			filename = os.path.basename(path)
			print(f"\nThe file '{filename}' has been decrypted.")

		elif os.path.isdir(path):
			dirname = os.path.basename(path)
			print(f"\nThe files in '{dirname}' have been decrypted.")
	
	except Exception as e:
		print(f"A problem occured: {e}")

if __name__ == "__main__":
	main()
