---
title: '"ctypes" --- A foreign function library for Python'
source_url: https://docs.python.org/es/3
source_path: library/ctypes.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2190
---

# "ctypes" --- A foreign function library for Python

**Source code:** Lib/ctypes

======================================================================

"ctypes" is a foreign function library for Python.  It provides C
compatible data types, and allows calling functions in DLLs or shared
libraries.  It can be used to wrap these libraries in pure Python.

This is an *optional module*. If it is missing from your copy of
CPython, look for documentation from your distributor (that is,
whoever provided Python to you). If you are the distributor, see
Requirements for optional modules.

Advertencia:

  "ctypes" provides low-level access to native libraries and the
  process's memory, bypassing Python's safety mechanisms and allowing
  execution of arbitrary native code. Incorrect use can corrupt data
  and objects, reveal sensitive information, cause crashes, or
  otherwise compromise the running process.

## tutorial de ctypes

Nota: Algunos ejemplos de código hacen referencia al tipo ctypes
"c_int". En las plataformas donde "sizeof(long) == sizeof(int)" es un
alias de "c_long". Por lo tanto, no debe confundirse si "c_long" se
imprime si espera "c_int" --- son en realidad del mismo tipo.

### Carga de bibliotecas de enlaces dinámicos

"ctypes" exports the "cdll", and on Windows "windll" and "oledll"
objects, for loading dynamic link libraries.

You load libraries by accessing them as attributes of these objects.
"cdll" loads libraries which export functions using the standard
"cdecl" calling convention, while "windll" libraries call functions
using the "stdcall" calling convention. "oledll" also uses the
"stdcall" calling convention, and assumes the functions return a
Windows "HRESULT" error code. The error code is used to automatically
raise an "OSError" exception when the function call fails.

Distinto en la versión 3.3: Los errores de Windows solían generar
"WindowsError", que ahora es un alias de "OSError".

Here are some examples for Windows. Note that "msvcrt" is the MS
standard C library containing most standard C functions, and uses the
"cdecl" calling convention:

   >>> from ctypes import *
   >>> print(windll.kernel32)
   <WinDLL 'kernel32', handle ... at ...>
   >>> print(cdll.msvcrt)
   <CDLL 'msvcrt', handle ... at ...>
   >>> libc = cdll.msvcrt
   >>>

Windows agrega automáticamente la extensión común ".dll".

Nota:

  Acceder a la biblioteca estándar de C a través de "cdll.msvcrt"
  utilizará una versión obsoleta de la biblioteca que puede ser
  incompatible con la utilizada por Python. Cuando sea posible, use la
  funcionalidad nativa de Python, o bien importe y use el módulo
  "msvcrt".

Other systems require the filename *including* the extension to load a
library, so attribute access can not be used to load libraries. Either
the "LoadLibrary()" method of the dll loaders should be used, or you
should load the library by creating an instance of "CDLL" by calling
the constructor.

For example, on Linux:

   >>> cdll.LoadLibrary("libc.so.6")
   <CDLL 'libc.so.6', handle ... at ...>
   >>> libc = CDLL("libc.so.6")
   >>> libc
   <CDLL 'libc.so.6', handle ... at ...>
   >>>

On macOS:

   >>> cdll.LoadLibrary("libc.dylib")
   <CDLL 'libc.dylib', handle ... at ...>
   >>> libc = CDLL("libc.dylib")
   >>> libc
   <CDLL 'libc.dylib', handle ... at ...>

### Acceder a las funciones de los dll cargados

Las funciones se acceden como atributos de los objetos dll:

   >>> libc.printf
   <_FuncPtr object at 0x...>
   >>> print(windll.kernel32.GetModuleHandleA)
   <_FuncPtr object at 0x...>
   >>> print(windll.kernel32.MyOwnFunction)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "ctypes.py", line 239, in __getattr__
       func = _StdcallFuncPtr(name, self)
   AttributeError: function 'MyOwnFunction' not found
   >>>

Note that win32 system dlls like "kernel32" and "user32" often export
ANSI as well as UNICODE versions of a function. The UNICODE version is
exported with a "W" appended to the name, while the ANSI version is
exported with an "A" appended to the name. The win32 "GetModuleHandle"
function, which returns a *module handle* for a given module name, has
the following C prototype, and a macro is used to expose one of them
as "GetModuleHandle" depending on whether UNICODE is defined or not:

   /* ANSI version */
   HMODULE GetModuleHandleA(LPCSTR lpModuleName);
   /* UNICODE version */
   HMODULE GetModuleHandleW(LPCWSTR lpModuleName);

*windll* no intenta seleccionar una de ellas por arte de magia, se
debe acceder a la versión que se necesita especificando
"GetModuleHandleA" o "GetModuleHandleW" explícitamente, y luego
llamarlo con bytes u objetos de cadena respectivamente.

A veces, las dlls exportan funciones con nombres que no son
identificadores válidos de Python, como ""??2@YAPAXI@Z"". En este caso
tienes que usar "getattr()" para recuperar la función:

   >>> getattr(cdll.msvcrt, "??2@YAPAXI@Z")
   <_FuncPtr object at 0x...>
   >>>

En Windows, algunas dlls exportan funciones no por nombre sino por
ordinal. Se pueden acceder a estas funciones indexando el objeto dll
con el número ordinal:

   >>> cdll.kernel32[1]
   <_FuncPtr object at 0x...>
   >>> cdll.kernel32[0]
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "ctypes.py", line 310, in __getitem__
       func = _StdcallFuncPtr(name, self)
   AttributeError: function ordinal 0 not found
   >>>

### Funciones de llamada

You can call these functions like any other Python callable. This
example uses the "rand()" function, which takes no arguments and
returns a pseudo-random integer:

   >>> print(libc.rand())
   1804289383

On Windows, you can call the "GetModuleHandleA()" function, which
returns a win32 module handle (passing "None" as single argument to
call it with a "NULL" pointer):

   >>> print(hex(windll.kernel32.GetModuleHandleA(None)))
   0x1d000000
   >>>

"ValueError" es lanzado cuando se llama a una función "stdcall" con la
convención de llamada "cdecl", o viceversa:

   >>> cdll.kernel32.GetModuleHandleA(None)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: Procedure probably called with not enough arguments (4 bytes missing)
   >>>

   >>> windll.msvcrt.printf(b"spam")
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: Procedure probably called with too many arguments (4 bytes in excess)
   >>>

Para saber la convención de llamada correcta, hay que mirar en el
archivo de encabezado C o en la documentación de la función que se
quiere llamar.

On Windows, "ctypes" uses win32 structured exception handling to
prevent crashes from general protection faults when functions are
called with invalid argument values:

   >>> windll.kernel32.GetModuleHandleA(32)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   OSError: exception: access violation reading 0x00000020
   >>>

The "faulthandler" module can help debug crashes, such as segmentation
faults produced by erroneous C library calls.

"None", integers, bytes objects and (unicode) strings are the only
native Python objects that can directly be used as parameters in these
function calls. "None" is passed as a C "NULL" pointer, bytes objects
and strings are passed as pointer to the memory block that contains
their data (char* or wchar_t*).  Python integers are passed as the
platform's default C int type, their value is masked to fit into the C
type.

Before we move on calling functions with other parameter types, we
have to learn more about "ctypes" data types.

### Tipos de datos fundamentales

"ctypes" defines a number of primitive C compatible data types:

+---------------------------+---------------------------+---------------------------+---------------------------+
| tipo ctypes               | Tipo C                    | Tipo Python               | "_type_"                  |
|===========================|===========================|===========================|===========================|
## | "c_bool"                  | _Bool                     | "bool"                    | "'?'"                     |

## | "c_char"                  | char                      | 1-character "bytes"       | "'c'"                     |

## | "c_wchar"                 | "wchar_t"                 | 1-character "str"         | "'u'"                     |

## | "c_byte"                  | char                      | "int"                     | "'b'"                     |

## | "c_ubyte"                 | unsigned char             | "int"                     | "'B'"                     |

## | "c_short"                 | short                     | "int"                     | "'h'"                     |

## | "c_ushort"                | unsigned short            | "int"                     | "'H'"                     |

## | "c_int"                   | int                       | "int"                     | "'i'" *                   |

## | "c_int8"                  | "int8_t"                  | "int"                     | *                         |

## | "c_int16"                 | "int16_t"                 | "int"                     | *                         |

## | "c_int32"                 | "int32_t"                 | "int"                     | *                         |

## | "c_int64"                 | "int64_t"                 | "int"                     | *                         |

## | "c_uint"                  | unsigned int              | "int"                     | "'I'" *                   |

## | "c_uint8"                 | "uint8_t"                 | "int"                     | *                         |

## | "c_uint16"                | "uint16_t"                | "int"                     | *                         |

## | "c_uint32"                | "uint32_t"                | "int"                     | *                         |

## | "c_uint64"                | "uint64_t"                | "int"                     | *                         |

## | "c_long"                  | long                      | "int"                     | "'l'"                     |

## | "c_ulong"                 | unsigned long             | "int"                     | "'L'"                     |

## | "c_longlong"              | long long                 | "int"                     | "'q'" *                   |

## | "c_ulonglong"             | unsigned long long        | "int"                     | "'Q'" *                   |

## | "c_size_t"                | "size_t"                  | "int"                     | *                         |

## | "c_ssize_t"               | "Py_ssize_t"              | "int"                     | *                         |

## | "c_time_t"                | "time_t"                  | "int"                     | *                         |

## | "c_float"                 | float                     | "float"                   | "'f'"                     |

## | "c_double"                | double                    | "float"                   | "'d'"                     |

## | "c_longdouble"            | long double               | "float"                   | "'g'" *                   |

## | "c_char_p"                | char* (terminado en NUL)  | "bytes" or "None"         | "'z'"                     |

