---
title: Defining extension modules
source_url: https://docs.python.org/es/3
source_path: c-api/extension-modules.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 260
---

# Defining extension modules

A C extension for CPython is a shared library (for example, a ".so"
file on Linux, ".pyd" DLL on Windows), which is loadable into the
Python process (for example, it is compiled with compatible compiler
settings), and which exports an initialization function.

To be importable by default (that is, by
"importlib.machinery.ExtensionFileLoader"), the shared library must be
available on "sys.path", and must be named after the module name plus
an extension listed in "importlib.machinery.EXTENSION_SUFFIXES".

Nota:

  Building, packaging and distributing extension modules is best done
  with third-party tools, and is out of scope of this document. One
  suitable tool is Setuptools, whose documentation can be found at
  https://setuptools.pypa.io/en/latest/setuptools.html.

Normally, the initialization function returns a module definition
initialized using "PyModuleDef_Init()". This allows splitting the
creation process into several phases:

* Before any substantial code is executed, Python can determine which
  capabilities the module supports, and it can adjust the environment
  or refuse loading an incompatible extension.

* By default, Python itself creates the module object -- that is, it
  does the equivalent of "object.__new__()" for classes. It also sets
  initial attributes like "__package__" and "__loader__".

* Afterwards, the module object is initialized using extension-
  specific code -- the equivalent of "__init__()" on classes.

This is called *multi-phase initialization* to distinguish it from the
legacy (but still supported) *single-phase initialization* scheme,
where the initialization function returns a fully constructed module.
See the single-phase-initialization section below for details.

Distinto en la versión 3.5: Added support for multi-phase
initialization (**PEP 489**).

## Multiple module instances

By default, extension modules are not singletons. For example, if the
"sys.modules" entry is removed and the module is re-imported, a new
module object is created, and typically populated with fresh method
and type objects. The old module is subject to normal garbage
collection. This mirrors the behavior of pure-Python modules.

Additional module instances may be created in sub-interpreters or
after Python runtime reinitialization ("Py_Finalize()" and
"Py_Initialize()"). In these cases, sharing Python objects between
module instances would likely cause crashes or undefined behavior.

To avoid such issues, each instance of an extension module should be
*isolated*: changes to one instance should not implicitly affect the
others, and all state owned by the module, including references to
Python objects, should be specific to a particular module instance.
See Aislamiento de módulos de extensión for more details and a
practical guide.

A simpler way to avoid these issues is raising an error on repeated
initialization.

All modules are expected to support sub-interpreters, or otherwise
explicitly signal a lack of support. This is usually achieved by
isolation or blocking repeated initialization, as above. A module may
also be limited to the main interpreter using the
"Py_mod_multiple_interpreters" slot.

## Initialization function

The initialization function defined by an extension module has the
following signature:

PyObject *PyInit_modulename(void)

Its name should be "PyInit_*<name>*", with "<name>" replaced by the
name of the module.

For modules with ASCII-only names, the function must instead be named
"PyInit_*<name>*", with "<name>" replaced by the name of the module.
When using Multi-phase initialization, non-ASCII module names are
allowed. In this case, the initialization function name is
"PyInitU_*<name>*", with "<name>" encoded using Python's *punycode*
encoding with hyphens replaced by underscores. In Python:

   def initfunc_name(name):
       try:
           suffix = b'_' + name.encode('ascii')
       except UnicodeEncodeError:
           suffix = b'U_' + name.encode('punycode').replace(b'-', b'_')
       return b'PyInit' + suffix

It is recommended to define the initialization function using a helper
macro:

PyMODINIT_FUNC

   Declare an extension module initialization function. This macro:

   * specifies the PyObject* return type,

   * adds any special linkage declarations required by the platform,
     and

   * for C++, declares the function as "extern "C"".

For example, a module called "spam" would be defined like this:

   static struct PyModuleDef spam_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "spam",
       ...
   };

   PyMODINIT_FUNC
   PyInit_spam(void)
   {
       return PyModuleDef_Init(&spam_module);
   }

It is possible to export multiple modules from a single shared library
by defining multiple initialization functions. However, importing them
requires using symbolic links or a custom importer, because by default
only the function corresponding to the filename is found. See the
Multiple modules in one library section in **PEP 489** for details.

The initialization function is typically the only non-"static" item
defined in the module's C source.

## Multi-phase initialization

Normally, the initialization function ("PyInit_modulename") returns a
"PyModuleDef" instance with non-"NULL" "m_slots". Before it is
returned, the "PyModuleDef" instance must be initialized using the
following function:

PyObject *PyModuleDef_Init(PyModuleDef *def)
    * Part of the Stable ABI since version 3.5.*

   Ensure a module definition is a properly initialized Python object
   that correctly reports its type and a reference count.

   Return *def* cast to "PyObject*", or "NULL" if an error occurred.

   Calling this function is required for Multi-phase initialization.
   It should not be used in other contexts.

   Note that Python assumes that "PyModuleDef" structures are
   statically allocated. This function may return either a new
   reference or a borrowed one; this reference must not be released.

   Added in version 3.5.

## Legacy single-phase initialization

Atención:

  Single-phase initialization is a legacy mechanism to initialize
  extension modules, with known drawbacks and design flaws. Extension
  module authors are encouraged to use multi-phase initialization
  instead.

In single-phase initialization, the initialization function
("PyInit_modulename") should create, populate and return a module
object. This is typically done using "PyModule_Create()" and functions
like "PyModule_AddObjectRef()".

Single-phase initialization differs from the default in the following
ways:

* Single-phase modules are, or rather *contain*, “singletons”.

  When the module is first initialized, Python saves the contents of
  the module's "__dict__" (that is, typically, the module's functions
  and types).

  For subsequent imports, Python does not call the initialization
  function again. Instead, it creates a new module object with a new
  "__dict__", and copies the saved contents to it. For example, given
  a single-phase module "_testsinglephase" [1] that defines a function
  "sum" and an exception class "error":

     >>> import sys
     >>> import _testsinglephase as one
     >>> del sys.modules['_testsinglephase']
     >>> import _testsinglephase as two
     >>> one is two
     False
     >>> one.__dict__ is two.__dict__
     False
     >>> one.sum is two.sum
     True
     >>> one.error is two.error
     True

  The exact behavior should be considered a CPython implementation
  detail.

* To work around the fact that "PyInit_modulename" does not take a
  *spec* argument, some state of the import machinery is saved and
  applied to the first suitable module created during the
  "PyInit_modulename" call. Specifically, when a sub-module is
  imported, this mechanism prepends the parent package name to the
  name of the module.

  A single-phase "PyInit_modulename" function should create “its”
  module object as soon as possible, before any other module objects
  can be created.

* Non-ASCII module names ("PyInitU_modulename") are not supported.

* Single-phase modules support module lookup functions like
  "PyState_FindModule()".

[1] "_testsinglephase" is an internal module used in CPython's self-
    test suite; your installation may or may not include it.
