Basic class to facilitate sequential "bruteforcing" I wrote in a very short amount of time whilst fueled by beer and strippers.
Written and tested with Python 3.6.1. typing.Union is not available previous to 3.5.x if I remember correctly.
Might add interpreter version checking later, if I can be bothered.
Possible additions and improvements in the future, or not.

## Example Screenshot
![Screenshot](/Screenshot.png)

## Example
### There's already an example at the bottom of the script, but here's another
```py
def comp_func(string: str) -> bool:
    # Perform comparison operations...
    pass

if __name__ == '__main__':
    from string import ascii_lowercase
    rec = RecursiveStringGen(6, charset=ascii_lowercase)
    result = rec.bruteforce(comp_func)
    print('String {0} found!'.format(result if result is not None else 'not'))
```
