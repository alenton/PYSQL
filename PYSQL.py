#!/usr/bin/env python3
# /Libraries

from tabulate import tabulate as tbl # type: ignore
from argparse import ArgumentParser as AP
from unit_converter.converter import converts as conv # type: ignore
from xlwt import Workbook # type: ignore
from cryptography.fernet import Fernet # type: ignore
import base64
import os
import ast
from math import *
import sys

__PARSER__ = AP(prog='PYSQL', description="A simple sql 'like' tool. more like python excel", epilog='Please read '
                                                                                                     'README.md at our '
                                                                                                     'github page for '
                                                                                                     'way more perfect '
                                                                                                     'explanation.')
__PARSER__.add_argument("-f", "--file",
                        help="Filename of the target file",
                        required=True)
__PARSER__.add_argument("-r", "--row",
                        help="For targeting a row or range of row.",
                        metavar='INDEX')
__PARSER__.add_argument("-c", "--column",
                        help="For targeting a column or range of column.",
                        metavar='INDEX')
__PARSER__.add_argument("--add-data",
                        help="Assign data to a cell, the coordinates of the cell is specified by -r and -c",
                        metavar="DATA")
__PARSER__.add_argument('--append',
                        help='Append data to already existing one',
                        action='store_true')
__PARSER__.add_argument('--annotation',
                        help='Type of data: str, int or float',
                        metavar='TYPE',
                        default='str')
__PARSER__.add_argument("--add-row",
                        help="Add no.rows to the table",
                        metavar="no.of rows to be added".upper())
__PARSER__.add_argument("--add-column",
                        help="Add no.columns to the table",
                        metavar="no.of columns to be added".upper())
__PARSER__.add_argument("--remove-row",
                        help="remove the row specified by -r, use '-' for ranged",
                        action="store_true")
__PARSER__.add_argument("--remove-column",
                        help="remove the column specified by -c, use '-' for ranged",
                        action="store_true")
__PARSER__.add_argument("--insert-row",
                        help="insert no.rows to given index by -r",
                        metavar="no.of rows to be inserted".upper())
__PARSER__.add_argument("--insert-column",
                        help="insert no.columns to given index -c",
                        metavar="no.of columns to be "
                                "inserted".upper())
__PARSER__.add_argument("-t", "--table",
                        help="print the table saved",
                        action="store_true")
__PARSER__.add_argument("-p", "--post",
                        help="Save into the file with changes given by the prompt at that time",
                        action="store_true")
__PARSER__.add_argument('-m', '--make',
                        help="create a file with some default data to begin with",
                        action='store_true')
__PARSER__.add_argument("-i", '--index',
                        help="show row index and column index of the table",
                        action="store_true")
__PARSER__.add_argument('--header',
                        help="First row as header, use it without --index argument",
                        action="store_true")
__PARSER__.add_argument("-s", "--style",
                        help="style of the grid. For available styles, check the README.md")
__PARSER__.add_argument("--function",
                        help="Some basic functions, for check README.md for available functions and how "
                             "to use it.",
                        metavar="<function> <x1> <x2> <y1> <y2> <tx> <ty>",
                        nargs="*")
__PARSER__.add_argument('--fg',
                        help="Color of the data, check the README.md for available colors")
__PARSER__.add_argument('--font-style',
                        help='Font of the data, check the README.md for available fonts')
__PARSER__.add_argument('--unicode',
                        help='Add unicode to the data with the corresponding number of the unicode',
                        metavar='CODE')
__PARSER__.add_argument("--set-default",
                        help='Change default of some keys.',
                        nargs="*")
__PARSER__.add_argument('--merge',
                        help='Merge two or more tabular files with the target file.',
                        nargs="*")
__PARSER__.add_argument('--vertical-merge',
                        help='Merge files vertically',
                        action='store_true')
__PARSER__.add_argument('--horizontal-merge',
                        help='Merge two or more tabular files with the target file vertically',
                        action='store_true')
__PARSER__.add_argument('--excel',
                        help='Import the file into xls format, when using this argument, none of the data '
                             'in the target file should be colored nor styled',
                        action='store_true')
__PARSER__.add_argument('--row-fill',
                        help='List of data to embed into a row specified by the -r argument'
                             ', Usage: --row-fill [list] <from>-<to>'
                             ', check README.md for more information',
                        metavar='LIST')
__PARSER__.add_argument('--column-fill',
                        help='List of data to embed into a column specified by the -c argument',
                        metavar='LIST')
__PARSER__.add_argument("--slice-fill",
                        help='The portion of the row or column which are selected for fill',
                        metavar='RANGE')
__PARSER__.add_argument('--force-fill',
                        help='Add rows and columns to adjust the data',
                        action='store_true')
__PARSER__.add_argument('--reverse-fill',
                        help='The list of data in reversed format',
                        action='store_true')
__PARSER__.add_argument('--functional-expression',
                        help='Functional expression for accomplishing certain mathematical '
                             'actions, check README.md for more information',
                        metavar='Expression')
