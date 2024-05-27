# For starters
This is PYSQL. No, it is not exactly SQL but gives almost **Excel** experience.

# In General
The help menu is not perfectly useful, We advise you to read this `README.md` Manuel for better instructions.
PYSQL, is a ascii based tabulator and editor. PYSQL is completely based 2D lists.

2D lists represents row and column, and it also most compatible with [tabulate](https://pypi.org/project/tabulate/).

# How does it work for you
This tool uses some modules for its perfection.
They are;

- **tabulate**, *for converting 2d lists into table*, *[Download](https://pypi.org/project/tabulate/)*
- **xlwt**, *for converting your table to .xls format*, *[Download](https://pypi.org/project/xlwt/)*
- **cryptography**, *for password protected files*, *[Download](https://pypi.org/project/xlwt/)*
- **unit_converter**, *for conversion of units*, *[Download](https://pypi.org/project/unit-converter/)*

Or just install with single command: `pip install tabulate xlwt cryptography unit_converter`

The others are already installed one which comes  with python

- **os**, *for checking if the file exists or not*
- **argparse**, _for parsing arguments_
- **base64**, *for encryption purposes*
- **math**, *to replicate mathematical operations of excel [kind of]*
- **ast**, *for converting string representation of list to list*

PYSQL do not have restriction over the extensions of the file. But `.txt` is recommendable.
# Perfect Usage guide
There are several arguments for Pysql.
We will get through one by one.
Here is an complete guide:
But first,
Here's a sample.
```
> python3 PYSQL.py -m -f SAMPLE.txt --table
╒══╤══╕
│  │  │
╘══╧══╛
```
>**Note**: The `-m` argument creates the file if it's new. If it's already exist, it will give you a warning that the file already exist. 

>**Note**:`-f` argument selects the file for action

>**Note**: `--table` argument shows the data as a table. 

>**Note**: The `-m` argument create a file with `[['','']]`,Remember, the framework works with the 2D list**


## **Accessing a file**
   `python3 pysql.py -f/--file <file-name>`
## **Creating a file**
You can create a new file with this command
  `python3 pysql.py -m/--make -f/--file <file-name>`

> Note: `-m` argument stands for `--make`, which obviously create an file.

> Note: You could create a empty file of any extensions and type `[['','']]`, that file can also be used.
## **Printing the currently saved table**
For printing the currently saved table, we use `--table` argument.
*Ex:*
`python3 pysql.py -f <file-name> -t/--table`
## Saving the file
   
To save the file for saving the changes, we use `--post` argument.

>**Note: This argument needs to be used on the command in which the change occurs. i.e., for every change `--post` argument needs to be parsed _if_ you want to save the change.**

> **Note: Also, using without `--post` argument, acts like a preview before you save it. i.e., if you are not sure about the result, run it without the `--post` argument using `--table`. The result will be shown with the changes you have parsed. If you have verified the result, run the same command with `--post` to save it.**

## Targeting a row

Row targeting is essential for some arguments. You can also target a range of rows using `-` symbol.
**Syntax**:
For single row:
`python3 pysql.py -f <file-name> -r <row-index>`

For ranged rows:
`python3 pysql.py -f <file-name> -r <from>-<to>`

## Targeting a column
It is similar to targeting a row. Targeting a column is used with `-c`argument.
**Syntax:**
`python3 pysql.py -f <file-name> -c <column-index>`
**For ranged:**
`python3 pysql.py -f <file-name> -c <from>-<to>`

## Adding a row
To add a row, we should use `--add-row` argument.
It is followed by the number of columns to be added.
**That is:**
`python3 pysql.py -f <file-name> --add-row 1`
This would add 1 row to the file.
In action:

    python3 PYSQL.py -m SAMPLE.txt -f SAMPLE.txt --table
    ╒══╤══╕
    │  │  │
    ╘══╧══╛
    python3 PYSQL.py -f SAMPLE.txt --add-row 1 --table
    ╒══╤══╕
    │  │  │
    ├──┼──┤
    │  │  │
    ╘══╧══╛

## Adding a column
Similar to`--add-row` argument,`--add-column` argument is same.
_No context_

## Removing a row
Unlike `--add-row` or `--add-column`. The `--remove-row` cannot take any parameters. It is a Boolean argument.
The row that needs to be removed will specified by `-r` argument.
 For ranged removing, You still can use `-r` with `'-'` as mentioned earlier.
In action:

    python3 PYSQL.py -f SAMPLE.txt --table
    ╒═══╕
    │ 1 │
    ├───┤
    │ 2 │
    ├───┤
    │ 3 │
    ├───┤
    │ 4 │
    ├───┤
    │ 5 │
    ╘═══╛
    
    python3 PYSQL.py -f SAMPLE.txt -r 2-4 --remove-row --table --post
    ╒═══╕
    │ 1 │
    ├───┤
    │ 5 │
    ╘═══╛

## Removing a column
It is as same as `--remove-row` argument. 
You should use `-c` with `--remove-column` for to work.
_No Other Context_
## Inserting a row
To Inserting a row in between two rows, we use `--insert-row` argument.
This argument is followed by the number of the rows to be added.
The index of the row at which the row has to be inserted is specified by `-r` argument.
That is,
`python3 PYSQL.py -f <file-name> -r <index> --insert-row <no.of rows>`
In action,

    python3 PYSQL.py -f SAMPLE.txt --table
    ╒═══╕
    │ 1 │
    ├───┤
    │ 5 │
    ╘═══╛
    python3 PYSQL.py -f SAMPLE.txt -r 2 --insert-row 1 --table --post
    ╒═══╕
    │ 1 │
    ├───┤
    │   │
    ├───┤
    │ 5 │
    ╘═══╛

We insert 1 row at the second position. That is, the position is defined by `-r`, while number of row have to be inserted defined by `--insert-row`.
## Inserting a column
Inserting a column is same as the inserting a row. 
For positioning, `-c` argument is used, and to control number of columns to be added, `--insert-column` argument should be used.

## Adding a data to a cell
To add a data to the table, three peace of information is needed,

- **Row index of the cell**, *specified by `-r`*
- **Column index of the cell**, *specified by `-c`*
- **Data to be added**, *specified by `--add-data`*

In Skeleton,
`python3 PYSQL.py --file <file-name> -r <index> -c <index> --add-data <data>`

For example:

    python3 PYSQL.py -f SAMPLE.txt --table
    ╒═══╕
    │ 1 │
    ├───┤
    │   │
    ├───┤
    │ 5 │
    ╘═══╛
    
    python3 PYSQL.py -f SAMPLE.txt -r 2 -c 1 --add-data 9 --table
    ╒════╕
    │  1 │
    ├────┤
    │  9 │
    ├────┤
    │  5 │
    ╘════╛
So, `-r` represents the row of the cell, and `-c` represents the column of the cell.

***Appending***
If you want to change the data by adding something to it, you can use `--append` argument.
Usage:
`python3 PYSQL.py --file <file-name> -r <index> -c <index> --add-data <data to be added> --append`
> Note: To use append, the previous data should be saved.

**Annotations**
Sometimes when you enter a number or a float, it gets converted into a string in the data.
To avoid this, `--annotation` is used.
This argument is followed by `'str', 'int', or 'float'`.
Which denotes the type of the character.

In action:

    > python3 PYSQL.py --file sample3.txt --table
    ╒══╤══╤══╕
    │  │  │  │
    ╘══╧══╧══╛
    
    > python3 PYSQL.py --file sample3.txt --add-data 5 -r 1 -c 1 --post --table
    ╒═══╤══╤══╕
    │ 5 │  │  │
    ╘═══╧══╧══╛
    
    > cat sample3.txt
    [['5', '', '']]
    
    > python3 PYSQL.py --file sample3.txt --add-data 5 -r 1 -c 2 --post --table --annotation int
    ╒═══╤═══╤══╕
    │ 5 │ 5 │  │
    ╘═══╧═══╧══╛
    
    > cat sample3.txt
    [['5', 5, '']]
    
    > python3 PYSQL.py --file sample3.txt --add-data 5 -r 1 -c 3 --post --table --annotation float
    ╒═══╤═══╤═══╕
    │ 5 │ 5 │ 5 │
    ╘═══╧═══╧═══╛
    
    > cat sample3.txt
    [['5', 5, 5.0]]
    
So the output might not vary, but inside the file you can see the type changed.
When the `--add-data` is called without `--annotation`, the data will be stored as str.
With `--annotation` you can convert it to either `int` or `float`

## Index, headers and style
**Index**
If you in case working with a large set of table, finding the index of the row or column would be difficult,
so, `--index` argument will number every row and column, for easy navigation.
In action:

    python3 PYSQL.py --table -f SAMPLE.TXT
    ╒══╤══╕
    │  │  │
    ╘══╧══╛
    
    python3 PYSQL.py --table -f SAMPLE.TXT --index
    ╒═════╤═════╤═════╕
    │   0 │ 1   │ 2   │
    ╞═════╪═════╪═════╡
    │   1 │     │     │
    ╘═════╧═════╧═════╛
> Note: The number of row or columns don't change when using the `--index` argument.

**Headers**
Headers are the same just like they sound.
This can be used with `--header` argument.
In any case, using this option will make the first row as the header.
In action:

    python3 PYSQL.py --table -f SAMPLE.txt
    ╒══╤══╕
    │  │  │
    ├──┼──┤
    │  │  │
    ├──┼──┤
    │  │  │
    ╘══╧══╛
    
    python3 PYSQL.py --table -f SAMPLE.txt --header
    ╒════╤════╕
    │    │    │
    ╞════╪════╡
    │    │    │
    ├────┼────┤
    │    │    │
    ╘════╧════╛
See those double lines at the bottom of the first row, it defines it's the header.

> Note: Using `--index` and `--header` at the same time will lead to canceling the **header** effect. Since the Index of each column is placed as a header when using `--index`.

**Style**
The style of the grid is set to `fancy_grid` by default.
Of course, Style is an option provided by the `tabulate` module.

You are free to change the style of the grid by, `--style` argument, followed by the style you prefer.
The available styles are,

- plain
- simple
- github
- grid
- simple_grid
- rounded_grid
- heavy_grid
- mixed_grid
- double_grid
- fancy_grid
- outline
- simple_outline
- rounded_outline
- heavy_outline
- mixed_outline
- double_outline
- fancy_outline
- pipe
- orgtbl
- asciidoc
- jira
- presto
- pretty
- psql
- rst
- mediawiki
- moinmoin
- youtrack
- html
- unsafehtml
- latex
- latex_raw
- latex_booktabs
- latex_longtable
- textile
- tsv

## Font style, Color and Unicode
There are three arguments for customizing your data.

**Font style**
Font style consists of 4 style,

- Bold
- Italic
- Underline
- Strikethrough


To use these fonts,
`python3 PYSQL.py --file <filename> -r <index> -c <index> --add-data <data> --font-style <style>`

**Color**
You can color your data.
The available colors are.
- Grey
- Brown
- Darkgreen
- Gold
- Indigo
- Purple
- Deepblue
- Red
- Green
- Yellow
- Blue
- Violet
- Cyan 

To use these color,
`python3 PYSQL.py --file <filename> -r <index> -c <index> --add-data <data> --fg <color>`

> Note: The fonts and colors are case-sensitive

**Unicode**
Unicode sometimes cannot be added into data just by using `--add-data`, such that
`--unicode` argument is followed by the code of the Unicode you have to use along with the data.
For example:
`python3 PYSQL.py --file <filename> -r <index> -c <index> --add-data <data> --unicode <code>`
In action:

    python3 PYSQL.py --file SAMPLE.TXT --table
    ╒══╤══╕
    │  │  │
    ├──┼──┤
    │  │  │
    ├──┼──┤
    │  │  │
    ╘══╧══╛
    
    python3 PYSQL.py --file SAMPLE.TXT -r 1 -c 1 --add-data 'Heart sign - ' --unicode 2665 --table
    ╒════════════════╤══╕
    │ Heart sign - ♥ │  │
    ├────────────────┼──┤
    │                │  │
    ├────────────────┼──┤
    │                │  │
    ╘════════════════╧══╛
  You still can use `--append` to add other data after it to it.

## Merging files
Let's say you have two or more files to work with merging them manually is hard,
so, the argument `--merge` can be used to merge multiple documents.
There are two ways you can merge files, vertically or horizontally.

**Vertically:**
Usage:
`python3 PYSQL.py --file <file1> --merge <file2> <file3> ... --vertical-merge`
In action:

    python3 PYSQL.py --file sample1.txt --table
    ╒════╤════╕
    │ f1 │ f1 │
    ╘════╧════╛
    
    python3 PYSQL.py --file sample2.txt --table
    ╒════╤════╕
    │ f2 │ f2 │
    ╘════╧════╛
    
    python3 PYSQL.py --file sample3.txt --table
    ╒════╤════╕
    │ f3 │ f3 │
    ╘════╧════╛
    
    python3 PYSQL.py --file sample4.txt --table
    ╒════╤════╕
    │ f4 │ f4 │
    ╘════╧════╛
    
    python3 PYSQL.py --file sample1.txt --merge sample2.txt sample3.txt sample4.txt --table --vertical-merge
    ╒════╤════╕
    │ f1 │ f1 │
    ├────┼────┤
    │ f2 │ f2 │
    ├────┼────┤
    │ f3 │ f3 │
    ├────┼────┤
    │ f4 │ f4 │
    ╘════╧════╛
Here i have merged three files with the target file.

**Horizontally**
Usage:
`python3 PYSQL.py --file <file1> --merge <file2> <file3> ... --horizontal-merge`
In action:

    python3 PYSQL.py --file sample.txt --table
    ╒═══╕
    │ 1 │
    ├───┤
    │ 2 │
    ├───┤
    │ 3 │
    ╘═══╛
    
    python3 PYSQL.py --file sample2.txt --table
    ╒═══╕
    │ 4 │
    ├───┤
    │ 5 │
    ├───┤
    │ 6 │
    ╘═══╛
    
    python3 PYSQL.py --file sample3.txt --table
    ╒═══╕
    │ 7 │
    ├───┤
    │ 8 │
    ├───┤
    │ 9 │
    ╘═══╛
    
    python3 PYSQL.py --file sample.txt --merge sample2.txt sample3.txt --horizontal-merge --table
    ╒═══╤═══╤═══╕
    │ 1 │ 4 │ 7 │
    ├───┼───┼───┤
    │ 2 │ 5 │ 8 │
    ├───┼───┼───┤
    │ 3 │ 6 │ 9 │
    ╘═══╧═══╧═══╛

> Note: The order of the file matters.

## Encryption and decryption using a password
In the PYSQL, you can encrypt and decrypt with a password you chose.
This section has 3 arguments, 
- `--passwd`, for assigning password
- `--encrypt`, action of encrypting
- `--decrypt`, action of decrypting

Now,
Usage,
**To encrypt**
`python3 PYSQL.py --file <file-name> --encrypt --passwd <key-phrase>`
**To decrypt**
`python3 PYSQL.py --file <file-name> --decrypt --passwd <key-phrase>`

In action:

    > cat sample1.txt
    [['f1', 'f1'], ['f2', 'f2'], ['f3', 'f3'], ['f4', 'f4']]
    
    > python3 PYSQL.py --file sample1.txt --encrypt --passwd PASSWORD
    [Success] The file has been successfully encrypted
    
    > cat sample1.txt
    Z0FBQUFBQm1VZmZOQjNZUUJIUldhMXpVTjE5S3czOEwwcmlBQjg4MUdTZWdyRGFmQ3ZieVI3RlhXeGtweEJPTjYwR3B1eEVRM0huNmtfcjktSlBFdU1BTlFnZ0ZnRTB0WUF1V21VaDVhWXc4OXkwbHVORmVYLTBQaV8tUUZoYS1fZjVBOHVXTnNPWThsTVVpYnFJMmZIMF8yLXZ0VEZqLUh3PT18c1VzYmZGY2M1UU90VTBqSmFNbks4ck1FajRpb1VzR2FxbjZMOElBbFJJQT18Z0FBQUFBQm1VZmZOT21pbUlPTnhPTUE3RFhNLW1NaDAzYWV5bDZZUzNMMFptZlhSTmFBbmo5NGp1V0lnenJlQkltdjU3TTdkQWY4QTdSem9PMkVfOUcydXFqYW1qbDlrYVE9PQ==
    
    > python3 PYSQL.py --file sample1.txt --decrypt --passwd PASSWORD
    [Verified] The password is verified.
    [I] Content has been decrypted
    
    > cat sample1.txt
    [['f1', 'f1'], ['f2', 'f2'], ['f3', 'f3'], ['f4', 'f4']]

##  Filling
Let's say you have a list of things to add into a row or column, you don't have to do it manually for each cell for each data of the list.
The arguments, `--row-fill` and `--column fill` will followed by the list of the datas to be filled in a particular row or column, 

The row and column to be filled is specified by `-r` and `-c` argument, and using `--row-fill` or `--coloum-fill` argument followed by *Quoted* string representation of a list.

In action:

    python3 PYSQL.py --file sample.txt --table
    ╒══╤══╤══╤══╤══╕
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ╘══╧══╧══╧══╧══╛
    
    python3 PYSQL.py --file sample.txt --table --row-fill '["h","e","l","l","o"]' -r 1
    ╒═══╤═══╤═══╤═══╤═══╕
    │ h │ e │ l │ l │ o │
    ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
    ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
    ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
    ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
    ╘═══╧═══╧═══╧═══╧═══╛
    
    python3 PYSQL.py --file sample.txt --table --column-fill '["h","e","l","l","o"]' -c 1
    ╒═══╤══╤══╤══╤══╕
    │ h │  │  │  │  │
    ├───┼──┼──┼──┼──┤
    │ e │  │  │  │  │
    ├───┼──┼──┼──┼──┤
    │ l │  │  │  │  │
    ├───┼──┼──┼──┼──┤
    │ l │  │  │  │  │
    ├───┼──┼──┼──┼──┤
    │ o │  │  │  │  │
    ╘═══╧══╧══╧══╧══╛
 Also, The length of the list of data is not necessarily need to be to be equal to number of row or column you have.
 For example:

      python3 PYSQL.py --file sample.txt --table
    ╒══╤══╤══╤══╤══╕
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ╘══╧══╧══╧══╧══╛
    
     python3 PYSQL.py --file sample.txt -r 1 --row-fill "['1','2','3']" --table
    ╒═══╤═══╤═══╤══╤══╕
    │ 1 │ 2 │ 3 │  │  │
    ├───┼───┼───┼──┼──┤
    │   │   │   │  │  │
    ├───┼───┼───┼──┼──┤
    │   │   │   │  │  │
    ├───┼───┼───┼──┼──┤
    │   │   │   │  │  │
    ├───┼───┼───┼──┼──┤
    │   │   │   │  │  │
    ╘═══╧═══╧═══╧══╧══╛
    
     python3 PYSQL.py --file sample.txt -r 1 --row-fill "['1','2','3','4','5','6']" --table
    ╒═══╤═══╤═══╤═══╤═══╕
    │ 1 │ 2 │ 3 │ 4 │ 5 │
    ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
    ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
    ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
    ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
    ╘═══╧═══╧═══╧═══╧═══╛
    
     python3 PYSQL.py --file sample.txt -r 1 --row-fill "['1','2','3','4','5','6']" --table --force-fill
    ╒═══╤═══╤═══╤═══╤═══╤═══╕
    │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │
    ├───┼───┼───┼───┼───┼───┤
    │   │   │   │   │   │   │
    ├───┼───┼───┼───┼───┼───┤
    │   │   │   │   │   │   │
    ├───┼───┼───┼───┼───┼───┤
    │   │   │   │   │   │   │
    ├───┼───┼───┼───┼───┼───┤
    │   │   │   │   │   │   │
    ╘═══╧═══╧═══╧═══╧═══╧═══╛
   
> Note: When the length of the list of the data is lesser than that of the row or column,  the data fills perfectly with empty cells remaining.

> Note: When the length of the list of the data is greater than that of the row or column, the data is filled fully, and delete the remaining data. unless when `--force-fill` is used.

Targeting a part of a row or column is possible, using `--slice-fill`
In action:

    python3 PYSQL.py --file sample2.txt --table
    ╒══╤══╤══╤══╤══╕
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ╘══╧══╧══╧══╧══╛
    
    python3 PYSQL.py -f sample2.txt -r 1 --row-fill "[1,2,3]" --slice-fill 2-4 -t
    ╒══╤═══╤═══╤═══╤══╕
    │  │ 1 │ 2 │ 3 │  │
    ├──┼───┼───┼───┼──┤
    │  │   │   │   │  │
    ├──┼───┼───┼───┼──┤
    │  │   │   │   │  │
    ├──┼───┼───┼───┼──┤
    │  │   │   │   │  │
    ╘══╧═══╧═══╧═══╧══╛
    
    python3 PYSQL.py -f sample2.txt -c 1 --column-fill "[1,2,3]" --slice-fill 2-4 -t
    ╒═══╤══╤══╤══╤══╕
    │   │  │  │  │  │
    ├───┼──┼──┼──┼──┤
    │ 1 │  │  │  │  │
    ├───┼──┼──┼──┼──┤
    │ 2 │  │  │  │  │
    ├───┼──┼──┼──┼──┤
    │ 3 │  │  │  │  │
    ╘═══╧══╧══╧══╧══╛

> Note; it is not advisable to use `--force-fill` with `--slice-fill`, 

Reverse the order of the list using `--reverse-fill`,
in action:

    python3 PYSQL.py -f sample2.txt -r 1 --row-fill "[1,2,3,4,5]" --reverse-fill -t
    ╒═══╤═══╤═══╤═══╤═══╕
    │ 5 │ 4 │ 3 │ 2 │ 1 │
    ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
    ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
    ├───┼───┼───┼───┼───┤
    │   │   │   │   │   │
    ╘═══╧═══╧═══╧═══╧═══╛

## Serial numbering
As the name suggests, it is what it is.
The argument `--serial-numbering` needs 3 datas.


- *row/column*, Whether to assign the numbers in a row or an column
- *cell range*, In the row or column, the some range of cell are targeted for serial-numbering,
- *number range*,  Exactly as it sounds, the range of numbers to be set as serial-number.

The index of the row or column is specified through `-r` or `-c`

In action:

    python3 PYSQL.py --file sample.txt --table
    ╒══╤══╤══╤══╤══╕
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ├──┼──┼──┼──┼──┤
    │  │  │  │  │  │
    ╘══╧══╧══╧══╧══╛
    
    python3 PYSQL.py --file sample.txt -r 1 --serial-numbering row 2-4 1-3 --table
    ╒══╤═══╤═══╤═══╤══╕
    │  │ 1 │ 2 │ 3 │  │
    ├──┼───┼───┼───┼──┤
    │  │   │   │   │  │
    ├──┼───┼───┼───┼──┤
    │  │   │   │   │  │
    ├──┼───┼───┼───┼──┤
    │  │   │   │   │  │
    ├──┼───┼───┼───┼──┤
    │  │   │   │   │  │
    ╘══╧═══╧═══╧═══╧══╛
    
    python3 PYSQL.py --file sample.txt -c 1 --serial-numbering column 2-4 1-3 --table
    ╒═══╤══╤══╤══╤══╕
    │   │  │  │  │  │
    ├───┼──┼──┼──┼──┤
    │ 1 │  │  │  │  │
    ├───┼──┼──┼──┼──┤
    │ 2 │  │  │  │  │
    ├───┼──┼──┼──┼──┤
    │ 3 │  │  │  │  │
    ├───┼──┼──┼──┼──┤
    │   │  │  │  │  │
    ╘═══╧══╧══╧══╧══╛

There are two other arguments,

- `--forced`, if the number range is higher than the cells selected
- `--reverse-sno`, if the you want a reverse serial-number list.

Both of these are Boolean commands, which means, it doesn't support any data parsing.

## Importing to MS Excel as .xls file
Yes, you can import your file as `.xls` file.
The argument `--excel` have to be used in order to do that.
Usage:
`python3 PYSQL.py --file <sample.txt> --excel`
And a file with same name as your filename will be created with `.xls` extension.

In action:

    > python3 PYSQL.py --file sample.txt --table
    ╒═══════╤═══════╤═══════╤═══════╤══╕
    │       │       │       │       │  │
    ├───────┼───────┼───────┼───────┼──┤
    │ data1 │ data2 │ data3 │ data4 │  │
    ├───────┼───────┼───────┼───────┼──┤
    │       │       │       │       │  │
    ├───────┼───────┼───────┼───────┼──┤
    │       │       │       │       │  │
    ├───────┼───────┼───────┼───────┼──┤
    │       │       │       │       │  │
    ╘═══════╧═══════╧═══════╧═══════╧══╛
    
    > python3 PYSQL.py --file sample.txt --excel
    
    > ls sample.txt.xls
    sample.txt.xls

## Functions
PYSQL have in basic has 4 functions.

- Average
- Max
- Min
- Sum
- Median

These are numeric functions,
Usage:
`python3 PYSQL.py --file <file-name> --function <function> <r1> <r2> <c1> <c2> <tr> <tc>`
Let's say that, some number are assigned between two vertical, horizontal, or diagonal corners.
The group of numbers can be selected using the coordinates of the corners.

> Note: When using functions, the datas in them should be an integer, not number in string type, you  can use `--annotation` when adding a data to a cell.

In action:

    python3 PYSQL.py --file sample.txt --table
    ╒══╤═══╤═══╤═══╤══╕
    │  │   │   │   │  │
    ├──┼───┼───┼───┼──┤
    │  │ 1 │ 4 │ 7 │  │
    ├──┼───┼───┼───┼──┤
    │  │ 2 │ 5 │ 8 │  │
    ├──┼───┼───┼───┼──┤
    │  │ 3 │ 6 │ 9 │  │
    ├──┼───┼───┼───┼──┤
    │  │   │   │   │  │
    ╘══╧═══╧═══╧═══╧══╛
   
In this table, the numbers are arranged from 2,2 (second row, second column) cell to 4,4 (fourth row, fourth column) cell
In this situation, r1 = 2, r2 = 4, c1 = 2, c2 = 4.
Let's say we are going to sum all these and add the result to the cell at 1,3.
Such that tr = 1, and tc = 3.
So,

    python3 PYSQL.py --file sample.txt --function sum 2 4 2 4 1 3 --table
    ╒══╤═══╤════╤═══╤══╕
    │  │   │ 45 │   │  │
    ├──┼───┼────┼───┼──┤
    │  │ 1 │ 4  │ 7 │  │
    ├──┼───┼────┼───┼──┤
    │  │ 2 │ 5  │ 8 │  │
    ├──┼───┼────┼───┼──┤
    │  │ 3 │ 6  │ 9 │  │
    ├──┼───┼────┼───┼──┤
    │  │   │    │   │  │
    ╘══╧═══╧════╧═══╧══╛
The same with other 3 functions

    python3 PYSQL.py --file sample.txt --function average 2 4 2 4 1 3 --table
    ╒══╤═══╤═════╤═══╤══╕
    │  │   │ 5   │   │  │
    ├──┼───┼─────┼───┼──┤
    │  │ 1 │ 4   │ 7 │  │
    ├──┼───┼─────┼───┼──┤
    │  │ 2 │ 5   │ 8 │  │
    ├──┼───┼─────┼───┼──┤
    │  │ 3 │ 6   │ 9 │  │
    ├──┼───┼─────┼───┼──┤
    │  │   │     │   │  │
    ╘══╧═══╧═════╧═══╧══╛
    
    python3 PYSQL.py --file sample.txt --function min 2 4 2 4 1 3 --table
    ╒══╤═══╤═══╤═══╤══╕
    │  │   │ 1 │   │  │
    ├──┼───┼───┼───┼──┤
    │  │ 1 │ 4 │ 7 │  │
    ├──┼───┼───┼───┼──┤
    │  │ 2 │ 5 │ 8 │  │
    ├──┼───┼───┼───┼──┤
    │  │ 3 │ 6 │ 9 │  │
    ├──┼───┼───┼───┼──┤
    │  │   │   │   │  │
    ╘══╧═══╧═══╧═══╧══╛
    
    python3 PYSQL.py --file sample.txt --function max 2 4 2 4 1 3 --table
    ╒══╤═══╤═══╤═══╤══╕
    │  │   │ 9 │   │  │
    ├──┼───┼───┼───┼──┤
    │  │ 1 │ 4 │ 7 │  │
    ├──┼───┼───┼───┼──┤
    │  │ 2 │ 5 │ 8 │  │
    ├──┼───┼───┼───┼──┤
    │  │ 3 │ 6 │ 9 │  │
    ├──┼───┼───┼───┼──┤
    │  │   │   │   │  │
    ╘══╧═══╧═══╧═══╧══╛

## Functional expressions
These are something which are really breath-taking to understand.
These are much like Regex (Regular expressions).

Let's say we have to add numbers from same row but with all left sided columns.
We can use functions, but what if we had to do that several no.of rows.

For that, we can use functional expressions.
In action:

    python3 PYSQL.py --file sample.txt --table
    ╒═══╤═══╤══╕
    │ 1 │ 2 │  │
    ├───┼───┼──┤
    │ 3 │ 4 │  │
    ├───┼───┼──┤
    │ 5 │ 6 │  │
    ╘═══╧═══╧══╛
    
    python3 PYSQL.py --file sample.txt --functional-expression "R[(r)][(c)-1]+R[(r)][(c)-2]" --functional-positioning column 3 1-3 --table
    ╒═══╤═══╤════╕
    │ 1 │ 2 │  3 │
    ├───┼───┼────┤
    │ 3 │ 4 │  7 │
    ├───┼───┼────┤
    │ 5 │ 6 │ 11 │
    ╘═══╧═══╧════╛
Before understanding `--function-expression`, understanding `--functional-positioning` will give you better hand.
At this segment of my command `--functional-positioning column 3 1-3`,
This means, the `--function-positioning` meant to handle the 'column' with index 3. in that column, cells from 1-3 are selected.

For each cell in this order, row index will be different but the column index will be same.
Such that, 
For each iterations of these cells. PYSQL takes the indexes, and replace the '(r)' and '(c)' and run the expression.

```
If for the first iteration. 
The select cell is 1,3. The script will assign
(r) = 1 & (c) = 3
Since the expression is "R[(r)][(c)-1]+R[(r)][(c)-2]"
After replacing, the script will evaulated like this,
= R[1][3-1] + R[1][3-2]
= R[1][2] + R[1][1]
Since we have '2' at cell 1,2 and '1' at cell 1,1.
The script will replace R[1][2] with '2' and R[1][1] '1', The 'R' represents your table. It is very crucial
So.
= 2 + 1
= 3

For the second iteration,
r = 2 & c = 3
= R[(r)][(c)-1]+R[(r)][(c)-2]
= R[2][3-1]+R[2][3-2]
= 4 + 3
= 7
```
I am sorry, this has became a math class and made so difficult about `--functional-expression`
Well at least, it is how it works.

This not only works on rows but on columns too..

    python3 PYSQL.py --file sample.txt --table
    ╒═══╤═══╤═══╤═══╤════╕
    │ 1 │ 2 │ 3 │ 4 │ 5  │
    ├───┼───┼───┼───┼────┤
    │ 6 │ 7 │ 8 │ 9 │ 10 │
    ├───┼───┼───┼───┼────┤
    │   │   │   │   │    │
    ╘═══╧═══╧═══╧═══╧════╛
    
    python3 PYSQL.py --file sample.txt --functional-expression "R[(r)-1][(c)]+R[(r)-2][(c)]" --functional-positioning row 3 1-5 --table
    ╒═══╤═══╤════╤════╤════╕
    │ 1 │ 2 │  3 │  4 │  5 │
    ├───┼───┼────┼────┼────┤
    │ 6 │ 7 │  8 │  9 │ 10 │
    ├───┼───┼────┼────┼────┤
    │ 7 │ 9 │ 11 │ 13 │ 15 │
    ╘═══╧═══╧════╧════╧════╛

Here are more example:
Subtracting,

    python3 PYSQL.py --file sample.txt --functional-expression "R[(r)][(c)-1]-R[(r)][(c)-2]" --functional-positioning column 3 1-3 --table
    ╒═══╤═══╤═══╕
    │ 1 │ 2 │ 1 │
    ├───┼───┼───┤
    │ 3 │ 4 │ 1 │
    ├───┼───┼───┤
    │ 5 │ 6 │ 1 │
    ╘═══╧═══╧═══╛
Sin and cosine

    py PYSQL.py --file sample.txt --functional-expression "sin(int(R[(r)][(c)-1]))" --functional-positioning column 2 1-3 --table
    ╒═══╤═══════════╕
    │ 2 │  0.909297 │
    ├───┼───────────┤
    │ 4 │ -0.756802 │
    ├───┼───────────┤
    │ 6 │ -0.279415 │
    ╘═══╧═══════════
    
    python3 PYSQL.py --file sample.txt --functional-expression "cos(int(R[(r)][(c)-1]))" --functional-positioning column 2 1-3 --table
    ╒═══╤═══════════╕
    │ 2 │ -0.416147 │
    ├───┼───────────┤
    │ 4 │ -0.653644 │
    ├───┼───────────┤
    │ 6 │  0.96017  │
    ╘═══╧═══════════╛
Of course, they are measured in radians.
This is how the functional-expression works.

Using functional expression,  we can also convert units, like
Converting cm to mm,

    py PYSQL.py --file sample.txt --functional-expression "conv(str(R[(r)][(c)-1])+'cm','mm')" --functional-positioning column 2 1-3 --table
    ╒═══╤════╕
    │ 2 │ 20 │
    ├───┼────┤
    │ 4 │ 40 │
    ├───┼────┤
    │ 6 │ 60 │
    ╘═══╧════╛
 Usage of conv expression: `"conv(str('<expression>'+'<convert from>', '<convert to>'))"`
This conversional expression can support almost every units.

# Errors you may expect:
There are 19 errors, which are most likely to be encountered,

- `Erno 0`: 'File does not exist'
- `Erno 1`: 'Something might have gone wrong, please check you inputs.'
- `Erno 2`: 'The file might have been corrupted or maybe encrypted. Couldn't extract info of the file'
- `Erno 3`: 'Either your -r/--row or -c/--column has invalid index. Please check again.'
- `Erno 4`: 'There might be something illegal happening with that unicode you entered, please check again.'
- `Erno 5`: 'That data cannot be converted into that type.'
- `Erno 6`: 'The indexes are invalid'
- `Erno 7`: 'No non-numerical characters should be included'
- `Erno 8`: 'It is not an available function'
- `Erno 9`: 'The files to be merged are not valid.'
- `Erno 10`: ''Might be something wrong with the file while converting to .xls, please check it''
- `Erno 11`: 'Using both slice_fill and force_fill is not advisable'
- `Erno 12`: 'The first arg of --functional-positioning should be either 'row' or 'column' '
- `Erno 13`: "Perhaps you might have not typed parenthesis for 'r' and 'c' or might missed the R"
- `Erno 14`: 'Maybe the function need an other type inputs.'
- `Erno 15`: 'The syntax of the expression might be invalid'
- `Erno 16`: 'The range or the index is not correctly defined for the serial numbering'
- `Erno 17`: 'The --passwd argument is must for using --encrypt and --decrypt'
- `Erno 18`: 'Password is incorrect for the decryption'
- `Erno 19`: 'The file already exists'

Each error will give you clue on what you might made wrong in the prompt.
Along with these error, there errors with python syntax. For handling any other errors.
If any unusual error occurs, please report us.

# The End
That was the entire quick Manuel, hope it was helpful.

# A Thank you
Thanks for having much patience for reading this Manuel and for using PYSQL.
We will be happy to receive any commentary on our tool. If any inconvenience faced, report us through issues.


