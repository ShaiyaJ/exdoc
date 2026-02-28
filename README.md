<div align="center">
    <h1>exdoc</h1>
    <p>~ <b>Ex</b>tendable <b>Doc</b>ument format ~</p>
</div>

## About

Exdoc is an extremely simple idea for an extendable document format. 

It is a text-based preprocessor. It uses the `#` to determine where to preprocess text.

```
# <path> inline text
```

```
## <path>
multi-line 
text
##
```

In these two cases, `<path>` will be executed as a program. The program will have the target file format and the given text supplied in stdin, and whatever the program produces on stdout will be replaced in the final document.

This makes it easy to extend using most conventional programming languages. You can create your own tools to perform specific tasks. You can even make these tools support multiple formats.

## Use

To use exdoc simply supply the python command with an input and output path like so:

```
python3 src/main.py input.txt output.txt
```