__PARSER__.add_argument('--functional-positioning',
                        help='Positioning the result with targeting, usage: '
                             '--functional-positioning <row/column> <index> <from>-<to>',
                        nargs="*")
__PARSER__.add_argument('--passwd',
                        help='Passwd for encrypting and decrypting')
__PARSER__.add_argument('--encrypt',
                        help='Action of encrypting with passwd specified by the --passwd argument, '
                             'It should not be used with other arguments except --file and --passwd',
                        action='store_true')
__PARSER__.add_argument('--decrypt',
                        help='Action of decrypting with passwd specified by the --passwd argument, '
                             'It should not be used with other arguments except --file and --passwd',
                        action='store_true')
__PARSER__.add_argument("--shift",
                        help='Shift set of datas to another area.',
                        nargs="*")
__PARSER__.add_argument("--shift-copy",
                        help="Shift the set of data while keeping the data as it is.",
                        action="store_true")
__PARSER__.add_argument('--serial-numbering',
                        help='Action of entering serial-numbers. usage: --serial-numbering '
                             '<row/column> <cell range> <number range>, the index of the row/column is specified by '
                             '-r/-c, ranged numbering is not supported',
                        nargs="*")
__PARSER__.add_argument('--force-sno',
                        help='If the number range is higher then the cell range, using this argument '
                             'will increase the cell-range',
                        action='store_true')
__PARSER__.add_argument('--reverse-sno',
                        help='Reverse the pattern of the numbers',
                        action='store_true')
__PARSER__.add_argument('--access-sub-list',
                        help="Access sub list given",
                         metavar='Title')
__PARSER__.add_argument('--set-sub-list',
                        help='Set an sub list',
                        metavar='<cords> <title>')
__PARSER__.add_argument('--set-dimension',
                        help='New dimension to the table',
                        metavar='TITLE')
__PARSER__.add_argument('--access-dimension',
                        help='Accessing a dimension',
                        metavar='TITLE')
__PARSER__.add_argument('--raw-detail',
                        help='Show raw details of the table',
                        action='store_true')
__PARSER__.add_argument('--tree',
                        help='Tree of the table,',
                        action='store_true')
__Dulux__ = __PARSER__.parse_args()


# Basic Functionality
def read(file_):
    with open(file_) as rfile:
        cont = rfile.read()
        rfile.close()
    return cont


def write(file_, content):
    with open(file_, 'w') as wfile:
        wfile.write(content)
        wfile.close()


def error(msg, avatar="ERROR"):
    return f"\033[01m\033[31m[\033[0m{avatar}\033[01m\033[31m] {msg}\033[0m"


def info(msg, avatar="INFO"):
    return f"\033[01m\033[34m[\033[0m{avatar}\033[01m\033[34m] {msg}\033[0m"


def success(msg, avatar="SUCCESS"):
    return f"\033[01m\033[32m[\033[0m{avatar}\033[01m\033[32m] {msg}\033[0m"


# Elementary variables
__FILE__ = __Dulux__.file
__Meta_Data__ = dict({})
__Primary_Data__ = []
__COLOR_DICT__ = {
    'Grey': '2',
    'Brown': '31',
    'Darkgreen': '32',
    'Gold': '33',
    'Indigo': '34',
    'Purple': '35',
    'Deepblue': '36',
    'Red': '91',
    'Green': '92',
    'Yellow': '93',
    'Blue': '94',
    'Violet': '95',
    'Cyan': '96',
    'Bold': '1',
    'Italic': '3',
    'Underline': '4',
    'Strikethrough': '9',
    'Doubleunderline': '21',
    'Reset': '0',
}
Repeatation = True
sys.setrecursionlimit(10**6)
# /Functions
Isfile = lambda: os.path.isfile(__FILE__)
GetContent = lambda: read(__FILE__)
isfloat = lambda string: string.replace(".", "", 1).isdigit()
srl = lambda string: ast.literal_eval(string)
average = lambda list: sum(list) / len(list)
max = lambda list: sorted(list)[-1]
min = lambda list: sorted(list)[0]
count = lambda list: len(list)


def set_default(args):
    try:
        key = args[0]
        value = args[1]
        if type(__Meta_Data__['__Defaults__'][key]).__name__ == 'bool':
            try:
                if type(ast.literal_eval(value)).__name__ == 'bool':
                   __Meta_Data__['__Defaults__'][key] = ast.literal_eval(value)
            except ValueError:
                print(error('Incorrect type, this key requires True or False input'))
                exit()
        elif key == 'Style':
            if value in ['plain', 'simple', 'github', 'grid', 'simple_grid', 'rounded_grid''heavy_grid', 'mixed_grid',
                         'double_grid', 'fancy_grid', 'outline', 'simple_outline', 'rounded_outline', 'heavy_outline',
                         'mixed_outline', 'double_outline', 'fancy_outline', 'pipe', 'orgtbl', 'asciidoc', 'jira',
                         'presto', 'pretty', 'psql', 'rst', 'mediawiki', 'moinmoin', 'youtrack', 'html', 'unsafehtml',
                         'latex', 'latex_raw', 'latex_booktabs', 'latex_longtable', 'textile', 'tsv']:
                __Meta_Data__['__Defaults__']['Style'] = value
            else:
                print(error('The style you mentioned is not defined in our library'))
    except KeyError:
        print(error("The Default key is invalid"))
        exit()

