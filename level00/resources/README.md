# Level 00

## Hint from the intra video
> FIND the first file who can run only as 'flag00'

### Check system for hints
```bash
ls -la
# no interesting file in the home directory

cat /etc/passwd
# confirms there is a path and a user for flag00

cat /home/flag/flag00
# 'permission denied' but this confirms the flag exists somewhere
```

### Search the system for files
```bash
find / -user flag00 2>/dev/null
# walks the entire filesystem to check for file
```

### Read the file
```bash
ls -la /usr/sbin/john
----r--r-- 1 flag00 flag00 15 Mar  5  2016 /usr/sbin/john
# permissions mean the file is only readable

cat /usr/sbin/john
```
Output : a string made up only of lowercase letters, some doubled and no digits
- Strong hint that it's an encoded piece of text rather than random data
- Try shifting each letter and check if any shift produces readable English or use online decoder