| "c_wchar_p"               | wchar_t* (terminado en    | "str" or "None"           | "'Z'"                     |
## |                           | NUL)                      |                           |                           |

## | "c_void_p"                | void*                     | "int" or "None"           | "'P'"                     |

## | "py_object"               | PyObject*                 | "object"                  | "'O'"                     |

## | VARIANT_BOOL              | short int                 | "bool"                    | "'v'"                     |

Additionally, if IEC 60559 compatible complex arithmetic (Annex G) is
supported in both C and "libffi", the following complex types are
available:

+---------------------------+---------------------------+---------------------------+---------------------------+
| tipo ctypes               | Tipo C                    | Tipo Python               | "_type_"                  |
|===========================|===========================|===========================|===========================|
## | "c_float_complex"         | float complex             | "complex"                 | "'F'"                     |

## | "c_double_complex"        | double complex            | "complex"                 | "'D'"                     |

## | "c_longdouble_complex"    | long double complex       | "complex"                 | "'G'"                     |

Todos estos tipos pueden ser creados llamándolos con un inicializador
opcional del tipo y valor correctos:

   >>> c_int()
   c_long(0)
   >>> c_wchar_p("Hello, World")
   c_wchar_p(140018365411392)
   >>> c_ushort(-3)
   c_ushort(65533)
   >>>

The constructors for numeric types will convert input using
"__bool__()", "__index__()" (for "int"), "__float__()" or
"__complex__()". This means "c_bool" accepts any object with a truth
value:

   >>> empty_list = []
   >>> c_bool(empty_list)
   c_bool(False)

Dado que estos tipos son mutables, su valor también puede ser cambiado
después:

   >>> i = c_int(42)
   >>> print(i)
   c_long(42)
   >>> print(i.value)
   42
   >>> i.value = -99
   >>> print(i.value)
   -99
   >>>

Assigning a new value to instances of the pointer types "c_char_p",
"c_wchar_p", and "c_void_p" changes the *memory location* they point
to, *not the contents* of the memory block (of course not, because
Python string objects are immutable):

   >>> s = "Hello, World"
   >>> c_s = c_wchar_p(s)
   >>> print(c_s)
   c_wchar_p(139966785747344)
   >>> print(c_s.value)
   Hello World
   >>> c_s.value = "Hi, there"
   >>> print(c_s)              # the memory location has changed
   c_wchar_p(139966783348904)
   >>> print(c_s.value)
   Hi, there
   >>> print(s)                # first object is unchanged
   Hello, World
   >>>

Sin embargo, debe tener cuidado de no pasarlos a funciones que esperan
punteros a la memoria mutable. Si necesitas bloques de memoria
mutables, ctypes tiene una función "create_string_buffer()" que los
crea de varias maneras. El contenido actual del bloque de memoria
puede ser accedido (o cambiado) con la propiedad "raw"; si quieres
acceder a él como cadena terminada NUL, usa la propiedad "value":

   >>> from ctypes import *
   >>> p = create_string_buffer(3)            # create a 3 byte buffer, initialized to NUL bytes
   >>> print(sizeof(p), repr(p.raw))
   3 b'\x00\x00\x00'
   >>> p = create_string_buffer(b"Hello")     # create a buffer containing a NUL terminated string
   >>> print(sizeof(p), repr(p.raw))
   6 b'Hello\x00'
   >>> print(repr(p.value))
   b'Hello'
   >>> p = create_string_buffer(b"Hello", 10) # create a 10 byte buffer
   >>> print(sizeof(p), repr(p.raw))
   10 b'Hello\x00\x00\x00\x00\x00'
   >>> p.value = b"Hi"
   >>> print(sizeof(p), repr(p.raw))
   10 b'Hi\x00lo\x00\x00\x00\x00\x00'
   >>>

The "create_string_buffer()" function replaces the old "c_buffer()"
function (which is still available as an alias).  To create a mutable
memory block containing unicode characters of the C type "wchar_t",
use the "create_unicode_buffer()" function.

### Funciones de llamada, continuación

Note que printf imprime al canal de salida estándar real, *no* a
"sys.stdout", por lo que estos ejemplos sólo funcionarán en el prompt
de la consola, no desde dentro de *IDLE* o *PythonWin*:

   >>> printf = libc.printf
   >>> printf(b"Hello, %s\n", b"World!")
   Hello, World!
   14
   >>> printf(b"Hello, %S\n", "World!")
   Hello, World!
   14
   >>> printf(b"%d bottles of beer\n", 42)
   42 bottles of beer
   19
   >>> printf(b"%f bottles of beer\n", 42.5)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ctypes.ArgumentError: argument 2: TypeError: Don't know how to convert parameter 2
   >>>

As has been mentioned before, all Python types except integers,
strings, and bytes objects have to be wrapped in their corresponding
"ctypes" type, so that they can be converted to the required C data
type:

   >>> printf(b"An int %d, a double %f\n", 1234, c_double(3.14))
   An int 1234, a double 3.140000
   31
   >>>

### Calling variadic functions

On a lot of platforms calling variadic functions through ctypes is
exactly the same as calling functions with a fixed number of
parameters. On some platforms, and in particular ARM64 for Apple
Platforms, the calling convention for variadic functions is different
than that for regular functions.

On those platforms it is required to specify the "argtypes" attribute
for the regular, non-variadic, function arguments:

   libc.printf.argtypes = [ctypes.c_char_p]

Because specifying the attribute does not inhibit portability it is
advised to always specify "argtypes" for all variadic functions.

### Funciones de llamada con sus propios tipos de datos personalizados

You can also customize "ctypes" argument conversion to allow instances
of your own classes be used as function arguments. "ctypes" looks for
an "_as_parameter_" attribute and uses this as the function argument.
The attribute must be an integer, string, bytes, a "ctypes" instance,
or an object with an "_as_parameter_" attribute:

   >>> class Bottles:
   ...     def __init__(self, number):
   ...         self._as_parameter_ = number
   ...
   >>> bottles = Bottles(42)
   >>> printf(b"%d bottles of beer\n", bottles)
   42 bottles of beer
   19
   >>>

If you don't want to store the instance's data in the "_as_parameter_"
instance variable, you could define a "@property" which makes the
attribute available on request.

### Especificar los tipos de argumentos requeridos (prototipos de funciones)

It is possible to specify the required argument types of functions
exported from DLLs by setting the "argtypes" attribute.

"argtypes" must be a sequence of C data types (the "printf()" function
is probably not a good example here, because it takes a variable
number and different types of parameters depending on the format
string, on the other hand this is quite handy to experiment with this
feature):

   >>> printf.argtypes = [c_char_p, c_char_p, c_int, c_double]
   >>> printf(b"String '%s', Int %d, Double %f\n", b"Hi", 10, 2.2)
   String 'Hi', Int 10, Double 2.200000
   37
   >>>

La especificación de un formato protege contra los tipos de argumentos
incompatibles (al igual que un prototipo para una función C), e
intenta convertir los argumentos en tipos válidos:

   >>> printf(b"%d %d %d", 1, 2, 3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ctypes.ArgumentError: argument 2: TypeError: 'int' object cannot be interpreted as ctypes.c_char_p
   >>> printf(b"%s %d %f\n", b"X", 2, 3)
   X 2 3.000000
   13
   >>>

If you have defined your own classes which you pass to function calls,
you have to implement a "from_param()" class method for them to be
able to use them in the "argtypes" sequence. The "from_param()" class
method receives the Python object passed to the function call, it
should do a typecheck or whatever is needed to make sure this object
is acceptable, and then return the object itself, its "_as_parameter_"
attribute, or whatever you want to pass as the C function argument in
this case. Again, the result should be an integer, string, bytes, a
"ctypes" instance, or an object with an "_as_parameter_" attribute.

### Tipos de retorno

By default functions are assumed to return the C int type.  Other
return types can be specified by setting the "restype" attribute of
the function object.

The C prototype of "time()" is "time_t time(time_t *)". Because
"time_t" might be of a different type than the default return type
int, you should specify the "restype" attribute:

   >>> libc.time.restype = c_time_t

The argument types can be specified using "argtypes":

   >>> libc.time.argtypes = (POINTER(c_time_t),)

To call the function with a "NULL" pointer as first argument, use
"None":

   >>> print(libc.time(None))
   1150640792

Here is a more advanced example, it uses the "strchr()" function,
which expects a string pointer and a char, and returns a pointer to a
string:

   >>> strchr = libc.strchr
   >>> strchr(b"abcdef", ord("d"))
   8059983
   >>> strchr.restype = c_char_p    # c_char_p is a pointer to a string
   >>> strchr(b"abcdef", ord("d"))
   b'def'
   >>> print(strchr(b"abcdef", ord("x")))
   None
   >>>

If you want to avoid the "ord("x")" calls above, you can set the
"argtypes" attribute, and the second argument will be converted from a
single character Python bytes object into a C char:

   >>> strchr.restype = c_char_p
   >>> strchr.argtypes = [c_char_p, c_char]
   >>> strchr(b"abcdef", b"d")
   b'def'
   >>> strchr(b"abcdef", b"def")
   Traceback (most recent call last):
   ctypes.ArgumentError: argument 2: TypeError: one character bytes, bytearray or integer expected
   >>> print(strchr(b"abcdef", b"x"))
   None
   >>> strchr(b"abcdef", b"d")
   b'def'
   >>>

You can also use a callable Python object (a function or a class for
example) as the "restype" attribute, if the foreign function returns
an integer.  The callable will be called with the *integer* the C
function returns, and the result of this call will be used as the
result of your function call. This is useful to check for error return
values and automatically raise an exception:

   >>> GetModuleHandle = windll.kernel32.GetModuleHandleA
   >>> def ValidHandle(value):
   ...     if value == 0:
   ...         raise WinError()
   ...     return value
   ...
   >>>
   >>> GetModuleHandle.restype = ValidHandle
   >>> GetModuleHandle(None)
   486539264
   >>> GetModuleHandle("something silly")
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<stdin>", line 3, in ValidHandle
   OSError: [Errno 126] The specified module could not be found.
   >>>

"WinError" es una función que llamará a la api Windows "FormatMessage"
para obtener la representación de la cadena de un código de error, y
retornará una excepción. "WinError" toma un parámetro de código de
error opcional, si no se usa ninguno, llama a "GetLastError`()" para
recuperarlo.

Please note that a much more powerful error checking mechanism is
available through the "errcheck" attribute; see the reference manual
for details.

### Pasar los punteros (o: pasar los parámetros por referencia)

A veces una función api C espera un *puntero* a un tipo de datos como
parámetro, probablemente para escribir en el lugar correspondiente, o
si los datos son demasiado grandes para ser pasados por valor. Esto
también se conoce cómo *pasar parámetros por referencia*.

"ctypes" exports the "byref()" function which is used to pass
parameters by reference.  The same effect can be achieved with the
"pointer()" function, although "pointer()" does a lot more work since
it constructs a real pointer object, so it is faster to use "byref()"
if you don't need the pointer object in Python itself:

   >>> i = c_int()
   >>> f = c_float()
   >>> s = create_string_buffer(b'\000' * 32)
   >>> print(i.value, f.value, repr(s.value))
   0 0.0 b''
   >>> libc.sscanf(b"1 3.14 Hello", b"%d %f %s",
   ...             byref(i), byref(f), s)
   3
   >>> print(i.value, f.value, repr(s.value))
   1 3.1400001049 b'Hello'
   >>>

### Estructuras y uniones

Structures and unions must derive from the "Structure" and "Union"
base classes which are defined in the "ctypes" module. Each subclass
must define a "_fields_" attribute.  "_fields_" must be a list of
*2-tuples*, containing a *field name* and a *field type*.

The field type must be a "ctypes" type like "c_int", or any other
derived "ctypes" type: structure, union, array, pointer.

Aquí hay un ejemplo simple de una estructura POINT, que contiene dos
enteros llamados *x* y *y*, y también muestra cómo inicializar una
estructura en el constructor:

   >>> from ctypes import *
   >>> class POINT(Structure):
   ...     _fields_ = [("x", c_int),
   ...                 ("y", c_int)]
   ...
   >>> point = POINT(10, 20)
   >>> print(point.x, point.y)
   10 20
   >>> point = POINT(y=5)
   >>> print(point.x, point.y)
   0 5
   >>> POINT(1, 2, 3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: too many initializers
   >>>

Sin embargo, se pueden construir estructuras mucho más complicadas.
Una estructura puede contener por sí misma otras estructuras usando
una estructura como tipo de campo.

Aquí hay una estructura RECT que contiene dos POINTs llamados
*upperleft* (superior izquierda)y *lowerright* (abajo a la derecha):

   >>> class RECT(Structure):
   ...     _fields_ = [("upperleft", POINT),
   ...                 ("lowerright", POINT)]
   ...
   >>> rc = RECT(point)
   >>> print(rc.upperleft.x, rc.upperleft.y)
   0 5
   >>> print(rc.lowerright.x, rc.lowerright.y)
   0 0
   >>>

Las estructuras anidadas también pueden ser inicializadas en el
constructor de varias maneras:

   >>> r = RECT(POINT(1, 2), POINT(3, 4))
   >>> r = RECT((1, 2), (3, 4))

Field *descriptor*s can be retrieved from the *class*, they are useful
for debugging because they can provide useful information. See
"CField":

   >>> POINT.x
   <ctypes.CField 'x' type=c_int, ofs=0, size=4>
   >>> POINT.y
   <ctypes.CField 'y' type=c_int, ofs=4, size=4>
   >>>

Advertencia:

  "ctypes" does not support passing unions or structures with bit-
  fields to functions by value.  While this may work on 32-bit x86,
  it's not guaranteed by the library to work in the general case.
  Unions and structures with bit-fields should always be passed to
  functions by pointer.

### Structure/union layout, alignment and byte order

By default, Structure and Union fields are laid out in the same way
the C compiler does it.  It is possible to override this behavior
entirely by specifying a "_layout_" class attribute in the subclass
definition; see the attribute documentation for details.

It is possible to specify the maximum alignment for the fields and/or
for the structure itself by setting the class attributes "_pack_"
and/or "_align_", respectively. See the attribute documentation for
details.

"ctypes" uses the native byte order for Structures and Unions.  To
build structures with non-native byte order, you can use one of the
"BigEndianStructure", "LittleEndianStructure", "BigEndianUnion", and
"LittleEndianUnion" base classes.  These classes cannot contain
pointer fields.

### Campos de bits en estructuras y uniones

It is possible to create structures and unions containing bit fields.
Bit fields are only possible for integer fields, the bit width is
specified as the third item in the "_fields_" tuples:

   >>> class Int(Structure):
   ...     _fields_ = [("first_16", c_int, 16),
   ...                 ("second_16", c_int, 16)]
   ...
   >>> print(Int.first_16)
   <ctypes.CField 'first_16' type=c_int, ofs=0, bit_size=16, bit_offset=0>
   >>> print(Int.second_16)
   <ctypes.CField 'second_16' type=c_int, ofs=0, bit_size=16, bit_offset=16>

It is important to note that bit field allocation and layout in memory
are not defined as a C standard; their implementation is compiler-
specific. By default, Python will attempt to match the behavior of a
"native" compiler for the current platform. See the "_layout_"
attribute for details on the default behavior and how to change it.

### Arreglos

Los arreglos son secuencias, que contienen un número fijo de
instancias del mismo tipo.

La forma recomendada de crear tipos de arreglos es multiplicando un
tipo de dato por un entero positivo:

   TenPointsArrayType = POINT * 10

Aquí hay un ejemplo de un tipo de datos algo artificial, una
estructura que contiene 4 POINTs entre otras cosas:

   >>> from ctypes import *
   >>> class POINT(Structure):
   ...     _fields_ = ("x", c_int), ("y", c_int)
   ...
   >>> class MyStruct(Structure):
   ...     _fields_ = [("a", c_int),
   ...                 ("b", c_float),
   ...                 ("point_array", POINT * 4)]
   >>>
   >>> print(len(MyStruct().point_array))
   4
   >>>

Las instancias se crean de la manera habitual, llamando a la clase:

   arr = TenPointsArrayType()
   for pt in arr:
       print(pt.x, pt.y)

El código anterior imprime una serie de líneas "0 0", porque el
contenido del arreglos se inicializa con ceros.

También se pueden especificar inicializadores del tipo correcto:

   >>> from ctypes import *
   >>> TenIntegers = c_int * 10
   >>> ii = TenIntegers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
   >>> print(ii)
   <c_long_Array_10 object at 0x...>
   >>> for i in ii: print(i, end=" ")
   ...
   1 2 3 4 5 6 7 8 9 10
   >>>

### Punteros

Pointer instances are created by calling the "pointer()" function on a
"ctypes" type:

   >>> from ctypes import *
   >>> i = c_int(42)
   >>> pi = pointer(i)
   >>>

Las instancias del puntero tienen un atributo "contents" que retorna
el objeto al que apunta el puntero, el objeto "i" arriba:

   >>> pi.contents
   c_long(42)
   >>>

Note that "ctypes" does not have OOR (original object return), it
constructs a new, equivalent object each time you retrieve an
attribute:

   >>> pi.contents is i
   False
   >>> pi.contents is pi.contents
   False
   >>>

Asignar otra instancia "c_int" al atributo de contenido del puntero
causaría que el puntero apunte al lugar de memoria donde se almacena:

   >>> i = c_int(99)
   >>> pi.contents = i
   >>> pi.contents
   c_long(99)
   >>>

Las instancias de puntero también pueden ser indexadas con números
enteros:

   >>> pi[0]
   99
   >>>

Asignando a un índice entero cambia el valor señalado:

   >>> print(i)
   c_long(99)
   >>> pi[0] = 22
   >>> print(i)
   c_long(22)
   >>>

También es posible usar índices diferentes de 0, pero debes saber lo
que estás haciendo, al igual que en C: Puedes acceder o cambiar
arbitrariamente las ubicaciones de memoria. Generalmente sólo usas
esta característica si recibes un puntero de una función C, y *sabes*
que el puntero en realidad apunta a un arreglo en lugar de a un solo
elemento.

Behind the scenes, the "pointer()" function does more than simply
create pointer instances, it has to create pointer *types* first. This
is done with the "POINTER()" function, which accepts any "ctypes"
type, and returns a new type:

   >>> PI = POINTER(c_int)
   >>> PI
   <class 'ctypes.LP_c_long'>
   >>> PI(42)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: expected c_long instead of int
   >>> PI(c_int(42))
   <ctypes.LP_c_long object at 0x...>
   >>>

Llamar al tipo de puntero sin un argumento crea un puntero "NULL". Los
punteros "NULL" tienen un valor booleano falso..:

   >>> null_ptr = POINTER(c_int)()
   >>> print(bool(null_ptr))
   False
   >>>

"ctypes" checks for "NULL" when dereferencing pointers (but
dereferencing invalid non-"NULL" pointers would crash Python):

   >>> null_ptr[0]
   Traceback (most recent call last):
       ....
   ValueError: NULL pointer access
   >>>

   >>> null_ptr[0] = 1234
   Traceback (most recent call last):
       ....
   ValueError: NULL pointer access
   >>>

### Thread safety without the GIL

From Python 3.13 onward, the *GIL* can be disabled on the *free-
threaded build*. In ctypes, reads and writes to a single object
concurrently is safe, but not across multiple objects:

      >>> number = c_int(42)
      >>> pointer_a = pointer(number)
      >>> pointer_b = pointer(number)

In the above, it's only safe for one object to read and write to the
address at once if the GIL is disabled. So, "pointer_a" can be shared
and written to across multiple threads, but only if "pointer_b" is not
also attempting to do the same. If this is an issue, consider using a
"threading.Lock" to synchronize access to memory:

      >>> import threading
      >>> lock = threading.Lock()
      >>> # Thread 1
      >>> with lock:
      ...    pointer_a.contents = 24
      >>> # Thread 2
      >>> with lock:
      ...    pointer_b.contents = 42

### Conversiones de tipos

Usually, ctypes does strict type checking.  This means, if you have
"POINTER(c_int)" in the "argtypes" list of a function or as the type
of a member field in a structure definition, only instances of exactly
the same type are accepted.  There are some exceptions to this rule,
where ctypes accepts other objects.  For example, you can pass
compatible array instances instead of pointer types.  So, for
"POINTER(c_int)", ctypes accepts an array of c_int:

   >>> class Bar(Structure):
   ...     _fields_ = [("count", c_int), ("values", POINTER(c_int))]
   ...
   >>> bar = Bar()
   >>> bar.values = (c_int * 3)(1, 2, 3)
   >>> bar.count = 3
   >>> for i in range(bar.count):
   ...     print(bar.values[i])
   ...
   1
   2
   3
   >>>

In addition, if a function argument is explicitly declared to be a
pointer type (such as "POINTER(c_int)") in "argtypes", an object of
the pointed type ("c_int" in this case) can be passed to the function.
ctypes will apply the required "byref()" conversion in this case
automatically.

Para poner un campo de tipo POINTER a "NULL", puedes asignar "None":

   >>> bar.values = None
   >>>

Sometimes you have instances of incompatible types.  In C, you can
cast one type into another type.  "ctypes" provides a "cast()"
function which can be used in the same way.  The "Bar" structure
defined above accepts "POINTER(c_int)" pointers or "c_int" arrays for
its "values" field, but not instances of other types:

   >>> bar.values = (c_byte * 4)()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: incompatible types, c_byte_Array_4 instance instead of LP_c_long instance
   >>>

Para estos casos, la función "cast()" es muy útil.

La función "cast()" puede ser usada para lanzar una instancia ctypes
en un puntero a un tipo de datos ctypes diferente. "cast()" toma dos
parámetros, un objeto ctypes que es o puede ser convertido en un
puntero de algún tipo, y un tipo de puntero ctypes. retorna una
instancia del segundo argumento, que hace referencia al mismo bloque
de memoria que el primer argumento:

   >>> a = (c_byte * 4)()
   >>> cast(a, POINTER(c_int))
   <ctypes.LP_c_long object at ...>
   >>>

Así, "cast()" puede ser usado para asignar al campo "values" de "Bar"
la estructura:

   >>> bar = Bar()
   >>> bar.values = cast((c_byte * 4)(), POINTER(c_int))
   >>> print(bar.values[0])
   0
   >>>

### Tipos incompletos

*Los Tipos Incompletos* son estructuras, uniones o matrices cuyos
miembros aún no están especificados. En C, se especifican mediante
declaraciones a futuro, que se definen más adelante:

   struct cell; /* forward declaration */

   struct cell {
       char *name;
       struct cell *next;
   };

La traducción directa al código de ctypes sería esta, pero no
funciona:

   >>> class cell(Structure):
   ...     _fields_ = [("name", c_char_p),
   ...                 ("next", POINTER(cell))]
   ...
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<stdin>", line 2, in cell
   NameError: name 'cell' is not defined
   >>>

because the new "class cell" is not available in the class statement
itself. In "ctypes", we can define the "cell" class and set the
"_fields_" attribute later, after the class statement:

   >>> from ctypes import *
   >>> class cell(Structure):
   ...     pass
   ...
   >>> cell._fields_ = [("name", c_char_p),
   ...                  ("next", POINTER(cell))]
   >>>

Vamos a intentarlo. Creamos dos instancias de "cell", y dejamos que se
apunten una a la otra, y finalmente seguimos la cadena de punteros
unas cuantas veces:

   >>> c1 = cell()
   >>> c1.name = b"foo"
   >>> c2 = cell()
   >>> c2.name = b"bar"
   >>> c1.next = pointer(c2)
   >>> c2.next = pointer(c1)
   >>> p = c1
   >>> for i in range(8):
   ...     print(p.name, end=" ")
   ...     p = p.next[0]
   ...
   foo bar foo bar foo bar foo bar
   >>>

### Funciones de retrollamadas (*callback*)

"ctypes" allows creating C callable function pointers from Python
callables. These are sometimes called *callback functions*.

Primero, debes crear una clase para la función de retrollamada. La
clase conoce la convención de llamada, el tipo de retorno, y el número
y tipos de argumentos que esta función recibirá.

La función de fábrica "CFUNCTYPE`()" crea tipos para las funciones de
retrollamada usando la convención de llamada "cdecl". En Windows, la
función de fábrica "WINFUNCTYPE()" crea tipos para funciones de
retrollamadas usando la convención de llamadas "stdcall".

Ambas funciones de fábrica se llaman con el tipo de resultado como
primer argumento, y las funciones de llamada de retorno con los tipos
de argumentos esperados como los argumentos restantes.

I will present an example here which uses the standard C library's
"qsort()" function, that is used to sort items with the help of a
callback function.  "qsort()" will be used to sort an array of
integers:

   >>> IntArray5 = c_int * 5
   >>> ia = IntArray5(5, 1, 7, 33, 99)
   >>> qsort = libc.qsort
   >>> qsort.restype = None
   >>>

"qsort()" must be called with a pointer to the data to sort, the
number of items in the data array, the size of one item, and a pointer
to the comparison function, the callback. The callback will then be
called with two pointers to items, and it must return a negative
integer if the first item is smaller than the second, a zero if they
are equal, and a positive integer otherwise.

Así que nuestra función de retrollamada recibe punteros a números
enteros, y debe retornar un número entero. Primero creamos el "tipo"
para la función de retrollamada:

   >>> CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
   >>>

Para empezar, aquí hay una simple llamada que muestra los valores que
se pasan:

   >>> def py_cmp_func(a, b):
   ...     print("py_cmp_func", a[0], b[0])
   ...     return 0
   ...
   >>> cmp_func = CMPFUNC(py_cmp_func)
   >>>

El resultado:

   >>> qsort(ia, len(ia), sizeof(c_int), cmp_func)
   py_cmp_func 5 1
   py_cmp_func 33 99
   py_cmp_func 7 33
   py_cmp_func 5 7
   py_cmp_func 1 7
   >>>

Ahora podemos comparar los dos artículos y obtener un resultado útil:

   >>> def py_cmp_func(a, b):
   ...     print("py_cmp_func", a[0], b[0])
   ...     return a[0] - b[0]
   ...
   >>>
   >>> qsort(ia, len(ia), sizeof(c_int), CMPFUNC(py_cmp_func))
   py_cmp_func 5 1
   py_cmp_func 33 99
   py_cmp_func 7 33
   py_cmp_func 1 7
   py_cmp_func 5 7
   >>>

Como podemos comprobar fácilmente, nuestro arreglo está ordenado
ahora:

   >>> for i in ia: print(i, end=" ")
   ...
   1 5 7 33 99
   >>>

Las funciones de fabrica pueden ser usadas como decoradores de
fabrica, así que podemos escribir:

   >>> @CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
   ... def py_cmp_func(a, b):
   ...     print("py_cmp_func", a[0], b[0])
   ...     return a[0] - b[0]
   ...
   >>> qsort(ia, len(ia), sizeof(c_int), py_cmp_func)
   py_cmp_func 5 1
   py_cmp_func 33 99
   py_cmp_func 7 33
   py_cmp_func 1 7
   py_cmp_func 5 7
   >>>

Nota:

  Make sure you keep references to "CFUNCTYPE()" objects as long as
  they are used from C code. "ctypes" doesn't, and if you don't, they
  may be garbage collected, crashing your program when a callback is
  made.Además, nótese que sí se llama a la función de retrollamada en
  un hilo creado fuera del control de Python (por ejemplo, por el
  código foráneo que llama a la retrollamada), ctypes crea un nuevo
  hilo Python tonto en cada invocación. Este comportamiento es
  correcto para la mayoría de los propósitos, pero significa que los
  valores almacenados con "threading.local" *no* sobreviven a través
  de diferentes llamadas de retorno, incluso cuando esas llamadas se
  hacen desde el mismo hilo C.

### Acceder a los valores exportados de los dlls

Some shared libraries not only export functions, they also export
variables. An example in the Python library itself is the
"Py_Version", Python runtime version number encoded in a single
constant integer.

"ctypes" can access values like this with the "in_dll()" class methods
of the type.  *pythonapi* is a predefined symbol giving access to the
Python C api:

   >>> version = ctypes.c_int.in_dll(ctypes.pythonapi, "Py_Version")
   >>> print(hex(version.value))
   0x30c00a0

Un ejemplo extendido que también demuestra el uso de punteros
accediendo al puntero "PyImport_FrozenModules" exportado por Python.

Citando los documentos para ese valor:

   Este puntero se inicializa para apuntar a un arreglo de registros
   "_frozen", terminados por uno cuyos miembros son todos "NULL" o
   cero. Cuando se importa un módulo congelado, se busca en esta
   tabla. El código de terceros podría jugar trucos con esto para
   proporcionar una colección de módulos congelados creada
   dinámicamente.

So manipulating this pointer could even prove useful. To restrict the
example size, we show only how this table can be read with "ctypes":

   >>> from ctypes import *
   >>>
   >>> class struct_frozen(Structure):
   ...     _fields_ = [("name", c_char_p),
   ...                 ("code", POINTER(c_ubyte)),
   ...                 ("size", c_int),
   ...                 ("get_code", POINTER(c_ubyte)),  # Function pointer
   ...                ]
   ...
   >>>

Hemos definido el tipo de datos "_frozen", por lo que podemos obtener
el puntero a la tabla:

   >>> FrozenTable = POINTER(struct_frozen)
   >>> table = FrozenTable.in_dll(pythonapi, "_PyImport_FrozenBootstrap")
   >>>

Como "tabla" es un "puntero" al arreglo de registros "struct_frozen",
podemos iterar sobre ella, pero sólo tenemos que asegurarnos de que
nuestro bucle termine, porque los punteros no tienen tamaño. Tarde o
temprano, probablemente se caerá con una violación de acceso o lo que
sea, así que es mejor salir del bucle cuando le demos a la entrada
"NULL":

   >>> for item in table:
   ...     if item.name is None:
   ...         break
   ...     print(item.name.decode("ascii"), item.size)
   ...
   _frozen_importlib 31764
   _frozen_importlib_external 41499
   zipimport 12345
   >>>

El hecho de que la Python estándar tenga un módulo congelado y un
paquete congelado (indicado por el miembro "tamaño" negativo) no se
conoce bien, sólo se usa para hacer pruebas. Pruébalo con "import
__hello__" por ejemplo.

### Sorpresas

There are some edges in "ctypes" where you might expect something
other than what actually happens.

Considere el siguiente ejemplo:

   >>> from ctypes import *
   >>> class POINT(Structure):
   ...     _fields_ = ("x", c_int), ("y", c_int)
   ...
   >>> class RECT(Structure):
   ...     _fields_ = ("a", POINT), ("b", POINT)
   ...
   >>> p1 = POINT(1, 2)
   >>> p2 = POINT(3, 4)
   >>> rc = RECT(p1, p2)
   >>> print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
   1 2 3 4
   >>> # now swap the two points
   >>> rc.a, rc.b = rc.b, rc.a
   >>> print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
   3 4 3 4
   >>>

Hm. Ciertamente esperábamos que la última declaración imprimiera "3 4
1 2". ¿Qué ha pasado? Aquí están los pasos de la línea "rc.a, rc.b =
rc.b, rc.a" arriba:

   >>> temp0, temp1 = rc.b, rc.a
   >>> rc.a = temp0
   >>> rc.b = temp1
   >>>

Note que "temp0" y "temp1" son objetos que todavía usan el buffer
interno del objeto "rc" de arriba. Así que ejecutando "rc.a = temp0"
copia el contenido del buffer de "temp0" en el buffer de "rc". Esto, a
su vez, cambia el contenido de "temp1". Por lo tanto, la última
asignación "rc.b = temp1", no tiene el efecto esperado.

Tengan en cuenta que la recuperación de subobjetos de Estructuras,
Uniones y Arreglos no *copia* el subobjeto, sino que recupera un
objeto contenido que accede al búfer subyacente del objeto raíz.

Otro ejemplo que puede comportarse de manera diferente a lo que uno
esperaría es este:

   >>> s = c_char_p()
   >>> s.value = b"abc def ghi"
   >>> s.value
   b'abc def ghi'
   >>> s.value is s.value
   False
   >>>

Nota:

  Los objetos instanciados desde "c_char_p" sólo pueden tener su valor
  fijado en bytes o enteros.

¿Por qué está imprimiendo "False"? Las instancias ctypes son objetos
que contienen un bloque de memoria más algunos *descriptor*s que
acceden al contenido de la memoria. Almacenar un objeto Python en el
bloque de memoria no almacena el objeto en sí mismo, en su lugar se
almacenan los "contenidos" del objeto. ¡Acceder a los contenidos de
nuevo construye un nuevo objeto Python cada vez!

### Tipos de datos de tamaño variable

"ctypes" provides some support for variable-sized arrays and
structures.

La función "resize()" puede ser usada para redimensionar el buffer de
memoria de un objeto ctypes existente. La función toma el objeto como
primer argumento, y el tamaño solicitado en bytes como segundo
argumento. El bloque de memoria no puede hacerse más pequeño que el
bloque de memoria natural especificado por el tipo de objeto, se lanza
un "ValueError" si se intenta:

   >>> short_array = (c_short * 4)()
   >>> print(sizeof(short_array))
   8
   >>> resize(short_array, 4)
   Traceback (most recent call last):
       ...
   ValueError: minimum size is 8
   >>> resize(short_array, 32)
   >>> sizeof(short_array)
   32
   >>> sizeof(type(short_array))
   8
   >>>

Esto está bien, pero ¿cómo se puede acceder a los elementos
adicionales contenidos en este arreglo?  Dado que el tipo todavía sabe
sólo 4 elementos, obtenemos errores al acceder a otros elementos:

   >>> short_array[:]
   [0, 0, 0, 0]
   >>> short_array[7]
   Traceback (most recent call last):
       ...
   IndexError: invalid index
   >>>

Another way to use variable-sized data types with "ctypes" is to use
the dynamic nature of Python, and (re-)define the data type after the
required size is already known, on a case by case basis.

## referencia ctypes

### Encontrar bibliotecas compartidas

Cuando se programa en un lenguaje compilado, se accede a las
bibliotecas compartidas cuando se compila/enlaza un programa, y cuándo
se ejecuta el programa.

The purpose of the "find_library()" function is to locate a library in
a way similar to what the compiler or runtime loader does (on
platforms with several versions of a shared library the most recent
should be loaded), while the ctypes library loaders act like when a
program is run, and call the runtime loader directly.

The "ctypes.util" module provides a function which can help to
determine the library to load.

ctypes.util.find_library(name)

   Intenta encontrar una biblioteca y retornar un nombre. *name* es el
   nombre de la biblioteca sin ningún prefijo como *lib*, sufijo como
   ".so", ".dylib" o número de versión (esta es la forma usada para la
   opción del enlazador posix "-l"). Si no se puede encontrar ninguna
   biblioteca, retorna "None".

La funcionalidad exacta depende del sistema.

On Linux, "find_library()" tries to run external programs
("/sbin/ldconfig", "gcc", "objdump" and "ld") to find the library
file. It returns the filename of the library file.

Note that if the output of these programs does not correspond to the
dynamic linker used by Python, the result of this function may be
misleading.

Distinto en la versión 3.6: En Linux, el valor de la variable de
entorno "LD_LIBRARY_PATH" se utiliza cuando se buscan bibliotecas, si
una biblioteca no puede ser encontrada por ningún otro medio.

Aquí hay algunos ejemplos:

   >>> from ctypes.util import find_library
   >>> find_library("m")
   'libm.so.6'
   >>> find_library("c")
   'libc.so.6'
   >>> find_library("bz2")
   'libbz2.so.1.0'
   >>>

On macOS and Android, "find_library()" uses the system's standard
naming schemes and paths to locate the library, and returns a full
pathname if successful:

   >>> from ctypes.util import find_library
   >>> find_library("c")
   '/usr/lib/libc.dylib'
   >>> find_library("m")
   '/usr/lib/libm.dylib'
   >>> find_library("bz2")
   '/usr/lib/libbz2.dylib'
   >>> find_library("AGL")
   '/System/Library/Frameworks/AGL.framework/AGL'
   >>>

On Windows, "find_library()" searches along the system search path,
and returns the full pathname, but since there is no predefined naming
scheme a call like "find_library("c")" will fail and return "None".

If wrapping a shared library with "ctypes", it *may* be better to
determine the shared library name at development time, and hardcode
that into the wrapper module instead of using "find_library()" to
locate the library at runtime.

### Listing loaded shared libraries

When writing code that relies on code loaded from shared libraries, it
can be useful to know which shared libraries have already been loaded
into the current process.

The "ctypes.util" module provides the "dllist()" function, which calls
the different APIs provided by the various platforms to help determine
which shared libraries have already been loaded into the current
process.

The exact output of this function will be system dependent. On most
platforms, the first entry of this list represents the current process
itself, which may be an empty string. For example, on glibc-based
Linux, the return may look like:

   >>> from ctypes.util import dllist
   >>> dllist()
   ['', 'linux-vdso.so.1', '/lib/x86_64-linux-gnu/libm.so.6', '/lib/x86_64-linux-gnu/libc.so.6', ... ]

### Cargando bibliotecas compartidas

There are several ways to load shared libraries into the Python
process.  One way is to instantiate "CDLL" or one of its subclasses:

class ctypes.CDLL(name, mode=DEFAULT_MODE, handle=None, use_errno=False, use_last_error=False, winmode=None)

   Represents a loaded shared library.

   Functions in this library use the standard C calling convention,
   and are assumed to return int. The Python *global interpreter lock*
   is released before calling any function exported by these
   libraries, and reacquired afterwards. For different function
   behavior, use a subclass: "OleDLL", "WinDLL", or "PyDLL".

   If you have an existing "handle" to an already loaded shared
   library, it can be passed as the *handle* argument to wrap the
   opened library in a new "CDLL" object. In this case, *name* is only
   used to set the "_name" attribute, but it may be adjusted and/or
   validated.

   If *handle* is "None", the underlying platform's *dlopen(3)* or
   "LoadLibrary()" function is used to load the library into the
   process, and to get a handle to it.

   *name* is the pathname of the shared library to open. If *name*
   does not contain a path separator, the library is found in a
   platform-specific way.

   On non-Windows systems, *name* can  be "None". In this case,
   "dlopen()" is called with "NULL", which opens the main program as a
   "library". (Some systems do the same is *name* is empty;
   "None"/"NULL" is more portable.)

   CPython implementation detail: Since CPython is linked to "libc", a
   "None" *name* is often used to access the C standard library:

      >>> printf = ctypes.CDLL(None).printf
      >>> printf.argtypes = [ctypes.c_char_p]
      >>> printf(b"hello\n")
      hello
      6

   To access the Python C API, prefer "ctypes.pythonapi" which works
   across platforms.

   El parámetro *mode* puede utilizarse para especificar cómo se carga
   la biblioteca. Para más detalles, consulte la página *dlopen(3)*
   del manual. En Windows, *mode* es ignorado. En los sistemas posix,
   RTLD_NOW siempre se agrega, y no es configurable.

   The *use_errno* parameter, when set to true, enables a ctypes
   mechanism that allows accessing the system "errno" error number in
   a safe way. "ctypes" maintains a thread-local copy of the system's
   "errno" variable; if you call foreign functions created with
   "use_errno=True" then the "errno" value before the function call is
   swapped with the ctypes private copy, the same happens immediately
   after the function call.

   La función "ctypes.get_errno()" retorna el valor de la copia
   privada de ctypes, y la función "ctypes.set_errno()" cambia la
   copia privada de ctypes a un nuevo valor y retorna el valor
   anterior.

   The *use_last_error* parameter, when set to true, enables the same
   mechanism for the Windows error code which is managed by the
   "GetLastError()" and "SetLastError()" Windows API functions;
   "ctypes.get_last_error()" and "ctypes.set_last_error()" are used to
   request and change the ctypes private copy of the windows error
   code.

   The *winmode* parameter is used on Windows to specify how the
   library is loaded (since *mode* is ignored). It takes any value
   that is valid for the Win32 API "LoadLibraryEx" flags parameter.
   When omitted, the default is to use the flags that result in the
   most secure DLL load, which avoids issues such as DLL hijacking.
   Passing the full path to the DLL is the safest way to ensure the
   correct library and dependencies are loaded.

   En Windows, la creación de una instancia "CDLL" puede fallar
   incluso si existe el nombre de la DLL. Cuando no se encuentra una
   DLL dependiente de la DLL cargada, se lanza un error "OSError" con
   el mensaje *"[WinError 126] No se pudo encontrar el módulo
   especificado".* Este mensaje de error no contiene el nombre de DLL
   que falta porque la API de Windows no retorna esta información, lo
   que dificulta el diagnóstico de este error. Para resolver este
   error y determinar qué DLL no se encuentra, debe buscar la lista de
   DLL dependientes y determinar cuál no se encuentra utilizando las
   herramientas de depuración y seguimiento de Windows.

   Ver también:

     Microsoft DUMPBIN tool -- A tool to find DLL dependents.

   Distinto en la versión 3.8: Añadido el parámetro *winmode*.

   Distinto en la versión 3.12: The *name* parameter can now be a
   *path-like object*.

   Instances of this class have no public methods.  Functions exported
   by the shared library can be accessed as attributes or by index.
   Please note that accessing the function through an attribute caches
   the result and therefore accessing it repeatedly returns the same
   object each time.  On the other hand, accessing it through an index
   returns a new object each time:

      >>> from ctypes import CDLL
      >>> libc = CDLL("libc.so.6")  # On Linux
      >>> libc.time == libc.time
      True
      >>> libc['time'] == libc['time']
      False

   The following public attributes are available. Their name starts
   with an underscore to not clash with exported function names:

   _handle

      El manejador del sistema usado para acceder a la biblioteca.

   _name

      El nombre de la biblioteca pasado en el constructor.

class ctypes.OleDLL

   See "CDLL", the superclass, for common information.

   Functions in this library use the "stdcall" calling convention, and
   are assumed to return the windows specific "HRESULT" code.
   "HRESULT" values contain information specifying whether the
   function call failed or succeeded, together with additional error
   code.  If the return value signals a failure, an "OSError" is
   automatically raised.

   Availability: Windows

   Distinto en la versión 3.3: "WindowsError" used to be raised, which
   is now an alias of "OSError".

class ctypes.WinDLL

   See "CDLL", the superclass, for common information.

   Functions in these libraries use the "stdcall" calling convention,
   and are assumed to return int by default.

   Availability: Windows

class ctypes.PyDLL

   See "CDLL", the superclass, for common information.

   When functions in this library are called, the Python GIL is *not*
   released during the function call, and after the function execution
   the Python error flag is checked. If the error flag is set, a
   Python exception is raised.

   Thus, this is only useful to call Python C API functions directly.

ctypes.RTLD_GLOBAL

   Flag para usar como parámetro *modo*. En las plataformas en las que
   esta bandera no está disponible, se define como el cero entero.

ctypes.RTLD_LOCAL

   Flag para usar como parámetro *modo*. En las plataformas en las que
   esto no está disponible, es lo mismo que *RTLD_GLOBAL*.

ctypes.DEFAULT_MODE

   El modo por defecto que se utiliza para cargar las bibliotecas
   compartidas. En OSX 10.3, esto es *RTLD_GLOBAL*, de lo contrario es
   lo mismo que *RTLD_LOCAL*.

Shared libraries can also be loaded by using one of the prefabricated
objects, which are instances of the "LibraryLoader" class, either by
calling the "LoadLibrary()" method, or by retrieving the library as
attribute of the loader instance.

class ctypes.LibraryLoader(dlltype)

   Clase que carga bibliotecas compartidas. *dlltype* debe ser uno de
   los tipos "CDLL", "PyDLL", "WinDLL", o "OleDLL".

   "__getattr__()" has special behavior: It allows loading a shared
   library by accessing it as attribute of a library loader instance.
   The result is cached, so repeated attribute accesses return the
   same library each time.

   LoadLibrary(name)

      Carga una biblioteca compartida en el proceso y la retorna. Este
      método siempre retorna una nueva instancia de la biblioteca.

Estos cargadores prefabricados de bibliotecas están disponibles:

ctypes.cdll

   Crea instancias de "CDLL".

ctypes.windll

   Creates "WinDLL" instances.

   Availability: Windows

ctypes.oledll

   Creates "OleDLL" instances.

   Availability: Windows

ctypes.pydll

   Crea instancias de "PyDLL".

Para acceder directamente a la API C de Python, se dispone de un
objeto de biblioteca compartida de Python listo-para-usar:

ctypes.pythonapi

   An instance of "PyDLL" that exposes Python C API functions as
   attributes.  Note that all these functions are assumed to return C
   int, which is of course not always the truth, so you have to assign
   the correct "restype" attribute to use these functions.

Loading a library through any of these objects raises an auditing
event "ctypes.dlopen" with string argument "name", the name used to
load the library.

Accessing a function on a loaded library raises an auditing event
"ctypes.dlsym" with arguments "library" (the library object) and
"name" (the symbol's name as a string or integer).

En los casos en los que sólo está disponible el manejador de la
biblioteca en lugar del objeto, al acceder a una función se produce un
evento de auditoría "ctypes.dlsym/handle" con los argumentos "handle"
(el manejador de la biblioteca en bruto) y "name".

### Funciones foráneas

As explained in the previous section, foreign functions can be
accessed as attributes of loaded shared libraries.  The function
objects created in this way by default accept any number of arguments,
accept any ctypes data instances as arguments, and return the default
result type specified by the library loader.

They are instances of a private local class "_FuncPtr" (not exposed in
"ctypes") which inherits from the private "_CFuncPtr" class:

   >>> import ctypes
   >>> lib = ctypes.CDLL(None)
   >>> issubclass(lib._FuncPtr, ctypes._CFuncPtr)
   True
   >>> lib._FuncPtr is ctypes._CFuncPtr
   False

class ctypes._CFuncPtr

   Clase base para funciones foráneas C invocables.

   Las instancias de funciones foráneas también son tipos de datos
   compatibles con C; representan punteros de funciones C.

   Este comportamiento puede personalizarse asignando a los atributos
   especiales del objeto de la función foránea.

   restype

      Asigne un tipo ctypes para especificar el tipo de resultado de
      la función externa. Use "None" para void, una función que no
      retorna nada.

      It is possible to assign a callable Python object that is not a
      ctypes type, in this case the function is assumed to return a C
      int, and the callable will be called with this integer, allowing
      further processing or error checking.  Using this is deprecated,
      for more flexible post processing or error checking use a ctypes
      data type as "restype" and assign a callable to the "errcheck"
      attribute.

   argtypes

      Asigne una tupla de tipos ctypes para especificar los tipos de
      argumentos que acepta la función. Las funciones que utilizan la
      convención de llamada "stdcall" sólo pueden ser llamadas con el
      mismo número de argumentos que la longitud de esta tupla; las
      funciones que utilizan la convención de llamada C aceptan
      también argumentos adicionales no especificados.

      When a foreign function is called, each actual argument is
      passed to the "from_param()" class method of the items in the
      "argtypes" tuple, this method allows adapting the actual
      argument to an object that the foreign function accepts.  For
      example, a "c_char_p" item in the "argtypes" tuple will convert
      a string passed as argument into a bytes object using ctypes
      conversion rules.

      New: It is now possible to put items in argtypes which are not
      ctypes types, but each item must have a "from_param()" method
      which returns a value usable as argument (integer, string,
      ctypes instance).  This allows defining adapters that can adapt
      custom objects as function parameters.

   errcheck

      Asigne una función Python u otra llamada a este atributo. El
      invocable será llamado con tres o más argumentos:

      callable(result, func, arguments)

         *result* is what the foreign function returns, as specified
         by the "restype" attribute.

         *func* es el propio objeto de la función foránea, lo que
         permite reutilizar el mismo objeto invocable para comprobar o
         postprocesar los resultados de varias funciones.

         *arguments* es una tupla que contiene los parámetros
         originalmente pasados a la llamada de la función, esto
         permite especializar el comportamiento en los argumentos
         utilizados.

      El objeto que retorna esta función será retornado por la llamada
      de la función foránea, pero también puede comprobar el valor del
      resultado y hacer una excepción si la llamada de la función
      foránea ha fallado.

En Windows, cuando una llamada a una función foránea plantea una
excepción de sistema (por ejemplo, debido a una violación de acceso),
será capturada y sustituida por una excepción Python adecuada. Además,
un evento de auditoría "ctypes.set_exception" con el argumento "code"
será levantado, permitiendo que un gancho de auditoría reemplace la
excepción con la suya propia.

Some ways to invoke foreign function calls as well as some of the
functions in this module may raise an auditing event
"ctypes.call_function" with arguments "function pointer" and
"arguments".

### Prototipos de funciones

Las funciones foráneas también pueden crearse mediante la
instanciación de prototipos de funciones. Los prototipos de funciones
son similares a los prototipos de funciones en C; describen una
función (tipo de retorno, tipos de argumentos, convención de llamada)
sin definir una implementación. Las funciones de fábrica deben ser
llamadas con el tipo de resultado deseado y los tipos de argumento de
la función, y pueden ser usadas como fábricas de decoradores, y como
tales, ser aplicadas a las funciones a través de la sintaxis
"@wrapper". Ver Funciones de retrollamadas (callback) para ejemplos.

ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

   El prototipo de función retornado crea funciones que usan la
   convención de llamada C estándar. La función liberará el GIL
   durante la llamada. Si *use_errno* se configura a true, la copia
   privada de ctypes de la variable del sistema "errno" se intercambia
   con el valor real "errno" antes y después de la llamada;
   *use_last_error* hace lo mismo con el código de error de Windows.

ctypes.WINFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

   The returned function prototype creates functions that use the
   "stdcall" calling convention.  The function will release the GIL
   during the call.  *use_errno* and *use_last_error* have the same
   meaning as above.

   Availability: Windows

ctypes.PYFUNCTYPE(restype, *argtypes)

   El prototipo de función retornado crea funciones que usan la
   convención de llamadas de Python. La función *no* liberará el GIL
   durante la llamada.

Los prototipos de funciones creados por estas funciones de fábrica
pueden ser instanciados de diferentes maneras, dependiendo del tipo y
el número de los parámetros en la llamada:

prototype(address)

   Retorna una función foránea en la dirección especificada que debe
   ser un número entero.

prototype(callable)

   Crear una función de llamada C (una función de retrollamada) a
   partir de un *callable* Python.

prototype(func_spec[, paramflags])

   Retorna una función foránea exportada por una biblioteca
   compartida. *func_spec* debe ser un 2-tupla "(name_or_ordinal,
   library)". El primer elemento es el nombre de la función exportada
   como cadena, o el ordinal de la función exportada como entero
   pequeño. El segundo elemento es la instancia de la biblioteca
   compartida.

prototype(vtbl_index, name[, paramflags[, iid]])

   Retorna una función foránea que llamará a un método COM.
   *vtbl_index* es el índice de la tabla de funciones virtuales, un
   pequeño entero no negativo. *name* es el nombre del método COM.
   *iid* es un puntero opcional para el identificador de la interfaz
   que se utiliza en el informe de errores extendido.

   If *iid* is not specified, an "OSError" is raised if the COM method
   call fails. If *iid* is specified, a "COMError" is raised instead.

   COM methods use a special calling convention: They require a
   pointer to the COM interface as first argument, in addition to
   those parameters that are specified in the "argtypes" tuple.

   Availability: Windows

El parámetro opcional *paramflags* crea envoltorios de funciones
foráneas con mucha más funcionalidad que las características descritas
anteriormente.

*paramflags* must be a tuple of the same length as "argtypes".

Cada elemento de esta tupla contiene más información sobre un
parámetro, debe ser una tupla que contenga uno, dos o tres elementos.

El primer elemento es un entero que contiene una combinación de flags
de dirección para el parámetro:

   1
      Especifica un parámetro de entrada a la función.

   2
      Parámetro de salida. La función foránea rellena un valor.

   4
      Parámetro de entrada que por defecto es el cero entero.

El segundo elemento opcional es el nombre del parámetro como cadena.
Si se especifica esto, se puede llamar a la función foránea con
parámetros con nombre.

El tercer elemento opcional es el valor por defecto de este parámetro.

The following example demonstrates how to wrap the Windows
"MessageBoxW" function so that it supports default parameters and
named arguments. The C declaration from the windows header file is
this:

   WINUSERAPI int WINAPI
   MessageBoxW(
       HWND hWnd,
       LPCWSTR lpText,
       LPCWSTR lpCaption,
       UINT uType);

Here is the wrapping with "ctypes":

   >>> from ctypes import c_int, WINFUNCTYPE, windll
   >>> from ctypes.wintypes import HWND, LPCWSTR, UINT
   >>> prototype = WINFUNCTYPE(c_int, HWND, LPCWSTR, LPCWSTR, UINT)
   >>> paramflags = (1, "hwnd", 0), (1, "text", "Hi"), (1, "caption", "Hello from ctypes"), (1, "flags", 0)
   >>> MessageBox = prototype(("MessageBoxW", windll.user32), paramflags)

La función foránea de "MessageBox" puede ser llamada de esta manera:

   >>> MessageBox()
   >>> MessageBox(text="Spam, spam, spam")
   >>> MessageBox(flags=2, text="foo bar")

Un segundo ejemplo demuestra los parámetros de salida. La función
"GetWindowRect" de win32 retorna las dimensiones de una ventana
especificada copiándolas en la estructura "RECT" que la persona que
llama tiene que suministrar. Aquí está la declaración C:

   WINUSERAPI BOOL WINAPI
   GetWindowRect(
        HWND hWnd,
        LPRECT lpRect);

Here is the wrapping with "ctypes":

   >>> from ctypes import POINTER, WINFUNCTYPE, windll, WinError
   >>> from ctypes.wintypes import BOOL, HWND, RECT
   >>> prototype = WINFUNCTYPE(BOOL, HWND, POINTER(RECT))
   >>> paramflags = (1, "hwnd"), (2, "lprect")
   >>> GetWindowRect = prototype(("GetWindowRect", windll.user32), paramflags)
   >>>

Las funciones con parámetros de salida retornarán automáticamente el
valor del parámetro de salida si hay uno solo, o una tupla que
contiene los valores del parámetro de salida cuando hay más de uno,
por lo que la función GetWindowRect retorna ahora una instancia RECT,
cuando se llama.

Output parameters can be combined with the "errcheck" protocol to do
further output processing and error checking.  The win32
"GetWindowRect" api function returns a "BOOL" to signal success or
failure, so this function could do the error checking, and raises an
exception when the api call failed:

   >>> def errcheck(result, func, args):
   ...     if not result:
   ...         raise WinError()
   ...     return args
   ...
   >>> GetWindowRect.errcheck = errcheck
   >>>

If the "errcheck" function returns the argument tuple it receives
unchanged, "ctypes" continues the normal processing it does on the
output parameters.  If you want to return a tuple of window
coordinates instead of a "RECT" instance, you can retrieve the fields
in the function and return them instead, the normal processing will no
longer take place:

   >>> def errcheck(result, func, args):
   ...     if not result:
   ...         raise WinError()
   ...     rc = args[1]
   ...     return rc.left, rc.top, rc.bottom, rc.right
   ...
   >>> GetWindowRect.errcheck = errcheck
   >>>

### Funciones de utilidad

ctypes.addressof(obj)

   Retorna la dirección del buffer de memoria como un entero. *obj*
   debe ser una instancia de tipo ctypes.

   Lanza un auditing event "ctypes.addressof" con el argumento "obj".

ctypes.alignment(obj_or_type)

   Retorna los requerimientos de alineación de un tipo de ctypes.
   *obj_or_type* debe ser un tipo o instancia ctypes.

ctypes.byref(obj[, offset])

   Retorna un puntero ligero a *obj*, que debe ser un ejemplo de un
   tipo de ctypes. *offset* es por defecto cero, y debe ser un entero
   que se añadirá al valor del puntero interno.

   "byref(obj, offset)" corresponde a este código C:

      (((char *)&obj) + offset)

   El objeto retornado sólo puede ser utilizado como un parámetro de
   llamada de función foránea. Se comporta de manera similar a
   "pointer(obj)", pero la construcción es mucho más rápida.

ctypes.CopyComPointer(src, dst)

   Copies a COM pointer from *src* to *dst* and returns the Windows
   specific "HRESULT" value.

   If *src* is not "NULL", its "AddRef" method is called, incrementing
   the reference count.

   In contrast, the reference count of *dst* will not be decremented
   before assigning the new value. Unless *dst* is "NULL", the caller
   is responsible for decrementing the reference count by calling its
   "Release" method when necessary.

   Availability: Windows

   Added in version 3.14.

ctypes.cast(obj, type)

   Esta función es similar a la del operador de reparto en C. retorna
   una nueva instancia de *type* que apunta al mismo bloque de memoria
   que *obj*. *type* debe ser un tipo de puntero, y *obj* debe ser un
   objeto que pueda ser interpretado como un puntero.

ctypes.create_string_buffer(init, size=None)
ctypes.create_string_buffer(size)

   Esta función crea un búfer de caracteres mutables. El objeto
   retornado es un arreglo de ctypes de "c_char".

   If *size* is given (and not "None"), it must be an "int". It
   specifies the size of the returned array.

   If the *init* argument is given, it must be "bytes". It is used to
   initialize the array items. Bytes not initialized this way are set
   to zero (NUL).

   If *size* is not given (or if it is "None"), the buffer is made one
   element larger than *init*, effectively adding a NUL terminator.

   If both arguments are given, *size* must not be less than
   "len(init)".

   Advertencia:

     If *size* is equal to "len(init)", a NUL terminator is not added.
     Do not treat such a buffer as a C string.

   For example:

      >>> bytes(create_string_buffer(2))
      b'\x00\x00'
      >>> bytes(create_string_buffer(b'ab'))
      b'ab\x00'
      >>> bytes(create_string_buffer(b'ab', 2))
      b'ab'
      >>> bytes(create_string_buffer(b'ab', 4))
      b'ab\x00\x00'
      >>> bytes(create_string_buffer(b'abcdef', 2))
      Traceback (most recent call last):
         ...
      ValueError: byte string too long

   Lanza un auditing event "ctypes.create_string_buffer" con
   argumentos "init", "size".

ctypes.create_unicode_buffer(init, size=None)
ctypes.create_unicode_buffer(size)

   Esta función crea un búfer de caracteres unicode mutable. El objeto
   retornado es un arreglo de ctypes de "c_wchar".

   The function takes the same arguments as "create_string_buffer()"
   except *init* must be a string and *size* counts "c_wchar".

   Lanza un auditing event "ctypes.create_unicode_buffer" con
   argumentos "init", "size".

ctypes.DllCanUnloadNow()

   This function is a hook which allows implementing in-process COM
   servers with ctypes.  It is called from the DllCanUnloadNow
   function that the _ctypes extension dll exports.

   Availability: Windows

ctypes.DllGetClassObject()

   This function is a hook which allows implementing in-process COM
   servers with ctypes.  It is called from the DllGetClassObject
   function that the "_ctypes" extension dll exports.

   Availability: Windows

ctypes.util.find_library(name)

   Intenta encontrar una biblioteca y retornar un nombre de ruta.
   *name* es el nombre de la biblioteca sin ningún prefijo como "lib",
   sufijo como ".so", ".dylib" o número de versión (esta es la forma
   usada para la opción del enlazador posix "-l"). Si no se puede
   encontrar ninguna biblioteca, retorna "None".

   La funcionalidad exacta depende del sistema.

   See Encontrar bibliotecas compartidas for complete documentation.

ctypes.util.find_msvcrt()

   Returns the filename of the VC runtime library used by Python, and
   by the extension modules.  If the name of the library cannot be
   determined, "None" is returned.

   Si necesita liberar memoria, por ejemplo, asignada por un módulo de
   extensión con una llamada al "free(void *)", es importante que
   utilice la función en la misma biblioteca que asignó la memoria.

   Availability: Windows

ctypes.util.dllist()

   Try to provide a list of paths of the shared libraries loaded into
   the current process.  These paths are not normalized or processed
   in any way.  The function can raise "OSError" if the underlying
   platform APIs fail. The exact functionality is system dependent.

   On most platforms, the first element of the list represents the
   current executable file. It may be an empty string.

   Availability: Windows, macOS, iOS, glibc, BSD libc, musl

   Added in version 3.14.

ctypes.FormatError([code])

   Returns a textual description of the error code *code*.  If no
   error code is specified, the last error code is used by calling the
   Windows API function "GetLastError()".

   Availability: Windows

ctypes.GetLastError()

   Returns the last error code set by Windows in the calling thread.
   This function calls the Windows "GetLastError()" function directly,
   it does not return the ctypes-private copy of the error code.

   Availability: Windows

ctypes.get_errno()

   Retorna el valor actual de la copia ctypes-private de la variable
   de sistema "errno" en el hilo de llamada.

   Lanza un auditing event "ctypes.get_errno" sin argumentos.

ctypes.get_last_error()

   Returns the current value of the ctypes-private copy of the system
   "LastError" variable in the calling thread.

   Availability: Windows

   Lanza un auditing event "ctypes.get_last_error" sin argumentos.

ctypes.memmove(dst, src, count)

   Igual que la función de la biblioteca estándar  de C *memmove*:
   copia *count* bytes de *src* a *dst*. *dst* y *src* deben ser
   enteros o instancias ctypes que pueden ser convertidos en punteros.

ctypes.memset(dst, c, count)

   Igual que la función de la biblioteca estándar de C *memset* C:
   llena el bloque de memoria en la dirección *dst* con *count* bytes
   de valor *c*. *dst* debe ser un número entero que especifique una
   dirección, o una instancia ctypes.

ctypes.POINTER(type, /)

   Create or return a ctypes pointer type. Pointer types are cached
   and reused internally, so calling this function repeatedly is
   cheap. *type* must be a ctypes type.

   **Detalles de implementación de CPython:** The resulting pointer
   type is cached in the "__pointer_type__" attribute of *type*. It is
   possible to set this attribute before the first call to "POINTER"
   in order to set a custom pointer type. However, doing this is
   discouraged: manually creating a suitable pointer type is difficult
   without relying on implementation details that may change in future
   Python versions.

ctypes.pointer(obj, /)

   Create a new pointer instance, pointing to *obj*. The returned
   object is of the type "POINTER(type(obj))".

   Nota: Si sólo quieres pasar un puntero a un objeto a una llamada de
   función foránea, deberías usar "byref(obj)" que es mucho más
   rápido.

ctypes.resize(obj, size)

   Esta función redimensiona el búfer de memoria interna de *obj*, que
   debe ser una instancia de tipo ctypes. No es posible hacer el
   buffer más pequeño que el tamaño nativo del tipo de objetos, como
   lo indica "size of (type(obj))", pero es posible agrandar el
   buffer.

ctypes.set_errno(value)

   Poner el valor actual de la copia ctypes-private de la variable del
   sistema "errno" en el hilo de llamada a *valor* y retornar el valor
   anterior.

   Lanza un auditing event "ctypes.set_errno" con argumento "errno".

ctypes.set_last_error(value)

   Sets the current value of the ctypes-private copy of the system
   "LastError" variable in the calling thread to *value* and return
   the previous value.

   Availability: Windows

   Lanza un auditing event "ctypes.set_last_error" con argumento
   "error".

ctypes.sizeof(obj_or_type)

   Retorna el tamaño en bytes de un buffer de memoria tipo ctypes o
   instancia. Hace lo mismo que el operador C "sizeof".

ctypes.string_at(ptr, size=-1)

   Return the byte string at *void *ptr*. If *size* is specified, it
   is used as size, otherwise the string is assumed to be zero-
   terminated.

   Raises an auditing event "ctypes.string_at" with arguments "ptr",
   "size".

ctypes.WinError(code=None, descr=None)

   Creates an instance of "OSError".  If *code* is not specified,
   "GetLastError()" is called to determine the error code. If *descr*
   is not specified, "FormatError()" is called to get a textual
   description of the error.

   Availability: Windows

   Distinto en la versión 3.3: An instance of "WindowsError" used to
   be created, which is now an alias of "OSError".

ctypes.wstring_at(ptr, size=-1)

   Return the wide-character string at *void *ptr*. If *size* is
   specified, it is used as the number of characters of the string,
   otherwise the string is assumed to be zero-terminated.

   Raises an auditing event "ctypes.wstring_at" with arguments "ptr",
   "size".

ctypes.memoryview_at(ptr, size, readonly=False)

   Return a "memoryview" object of length *size* that references
   memory starting at *void *ptr*.

   If *readonly* is true, the returned "memoryview" object can not be
   used to modify the underlying memory. (Changes made by other means
   will still be reflected in the returned object.)

   This function is similar to "string_at()" with the key difference
   of not making a copy of the specified memory. It is a semantically
   equivalent (but more efficient) alternative to "memoryview((c_byte
   * size).from_address(ptr))". (While "from_address()" only takes
   integers, *ptr* can also be given as a "ctypes.POINTER" or a
   "byref()" object.)

   Raises an auditing event "ctypes.memoryview_at" with arguments
   "address", "size", "readonly".

   Added in version 3.14.

