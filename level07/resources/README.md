# level07

```jsx
level07@SnowCrash:~$ ls -la
-rwsr-sr-x 1 flag07  level07 8805 Mar  5  2016 level07
```

The binary executes with flag07 privileges.

```jsx
level07@SnowCrash:~$ ./level07
level07

level07@SnowCrash:~$ ltrace ./level07
```

When we run ltrace on the binary, we see that:

- getenv("LOGNAME") : the program retrieves the value of the LOGNAME environment variable
- system("/bin/echo level07 “ : the program calls the system function, which executes terminal commands
→ Here, it displays level07 in the terminal.

```jsx
level07@SnowCrash:~$ env | grep LOGNAME
LOGNAME=level07
```

The LOGNAME environment variable is equal to level07, so we wonder if the program's purpose is to display the value of this environment variable.
→ By exporting the variable with a different value and running the program, we realize that this is indeed the case, and that the system command is modified as well: whatever follows echo is the value retrieved by getenv("LOGNAME").

Since the binary runs with flag07 permissions, we simply need to replace the value of LOGNAME with "; getflag":

```jsx
level07@SnowCrash:~$ export LOGNAME="; getflag"
```

The system command executed by the program will then be: system("/bin/echo ; getflag ")
→ The ; is used to concatenate and separate the echo command from the getflag command, so that system executes both one after the other, rather than simply displaying "getflag" on the terminal.

```jsx
level07@SnowCrash:~$ ./level07

Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```

We execute the binary and system runs both commands, thus displaying the flag.

flag : fiumuikeil55xe9cu4dood66h