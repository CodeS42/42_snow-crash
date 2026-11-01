# level01

In older Linux systems, password hashes were stored in /etc/passwd.

```jsx
cat /etc/passwd | grep flag01
```

The output is: 42hDRfypTqqnw

On the terminal of a Kali Linux VM:

```jsx
echo “42hDRfypTqqnw” > hash.txt
john hash.txt
```

- echo “42hDRfypTqqnw” > hash.txt: writes the hashed password to a text file
- john hash.txt:
    - reads the text file and identifies the encryption type
    - encrypts the passwords in its database one by one using the same encryption type as my hashed password, and compares the result with the hashed password in the file to see if they match
    - displays the decrypted password on the terminal and saves it to a file named john.pot in the .john folder


John displays the password : abcdefg