### Tipos de datos

class ctypes._CData

   Esta clase no pública es la clase de base común de todos los tipos
   de datos de los ctypes. Entre otras cosas, todas las instancias de
   tipo ctypes contienen un bloque de memoria que contiene datos
   compatibles con C; la dirección del bloque de memoria es retornada
   por la función de ayuda "addressof()". Otra variable de instancia
   se expone como "_objetos"; ésta contiene otros objetos de Python
   que deben mantenerse vivos en caso de que el bloque de memoria
   contenga punteros.

   Métodos comunes de tipos de datos ctypes, estos son todos métodos
   de clase (para ser exactos, son métodos del *metaclass*):

   from_buffer(source[, offset])

      Este método retorna una instancia ctypes que comparte el buffer
      del objeto *source*. El objeto *source* debe soportar la
      interfaz del buffer de escritura. El parámetro opcional *offset*
      especifica un offset en el buffer de la fuente en bytes; el
      valor por defecto es cero. Si el buffer de la fuente no es lo
      suficientemente grande se lanza un "ValueError".

      Lanza un auditing event "ctypes.cdata/buffer" con argumentos
      "pointer", "size", "offset".

   from_buffer_copy(source[, offset])

      Este método crea una instancia ctypes, copiando el buffer del
      buffer de objetos *source* que debe ser legible. El parámetro
      opcional *offset* especifica un offset en el buffer de origen en
      bytes; el valor por defecto es cero. Si el buffer de fuente no
      es lo suficientemente grande se lanza un "ValueError".

      Lanza un auditing event "ctypes.cdata/buffer" con argumentos
      "pointer", "size", "offset".

   from_address(address)

      Este método retorna una instancia de tipo ctypes utilizando la
      memoria especificada por *address* que debe ser un entero.

      Este método, y otros que indirectamente llaman a este método,
      lanzan un auditing event "ctypes.cdata" con argumento "address".

   from_param(obj)

      This method adapts *obj* to a ctypes type.  It is called with
      the actual object used in a foreign function call when the type
      is present in the foreign function's "argtypes" tuple; it must
      return an object that can be used as a function call parameter.

      Todos los tipos de datos ctypes tienen una implementación por
      defecto de este método de clase que normalmente retorna *obj* si
      es una instancia del tipo. Algunos tipos aceptan también otros
      objetos.

   in_dll(library, name)

      Este método retorna una instancia de tipo ctypes exportada por
      una biblioteca compartida. *name* es el nombre del símbolo que
      exporta los datos, *library* es la biblioteca compartida
      cargada.

   Common class variables of ctypes data types:

   __pointer_type__

      The pointer type that was created by calling "POINTER()" for
      corresponding ctypes data type. If a pointer type was not yet
      created, the attribute is missing.

      Added in version 3.14.

   Variables de instancia común de los tipos de datos de ctypes:

   _b_base_

      A veces, las instancias de datos ctypes no poseen el bloque de
      memoria que contienen, sino que comparten parte del bloque de
      memoria de un objeto base. El miembro de sólo lectura "_b_base_"
      es el objeto raíz ctypes que posee el bloque de memoria.

   _b_needsfree_

      Esta variable de sólo lectura es verdadera cuando la instancia
      de datos ctypes ha sido asignada a el propio bloque de memoria,
      falsa en caso contrario.

   _objects

      Este miembro es "None" o un diccionario que contiene objetos de
      Python que deben mantenerse vivos para que el contenido del
      bloque de memoria sea válido. Este objeto sólo se expone para su
      depuración; nunca modifique el contenido de este diccionario.