def TableTree():
    try:
        space = '    '
        branch = chr(9474) + '  '
        tee = chr(9500) + chr(9472) + ' '
        last = chr(9492) + chr(9472) + ' '
        global Repeatation
        def FDSL():
            List = []
            for i in Dict:
                if not i.split('/')[0] in List:
                    List.append(i.split('/')[0])
            return List
        def Has_sub_lists(tier):
            for i in Dict:
                if tier+'/' in i:
                    return True
            else:
                return False
        def get_sub_lists(tier):
            List2 = []
            for i in Dict:
                if (tier+'/' in i) and (i.split(tier+'/')[0]==''):
                    List2.append(i)
            Length_of_tier = len(tier.split('/'))
            for i in List2:
                if not len(i.split('/')) == Length_of_tier+1:
                    List2.remove(i)
            return List2
        def Tree(Lists, prefix=''):
            global Repeatation
            if Repeatation:
                sub_lists = FDSL()
                Repeatation = False
            else:
                sub_lists = get_sub_lists(tier=Lists)
            sub_lists.sort()
            pointers = [tee]*(len(sub_lists)-1)+[last]
            for pointer, sub_list in zip(pointers, sub_lists):
                yield prefix + pointer + sub_list.split('/')[-1]
                if Has_sub_lists(tier=sub_list):
                    extension = branch if pointer == tee else space
                    yield from Tree(Lists=sub_list, prefix=prefix+extension)
        global __Meta_Data__
        for j in __Meta_Data__:
            Repeatation = True
            if not j == '__Defaults__':
                if j == '1D':
                    print('PRIMARY DATA')
                else:
                    print(j, ' [Dimension]')
                Dict = __Meta_Data__[j]['Sub_lists']
                for i in Tree(Lists=Dict):
                    print(i)
    except Exception as ex:
        print(error(ex, avatar=type(ex).__name__))
        exit()

def Numerals(x1, y1, x2, y2, list):
    try:
        if x1 == x2:
            numbers = list[x1 - 1][y1 - 1:y2]
        elif y1 == y2:
            numbers = [i[y1 - 1] for i in list[x1 - 1:x2]]
        else:
            numbers_ = [i[y1 - 1:y2] for i in list[x1 - 1:x2]]
            numbers = []
            for i in numbers_:
                for j in i:
                    numbers.append(j)
        numbers2 = []
        for i in numbers:
            if type(i).__name__ == "str":
                if i == '':
                    pass
                else:
                    numbers2.append(int(i))
            else:
                numbers2.append(i)
        return numbers2
    except IndexError:
        print(error('The indexes are invalid'))
    except ValueError:
        print(error('No non-numerical characters should be included'))
        exit()


def PostContent():
    global __FILE__, __Primary_Data__, __Meta_Data__
    if not __Dulux__.access_dimension:
        if __Dulux__.access_sub_list:
            __Meta_Data__['1D']['Sub_lists'][__Dulux__.access_sub_list] = __Primary_Data__
        else:
            __Meta_Data__['1D']["__Primary_Data__"] = __Primary_Data__
    else:
        if __Dulux__.access_sub_list:
            __Meta_Data__[__Dulux__.access_dimension]['Sub_lists'][__Dulux__.access_sub_list] = __Primary_Data__
        else:
            __Meta_Data__[__Dulux__.access_dimension]['__Primary_Data__'] = __Primary_Data__
    write(file_=__FILE__, content=str(__Meta_Data__))


def ListContent():
    try:
        global __Primary_Data__, __Meta_Data__
        if __Dulux__.decrypt:
            return
        else:
            global __Primary_Data__, __FILE__
            content = GetContent()
            __Meta_Data__ = srl(content)
            if not __Dulux__.access_dimension:
                if __Dulux__.access_sub_list:
                    __Primary_Data__ = __Meta_Data__['1D']['Sub_lists'][f"{__Dulux__.access_sub_list}"]
                else:
                    __Primary_Data__ = __Meta_Data__['1D']['__Primary_Data__']
            else:
                if __Dulux__.access_sub_list:
                    __Primary_Data__ = __Meta_Data__[__Dulux__.access_dimension]['Sub_lists'][__Dulux__.access_sub_list]
                else:
                    __Primary_Data__ = __Meta_Data__[__Dulux__.access_dimension]['__Primary_Data__']
    except ValueError as E:
        if "malformed node or string" in E:
            print(error("The file might have been corrupted or maybe encrypted. Couldn't extract info of the file"))
            exit()
    except KeyError:
        print(error('Error occured, Try checking the name of the sub-list or dimension, else check wheter it is saved or not'))
        exit()

