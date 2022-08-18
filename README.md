
# Python - Rail fence cipher 

This project is a python implementation of rail fence cipher algorithm. 
The rail fence cipher is a classical type of transposition cipher.

Read more about algorithm here:

https://en.wikipedia.org/wiki/Rail_fence_cipher

The implementation was created by Kamil Zych.
## Required:

- Python 3.x
## Running:


To run this program, you can use this command:
```Python
python main.py e 5 "sentence"

```
where:

```
e - letter e/d stands for encryption/decryption mode

5 - secret key used to encrypt/decrypt sentence

"sentence" - message to encrypt/decrypt

```
## Examples:

Note that spaces and punctuation are not omitted

``` Python
python main.py e 3 "sentence"
Output: seetnenc
```

``` Python
python main.py d 3 "seetnenc"
Output: sentence
```

``` Python
python main.py e 2 "we are discovered. run at once"
Output: w r icvrd u toceaedsoee.rna ne
```

``` Python
python main.py e 2 "w r icvrd u toceaedsoee.rna ne"
Output: we are discovered. run at once
```



