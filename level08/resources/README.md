# Level 08

## Check what is available at level launch
```bash
ls -la
# level08 program and a token file
```

## Read files
```bash
./level08
./level08 [file to read]

./level08 token
You may not access 'token'
```
If we try to read or launch files, we see it's not possible to just access/read the token like this.  
We have to do something similar to level 03, a symbolic link to be able to execute the program.

```bash
ln -s /home/user/level08/token /tmp/getToken

./level08 /tmp/getToken
```
You will get the password for the command `su flag08` and then you can launch the `getflag` command.