# level09

```jsx
level09@SnowCrash:~$ ls -l
total 12
-rwsr-sr-x 1 flag09 level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09 level09   26 Mar  5  2016 token
```

- level09 executes with flag09 privileges
- It is possible to read the token file

```jsx
level09@SnowCrash:~$ cat token
f4kmm6p|=�p�n��DB�Du{��
```

Unreadable string in the token file: contains non-printable characters.

```jsx
level09@SnowCrash:~$ ./level09 token
tpmhr
```

"tpmhr" has the same number of characters as "token".

We test with a custom string:

```jsx
level09@SnowCrash:~$ ./level09 aaa
abc
```

We realize that level09 shifts characters by an amount equal to their index position in the string:

- a (index 0) is shifted by 0, so it remains: a
- a (index 1) is shifted by 1, so it becomes: b
- a (index 2) is shifted by 2, so it becomes: c

```jsx
level09@SnowCrash:~$ ltrace ./level09 aaa
__libc_start_main(0x80487ce, 2, 0xbffff7e4, 0x8048aa0, 0x8048b10 <unfinished ...>
ptrace(0, 0, 1, 0, 0xb7e2fe38)                    = -1
puts("You should not reverse this"You should not reverse this
)               = 28
+++ exited (status 1) +++
```

- "You should not reverse this"

The first idea would be to take the string inside token and pass it to level09 so that it performs the necessary shift to display the real flag. But we cannot do this because non-printable characters are transformed once printed in the terminal.

The second idea would be to write a script that directly opens the file to access the raw bytes, applies the same forward shift, and displays it. But doing so still results in non-printable characters.

We actually need to consider the hint phrase: "You should not reverse this".
→ The third (and correct) idea is to write a script that opens the file directly to access the actual bytes, applies the same shift mechanism IN REVERSE, and prints the result.

So we create a main.c file in /tmp:

```jsx
#include <stdio.h>

int main(int argc, char** argv)
{
        FILE *file = fopen("/home/user/level09/token", "r");
        if(!file)
        {
                return(1);
        }

        int c;
        int i = 0;

        while((c = fgetc(file)) != EOF && c != '\n')
        {
                putchar(c - i);
                i++;
        }
        putchar('\n');

        fclose(file);
        return(0);
}
```

```jsx
level09@SnowCrash:/tmp$ gcc main.c
level09@SnowCrash:/tmp$ ./a.out
f3iji1ju5yuevaus41q1afiuq
```

We finally obtain the password to log into flag09.

flag : f3iji1ju5yuevaus41q1afiuq

getflag : s5cAJpM8ev6XHw998pRWG728z