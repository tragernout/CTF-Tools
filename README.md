# Here is my own-write tools for CTF-tasks.
## date_gen.py
This is a date generator for wordlists.
### Example:
```
$ python3 date_gen.py <start year> <last year> <separator> <type of output(in int)>
```
### Example with args:
```
$ python3 date_gen.py 2020 2021 - 1
```
```
2020-01-01
2020-01-02
2020-01-03
2020-01-04
2020-01-05
2020-01-06
2020-01-07
2020-01-08
2020-01-09
2020-01-10
2020-01-11
2020-01-12
2020-01-13
2020-01-14
2020-01-15
2020-01-16
2020-01-17
...
```
## brute_pdfs.py
Example of brute files on site(pdfs). Url like that:<br>
http://example/documents/YYYY-MM-DD-upload.pdf