### Tipos de datos fundamentales

class ctypes._SimpleCData

   Esta clase no pública es la clase base de todos los tipos de datos
   de ctypes fundamentales. Se menciona aquí porque contiene los
   atributos comunes de los tipos de datos de ctypes fundamentales.
   "_SimpleCData" es una subclase de "_CData", por lo que hereda sus
   métodos y atributos. Los tipos de datos ctypes que no son y no
   contienen punteros ahora pueden ser archivados.

   Los instancias tienen un solo atributo:

   value

      Este atributo contiene el valor real de la instancia. Para los
      tipos enteros y punteros, es un entero, para los tipos de
      caracteres, es un objeto o cadena de bytes de un solo carácter,
      para los tipos de punteros de caracteres es un objeto o cadena
      de bytes de Python.

      When the "value" attribute is retrieved from a ctypes instance,
      usually a new object is returned each time.  "ctypes" does *not*
      implement original object return, always a new object is
      constructed.  The same is true for all other ctypes object
      instances.

   Each subclass has a class attribute:

   _type_

      Class attribute that contains an internal type code, as a
      single-character string. See Tipos de datos fundamentales for a
      summary.

      Types marked * in the summary may be (or always are) aliases of
      a different "_SimpleCData" subclass, and will not necessarily
      use the listed type code. For example, if the platform's long,
      long long and time_t C types are the same, then "c_long",
      "c_longlong" and "c_time_t" all refer to a single class,
      "c_long", whose "_type_" code is "'l'". The "'L'" code will be
      unused.

      Ver también:

        The "array" and struct modules, as well as third-party modules
        like numpy, use similar -- but slightly different -- type
        codes.

