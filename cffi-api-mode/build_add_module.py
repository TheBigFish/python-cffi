# import os
# from cffi import FFI

# cwd = os.path.join(os.path.dirname(__file__), ".")

# ffi = FFI()

# ffi.set_source("_add_module",
#     '#include <add.h>',
#     libraries=["add"],
#     library_dirs=[cwd],
#     include_dirs=[cwd],
# )

# ffi.cdef("int add(int a, int b);")

# if __name__ == "__main__":
#     ffi.compile()

import os
from cffi import FFI
ffibuilder = FFI()

cwd = os.path.join(os.path.dirname(__file__), ".")

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("""
    int add(int a, int b);
""")

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_add",
"""
     #include "add.h"   // the C header of the library
""",
     libraries=['add'],
     library_dirs=[cwd])   # library name, for the linker

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)