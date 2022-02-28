from pathlib import Path
from . import readcodearray

# Row-major: Mathematica, Numpy
# Column-major: Julia, Matlab/Octave, R, Maple, IDL/GDL

# start counting at 0: Python, IDL
# start counting at 1: Julia, Mathematica, Matlab/Octave, R, Maple,

# inclusive end index: Julia, Mathematica, Matlab/Octave, R, Maple, IDL/GDL
# non-inclusive end index: Python

def readcodedarr(dra, indicespath, valuespath):
    if len(dra) > 2:
       k, position = 2, 'third'
    elif len(dra) == 2:
        k, position = 1, 'second'
    else:
        k, position = 0, 'first'
    ct = f"import darr\n" \
         f"# path_to_data_dir is the directory that contains this README\n" \
         f"a = darr.RaggedArray(path='path_to_data_dir')\n" \
         f"# example to read {position} (k={k}) subarray:\n" \
         f"sa = a[2]\n"

    return ct


def readcodenumpymemmap(dra, indicespath, valuespath):
    rci = readcodearray.readcode(dra._indices, 'numpymemmap',
                                 varname='i',
                                 basepath=indicespath)
    rcv = readcodearray.readcode(dra._values, 'numpymemmap',
                                 varname='v',
                                 basepath=valuespath)
    rcv = ''.join(rcv.splitlines(keepends=True)[1:]) # get rid of import
    rff = 'def get_subarray(k):\n' \
          '    starti, endi = i[k]\n' \
          '    return v[starti:endi]\n'
    if len(dra) > 2:
       k, position = 2, 'third'
    elif len(dra) == 2:
        k, position = 1, 'second'
    else:
        k, position = 0, 'first'
    rca = f'# example to read {position} (k={k}) subarray:\n' \
          f'sa = get_subarray({k})\n' \

    ## the mext is never going to happen as Darr is based on memmap
    ## comment out
    # if (rci is None) or (rcv is None):
    #     return None
    # else:
    return f'{rci}{rcv}{rff}{rca}'


def readcoder(dra, indicespath, valuespath):
    rci = readcodearray.readcode(dra._indices, 'R',
                                 varname='i',
                                 basepath=indicespath)
    rcv = readcodearray.readcode(dra._values, 'R',
                                 varname='v',
                                 basepath=valuespath)
    if (rci is None) or (rcv is None):
        return None
    rci = f"# read array of indices to be used on values array\n{rci}"

    rcv = f"# read array of values:\n{rcv}"
    rff = 'get_subarray <- function(k){\n' \
          '    starti = i[1,k]+1  # R starts counting from 1\n' \
          '    endi = i[2,k]  # R has inclusive end index\n'
    commas = len(dra._arrayinfo['atom'])*','
    rff = f'{rff}    return (v[{commas}starti:endi])}}\n'
    rff = f"# create function to get subarrays:\n{rff}"
    if len(dra) > 2:
       k, position = 3, 'third'
    elif len(dra) == 2:
        k, position = 2, 'second'
    else:
        k, position = 1, 'first'
    rca =  f"# example to read {position} (k={k}) subarray:\n" \
           f"sa = get_subarray({k})\n"
    return f'{rci}{rcv}{rff}{rca}'

def readcodematlab(dra, indicespath, valuespath, varname='sa'):
    rci = readcodearray.readcode(dra._indices, 'matlab',
                                 varname='i',
                                 basepath=indicespath)
    rcv = readcodearray.readcode(dra._values, 'matlab',
                                 varname='v',
                                 basepath=valuespath)
    if (rci is None) or (rcv is None):
        return None
    numtype = dra.dtype.name
    rci = f"% read indice array, to be used on values array later:\n{rci}"
    rcv = f"% read {numtype} values array:\n{rcv}"
    if len(dra) > 2:
       k, position = 3, 'third'
    elif len(dra) == 2:
        k, position = 2, 'second'
    else:
        k, position = 1, 'first'
    dims = len(dra._arrayinfo['atom']) * ':,'
    rca = f'% create an anonymous function that returns the k-th subarray\n' \
          f'% from the values array:\n' \
          f'get_subarray = @(k) v({dims}i(1,k)+1:i(2,k));\n' \
          f'% example to read {position} (k={k}) subarray:\n' \
          f'sa = get_subarray({k});'
    return f'{rci}{rcv}{rca}\n'

# not supporting versions < 1 anymore
def readcodejulia(dra, indicespath, valuespath):
    rci = readcodearray.readcode(dra._indices, 'julia_ver1',
                                 varname='i',
                                 basepath=indicespath)
    rcv = readcodearray.readcode(dra._values, 'julia_ver1',
                                 varname='v',
                                 basepath=valuespath)
    if (rci is None) or (rcv is None):
        return None
    numtype = dra.dtype.name
    rci = f"# read indices array, to be used on values array later:\n{rci}"
    rcv = f"# read {numtype} values array:\n{rcv}"
    dims = len(dra._arrayinfo['atom']) * ':,'
    rff = f'function get_subarray(k)\n' \
          f'    starti = i[1,k]+1  # Julia starts counting from 1\n' \
          f'    endi = i[2,k]  # Julia has inclusive end index\n' \
          f'    v[{dims}starti:endi]\n' \
          f'end\n'
    rff = f"# create a function that returns the k-th subarray\n" \
          f"# from the values array:\n{rff}"
    if   len(dra) > 2:
       k, position = 3, 'third'
    elif len(dra) == 2:
        k, position = 2, 'second'
    else:
        k, position = 1, 'first'
    rca =  f'# example to read {position} (k={k}) subarray:\n' \
           f'sa = get_subarray({k})'
    return f'{rci}{rcv}{rff}{rca}\n'