Fundamental data types, when returned as foreign function call
results, or, for example, by retrieving structure field members or
array items, are transparently converted to native Python types.  In
other words, if a foreign function has a "restype" of "c_char_p", you
will always receive a Python bytes object, *not* a "c_char_p"
instance.

Subclasses of fundamental data types do *not* inherit this behavior.
So, if a foreign functions "restype" is a subclass of "c_void_p", you
will receive an instance of this subclass from the function call. Of
course, you can get the value of the pointer by accessing the "value"
attribute.

Estos son los tipos de datos fundamentales de ctypes:

class ctypes.c_byte

   Representa el tipo de datos C signed char e interpreta el valor
   como un entero pequeño. El constructor acepta un inicializador
   entero opcional; no se realiza ninguna comprobación de
   desbordamiento.

class ctypes.c_char

   Representa el tipo de datos C char e interpreta el valor como un
   solo carácter. El constructor acepta un inicializador de cadena
   opcional, la longitud de la cadena debe ser exactamente un
   carácter.

class ctypes.c_char_p

   Representa el tipo de datos C char* cuando apunta a una cadena
   terminada en cero. Para un puntero de carácter general que también
   puede apuntar a datos binarios, se debe usar "POINTER(c_char)". El
   constructor acepta una dirección entera o un objeto de bytes.

