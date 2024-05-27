#!/usr/bin/env python3
# /Libraries

from tabulate import tabulate as tbl
from argparse import ArgumentParser as AP
from unit_converter.converter import converts as conv
from xlwt import Workbook
from cryptography.fernet import Fernet
import base64
import os
import ast
from math import *

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
__PARSER__.add_argument('--merge',
                        help='Merge two or more tabular files with the target file.',
                        nargs="*")
__PARSER__.add_argument('--vertical-merge',
                        help='Merge files vertically',
                        action='store_true')
__PARSER__.add_argument('--horizontal-merge'
                        ,help='Merge two or more tabular files with the target file vertically',
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


def error(msg, avatar="F"):
    return f"\033[01m\033[31m[\033[0m{avatar}\033[01m\033[31m] {msg}\033[0m"


def info(msg, avatar="I"):
    return f"\033[01m\033[34m[\033[0m{avatar}\033[01m\033[34m] {msg}\033[0m"


def success(msg, avatar="S"):
    return f"\033[01m\033[32m[\033[0m{avatar}\033[01m\033[32m] {msg}\033[0m"


isfloat = lambda string: string.replace(".", "", 1).isdigit()
srl = lambda string: ast.literal_eval(string)
__FILE__ = __Dulux__.file
__Primary_Data__ = []


# /Functions
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
        print(error('The indexes are invalid', avatar='Erno: 6'))
    except ValueError:
        print(error('No non-numerical characters should be included', avatar='Erno: 7'))
        exit()


average = lambda list: sum(list) / len(list)
max = lambda list: sorted(list)[-1]
min = lambda list: sorted(list)[0]
count = lambda list: len(list)

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


def Isfile():
    global __FILE__
    return os.path.isfile(__FILE__)


def GetContent():
    global __FILE__
    return read(__FILE__)


def PostContent():
    global __FILE__, __Primary_Data__
    write(file_=__FILE__, content=str(__Primary_Data__))


def ListContent():
    try:
        if __Dulux__.decrypt:
            return
        else:
            global __Primary_Data__, __FILE__
            content = GetContent()
            __Primary_Data__ = srl(content)
    except ValueError as E:
        if "malformed node or string" in E:
            print(error("The file might have been corrupted or maybe encrypted. Couldn't extract info of the file",
                        avatar="Erno: 2"))


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
        print(error('The style or the color you have entered is not compatible with PYSQL, please check other variants',
                    avatar='Erno: 5'))
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
                        print(error('That data cannot be converted into that type.', avatar="Erno 5"))
                        exit()
                else:
                    data1 = str(prev_data) + data
        else:
            try:
                unicode = f"\\u{unicode}".encode("ASCII", errors="backslashreplace").decode("unicode_escape")
            except SyntaxError:
                print((error('There might be something illegal happening with that unicode you entered',
                             avatar="Erno: 4")))
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
            print(error('Using both slice_fill and force_fill is not advisable', avatar='Erno: 11'))
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


def functional_expression(expression, syntax):
    try:
        global __Primary_Data__
        range1 = int(syntax[2].split("-")[0])
        range2 = int(syntax[2].split("-")[1])
        R = __Primary_Data__
        if syntax[0] == 'column':
            column_index = int(syntax[1]) - 1
            for i, j in zip(__Primary_Data__[range1 - 1:range2], range(range1 - 1, range2)):
                ex_ = expression.replace('(r)', str(j)).replace('(c)', str(column_index))
                i[column_index] = eval(ex_)
        elif syntax[0] == 'row':
            row_index = int(syntax[1]) - 1
            for j in range(range1 - 1, range2):
                ex_ = expression.replace('(r)', str(row_index)).replace('(c)', str(j))
                __Primary_Data__[row_index][j] = eval(ex_)
        else:
            print(error('The first arg of --functional-positioning should be either \'row\' or \'column\' ',
                        avatar='Erno 12'))
            return
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))
        if (type(ex).__name__ == 'ValueError') or (type(ex).__name__ == 'TypeError'):
            print(error('Maybe the function need an other type inputs.', avatar='Erno: 14'))
        if Ex == "name 'c' is not defined" or Ex == "name 'r' is not defined":
            print(error('Perhaps you might have not typed parenthesis for \'r\' and \'c\' or might missed the R',
                        avatar='Erno: 13'))
        else:
            print(error('The syntax of the expression might be invalid', avatar='Erno: 15'))


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
        print(error('The range or the index is not correctly defined for the serial numbering', avatar='Erno: 16'))
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def encoding(passwd):
    try:
        if passwd is None:
            print(
                error('The --passwd argument is must for using --encrypt and --decrypt', avatar='Erno: 17'))
            return
        file = __Dulux__.file
        key = Fernet.generate_key()
        Cf = Fernet(key)
        passwd_enc = (Cf.encrypt(passwd.encode('ascii'))).decode('ascii')
        content = read(file)
        content_enc = (Cf.encrypt(content.encode('ascii'))).decode('ascii')
        Rect = (base64.b64encode(f"{content_enc}|{key.decode('ascii')}|{passwd_enc}".encode('ascii'))).decode('ascii')
        write(file_=file, content=Rect)
        print(success('The file has been successfully encrypted', avatar='Success'))
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def decoding(passwd):
    try:
        if passwd is None:
            print(
                error('The --passwd argument is must for using --encrypt and --decrypt', avatar='Erno: 17'))
            return
        file = __Dulux__.file
        content = read(file)
        content_dec = (base64.b64decode(content.encode('ascii'))).decode('ascii')

        enc_content = content_dec.split("|")[0]
        key = content_dec.split("|")[1]
        passwd_enc = content_dec.split("|")[2]

        Cf = Fernet(key.encode('ascii'))
        if (Cf.decrypt(passwd_enc.encode('ascii'))).decode('ascii') == passwd:
            print(success('The password is verified.', avatar='Verified'))
        else:
            print(error('Password is incorrect for the decryption', avatar='Erno: 18'))
            return
        dec_cont = (Cf.decrypt(enc_content.encode('ascii'))).decode('ascii')
        write(file_=file, content=dec_cont)
        print(info('Content has been decrypted'))
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def readtbl(index=False, header=False, style=None):
    try:
        if style is None:
            style = 'fancy_grid'
        global __Primary_Data__
        if index:
            __COPY__ = __Primary_Data__.copy()
            row_index = len(__COPY__)
            for i, j in zip(__COPY__, range(row_index)):
                i = [j + 1] + i
                __COPY__[j] = i
            print(tbl(__COPY__, headers=[i for i in range(len(__COPY__[0]))], tablefmt=style))
        else:
            if header:
                print(tbl(__Primary_Data__, headers="firstrow", tablefmt=style))
            else:
                print(tbl(__Primary_Data__, tablefmt=style))
    except Exception as Ex:
        print(error(Ex, avatar=type(Ex).__name__))