def colorize_data(Style, data):
    try:
        Source = ""
        if Style['Fs'] is not None:
            Source += f'\033[{__COLOR_DICT__[Style["Fs"]]}m'
        if Style['Fg'] is not None:
            Source += f'\033[{__COLOR_DICT__[Style["Fg"]]}m'
        Source += data + "\033[0m"
        return Source
    except KeyError:
        print(error('The style or the color you have entered is not compatible with PYSQL, please check other variants'))
        exit()


def add_data(row, column, data, Style, unicode, append_data=False, annotation='str'):
    try:
        global __Primary_Data__
        data1 = ""
        row, column = int(row), int(column)
        prev_data = __Primary_Data__[row - 1][column - 1]
        if unicode is None:
            if Style:
                if append_data:
                    data1 = str(prev_data) + colorize_data(Style, f'{data}')
                else:
                    data1 = colorize_data(Style, f'{data}')

            else:
                if not append_data:
                    try:
                        data1 = eval(f"{annotation}(str(data))")
                    except ValueError:
                        print(error('That data cannot be converted into that type.'))
                        exit()
                else:
                    data1 = str(prev_data) + data
        else:
            try:
                unicode = f"\\u{unicode}".encode("ASCII", errors="backslashreplace").decode("unicode_escape")
            except SyntaxError:
                print((error('There might be something illegal happening with that unicode you entered')))
            if Style:
                if not append_data:
                    data1 = colorize_data(Style, f'{data}{unicode}')
                else:
                    data1 = str(prev_data) + colorize_data(Style, f'{data}{unicode}')
            else:
                if not append_data:
                    data1 = f"{data}{unicode}"
                else:
                    data1 = str(prev_data) + f"{data}{unicode}"
        __Primary_Data__[row - 1][column - 1] = data1
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def row_embed(row, data, slicing=None, force_fill=False, reverse=False):
    try:
        global __Primary_Data__
        datas = srl(data)
        if reverse:
            datas = datas[::-1]
        else:
            pass
        row = int(row)
        length = range(len(__Primary_Data__[row - 1]))
        l = __Primary_Data__[row - 1]
        if not force_fill:
            if slicing is None:
                for i, j in zip(datas, length):
                    l[j] = i
            else:
                x = int(slicing.split("-")[0]) - 1
                y = int(slicing.split('-')[1])
                L = __Primary_Data__[row - 1][x:y]
                for i, j in zip(datas, range(len(L))):
                    L[j] = i
                __Primary_Data__[row - 1][x:y] = L
        else:
            Len_data = len(datas)
            Len_row = len(__Primary_Data__[0])
            if Len_data > Len_row:
                add_column(Len_data - Len_row)
                for i, j in zip(datas, range(len(__Primary_Data__[0]))):
                    l[j] = i
            else:
                for i, j in zip(datas, range(len(__Primary_Data__[0]))):
                    l[j] = i
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def column_embed(column, data, force_fill=False, slicing=None, reverse=False):
    try:
        global __Primary_Data__
        datas = srl(data)
        if force_fill and (slicing is not None):
            print(error('Using both slice_fill and force_fill is not advisable'))
        if reverse:
            datas = datas[::-1]
        else:
            pass
        column = int(column) - 1
        if not force_fill:
            if slicing is not None:
                x = int(slicing.split("-")[0]) - 1
                y = int(slicing.split('-')[1])
                L = __Primary_Data__[x:y]
                for i, k in zip(datas, L):
                    k[column] = i
                __Primary_Data__[x:y] = L
            else:
                for (i, j) in zip(__Primary_Data__, datas):
                    i[column] = j
        else:
            Len_data = len(datas)
            Len_column = len(__Primary_Data__)
            if Len_data > Len_column:
                add_row(Len_data - Len_column)
                for (i, j) in zip(__Primary_Data__, datas):
                    i[column] = j
            else:
                for (i, j) in zip(__Primary_Data__, datas):
                    i[column] = j
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def shift(args, copy=False):
    try:
        global __Primary_Data__

        row1 = int(args[0].split(",")[0])
        column1 = int(args[0].split(",")[1])
        row2 = int(args[1].split(",")[0])
        column2 = int(args[1].split(",")[1])
        r3 = int(args[2].split(",")[0])
        c3 = int(args[2].split(",")[1])

        if row1 == row2 and column1 == column2:
            data = __Primary_Data__[row1 - 1][column1 - 1]
            if not copy:
                __Primary_Data__[row1 - 1][column1 - 1] = ""

            __Primary_Data__[r3 - 1][c3 - 1] = data
        elif row1 == row2 and column1 != column2:
            data = __Primary_Data__[row1 - 1][column1 - 1:column2]
            if not copy:
                __Primary_Data__[row1 - 1][column1 - 1:column2] = len(data) * ['']

            try:
                __Primary_Data__[r3 - 1][c3 - 1:len(data) + c3 - 1] = data
            except IndexError:
                l1 = len(__Primary_Data__[r3 - 1][c3 - 1:-1])
                l2 = len(__Primary_Data__[row1 - 1][column1 - 1:column2])
                c = l2 - l1
                add_column(c)
                __Primary_Data__[r3 - 1][c3 - 1:len(data) + c3 - 1] = data
        elif row1 != row2 and column1 == column2:
            data = [i[column1 - 1] for i in __Primary_Data__[row1 - 1:row2]]
            if not copy:
                for i in __Primary_Data__[row1 - 1:row2]:
                    i[column1 - 1] = ""

            if len(__Primary_Data__[row1 - 1:row2]) <= len(__Primary_Data__[r3 - 1:]):
                for i, j in zip(__Primary_Data__[r3 - 1:len(data) + r3 - 1], data):
                    i[column1] = j
            else:
                l1 = len(__Primary_Data__[row1 - 1:row2])
                l2 = len(__Primary_Data__[r3 - 1:])
                r = l1 - l2
                add_row(r)
                for i, j in zip(__Primary_Data__[r3 - 1:len(data) + r3 - 1], data):
                    i[column1] = j
        else:
            data = []
            for i in __Primary_Data__[row1 - 1:row2]:
                data.append(i[column1 - 1:column2])
                if not copy:
                    i[column1 - 1:column2] = (column2 - (column1 - 1)) * ['']
            if len(data) > len(__Primary_Data__[r3 - 1:]):
                l = len(data) - len(__Primary_Data__[r3 - 1:])
                add_row(l)
            if len(data[0]) > len(__Primary_Data__[0][c3 - 1:]):
                l = len(data[0]) - len(__Primary_Data__[0][c3 - 1:])
                add_column(l)
            for i, j in zip(__Primary_Data__[r3 - 1:len(data) + r3 - 1], data):
                i[c3 - 1:len(data[0]) + c3 - 1] = j
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def functional_expression(expression, position):
    try:
        global __Primary_Data__
        range1 = int(position.split("-")[0])
        range2 = int(position.split("-")[1])
        R = __Primary_Data__
        if __Dulux__.column:
            column_index = int(__Dulux__.column) - 1
            for i, j in zip(__Primary_Data__[range1 - 1:range2], range(range1 - 1, range2)):
                ex_ = expression.replace('(r)', str(j)).replace('(c)', str(column_index))
                i[column_index] = eval(ex_)
        elif __Dulux__.row:
            row_index = int(__Dulux__.row) - 1
            for j in range(range1 - 1, range2):
                ex_ = expression.replace('(r)', str(row_index)).replace('(c)', str(j))
                __Primary_Data__[row_index][j] = eval(ex_)
        else:
            print(error('The first arg of --functional-positioning should be either \'row\' or \'column\' '))
            return
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))
        if (type(Ex).__name__ == 'ValueError') or (type(Ex).__name__ == 'TypeError'):
            print(error('Maybe the function need an other type inputs.'))
        if Ex == "name 'c' is not defined" or Ex == "name 'r' is not defined":
            print(error('Perhaps you might have not typed parenthesis for \'r\' and \'c\' or might missed the R'))
        else:
            print(error('The syntax of the expression might be invalid'))