class ctypes.c_double

   Representa el tipo de datos C double. El constructor acepta un
   inicializador flotante opcional.

class ctypes.c_longdouble

   Representa el tipo de datos C long double. El constructor acepta un
   inicializador flotante opcional. En plataformas donde "sizeof(long
   double) == sizeof(double)" es un alias de "c_double".

class ctypes.c_float

   Representa el tipo de datos C float. El constructor acepta un
   inicializador flotante opcional.

class ctypes.c_double_complex

   Represents the C double complex datatype, if available.  The
   constructor accepts an optional "complex" initializer.

   Added in version 3.14.

class ctypes.c_float_complex

   Represents the C float complex datatype, if available.  The
   constructor accepts an optional "complex" initializer.

   Added in version 3.14.

class ctypes.c_longdouble_complex

   Represents the C long double complex datatype, if available.  The
   constructor accepts an optional "complex" initializer.

   Added in version 3.14.

class ctypes.c_int

   Representa el tipo de datos C signed int. El constructor acepta un
   inicializador entero opcional; no se realiza ninguna comprobación
   de desbordamiento. En plataformas donde "sizeof(int) ==
   sizeof(long)" es un alias de "c_long".

class ctypes.c_int8

   Represents the C 8-bit signed int datatype.  It is an alias for
   "c_byte".

