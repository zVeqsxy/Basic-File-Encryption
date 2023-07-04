# Basic-File-Encryption

The following code represents a File-Encryption program (Ransomware) for educational purposes only. 
It is inspired by a tutorial I watched and serves the purpose of enhancing understanding about encryption concepts.

-------------

# DISCLAIMER

### The ransomware is intended solely for educational purposes and knowledge sharing.
### It is strictly prohibited to utilize this code or any associated techniques to cause harm, engage in illegal activities, or compromise the security and privacy of individuals or systems.

-------------

# What's a Ransomware?

A ransomware is a malicious software that specifically targets and restricts legitimate users from accessing their devices or data.
It operates by demanding a ransom payment in exchange for restoring the normal functionality of the affected system. 
Ransomware has gained prominence as a widespread extortion tool, with the most successful variant being encryption-based ransomware. 
This particular type encrypts the victim's data, and the decryption key is provided only after the ransom is paid to the attacker.

For a ransomware to achieve broad success, it typically needs to satisfy three key conditions:

**Condition 1**: The malicious binary code does not contain any easily accessible secrets, such as decryption keys. In some cases, advanced techniques like white box cryptography are employed to achieve this.

**Condition 2**: The ability to decrypt the compromised device remains solely with the attacker who initiated the ransomware attack.

**Condition 3**: Decrypting one device does not provide any useful information for other infected devices. As a result, the decryption key is not shared among them.

-------------

# Project tasks

This project consists of two Python scripts, **`encrypt.py`** and **`decrypt.py`**, that allow you to encrypt and decrypt files using the Fernet encryption algorithm provided by the **`cryptography`** library. The encryption key is securely generated and stored in a separate file.


## **Features**

- Encrypt individual files or all files in a directory using `Fernet` library.
- Decrypt encrypted files back to their original state.
- Password-based authentication using `bcrypt` library for extra security.
- Automatic exclusion of sensitive files from encryption and decryption.


## Installation

1. Clone or download the repository.
    
    ```
    git clone https://github.com/zVeqsxy/Basic-File-Encryption.git 
    ```
    
2. Change your directory to **`Basic-File-Encryption`**.
    
    ```
    cd Basic-File-Encryption
    ```
    
3. Install the required dependencies by running the following command:
    
    ```
    pip install -r requirements.txt
    ```
    

## Usage

### Encryption

1. Run the script using the following command:
    
    ```
    python encrypt.py 
    ```
    
2. You will be prompted to enter the path of the file or directory you want to encrypt.
3. Initialize the password for authentication. The password will be securely hashed and stored in a file named **`pw.key`** for later use.
4. The script will generate an encryption key and store it in a file named **`thekey.key`**.
5. The specified file(s) will be encrypted using the encryption key.
6. When a file or directory is encrypted, a success message will be displayed with the corresponding name.

### **Decryption**

1. Run the script using the following command:
    
    ```
    python decrypt.py
    ```
    
2. You will be prompted to enter the path of the file or directory you want to decrypt.
3. The script compares the provided password and the hashed password from the **`pw.key`** file.
4. After the successful Authentication, the specified file(s) will be decrypted using the encryption key from the **`thekey.key`** file after the comparison was successful.
5. When a file or directory is decrypted, a success message will be displayed with the corresponding name.

-------------

## Notes

- The Files in the directory **`Basic-File-Encryption`** are automatically excluded from encryption and decryption operations to prevent accidental modification.
- If the specified file or directory does not exist or the path is invalid, an error message will be displayed.
- If the provided password during decryption does not match the stored password hash, an error message will be displayed.