def functions(arguments):
    try:
        global __Primary_Data__
        function, x1, x2, y1, y2, tx, ty = arguments
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        tx = int(tx)
        ty = int(ty)
        numbers = Numerals(x1, y1, x2, y2, __Primary_Data__)
        result = eval(f"{function}(numbers)")
        try:
            __Primary_Data__[tx - 1][ty - 1] = result
        except IndexError:
            print(error('The indexes are invalid', avatar='Erno: 6'))
    except NameError:
        print(error("It is not an available function", avatar='Erno 8'))
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
                    print(error('The files to be merged are not valid.', avatar='Erno: 9'))
                nomc = len(d[0])
                if noc > nomc:
                    count = noc-nomc
                    for i in d:
                        i += count*['']
                elif noc < nomc:
                    count = nomc-noc
                    add_column(count)
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
                print(error('The files to be merged are not valid.', avatar='Erno: 9'))
                return
            nomr = len(d)
            cl = len(d[0])
            if nor > nomr:
                count = nor-nomr
                for i in range(count):
                    d += [cl*['']]
            elif nor < nomr:
                count = nomr-nor
                add_row(count)
            if tlist == []:
                tlist = d
            else:
                for i,j in zip(tlist, d):
                    i += j
        for i,j in zip(__Primary_Data__, tlist):
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
        print(error('Might be something wrong with the file while converting to .xls, please check it',
                    avatar='Erno: 10'))


if __Dulux__.make:
    if not Isfile():
        with open(__Dulux__.file, "w") as file:
            file.write("[['','']]")
            file.close()
    else:
        print(error('The file already exists.', avatar="Erno: 19"))
if Isfile():
    pass
else:
    print(error('File does not exist', avatar='Erno: 0'))
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
    print(error('Either your -r/--row or -c/--column has invalid index. Please check again.',
                avatar='Erno: 3'))
    exit()

# Interpretation of arguments
try:
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

    if __Dulux__.table and __Dulux__.index:
        readtbl(index=True, header=False, style=__Dulux__.style)
    elif __Dulux__.table and __Dulux__.header:
        readtbl(index=False, header=True, style=__Dulux__.style)
    elif __Dulux__.table:
        readtbl(style=__Dulux__.style)
    if __Dulux__.post:
        PostContent()
except Exception as ex:
    print(error(ex, avatar=type(ex).__name__))
    print(error('Something might have gone wrong, please check you inputs.', avatar='Erno: 1'))
