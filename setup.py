import sys
import versioneer
import setuptools

if sys.version_info < (3,6):
    print("Darr requires Python 3.6 or higher please upgrade")
    sys.exit(1)

long_description = \
"""|Github CI Status| |Appveyor Status| |PyPi version| |Conda Forge|
|Codecov Badge| |Docs Status| |Zenodo Badge| |PyUp Badge|

Darr is a Python library that stores NumPy arrays on disk in a way that is
simple and self-documented, which makes them easily accessible from a wide
range of computing environments. Arrays are automatically kept up-to-date
with a full explanation of how data is stored, including code to read
itself in languages such as R, Julia, IDL, Matlab, Maple, and Mathematica,
or in Python/Numpy without Darr (see `example
<https://github.com/gbeckers/Darr/tree/master/examplearrays/arrays
/array_int32_2D.darr>`__). Keeping data universally readable and documented is
a pillar of good scientific practice, and a good idea in general. More
rationale for a tool-independent approach to numeric array storage is provided
`here <https://darr.readthedocs.io/en/latest/rationale.html>`__.

Under the hood, Darr uses NumPy memory-mapped arrays, which is a widely
established and trusted way of working with disk-based numerical arrays, and
which makes Darr fully NumPy compatible. This enables efficient out-of-core
read/write access to potentially very large arrays. What Darr adds is that it
automatically keeps your arrays fully documented, open, and thus widely
readable. Further, Darr adds functionality to make your life easier in other
ways, such as the support for ragged arrays, the ability to create arrays from
iterators, append and truncate functionality, and the easy use of metadata.

Flat binary files and (JSON) text files are accompanied by a README text file
that explains how the array and metadata are stored (`see example arrays
<https://github.com/gbeckers/Darr/tree/master/examplearrays/>`__).
It is trivially easy to share your arrays with others or with yourself when
working in different computing environments because they always contains clear
documentation of the specific data at hand, including code to read it.
Does your colleague want to try out an interesting algorithm in R or Matlab
on your arrays?  No need to export anything or to provide elaborate
explanation. No dependence on complicated formats or specialized libraries.
No looking up things. A copy-paste of a few lines of code from the
documentation stored with the data is sufficient. Self-documentation and code
examples are automatically updated as you change your arrays when working
with them.

See this `tutorial <https://darr.readthedocs.io/en/latest/tutorialarray.html>`__
for a brief introduction, or the
`documentation <http://darr.readthedocs.io/>`__ for more info.

Darr is currently pre-1.0, still undergoing development. It is open source and
freely available under the `New BSD License
<https://opensource.org/licenses/BSD-3-Clause>`__ terms.

Features
--------
-  Data is stored purely based on flat binary and text files, maximizing
   universal readability.
-  Automatic self-documention, including copy-paste ready code snippets for
   reading the array in a number of popular data analysis environments, such as
   Python (without Darr), R, Julia, Octave/Matlab, GDL/IDL, and Mathematica
   (see `example array
   <https://github.com/gbeckers/Darr/tree/master/examplearrays/arrays/array_int32_2D.darr>`__).
-  Disk-persistent array data is directly accessible through `NumPy
   indexing <https://numpy.org/doc/stable/reference/arrays.indexing.html>`__
   and may be larger than RAM and that is easily appendable.
-  Supports ragged arrays.
-  Easy use of metadata, stored in a widely readable separate
   `JSON <https://en.wikipedia.org/wiki/JSON>`__ text file.
-  Many numeric types are supported: (u)int8-(u)int64, float16-float64,
   complex64, complex128.
-  Integrates easily with the `Dask <https://dask.pydata.org/en/latest/>`__
   library for out-of-core computation on very large arrays.
-  Minimal dependencies, only `NumPy <http://www.numpy.org/>`__.

See the `documentation <http://darr.readthedocs.io/>`__ for more information.

.. |Github CI Status| image:: https://github.com/gbeckers/Darr/actions/workflows/python_package.yml/badge.svg
   :target: https://github.com/gbeckers/Darr/actions/workflows/python_package.yml
.. |Appveyor Status| image:: https://ci.appveyor.com/api/projects/status/github/gbeckers/darr?svg=true
   :target: https://ci.appveyor.com/project/gbeckers/darr
.. |PyPi version| image:: https://img.shields.io/badge/pypi-0.5.3-orange.svg
   :target: https://pypi.org/project/darr/
.. |Conda Forge| image:: https://anaconda.org/conda-forge/darr/badges/version.svg
   :target: https://anaconda.org/conda-forge/darr
.. |Docs Status| image:: https://readthedocs.org/projects/darr/badge/?version=stable
   :target: https://darr.readthedocs.io/en/stable/
.. |Repo Status| image:: https://www.repostatus.org/badges/latest/active.svg
   :alt: Project Status: Active – The project has reached a stable, usable state and is being actively developed.
   :target: https://www.repostatus.org/#active
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/c0157592ce7a4ecca5f7d8527874ce54
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/gbeckers/Darr?utm_source=github.com&utm_medium=referral&utm_content=gbeckers/Darr&utm_campaign=Badge_Grade_Dashboard
.. |PyUp Badge| image:: https://pyup.io/repos/github/gbeckers/Darr/shield.svg
   :target: https://pyup.io/repos/github/gbeckers/Darr/
   :alt: Updates
.. |Zenodo Badge| image:: https://zenodo.org/badge/151593293.svg
   :target: https://zenodo.org/badge/latestdoi/151593293
.. |Codecov Badge| image:: https://codecov.io/gh/gbeckers/Darr/branch/master/graph/badge.svg?token=BBV0WDIUSJ
   :target: https://codecov.io/gh/gbeckers/Darr

"""

setuptools.setup(
    name='darr',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=['darr', 'darr.tests'],
    url='https://github.com/gbeckers/darr',
    license='BSD-3',
    author='Gabriel J.L. Beckers',
    author_email='gabriel@gbeckers.nl',
    description='Memory-mapped numeric arrays, based on a '\
                'format that is self-explanatory and tool-independent',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    python_requires='>=3.6',
    install_requires=['numpy', 'packaging'],
    data_files = [("", ["LICENSE"])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
    ],
    project_urls={  # Optional
        'Source': 'https://github.com/gbeckers/darr',
    },
)