class ctypes.c_int16

   Representa el tipo de datos signed int de C de 16 bits. Por lo
   general, un alias para "c_short".

class ctypes.c_int32

   Representa el tipo de datos signed int de C de 32 bits. Por lo
   general, un alias para "c_int".

class ctypes.c_int64

   Representa el tipo de datos signed int de C de 64 bits. Por lo
   general, un alias para "c_longlong".

class ctypes.c_long

   Representa el tipo de datos C signed long. El constructor acepta un
   inicializador entero opcional; no se realiza ninguna comprobación
   de desbordamiento.

class ctypes.c_longlong

   Represents the C signed long long datatype.  The constructor
   accepts an optional integer initializer; no overflow checking is
   done. On platforms where "sizeof(long long) == sizeof(long)" it is
   an alias to "c_long".

class ctypes.c_short

   Representa el tipo de datos C signed short. El constructor acepta
   un inicializador entero opcional; no se realiza ninguna
   comprobación de desbordamiento.

class ctypes.c_size_t

   Represents the C "size_t" datatype. Usually an alias for another
   unsigned integer type.

class ctypes.c_ssize_t

   Represents the "Py_ssize_t" datatype. This is a signed version of
   "size_t"; that is, the POSIX "ssize_t" type. Usually an alias for
   another integer type.

   Added in version 3.2.

class ctypes.c_time_t

   Represents the C "time_t" datatype. Usually an alias for another
   integer type.

   Added in version 3.12.

class ctypes.c_ubyte

   Representa el tipo de datos C unsigned char, interpreta el valor
   como un entero pequeño. El constructor acepta un inicializador
   entero opcional; no se realiza ninguna comprobación de
   desbordamiento.

class ctypes.c_uint

   Representa el tipo de datos C unsigned int. El constructor acepta
   un inicializador entero opcional; no se realiza ninguna
   comprobación de desbordamiento. En plataformas donde "sizeof(int)
   == sizeof(long)" es un alias para "c_ulong".

class ctypes.c_uint8

   Represents the C 8-bit unsigned int datatype.  It is an alias for
   "c_ubyte".

class ctypes.c_uint16

   Representa el tipo de datos unsigned int de C de 16 bits. Por lo
   general, un alias para "c_ushort".

class ctypes.c_uint32

   Representa el tipo de datos unsigned int de C de 32 bits. Por lo
   general, un alias para "c_uint".

class ctypes.c_uint64

   Representa el tipo de datos unsigned int de C de 64 bits. Por lo
   general, un alias para "c_ulonglong".

class ctypes.c_ulong

   Representa el tipo de datos C unsigned long. El constructor acepta
   un inicializador entero opcional; no se realiza ninguna
   comprobación de desbordamiento.

class ctypes.c_ulonglong

   Represents the C unsigned long long datatype.  The constructor
   accepts an optional integer initializer; no overflow checking is
   done. On platforms where "sizeof(long long) == sizeof(long)" it is
   an alias to "c_long".

class ctypes.c_ushort

   Representa el tipo de datos C unsigned short. El constructor acepta
   un inicializador entero opcional; no se realiza ninguna
   comprobación de desbordamiento.

class ctypes.c_void_p

   Representa el tipo C void*. El valor se representa como un número
   entero. El constructor acepta un inicializador entero opcional.

class ctypes.c_wchar

   Represents the C "wchar_t" datatype, and interprets the value as a
   single character unicode string.  The constructor accepts an
   optional string initializer, the length of the string must be
   exactly one character.

class ctypes.c_wchar_p

   Representa el tipo de datos C wchar_t*, que debe ser un puntero a
   una cadena de caracteres anchos terminada en cero. El constructor
   acepta una dirección entera o una cadena.

class ctypes.c_bool

   Representa el tipo de dato C bool (más precisamente, _Bool de C99).
   Su valor puede ser "True" o "False", y el constructor acepta
   cualquier objeto que tenga un valor de verdad.

