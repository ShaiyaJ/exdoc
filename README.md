<div align="center">
    <h1>exdoc</h1>
    <p>~ <b>Ex</b>tendable <b>Doc</b>ument format ~</p>
</div>

## About
Exdoc is a file preprocessor which uses executable commands to determine content.

```
# (command) <content>
```

Is equivalent to

```
printf content | command
```

Whatever the above produces on stdout is the output text of the document

Furthermore, there's modifiers that augment the behaviour of exdoc blocks...

### `!`

```
#!* (command) <content>
```

`!` suppresses the filetype from being given to `command`.

By default exdoc will output the target filetype in the first line of stdin - some commands may mess up when this is done, e.g.

```
# (cat -) <test>
```

Will produce

```
txt
test
```

But 

```
#! (cat -) <test>
```

Will produce

```
test
```

### `*`
```
#* (command) <content>
```

`*` evaluates the command output again - it enables recursion, e.g.

```
#! (cat -) <#! (cat -) <test\>>
```

Will produce

```
test
```

Note the `\>`, which will be replaced with `>` when processing.

### `!*`
Combines the effects of `!` and `*`.