def add_row(rows):
    try:
        global __Primary_Data__
        rows = int(rows)
        present_no_of_columns = len(__Primary_Data__[0])
        for i in range(rows):
            lists = [''] * present_no_of_columns
            __Primary_Data__.append(lists)
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def add_column(columns):
    try:
        global __Primary_Data__
        columns = int(columns)
        for i in __Primary_Data__:
            i += ([''] * columns)

    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def remove_row(index):
    try:
        global __Primary_Data__
        if "-" in index:
            range1 = int(index.split("-")[0]) - 1
            range2 = int(index.split("-")[1])
            del __Primary_Data__[range1:range2]
        else:
            index = int(index)
            index -= 1
            del __Primary_Data__[index]
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def remove_column(index):
    try:
        global __Primary_Data__
        if "-" in index:
            for i in __Primary_Data__:
                range1 = int(index.split("-")[0]) - 1
                range2 = int(index.split("-")[1])
                del i[range1:range2]
        else:
            index = int(index)
            index -= 1
            for i in __Primary_Data__:
                del i[index]
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def insert_row(index, no_of=1):
    try:
        global __Primary_Data__
        index = int(index)
        no_of = int(no_of)
        index -= 1
        no_of_columns = len(__Primary_Data__[0])
        new_list = [''] * no_of_columns
        for i in range(no_of):
            __Primary_Data__.insert(index, new_list)
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def insert_column(index, no_of=1):
    try:
        global __Primary_Data__
        index = int(index)
        no_of = int(no_of)
        index -= 1
        for i in __Primary_Data__:
            for j in range(no_of):
                i.insert(index, '')
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def serial_numbering(args, index, force=False, reverse=False):
    try:
        global __Primary_Data__
        roc, cell_range, number_range = args
        index = int(index) - 1
        cell_range_1 = int(cell_range.split("-")[0]) - 1
        cell_range_2 = int(cell_range.split("-")[1])
        number_range_1 = int(number_range.split("-")[0])
        number_range_2 = int(number_range.split("-")[1])
        len_of_cell_range = cell_range_2 - cell_range_1
        len_of_number_range = number_range_2 - number_range_1 + 1
        if force and (len_of_cell_range < len_of_number_range):
            u = len_of_number_range - len_of_cell_range
            if roc == 'column':
                add_row(u)
                column_index = index
                range_iterator = range(number_range_1, number_range_2 + 1 + u) if not reverse else range(
                    number_range_2 + u - 1, number_range_1 - 1, -1)
                for i, j in zip(__Primary_Data__[cell_range_1:cell_range_2 + u], range_iterator):
                    i[column_index] = j
            elif roc == 'row':
                add_column(u)
                row_index = index
                range_iterator = range(cell_range_1, cell_range_2 + u) if not reverse else range(cell_range_2 + u - 1,
                                                                                                 cell_range_1 - 1, -1)
                for j, k in zip(range(number_range_1, number_range_2 + 1), range_iterator):
                    __Primary_Data__[row_index][k] = j
        elif not force:
            if roc == 'column':
                column_index = index
                range_iterator = range(number_range_1, number_range_2 + 1) if not reverse else range(number_range_2,
                                                                                                     number_range_1 - 1,
                                                                                                     -1)
                for i, j in zip(__Primary_Data__[cell_range_1:cell_range_2], range_iterator):
                    i[column_index] = j
            elif roc == 'row':
                row_index = index
                range_iterator = range(number_range_1, number_range_2 + 1) if not reverse else range(number_range_2,
                                                                                                     number_range_1 - 1,
                                                                                                     -1)
                for j, k in zip(range_iterator, range(cell_range_1, cell_range_2)):
                    __Primary_Data__[row_index][k] = j
    except IndexError:
        print(error('The range or the index is not correctly defined for the serial numbering'))
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def encoding(passwd):
    try:
        if passwd is None:
            print(
                error('The --passwd argument is must for using --encrypt and --decrypt'))
            return
        file_ = __Dulux__.file
        key = Fernet.generate_key()
        Cf = Fernet(key)
        passwd_enc = (Cf.encrypt(passwd.encode('ascii'))).decode('ascii')
        content = read(file_)
        content_enc = (Cf.encrypt(content.encode('ascii'))).decode('ascii')
        Rect = (base64.b64encode(f"{content_enc}|{key.decode('ascii')}|{passwd_enc}".encode('ascii'))).decode('ascii')
        write(file_=file_, content=Rect)
        print(success('The file has been successfully encrypted', avatar='Success'))
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def decoding(passwd):
    try:
        if passwd is None:
            print(
                error('The --passwd argument is must for using --encrypt and --decrypt'))
            return
        file__ = __Dulux__.file
        content = read(file__)
        content_dec = (base64.b64decode(content.encode('ascii'))).decode('ascii')

        enc_content = content_dec.split("|")[0]
        key = content_dec.split("|")[1]
        passwd_enc = content_dec.split("|")[2]

        Cf = Fernet(key.encode('ascii'))
        if (Cf.decrypt(passwd_enc.encode('ascii'))).decode('ascii') == passwd:
            print(success('The password is verified.', avatar='Verified'))
        else:
            print(error('Password is incorrect for the decryption'))
            return
        dec_cont = (Cf.decrypt(enc_content.encode('ascii'))).decode('ascii')
        write(file_=file__, content=dec_cont)
        print(info('Content has been decrypted'))
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def readtbl(index=False, header=False, style=None):
    try:
        global __Meta_Data__, __Primary_Data__

        if style is None:
            if __Meta_Data__['__Defaults__']['Style'] != 'fancy_grid':
                style = __Meta_Data__['__Defaults__']['Style']
            else:
                style = 'fancy_grid'

        if index or (__Meta_Data__['__Defaults__']['Index']):
            __COPY__ = __Primary_Data__.copy()
            row_index = len(__COPY__)
            for i, j in zip(__COPY__, range(row_index)):
                i = [j + 1] + i
                __COPY__[j] = i
            print(tbl(__COPY__, headers=[i for i in range(len(__COPY__[0]))], tablefmt=style))

        else:
            if header or (__Meta_Data__['__Defaults__']['Headers']):
                print(tbl(__Primary_Data__, headers="firstrow", tablefmt=style))
            else:
                # print(__Primary_Data__)
                print(tbl(__Primary_Data__, tablefmt=style))
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def functions(arguments):
    try:
        global __Primary_Data__
        function, coord1, coord2, target_coord = arguments
        x1,y1 = [int(i) for i in coord1.split(",")]
        x2,y2 = [int(i) for i in coord2.split(',')]
        tx,ty = [int(i) for i in target_coord.split(",")]
        numbers = Numerals(x1, y1, x2, y2, __Primary_Data__)
        result = eval(f"{function}(numbers)")
        try:
            __Primary_Data__[tx - 1][ty - 1] = result
        except IndexError:
            print(error('The indexes are invalid'))
    except NameError:
        print(error("It is not an available function"))
    except Exception as ex:
        print(error(ex, avatar=type(ex).__name__))


