# Basic-File-Encryption

The following code represents a File-Encryption program for educational purposes only. 
It is inspired by a tutorial I watched and serves the purpose of enhancing understanding about encryption concepts.


# Project tasks

This project consists of two Python scripts, **`encrypt.py`** and **`decrypt.py`**, that allow you to encrypt and decrypt files using the Fernet encryption algorithm provided by the **`cryptography`** library. The encryption key is securely generated and stored in a separate file.


## Features

- Encrypt individual files or all files in a directory using `cryptography` library.
- Decrypt encrypted files back to their original state.
- Password-based authentication using `bcrypt` library for extra security.
- Automatic exclusion of sensitive files from encryption and decryption.


## Installation

1. Clone or download the repository.
    
    ``` bash
    git clone https://github.com/zVeqsxy/Basic-File-Encryption.git 
    ```
    
2. Change your directory to **`Basic-File-Encryption`**.
    
    ``` bash
    cd Basic-File-Encryption
    ```
    
3. Install the required dependencies by running the following command:
    
    ``` bash
    pip install -r requirements.txt
    ```
    

## Usage

### Encryption

1. Run the script using the following command:
    
    ```bash
    python encrypt.py 
    ```
    
2. You will be prompted to enter the path of the file or directory you want to encrypt.
3. Initialize the password for authentication. The password will be securely hashed and stored in a file named **`pw.key`** for later use.
4. The script will generate an encryption key and store it in a file named **`thekey.key`**.
5. The specified file(s) will be encrypted using the encryption key.
6. When a file or directory is encrypted, a success message will be displayed with the corresponding name.

### Decryption

1. Run the script using the following command:
    
    ```bash
    python decrypt.py
    ```
    
2. You will be prompted to enter the path of the file or directory you want to decrypt.
3. The script compares the provided password and the hashed password from the **`pw.key`** file.
4. After the successful Authentication, the specified file(s) will be decrypted using the encryption key from the **`thekey.key`** file after the comparison was successful.
5. When a file or directory is decrypted, a success message will be displayed with the corresponding name.


## Notes

- The Files in the directory **`Basic-File-Encryption`** are automatically excluded from encryption and decryption operations to prevent accidental modification.
- If the specified file or directory does not exist or the path is invalid, an error message will be displayed.
- If the provided password during decryption does not match the stored password hash, an error message will be displayed.<br><br>

-------------------


> **⚠️DISCLAIMER**:
*This program is intended solely for educational purposes and knowledge sharing. It is strictly prohibited to utilize this code or any associated techniques to cause harm, engage in illegal activities, or compromise the security and privacy of individuals or systems. The developer is not responsible for any misuse, damage, or loss caused by the usage of this project*



## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). 

## Contact

For any inquiries or questions, please contact [Mohamad Kanoua](mailto:Reyhamudi609@gmail.com).
