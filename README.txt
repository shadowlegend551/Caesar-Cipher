# - Reads the input from file.
I.E. "#text.txt" gets the input from file called "text.txt"

@ - Outputs processed text to file.
I.E. "@outputfile.txt" outputs the processed text to file "outputfile.txt"

& - Uses a different character set. Default is "default"

? - Outputs all possibilities.

< - Encode.
I.E. "< 3" encodes input with key 3.

> - Decode.
I.E. "> 3" decodes input with key 3. (decode key is key*(-1))

* - Edit charsets.
I.E. '* newcharset "abc"' creates a new charset called "newcharset" containing the string "abc".

NOTE: Remember to have two spaces around charset contents.

Input text is text in parentheses


EXAMPLES:
$~ < 3 "hello"
Outputs: "khoor"

$~ > 3 "khoor"
Outputs: "hello"

$~ #file.txt @file2.txt &newcharset -f
Outputs all variations of file.txt's contents to file2.txt using charset "newcharset".


How charsets work?:

Basically if charset was "abcd", input "cab" and encode key 3,
the program would look at the first letter of input (c), look for it
in the charset and change it by encode key in charset.
So the letter c would move 3 steps in charset,
it would become "b", a would become "d" and so on iterating over the string.

If you want a deeper understading of the inner life of the code, read it
and the comments.