def median(numbers):
    try:
        l = len(numbers)
        if l % 2 == 0:
            a1 = int((l / 2) - 1)
            a2 = int(l / 2)
            med = (numbers[a1] + numbers[a2]) / 2
        else:
            med = numbers[int(((l - 1) / 2))]
        return med
    except Exception as ex:
        print(error(ex, avatar=type(ex).__name__))


def vertical_merge(files):
    try:
        global __Primary_Data__
        tlist = []
        noc = len(__Primary_Data__[0])
        for i in files:
            with open(i) as file_:
                cont = file_.read()
                try:
                    d = srl(cont)
                except ValueError:
                    print(error('The files to be merged are not valid.'))
                nomc = len(d[0])
                if noc > nomc:
                    count_ = noc - nomc
                    for i in d:
                        i += count_ * ['']
                elif noc < nomc:
                    count_ = nomc - noc
                    add_column(count_)
                tlist += d
        __Primary_Data__ = __Primary_Data__ + tlist
    except Exception as ex:
        print(error(ex, avatar=type(ex).__name__))


def horizontal_merge(files):
    try:
        global __Primary_Data__
        tlist = []
        nor = len(__Primary_Data__)
        for i in files:
            cont = read(i)
            try:
                d = srl(cont)
            except ValueError:
                print(error('The files to be merged are not valid.'))
                return
            nomr = len(d)
            cl = len(d[0])
            if nor > nomr:
                count__ = nor - nomr
                for i in range(count__):
                    d += [cl * ['']]
            elif nor < nomr:
                count__ = nomr - nor
                add_row(count__)
            if not tlist:
                tlist = d
            else:
                for i, j in zip(tlist, d):
                    i += j
        for i, j in zip(__Primary_Data__, tlist):
            i += j

    except Exception as ex:
        print(error(ex, avatar=type(ex).__name__))


