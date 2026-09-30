# Level 14

## Check what is available at level launch
```bash
ls -la

find / -user flag14 2>/dev/null

cat /etc/passwd
flag00:x:3000:3000::/home/flag/flag00:/bin/bash
[...]
flag14:x:3014:3014::/home/flag/flag14:/bin/bash

```
The commands don't give us anything special to help us move forward but we can see that each flag has an associated number. Here flag14 corresponds to `3014`.

```bash
ls -la /bin/getflag 
-rwxr-xr-x 1 root root 11833 Aug 30  2015 /bin/getflag

scp -P 4242 level14@xx.xx.xx.xx:/bin/getflag ./
# password of lvl : 2A31L79asukciNyi8uppkEuSx
```
We can see that we have permission to read the file so we can retrieve it, using `scp` command, to decompile it.

## Reading getflag program
By decompiling the `getflag` program and looking for flag14 `3014`, it brings us to this line :
```c
fputs((char *)ft_des("g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|"), g3);
```
It's possible to reconstruct the encryption that was used for the password but we decided we didn't want to do that.  
We decided to run the program through `gdb` because with it we can control the execution of the real process and directly modify the execution.

```bash
gdb /bin/getflag

set logging file /tmp/gdb.txt
set logging on
disassemble main
set logging off
```
We can retrieve and save the output of the assembly code and transfer it to our machine to make analysing the code easier.

## Resolving level
Remember that flag14 is associated with the number `3014`, if we convert it to hex it becomes `BC6`.
```asm
0x08048bb6 <+624>:	cmp    $0xbc6,%eax
0x08048bbb <+629>:	je     0x8048de5 <main+1183>
[...]
0x08048de5 <+1183>:	mov    0x804b060,%eax
```
Looking for the number, we can see there's a comparison at some point and if a match is found, it jumps to a certain address.

```asm
0x08048989 <+67>:	call   0x8048540 <ptrace@plt>
[...]
0x08048afd <+439>:	call   0x80484b0 <getuid@plt>
```
If we run the program "normally" with gdb, we will get stuck because we can see in the code the use of `ptrace` and `getuid`, which check our permissions.  
But gdb lets us set `breakpoints` at certain points in the code, which will stop the program at that indicated point.

```bash
(gdb) break *0x0804894a
Breakpoint 1 at 0x804894a
(gdb) info breakpoints 
Num     Type           Disp Enb Address    What
1       breakpoint     keep y   0x0804894a <main+4>

(gdb) run
```
We can set a `breakpoint` before the call to `ptrace` to avoid the checking.  
We can run the program and we need to go to the address indicated when a match is found for flag14. gdb lets us do this by directly specifying the memory address.

```bash
(gdb) jump *0x08048de5
Continuing at 0x8048de5.
```
By going to this address, gdb will show us the expected password for the `su flag` command.
