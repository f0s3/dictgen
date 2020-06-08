# dictgen
Generate any dictionary for bruteforce attacks using regex pattern.

## Installation:
`pip install sre_yield`

`git clone https://github.com/f0s3/dictgen.git`

`cd dictgen`

or as a one-liner:

`pip install sre_yield;git clone https://github.com/f0s3/dictgen.git;cd dictgen`

## Examples:

8-character password, any case with numbers:
```
python3 dictgen.py -p="[a-zA-Z0-9]{8,8}" -f filename.txt
```
same, but from 8 to 12 symbols:
```
python3 dictgen.py -p="[a-zA-Z0-9]{8,12}" -f filename.txt
```
let's say that we know that password contains `123` at the end:
```
python3 dictgen.py -p="[a-z]{5,7}123" -f filename.txt
```