def conv_xls(file_):
    try:
        XLFILE = Workbook()
        sheet = XLFILE.add_sheet(file_)

        with open(file_) as f:
            context = f.read()
        list_ = srl(context)
        for i in range(len(list_)):
            for j in range(len(list_[i])):
                sheet.write(i, j, list_[i][j])
        XLFILE.save(file_ + ".xls")
    except Exception as ex:
        print(error(ex, avatar=type(ex).__name__))
        print(error('Might be something wrong with the file while converting to .xls, please check it'))

def set_sub_list(Title):
    try:
        global __Primary_Data__, __Meta_Data__
        row, column = int(__Dulux__.row), int(__Dulux__.column)
        if not __Dulux__.access_dimension:
            if __Dulux__.access_sub_list:
                __Meta_Data__['1D']['Sub_lists'][f'{__Dulux__.access_sub_list}/{Title}({row},{column})'] = [['','']]
            else:
                __Meta_Data__['1D']['Sub_lists'][f'{Title}({row},{column})'] = [['','']]
        else:
            if __Dulux__.access_sub_list:
                __Meta_Data__[__Dulux__.access_dimension]['Sub_lists'][f'{__Dulux__.access_sub_list}/{Title}({row},{column})'] = [['','']]
            else:
                __Meta_Data__[__Dulux__.access_dimension]['Sub_lists'][f'{Title}({row},{column})'] = [['','']]
        __Primary_Data__[row-1][column-1] = Title + ":<Sub-list>"
    except Exception as ex:
        print(error(ex, avatar=type(ex).__name__))

def Raw_Detail():
    try:
        global __Meta_Data__
        print(f'Raw details of {__Dulux__.file}:')
        for i in __Meta_Data__:
                if i == '__Defaults__':
                    pass
                else:
                    if i == '1D':
                        print('Primary data <First dimension>:- ')
                    else:
                        print(f"Dimension {i}")
                    print(f'\tPrimary data: {__Meta_Data__[i]["__Primary_Data__"]}')
                    print(f'\tSub lists:')
                    for j in __Meta_Data__[i]['Sub_lists']:
                        print(f'\t\t{j}:{__Meta_Data__[i]['Sub_lists'][j]}')
        print('Defaults:')
        for i,j in zip(__Meta_Data__['__Defaults__'],__Meta_Data__['__Defaults__'].values()):
            print(f"\t{i}:{j}")
    except Exception as ex:
        print(error(ex, avatar=type(ex).__name__))

def set_dimension(Title):
    try:
        global __Meta_Data__
        __Meta_Data__[Title] = {'__Primary_Data__':[['','']], 'Sub_lists':{}}
    except Exception as ex:
        print(error(ex, avatar=type(ex).__name__))