class ctypes.HRESULT

   Represents a "HRESULT" value, which contains success or error
   information for a function or method call.

   Availability: Windows

class ctypes.py_object

   Representa el tipo de dato de C PyObject*.  Llamar esto sin un
   argumento crea un puntero PyObject* "NULL".

   Distinto en la versión 3.14: "py_object" is now a *generic type*.

The "ctypes.wintypes" module provides quite some other Windows
specific data types, for example "HWND", "WPARAM", "VARIANT_BOOL" or
"DWORD". Some useful structures like "MSG" or "RECT" are also defined.

### Tipos de datos estructurados

class ctypes.Union(*args, **kw)

   Clase base abstracta para uniones en orden de bytes nativos.

   Unions share common attributes and behavior with structures; see
   "Structure" documentation for details.

class ctypes.BigEndianUnion(*args, **kw)

   Clase base abstracta para uniones en orden de bytes *big endian*.

   Added in version 3.11.

class ctypes.LittleEndianUnion(*args, **kw)

   Clase base abstracta para uniones en orden de bytes *little
   endian*.

   Added in version 3.11.

class ctypes.BigEndianStructure(*args, **kw)

   Clase base abstracta para estructuras en orden de bytes *big
   endian*.

class ctypes.LittleEndianStructure(*args, **kw)

   Clase base abstracta para estructuras en orden de bytes *little
   endian*.

Las estructuras y uniones con un orden de bytes no nativo no pueden
contener campos de tipo puntero ni ningún otro tipo de datos que
contenga campos de tipo puntero.

class ctypes.Structure(*args, **kw)

   Clase base abstracta para estructuras en orden de bytes *native*.

   Concrete structure and union types must be created by subclassing
   one of these types, and at least define a "_fields_" class
   variable. "ctypes" will create *descriptor*s which allow reading
   and writing the fields by direct attribute accesses.  These are the

   _fields_

      Una secuencia que define los campos de estructura. Los elementos
      deben ser de 2 o 3 tuplas. El primer ítem es el nombre del
      campo, el segundo ítem especifica el tipo de campo; puede ser
      cualquier tipo de datos ctypes.

      Para los campos de tipo entero como "c_int", se puede dar un
      tercer elemento opcional. Debe ser un pequeño entero positivo
      que defina el ancho de bit del campo.

      Los nombres de los campos deben ser únicos dentro de una
      estructura o unión. Esto no se comprueba, sólo se puede acceder
      a un campo cuando los nombres se repiten.

      Es posible definir la variable de clase "_fields_" *después* de
      la sentencia de clase que define la subclase Estructura, esto
      permite crear tipos de datos que se refieren directa o
      indirectamente a sí mismos:

         class List(Structure):
             pass
         List._fields_ = [("pnext", POINTER(List)),
                          ...
                         ]

      The "_fields_" class variable can only be set once. Later
      assignments will raise an "AttributeError".

      Additionally, the "_fields_" class variable must be defined
      before the structure or union type is first used: an instance or
      subclass is created, "sizeof()" is called on it, and so on.
      Later assignments to "_fields_" will raise an "AttributeError".
      If "_fields_" has not been set before such use, the structure or
      union will have no own fields, as if "_fields_" was empty.

      Sub-subclasses of structure types inherit the fields of the base
      class plus the "_fields_" defined in the sub-subclass, if any.

   _pack_

      An optional small integer that allows overriding the alignment
      of structure fields in the instance.

      This is only implemented for the MSVC-compatible memory layout
      (see "_layout_").

      Setting "_pack_" to 0 is the same as not setting it at all.
      Otherwise, the value must be a positive power of two. The effect
      is equivalent to "#pragma pack(N)" in C, except "ctypes" may
      allow larger *n* than what the compiler accepts.

      "_pack_" must already be defined when "_fields_" is assigned,
      otherwise it will have no effect.

      Deprecated since version 3.14, will be removed in version 3.19:
      For historical reasons, if "_pack_" is non-zero, the MSVC-
      compatible layout will be used by default. On non-Windows
      platforms, this default is deprecated and is slated to become an
      error in Python 3.19. If it is intended, set "_layout_" to
      "'ms'" explicitly.

   _align_

      An optional small integer that allows increasing the alignment
      of the structure when being packed or unpacked to/from memory.

      The value must not be negative. The effect is equivalent to
      "__attribute__((aligned(N)))" on GCC or "#pragma align(N)" on
      MSVC, except "ctypes" may allow values that the compiler would
      reject.

      "_align_" can only *increase* a structure's alignment
      requirements. Setting it to 0 or 1 has no effect.

      Using values that are not powers of two is discouraged and may
      lead to surprising behavior.

      "_align_" must already be defined when "_fields_" is assigned,
      otherwise it will have no effect.

      Added in version 3.13.

   _layout_

      An optional string naming the struct/union layout. It can
      currently be set to:

      * ""ms"": the layout used by the Microsoft compiler (MSVC). On
        GCC and Clang, this layout can be selected with
        "__attribute__((ms_struct))".

      * ""gcc-sysv"": the layout used by GCC with the System V or
        “SysV-like” data model, as used on Linux and macOS. With this
        layout, "_pack_" must be unset or zero.

      If not set explicitly, "ctypes" will use a default that matches
      the platform conventions. This default may change in future
      Python releases (for example, when a new platform gains official
      support, or when a difference between similar platforms is
      found). Currently the default will be:

      * On Windows: ""ms""

      * When "_pack_" is specified: ""ms"". (This is deprecated; see
        "_pack_" documentation.)

      * Otherwise: ""gcc-sysv""

      "_layout_" must already be defined when "_fields_" is assigned,
      otherwise it will have no effect.

      Added in version 3.14.

   _anonymous_

      Una secuencia opcional que enumera los nombres de los campos sin
      nombre (anónimos). "_anonymous_" debe estar ya definida cuando
      se asigna "_fields_", de lo contrario no tendrá ningún efecto.

      The fields listed in this variable must be structure or union
      type fields. "ctypes" will create descriptors in the structure
      type that allows accessing the nested fields directly, without
      the need to create the structure or union field.

      Aquí hay un tipo de ejemplo (Windows):

         class _U(Union):
             _fields_ = [("lptdesc", POINTER(TYPEDESC)),
                         ("lpadesc", POINTER(ARRAYDESC)),
                         ("hreftype", HREFTYPE)]

         class TYPEDESC(Structure):
             _anonymous_ = ("u",)
             _fields_ = [("u", _U),
                         ("vt", VARTYPE)]

      La estructura "TYPEDESC" describe un tipo de datos COM, el campo
      "vt" especifica cuál de los campos de unión es válido. Como el
      campo "u" está definido como campo anónimo, ahora es posible
      acceder a los miembros directamente desde la instancia TYPEDESC.
      "td.lptdesc" y "td.u.lptdesc" son equivalentes, pero el primero
      es más rápido ya que no necesita crear una instancia de unión
      temporal:

         td = TYPEDESC()
         td.vt = VT_PTR
         td.lptdesc = POINTER(some_type)
         td.u.lptdesc = POINTER(some_type)

   Es posible definir subclases de estructuras, que heredan los campos
   de la clase base. Si la definición de la subclase tiene una
   variable "_fields_" separada, los campos especificados en ella se
   añaden a los campos de la clase base.

   Los constructores de estructuras y uniones aceptan tanto argumentos
   posicionales como de palabras clave. Los argumentos posicionales se
   usan para inicializar los campos de los miembros en el mismo orden
   en que aparecen en "_fields_". Los argumentos de palabras clave en
   el constructor se interpretan como asignaciones de atributos, por
   lo que inicializarán "_fields_" con el mismo nombre, o crearán
   nuevos atributos para nombres no presentes en "_fields_".

class ctypes.CField(*args, **kw)

   Descriptor for fields of a "Structure" and "Union". For example:

      >>> class Color(Structure):
      ...     _fields_ = (
      ...         ('red', c_uint8),
      ...         ('green', c_uint8),
      ...         ('blue', c_uint8),
      ...         ('intense', c_bool, 1),
      ...         ('blinking', c_bool, 1),
      ...    )
      ...
      >>> Color.red
      <ctypes.CField 'red' type=c_ubyte, ofs=0, size=1>
      >>> Color.green.type
      <class 'ctypes.c_ubyte'>
      >>> Color.blue.byte_offset
      2
      >>> Color.intense
      <ctypes.CField 'intense' type=c_bool, ofs=3, bit_size=1, bit_offset=0>
      >>> Color.blinking.bit_offset
      1

   All attributes are read-only.

   "CField" objects are created via "_fields_"; do not instantiate the
   class directly.

   Added in version 3.14: Previously, descriptors only had "offset"
   and "size" attributes and a readable string representation; the
   "CField" class was not available directly.

   name

      Name of the field, as a string.

   type

      Type of the field, as a ctypes class.

   offset
   byte_offset

      Offset of the field, in bytes.

      For bitfields, this is the offset of the underlying byte-aligned
      *storage unit*; see "bit_offset".

   byte_size

      Size of the field, in bytes.

      For bitfields, this is the size of the underlying *storage
      unit*. Typically, it has the same size as the bitfield's type.

   size

      For non-bitfields, equivalent to "byte_size".

      For bitfields, this contains a backwards-compatible bit-packed
      value that combines "bit_size" and "bit_offset". Prefer using
      the explicit attributes instead.

   is_bitfield

      True if this is a bitfield.

   bit_offset
   bit_size

      The location of a bitfield within its *storage unit*, that is,
      within "byte_size" bytes of memory starting at "byte_offset".

      To get the field's value, read the storage unit as an integer,
      shift left by "bit_offset" and take the "bit_size" least
      significant bits.

      For non-bitfields, "bit_offset" is zero and "bit_size" is equal
      to "byte_size * 8".

   is_anonymous

      True if this field is anonymous, that is, it contains nested
      sub-fields that should be merged into a containing structure or
      union.

### Arreglos y punteros

class ctypes.Array(*args)

   Clase base abstracta para arreglos.

   The recommended way to create concrete array types is by
   multiplying any "ctypes" data type with a non-negative integer.
   Alternatively, you can subclass this type and define "_length_" and
   "_type_" class variables. Array elements can be read and written
   using standard subscript and slice accesses; for slice reads, the
   resulting object is *not* itself an "Array".

   Arrays are generic over the type of their elements.

   _length_

      Un número entero positivo que especifica el número de elementos
      del conjunto. Los subíndices fuera de rango dan como resultado
      un "IndexError". Será retornado por "len()".

   _type_

      Especifica el tipo de cada elemento del arreglo.

   Los constructores de subclases de arreglos aceptan argumentos
   posicionales, usados para inicializar los elementos en orden.

ctypes.ARRAY(type, length)

   Create an array. Equivalent to "type * length", where *type* is a
   "ctypes" data type and *length* an integer.

   Soft deprecated since version 3.14: In favor of multiplication.

class ctypes._Pointer

   Clase base, privada y abstracta para punteros.

   Los tipos de punteros concretos se crean llamando a "POINTER()" con
   el tipo que será apuntado; esto se hace automáticamente por
   "pointer()".

   Si un puntero apunta a un arreglo, sus elementos pueden ser leídos
   y escritos usando accesos de subíndices y cortes estándar. Los
   objetos punteros no tienen tamaño, así que "len()" lanzará un
   "TypeError". Los subíndices negativos se leerán de la memoria
   *antes* que el puntero (como en C), y los subíndices fuera de rango
   probablemente se bloqueen con una violación de acceso (si tienes
   suerte).

   _type_

      Especifica el tipo apuntado.

   contents

      Retorna el objeto al que el puntero apunta. Asignando a este
      atributo cambia el puntero para que apunte al objeto asignado.

### Exceptions

exception ctypes.ArgumentError

   Esta excepción se lanza cuando una llamada a una función foránea no
   puede convertir uno de los argumentos pasados.

exception ctypes.COMError(hresult, text, details)

   This exception is raised when a COM method call failed.

   hresult

      The integer value representing the error code.

   text

      The error message.

   details

      The 5-tuple "(descr, source, helpfile, helpcontext, progid)".

      *descr* is the textual description.  *source* is the language-
      dependent "ProgID" for the class or application that raised the
      error.  *helpfile* is the path of the help file.  *helpcontext*
      is the help context identifier.  *progid* is the "ProgID" of the
      interface that defined the error.

   Availability: Windows

   Added in version 3.14.
