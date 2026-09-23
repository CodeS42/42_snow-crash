# Level 06

## Check what is available at level launch
```bash
ls -la
# level06 prog and a php file
```
```bash
./level06
```
Running the `level06` program gives us an error message telling us the program cannot be launched like this.

## Read and understand PHP file
```bash
cat level06.php
```
Looking at what's inside the PHP file we understand it's the same principle as level 04, where we had to
inject a shell command via a Perl script. Except here it's a PHP code injection.

```bash
$a = file_get_contents($y);
$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
```
This is the important part.  
The script will read the entire file and take as an argument some content, where the regex tells us it's
looking for something matching the pattern `[x code]`, content which will be inserted into `y`.  
The key point is the `/e` modifier in `preg_replace`. This modifier means the replacement string will
be treated as PHP code to be executed, instead of plain text.

```bash
echo [x '${`getflag`}'] > /tmp/getToken

./level06 /tmp/getToken
```
The error message will contain the value it tried to use as a variable name.