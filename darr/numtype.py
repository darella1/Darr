import sys
import numpy as np

# mathematica: https://reference.wolfram.com/language/ref/BinaryRead.html
# Octave: https://octave.org/doc/v4.2.0/Binary-I_002fO.html
# Matlab: https://mathworks.com/help/matlab/ref/fread.html
# R: https://www.rdocumentation.org/packages/base/versions/3.4.3/topics/readBin
# Julia: https://docs.julialang.org/en/release-0.4/manual/integers-and- floating-point-numbers/
# Maple: https://www.maplesoft.com/support/help/maple/view.aspx?path=FileTools%2FBinary%2FRead


numtypesdescr = {
    'int8': '8-bit signed integer (-128 to 127)',
    'int16': '16‐bit signed integer (-32768 to 32767)',
    'int32': '32‐bit signed integer (-2147483648 to 2147483647)',
    'int64': '64‐bit signed integer (-9223372036854775808 to '
             '9223372036854775807)',
    'uint8': '8‐bit unsigned integer (0 to 255)',
    'uint16': '16‐bit unsigned integer (0 to 65535)',
    'uint32': '32‐bit unsigned integer (0 to 4294967295)',
    'uint64': '64‐bit unsigned integer (0 to 18446744073709551615)',
    'float16': '16-bit half precision float (sign bit, 5 bits exponent, 10 '
               'bits mantissa)',
    'float32': '32-bit IEEE single precision float (sign bit, 8 bits exponent, '
               '23 bits mantissa)',
    'float64': '64-bit IEEE double precision float (sign bit, 11 bits '
               'exponent, 52 bits mantissa)',
    'complex64':'64-bit IEEE single‐precision complex number, represented by '
                'two 32 - bit floats (real and imaginary components)',
    'complex128': '128-bit IEEE double‐precision complex number, represented '
                  'by two 64 - bit floats (real and imaginary components)',
}

def arrayinfotodtype(arrayinfo):
    """Produces a numpy dtype description string like '<f8' based on a dictionary
    with type description details (as present in json array description file).

    Parameters
    ----------
    arrayinfo: dict
        A dictionary containing info on the numeric type. The following keys
        are required: 'numtype', 'byteorder'.

    Returns
    -------
    str
        dtype description string that can be used to instantiate numpy arrays

    """

    numtype = arrayinfo['numtype']
    byteorder = arrayinfo['byteorder']
    if numtype not in numtypesdescr.keys():
        raise ValueError(
            f"'{numtype}' is not a valid numeric type")
    if byteorder not in ('little', 'big'):
        raise ValueError(f"'{byteorder}' is not a valid order")
    endianness = {'big': '>', 'little': '<'}[byteorder]
    return np.dtype(numtype).newbyteorder(endianness).str


def arraynumtypeinfo(ndarray):
    """Returns a dictionary with numeric type and layout info, to be used
    for saving as json.

    """
    sys_is_le = (sys.byteorder == 'little')
    bo = ndarray.dtype.byteorder
    if (bo == '<') or (sys_is_le and (bo in ('|', '='))):
        bostr = 'little'
    else:
        bostr = 'big'
    return {  # 'dtypedescr': str(ndarray.dtype.descr[0][1]),
        'numtype': ndarray.dtype.name,
        'arrayorder': 'C' if ndarray.flags['C_CONTIGUOUS'] else 'F',
        'shape': ndarray.shape,
        'byteorder': bostr}