def readcodemathematica(dra, indicespath, valuespath):
    numtype = dra.dtype.name
    rci = readcodearray.readcode(dra._indices, 'mathematica',
                                 varname='i',
                                 basepath=indicespath)
    rci = f"(* read indices array, to be used on values array later: *)\n{rci}"
    rcv = readcodearray.readcode(dra._values, 'mathematica',
                                 varname='v',
                                 basepath=valuespath)
    rcv = f"(* read {numtype} values array: *)\n{rcv}"
    if (rci is None) or (rcv is None):
        return None
    if   len(dra) > 2:
       k, position = 3, 'third'
    elif len(dra) == 2:
        k, position = 2, 'second'
    else:
        k, position = 1, 'first'
    rff = f'(* create a function that returns the k-th subarray\n' \
          f'   from the values array *):\n' \
          f'getsubarray[k_?IntegerQ] := \n' \
          f'    Module[{{l}},\n' \
          f'        l = k;\n' \
          f'        starti = i[[l,1]] + 1;\n' \
          f'        endi = i[[l,2]];\n' \
          f'        v[[starti;;endi]]]\n' \
          f'(* example to read {position} (k={k}) subarray: *)\n'\
          f'sa = getsubarray[{k}]\n'
    return f'{rci}{rcv}{rff}'

def readcodemaple(dra, indicespath, valuespath):
    numtype = dra.dtype.name
    rci = readcodearray.readcode(dra._indices, 'maple',
                                 varname='i',
                                 basepath=indicespath)
    rci = f"# read indices array, to be used on values array later:\n{rci}"
    rcv = readcodearray.readcode(dra._values, 'maple',
                                 varname='v',
                                 basepath=valuespath)
    rcv = f"# read {numtype} values array:\n{rcv}"
    if (rci is None) or (rcv is None):
        return None
    if   len(dra) > 2:
       k, position = 3, 'third'
    elif len(dra) == 2:
        k, position = 2, 'second'
    else:
        k, position = 1, 'first'
    dims = len(dra._arrayinfo['atom']) * '..,'
    rff = f'# create a function that returns the k-th subarray\n' \
          f'# from the values array:\n' \
          f'getsubarray := proc (k::integer);\n' \
          f'    v({dims} i(1,k) + 1 .. i(2,k));\n' \
          f'end proc;\n' \
          f'# example to read {position} (k={k}) subarray:\n'\
          f'sa = getsubarray({k});\n'
    return f'{rci}{rcv}{rff}'

# This has to be checked with IDL
def readcodeidl(dra, indicespath, valuespath):
    rci = readcodearray.readcode(dra._indices, 'idl',
                                 varname='i',
                                 basepath=indicespath)
    rcv = readcodearray.readcode(dra._values, 'idl',
                                 varname='v',
                                 basepath=valuespath)
    if (rci is None) or (rcv is None):
        return None
    if   len(dra) > 2:
       k, position = 2, 'third'
    elif len(dra) == 2:
        k, position = 1, 'second'
    else:
        k, position = 0, 'first'
    numtype = dra.dtype.name
    rci = f"; read indices array, to be used on values array later:\n{rci}"
    rcv = f"; read {numtype} values array:\n{rcv}"
    dims = len(dra._arrayinfo['atom']) * '*,'
    rff = f"; example to get the {position} (k={k}) subarray from the values " \
          f"array:\n"
    rca =  f'k = {k} ; set k to the subarray you want\n' \
           f'sa =  v[{dims}i[0,k]:i[1,k]-1] ; get subarray\n'
    return f'{rci}{rcv}{rff}{rca}'


readcodefunc = {
        'darr' : readcodedarr,
        'idl': readcodeidl,
        'julia': readcodejulia,
        'maple': readcodemaple,
        'mathematica': readcodemathematica,
        'matlab': readcodematlab,
        'numpymemmap': readcodenumpymemmap,
        'R': readcoder,
}

def readcode(dra, language, basepath='', abspath=False):
    """Produces the code to read the Darr raggedarray `dra` in a given
    programming language.

    Parameters
    ----------
    dra: Darr raggedarray
    language: str
        A supported language, such as 'julia', 'R', or 'matlab'
    abspath: bool
        Should the paths to the data files be absolute or not? Default:
        True.
    basepath: str or pathlib.Path or None
        Path relative to which the binary array data file should be
        provided. Default: None.

    Returns
    -------
    A string with code

    """
    if language not in readcodefunc:
        raise ValueError(f"'{language}' not supported ({readcodefunc.keys()})")
    if abspath:
        ip = dra._indices.path.absolute()
        vp = dra._values.path.absolute()
    elif basepath is not None:
        ip = Path(basepath) / dra._indicesdirname
        vp = Path(basepath) / dra._valuesdirname
    else:
        ip = Path(dra._indicesdirname)
        vp = Path(dra._valuesdirname)
    return readcodefunc[language](dra=dra, indicespath=ip, valuespath=vp)