# elementary conditions
if __Dulux__.make:
    if not Isfile():
        with open(__Dulux__.file, "w") as file:
            file.write("{'1D':{'__Primary_Data__':[['','']], 'Sub_lists':{}},'__Defaults__': {'Index': False, 'Headers': False, 'Style': 'fancy_grid', 'Table': False}}")
            file.close()
    else:
        print(error('The file already exists.'))
        exit()
if Isfile():
    pass
else:
    print(error('File does not exist'))
    exit()

ListContent()

try:
    if __Dulux__.row and '-' in __Dulux__.row:
        r1, r2 = __Dulux__.row.split("-")
        A = __Primary_Data__[int(r1) - 1], __Primary_Data__[int(r2) - 1]
    elif __Dulux__.row and str(__Dulux__.row).isnumeric():
        A = __Primary_Data__[int(__Dulux__.row) - 1]
    if __Dulux__.column and '-' in __Dulux__.column:
        c1, c2 = __Dulux__.column.split("-")
        A = __Primary_Data__[0][int(c1) - 1], __Primary_Data__[0][int(c2) - 1]
    elif __Dulux__.column and str(__Dulux__.column).isnumeric():
        A = __Primary_Data__[0][int(__Dulux__.column) - 1]
except IndexError:
    print(error('Either your -r/--row or -c/--column has invalid index. Please check again.'))
    exit()
# print(__Primary_Data__)
# Interpretation of arguments
if __Dulux__.set_dimension:
    set_dimension(__Dulux__.set_dimension)
if __Dulux__.set_sub_list:
    set_sub_list(__Dulux__.set_sub_list)
if __Dulux__.set_default:
    set_default(__Dulux__.set_default)
if __Dulux__.vertical_merge and __Dulux__.merge:
    vertical_merge(__Dulux__.merge)
elif __Dulux__.horizontal_merge and __Dulux__.merge:
    horizontal_merge(__Dulux__.merge)
if __Dulux__.excel:
    conv_xls(__Dulux__.file)

if __Dulux__.add_data and (__Dulux__.row and __Dulux__.column) and (__Dulux__.font_style or __Dulux__.fg):
    add_data(__Dulux__.row, __Dulux__.column, __Dulux__.add_data,
             Style={'Fs': __Dulux__.font_style, 'Fg': __Dulux__.fg}, unicode=__Dulux__.unicode,
             append_data=__Dulux__.append, annotation=__Dulux__.annotation)
elif __Dulux__.add_data and (__Dulux__.row and __Dulux__.column):
    add_data(__Dulux__.row, __Dulux__.column, __Dulux__.add_data,
             Style=None, unicode=__Dulux__.unicode,
             append_data=__Dulux__.append, annotation=__Dulux__.annotation)

if __Dulux__.add_row:
    add_row(__Dulux__.add_row)

if __Dulux__.add_column:
    add_column(__Dulux__.add_column)

if __Dulux__.remove_row and __Dulux__.row:
    remove_row(__Dulux__.row)

if __Dulux__.remove_column and __Dulux__.column:
    remove_column(__Dulux__.column)

if __Dulux__.insert_row and __Dulux__.row:
    insert_row(__Dulux__.row, no_of=__Dulux__.insert_row)

if __Dulux__.insert_column and __Dulux__.column:
    insert_column(__Dulux__.column, no_of=__Dulux__.insert_column)

if __Dulux__.function:
    functions(__Dulux__.function)

if __Dulux__.row_fill and __Dulux__.row:
    row_embed(__Dulux__.row, __Dulux__.row_fill, force_fill=__Dulux__.force_fill, slicing=__Dulux__.slice_fill,
              reverse=__Dulux__.reverse_fill)
if __Dulux__.column_fill and __Dulux__.column:
    column_embed(__Dulux__.column, __Dulux__.column_fill, force_fill=__Dulux__.force_fill,
                 slicing=__Dulux__.slice_fill, reverse=__Dulux__.reverse_fill)

if __Dulux__.functional_expression and __Dulux__.functional_positioning:
    functional_expression(__Dulux__.functional_expression, __Dulux__.functional_positioning)

if __Dulux__.encrypt and __Dulux__.passwd:
    encoding(__Dulux__.passwd)
elif __Dulux__.decrypt and __Dulux__.passwd:
    decoding(__Dulux__.passwd)

if __Dulux__.serial_numbering and __Dulux__.row:
    serial_numbering(__Dulux__.serial_numbering, int(__Dulux__.row), __Dulux__.force_sno, __Dulux__.reverse_sno)
if __Dulux__.serial_numbering and __Dulux__.column:
    serial_numbering(__Dulux__.serial_numbering, int(__Dulux__.column), __Dulux__.force_sno, __Dulux__.reverse_sno)

if __Dulux__.shift:
    shift(__Dulux__.shift, copy=__Dulux__.shift_copy)

if __Dulux__.table or __Meta_Data__['__Defaults__']['Table']:
    readtbl(style=__Dulux__.style, index=__Dulux__.index, header=__Dulux__.header)

if __Dulux__.post:
    PostContent()

if __Dulux__.raw_detail:
    Raw_Detail()
if __Dulux__.tree:
    TableTree()
