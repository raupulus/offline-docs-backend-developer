---
title: Type Object Structures
source_url: https://docs.python.org/es/3
source_path: c-api/typeobj.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 750
---

# Type Object Structures

Perhaps one of the most important structures of the Python object
system is the structure that defines a new type: the "PyTypeObject"
structure.  Type objects can be handled using any of the "PyObject_*"
or "PyType_*" functions, but do not offer much that's interesting to
most Python applications. These objects are fundamental to how objects
behave, so they are very important to the interpreter itself and to
any extension module that implements new types.

Los objetos de tipo son bastante grandes en comparación con la mayoría
de los tipos estándar. La razón del tamaño es que cada objeto de tipo
almacena una gran cantidad de valores, principalmente punteros de
función C, cada uno de los cuales implementa una pequeña parte de la
funcionalidad del tipo. Los campos del objeto tipo se examinan en
detalle en esta sección. Los campos se describirán en el orden en que
aparecen en la estructura.

Además de la siguiente referencia rápida, la sección Ejemplos
proporciona una visión rápida del significado y uso de "PyTypeObject".

## Referencia rápida

### "ranuras *tp*" (*tp slots*)

+--------------------+--------------------+--------------------+-----+-----+-----+-----+
| Ranura             | Type               | métodos/atributos  | Información           |
| "PyTypeObject" [1] |                    | especiales         | [2]                   |
|                    |                    |                    +-----+-----+-----+-----+
|                    |                    |                    | O   | T   | D   | I   |
|                    |                    |                    |     |     |     |     |
|====================|====================|====================|=====|=====|=====|=====|
## | <R> "tp_name"      | const char *       | __name__           | X   | X   |     |     |

## | "tp_basicsize"     | "Py_ssize_t"       |                    | X   | X   |     | X   |

## | "tp_itemsize"      | "Py_ssize_t"       |                    |     | X   |     | X   |

## | "tp_dealloc"       | "destructor"       |                    | X   | X   |     | X   |

| "tp_vectorcall_of  | "Py_ssize_t"       |                    |     | X   |     | X   |
## | fset"              |                    |                    |     |     |     |     |

| ("tp_getattr")     | "getattrfunc"      | __getattribute__,  |     |     |     | G   |
## |                    |                    | __getattr__        |     |     |     |     |

| ("tp_setattr")     | "setattrfunc"      | __setattr__,       |     |     |     | G   |
## |                    |                    | __delattr__        |     |     |     |     |

| "tp_as_async"      | "PyAsyncMethods" * | sub-ranuras (sub-  |     |     |     | %   |
## |                    |                    | slots)             |     |     |     |     |

## | "tp_repr"          | "reprfunc"         | __repr__           | X   | X   |     | X   |

| "tp_as_number"     | "PyNumberMethods"  | sub-ranuras (sub-  |     |     |     | %   |
## |                    | *                  | slots)             |     |     |     |     |

| "tp_as_sequence"   | "PySequenceMethod  | sub-ranuras (sub-  |     |     |     | %   |
## |                    | s" *               | slots)             |     |     |     |     |

| "tp_as_mapping"    | "PyMappingMethods" | sub-ranuras (sub-  |     |     |     | %   |
## |                    | *                  | slots)             |     |     |     |     |

## | "tp_hash"          | "hashfunc"         | __hash__           | X   |     |     | G   |

## | "tp_call"          | "ternaryfunc"      | __call__           |     | X   |     | X   |

## | "tp_str"           | "reprfunc"         | __str__            | X   |     |     | X   |

| "tp_getattro"      | "getattrofunc"     | __getattribute__,  | X   | X   |     | G   |
## |                    |                    | __getattr__        |     |     |     |     |

| "tp_setattro"      | "setattrofunc"     | __setattr__,       | X   | X   |     | G   |
## |                    |                    | __delattr__        |     |     |     |     |

| "tp_as_buffer"     | "PyBufferProcs" *  | sub-ranuras (sub-  |     |     |     | %   |
## |                    |                    | slots)             |     |     |     |     |

## | "tp_flags"         | unsigned long      |                    | X   | X   |     | ?   |

## | "tp_doc"           | const char *       | __doc__            | X   | X   |     |     |

## | "tp_traverse"      | "traverseproc"     |                    |     | X   |     | G   |

## | "tp_clear"         | "inquiry"          |                    |     | X   |     | G   |

| "tp_richcompare"   | "richcmpfunc"      | __lt__, __le__,    | X   |     |     | G   |
|                    |                    | __eq__, __ne__,    |     |     |     |     |
## |                    |                    | __gt__, __ge__     |     |     |     |     |

| ("tp_weaklistoffs  | "Py_ssize_t"       |                    |     | X   |     | ?   |
## | et")               |                    |                    |     |     |     |     |

## | "tp_iter"          | "getiterfunc"      | __iter__           |     |     |     | X   |

## | "tp_iternext"      | "iternextfunc"     | __next__           |     |     |     | X   |

## | "tp_methods"       | "PyMethodDef" []   |                    | X   | X   |     |     |

## | "tp_members"       | "PyMemberDef" []   |                    |     | X   |     |     |

## | "tp_getset"        | "PyGetSetDef" []   |                    | X   | X   |     |     |

## | "tp_base"          | "PyTypeObject" *   | __base__           |     |     | X   |     |

## | "tp_dict"          | "PyObject" *       | __dict__           |     |     | ?   |     |

## | "tp_descr_get"     | "descrgetfunc"     | __get__            |     |     |     | X   |

| "tp_descr_set"     | "descrsetfunc"     | __set__,           |     |     |     | X   |
## |                    |                    | __delete__         |     |     |     |     |

## | ("tp_dictoffset")  | "Py_ssize_t"       |                    |     | X   |     | ?   |

## | "tp_init"          | "initproc"         | __init__           | X   | X   |     | X   |

## | "tp_alloc"         | "allocfunc"        |                    | X   |     | ?   | ?   |

## | "tp_new"           | "newfunc"          | __new__            | X   | X   | ?   | ?   |

## | "tp_free"          | "freefunc"         |                    | X   | X   | ?   | ?   |

## | "tp_is_gc"         | "inquiry"          |                    |     | X   |     | X   |

## | <"tp_bases">       | "PyObject" *       | __bases__          |     |     | ~   |     |

## | <"tp_mro">         | "PyObject" *       | __mro__            |     |     | ~   |     |

## | ["tp_cache"]       | "PyObject" *       |                    |     |     |           |

## | ["tp_subclasses"]  | void *             | __subclasses__     |     |     |           |

## | ["tp_weaklist"]    | "PyObject" *       |                    |     |     |           |

## | ("tp_del")         | "destructor"       |                    |     |     |     |     |

## | ["tp_version_tag"] | unsigned int       |                    |     |     |           |

## | "tp_finalize"      | "destructor"       | __del__            |     |     |     | X   |

## | "tp_vectorcall"    | "vectorcallfunc"   |                    |     |     |     |     |

## | ["tp_watched"]     | unsigned char      |                    |     |     |     |     |

[1] **()**: A slot name in parentheses indicates it is (effectively)
    deprecated.

    **<>**: Names in angle brackets should be initially set to "NULL"
    and treated as read-only.

    **[]**: Names in square brackets are for internal use only.

    **<R>** (as a prefix) means the field is required (must be
    non-"NULL").

[2] Columnas:

    **"O"**:  set on "PyBaseObject_Type"

    **"T"**:  set on "PyType_Type"

    **"D"**:  por defecto (si la ranura está establecida como "NULL")

       X - PyType_Ready sets this value if it is NULL
       ~ - PyType_Ready always sets this value (it should be NULL)
       ? - PyType_Ready may set this value depending on other slots

       Also see the inheritance column ("I").

    **"I"**:  herencia

       X - type slot is inherited via *PyType_Ready* if defined with a *NULL* value
       % - the slots of the sub-struct are inherited individually
       G - inherited, but only in combination with other slots; see the slot's description
       ? - it's complicated; see the slot's description

    Tenga en cuenta que algunos espacios se heredan efectivamente a
    través de la cadena de búsqueda de atributos normal.

### sub-ranuras (*sub-slots*)

+----------------------------+-------------------+--------------+
| Ranuras (*Slot*)           | Type              | métodos      |
|                            |                   | especiales   |
|============================|===================|==============|
## | "am_await"                 | "unaryfunc"       | __await__    |

## | "am_aiter"                 | "unaryfunc"       | __aiter__    |

## | "am_anext"                 | "unaryfunc"       | __anext__    |

## | "am_send"                  | "sendfunc"        |              |

## |                                                               |

| "nb_add"                   | "binaryfunc"      | __add__      |
## |                            |                   | __radd__     |

## | "nb_inplace_add"           | "binaryfunc"      | __iadd__     |

| "nb_subtract"              | "binaryfunc"      | __sub__      |
## |                            |                   | __rsub__     |

## | "nb_inplace_subtract"      | "binaryfunc"      | __isub__     |

| "nb_multiply"              | "binaryfunc"      | __mul__      |
## |                            |                   | __rmul__     |

## | "nb_inplace_multiply"      | "binaryfunc"      | __imul__     |

| "nb_remainder"             | "binaryfunc"      | __mod__      |
## |                            |                   | __rmod__     |

## | "nb_inplace_remainder"     | "binaryfunc"      | __imod__     |

| "nb_divmod"                | "binaryfunc"      | __divmod__   |
## |                            |                   | __rdivmod__  |

| "nb_power"                 | "ternaryfunc"     | __pow__      |
## |                            |                   | __rpow__     |

## | "nb_inplace_power"         | "ternaryfunc"     | __ipow__     |

## | "nb_negative"              | "unaryfunc"       | __neg__      |

## | "nb_positive"              | "unaryfunc"       | __pos__      |

## | "nb_absolute"              | "unaryfunc"       | __abs__      |

## | "nb_bool"                  | "inquiry"         | __bool__     |

## | "nb_invert"                | "unaryfunc"       | __invert__   |

| "nb_lshift"                | "binaryfunc"      | __lshift__   |
## |                            |                   | __rlshift__  |

## | "nb_inplace_lshift"        | "binaryfunc"      | __ilshift__  |

| "nb_rshift"                | "binaryfunc"      | __rshift__   |
## |                            |                   | __rrshift__  |

## | "nb_inplace_rshift"        | "binaryfunc"      | __irshift__  |

| "nb_and"                   | "binaryfunc"      | __and__      |
## |                            |                   | __rand__     |

## | "nb_inplace_and"           | "binaryfunc"      | __iand__     |

| "nb_xor"                   | "binaryfunc"      | __xor__      |
## |                            |                   | __rxor__     |

## | "nb_inplace_xor"           | "binaryfunc"      | __ixor__     |

| "nb_or"                    | "binaryfunc"      | __or__       |
## |                            |                   | __ror__      |

## | "nb_inplace_or"            | "binaryfunc"      | __ior__      |

## | "nb_int"                   | "unaryfunc"       | __int__      |

## | "nb_reserved"              | void *            |              |

## | "nb_float"                 | "unaryfunc"       | __float__    |

## | "nb_floor_divide"          | "binaryfunc"      | __floordiv__ |

| "nb_inplace_floor_divide"  | "binaryfunc"      | __ifloordiv  |
## |                            |                   | __           |

## | "nb_true_divide"           | "binaryfunc"      | __truediv__  |

## | "nb_inplace_true_divide"   | "binaryfunc"      | __itruediv__ |

## | "nb_index"                 | "unaryfunc"       | __index__    |

| "nb_matrix_multiply"       | "binaryfunc"      | __matmul__   |
## |                            |                   | __rmatmul__  |

| "nb_inplace_matrix_multip  | "binaryfunc"      | __imatmul__  |
## | ly"                        |                   |              |

## |                                                               |

## | "mp_length"                | "lenfunc"         | __len__      |

## | "mp_subscript"             | "binaryfunc"      | __getitem__  |

| "mp_ass_subscript"         | "objobjargproc"   | __setitem__, |
## |                            |                   | __delitem__  |

## |                                                               |

## | "sq_length"                | "lenfunc"         | __len__      |

## | "sq_concat"                | "binaryfunc"      | __add__      |

## | "sq_repeat"                | "ssizeargfunc"    | __mul__      |

## | "sq_item"                  | "ssizeargfunc"    | __getitem__  |

| "sq_ass_item"              | "ssizeobjargproc" | __setitem__  |
## |                            |                   | __delitem__  |

## | "sq_contains"              | "objobjproc"      | __contains__ |

## | "sq_inplace_concat"        | "binaryfunc"      | __iadd__     |

## | "sq_inplace_repeat"        | "ssizeargfunc"    | __imul__     |

## |                                                               |

## | "bf_getbuffer"             | "getbufferproc()" | __buffer__   |

| "bf_releasebuffer"         | "releasebufferpr  | __release_b  |
## |                            | oc()"             | uffer__      |

### ranura de *typedefs*

+-------------------------------+-------------------------------+------------------------+
| typedef                       | Tipos parámetros              | Tipo de retorno        |
|===============================|===============================|========================|
## | "allocfunc"                   | "PyTypeObject" * "Py_ssize_t" | "PyObject" *           |

## | "destructor"                  | "PyObject" *                  | void                   |

## | "freefunc"                    | void *                        | void                   |

| "traverseproc"                | "PyObject" * "visitproc" void | int                    |
## |                               | *                             |                        |

| "newfunc"                     | "PyTypeObject" * "PyObject" * | "PyObject" *           |
## |                               | "PyObject" *                  |                        |

| "initproc"                    | "PyObject" * "PyObject" *     | int                    |
## |                               | "PyObject" *                  |                        |

## | "reprfunc"                    | "PyObject" *                  | "PyObject" *           |

## | "getattrfunc"                 | "PyObject" * const char *     | "PyObject" *           |

| "setattrfunc"                 | "PyObject" * const char *     | int                    |
## |                               | "PyObject" *                  |                        |

## | "getattrofunc"                | "PyObject" * "PyObject" *     | "PyObject" *           |

| "setattrofunc"                | "PyObject" * "PyObject" *     | int                    |
## |                               | "PyObject" *                  |                        |

| "descrgetfunc"                | "PyObject" * "PyObject" *     | "PyObject" *           |
## |                               | "PyObject" *                  |                        |

| "descrsetfunc"                | "PyObject" * "PyObject" *     | int                    |
## |                               | "PyObject" *                  |                        |

## | "hashfunc"                    | "PyObject" *                  | Py_hash_t              |

## | "richcmpfunc"                 | "PyObject" * "PyObject" * int | "PyObject" *           |

## | "getiterfunc"                 | "PyObject" *                  | "PyObject" *           |

## | "iternextfunc"                | "PyObject" *                  | "PyObject" *           |

## | "lenfunc"                     | "PyObject" *                  | "Py_ssize_t"           |

| "getbufferproc"               | "PyObject" * "Py_buffer" *    | int                    |
## |                               | int                           |                        |

## | "releasebufferproc"           | "PyObject" * "Py_buffer" *    | void                   |

## | "inquiry"                     | "PyObject" *                  | int                    |

## | "unaryfunc"                   | "PyObject" *                  | "PyObject" *           |

## | "binaryfunc"                  | "PyObject" * "PyObject" *     | "PyObject" *           |

| "ternaryfunc"                 | "PyObject" * "PyObject" *     | "PyObject" *           |
## |                               | "PyObject" *                  |                        |

## | "ssizeargfunc"                | "PyObject" * "Py_ssize_t"     | "PyObject" *           |

| "ssizeobjargproc"             | "PyObject" * "Py_ssize_t"     | int                    |
## |                               | "PyObject" *                  |                        |

## | "objobjproc"                  | "PyObject" * "PyObject" *     | int                    |

| "objobjargproc"               | "PyObject" * "PyObject" *     | int                    |
## |                               | "PyObject" *                  |                        |

Vea Tipo Ranura typedefs abajo para más detalles.

## Definición de "PyTypeObject"

The structure definition for "PyTypeObject" can be found in
"Include/cpython/object.h".  For convenience of reference, this
repeats the definition found there:

   typedef struct _typeobject {
       PyObject_VAR_HEAD
       const char *tp_name; /* For printing, in format "<module>.<name>" */
       Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */

       /* Methods to implement standard operations */

       destructor tp_dealloc;
       Py_ssize_t tp_vectorcall_offset;
       getattrfunc tp_getattr;
       setattrfunc tp_setattr;
       PyAsyncMethods *tp_as_async; /* formerly known as tp_compare (Python 2)
                                       or tp_reserved (Python 3) */
       reprfunc tp_repr;

       /* Method suites for standard classes */

       PyNumberMethods *tp_as_number;
       PySequenceMethods *tp_as_sequence;
       PyMappingMethods *tp_as_mapping;

       /* More standard operations (here for binary compatibility) */

       hashfunc tp_hash;
       ternaryfunc tp_call;
       reprfunc tp_str;
       getattrofunc tp_getattro;
       setattrofunc tp_setattro;

       /* Functions to access object as input/output buffer */
       PyBufferProcs *tp_as_buffer;

       /* Flags to define presence of optional/expanded features */
       unsigned long tp_flags;

       const char *tp_doc; /* Documentation string */

       /* Assigned meaning in release 2.0 */
       /* call function for all accessible objects */
       traverseproc tp_traverse;

       /* delete references to contained objects */
       inquiry tp_clear;

       /* Assigned meaning in release 2.1 */
       /* rich comparisons */
       richcmpfunc tp_richcompare;

       /* weak reference enabler */
       Py_ssize_t tp_weaklistoffset;

       /* Iterators */
       getiterfunc tp_iter;
       iternextfunc tp_iternext;

       /* Attribute descriptor and subclassing stuff */
       PyMethodDef *tp_methods;
       PyMemberDef *tp_members;
       PyGetSetDef *tp_getset;
       // Strong reference on a heap type, borrowed reference on a static type
       PyTypeObject *tp_base;
       PyObject *tp_dict;
       descrgetfunc tp_descr_get;
       descrsetfunc tp_descr_set;
       Py_ssize_t tp_dictoffset;
       initproc tp_init;
       allocfunc tp_alloc;
       newfunc tp_new;
       freefunc tp_free; /* Low-level free-memory routine */
       inquiry tp_is_gc; /* For PyObject_IS_GC */
       PyObject *tp_bases;
       PyObject *tp_mro; /* method resolution order */
       PyObject *tp_cache; /* no longer used */
       void *tp_subclasses;  /* for static builtin types this is an index */
       PyObject *tp_weaklist; /* not used for static builtin types */
       destructor tp_del;

       /* Type attribute cache version tag. Added in version 2.6.
        * If zero, the cache is invalid and must be initialized.
        */
       unsigned int tp_version_tag;

       destructor tp_finalize;
       vectorcallfunc tp_vectorcall;

       /* bitset of which type-watchers care about this type */
       unsigned char tp_watched;

       /* Number of tp_version_tag values used.
        * Set to _Py_ATTR_CACHE_UNUSED if the attribute cache is
        * disabled for this type (e.g. due to custom MRO entries).
        * Otherwise, limited to MAX_VERSIONS_PER_CLASS (defined elsewhere).
        */
       uint16_t tp_versions_used;
   } PyTypeObject;

## Ranuras (*Slots*) "PyObject"

The type object structure extends the "PyVarObject" structure. The
"ob_size" field is used for dynamic types (created by "type_new()",
usually called from a class statement). Note that "PyType_Type" (the
metatype) initializes "tp_itemsize", which means that its instances
(i.e. type objects) *must* have the "ob_size" field.

"PyObject.ob_refcnt"

   The type object's reference count is initialized to "1" by the
   "PyObject_HEAD_INIT" macro.  Note that for statically allocated
   type objects, the type's instances (objects whose "ob_type" points
   back to the type) do *not* count as references.  But for
   dynamically allocated type objects, the instances *do* count as
   references.

   **Herencia:**

   Este campo no es heredado por los subtipos.

"PyObject.ob_type"

   Este es el tipo del tipo, en otras palabras, su metatipo. Se
   inicializa mediante el argumento de la macro "PyObject_HEAD_INIT",
   y su valor normalmente debería ser "&PyType_Type". Sin embargo,
   para los módulos de extensión cargables dinámicamente que deben ser
   utilizables en Windows (al menos), el compilador se queja de que
   este no es un inicializador válido. Por lo tanto, la convención es
   pasar "NULL" al macro "PyObject_HEAD_INIT" e inicializar este campo
   explícitamente al comienzo de la función de inicialización del
   módulo, antes de hacer cualquier otra cosa. Esto normalmente se
   hace así:

      Foo_Type.ob_type = &PyType_Type;

   This should be done before any instances of the type are created.
   "PyType_Ready()" checks if "ob_type" is "NULL", and if so,
   initializes it to the "ob_type" field of the base class.
   "PyType_Ready()" will not change this field if it is non-zero.

   **Herencia:**

   Este campo es heredado por subtipos.

## Ranuras "PyVarObject"

"PyVarObject.ob_size"

   Para objetos de tipo estáticamente asignados, debe inicializarse a
   cero. Para objetos de tipo dinámicamente asignados, este campo
   tiene un significado interno especial.

   This field should be accessed using the "Py_SIZE()" macro.

   **Herencia:**

   Este campo no es heredado por los subtipos.

## Ranuras "PyTypeObject"

Each slot has a section describing inheritance.  If "PyType_Ready()"
may set a value when the field is set to "NULL" then there will also
be a "Default" section.  (Note that many fields set on
"PyBaseObject_Type" and "PyType_Type" effectively act as defaults.)

const char *PyTypeObject.tp_name

   Pointer to a NUL-terminated string containing the name of the type.
   For types that are accessible as module globals, the string should
   be the full module name, followed by a dot, followed by the type
   name; for built-in types, it should be just the type name.  If the
   module is a submodule of a package, the full package name is part
   of the full module name.  For example, a type named "T" defined in
   module "M" in subpackage "Q" in package "P" should have the
   "tp_name" initializer ""P.Q.M.T"".

   Para objetos de tipo dinámicamente asignados, éste debe ser sólo el
   nombre del tipo, y el nombre del módulo almacenado explícitamente
   en el dict tipo que el valor de "'__module__'" clave.

   For statically allocated type objects, the *tp_name* field should
   contain a dot. Everything before the last dot is made accessible as
   the "__module__" attribute, and everything after the last dot is
   made accessible as the "__name__" attribute.

   If no dot is present, the entire "tp_name" field is made accessible
   as the "__name__" attribute, and the "__module__" attribute is
   undefined (unless explicitly set in the dictionary, as explained
   above).  This means your type will be impossible to pickle.
   Additionally, it will not be listed in module documentations
   created with pydoc.

   Este campo no debe ser "NULL". Es el único campo obligatorio en
   "PyTypeObject()" (que no sea potencialmente "tp_itemsize").

   **Herencia:**

   Este campo no es heredado por los subtipos.

Py_ssize_t PyTypeObject.tp_basicsize
Py_ssize_t PyTypeObject.tp_itemsize

   Estos campos permiten calcular el tamaño en bytes de instancias del
   tipo.

   There are two kinds of types: types with fixed-length instances
   have a zero "tp_itemsize" field, types with variable-length
   instances have a non-zero "tp_itemsize" field.  For a type with
   fixed-length instances, all instances have the same size, given in
   "tp_basicsize". (Exceptions to this rule can be made using
   "PyUnstable_Object_GC_NewWithExtraData()".)

   For a type with variable-length instances, the instances must have
   an "ob_size" field, and the instance size is "tp_basicsize" plus N
   times "tp_itemsize", where N is the "length" of the object.

   Functions like "PyObject_NewVar()" will take the value of N as an
   argument, and store in the instance's "ob_size" field. Note that
   the "ob_size" field may later be used for other purposes. For
   example, "int" instances use the bits of "ob_size" in an
   implementation-defined way; the underlying storage and its size
   should be accessed using "PyLong_Export()".

   Nota:

     The "ob_size" field should be accessed using the "Py_SIZE()" and
     "Py_SET_SIZE()" macros.

   Also, the presence of an "ob_size" field in the instance layout
   doesn't mean that the instance structure is variable-length. For
   example, the "list" type has fixed-length instances, yet those
   instances have a "ob_size" field. (As with "int", avoid reading
   lists' "ob_size" directly. Call "PyList_Size()" instead.)

   The "tp_basicsize" includes size needed for data of the type's
   "tp_base", plus any extra data needed by each instance.

   The  correct way to set "tp_basicsize" is to use the "sizeof"
   operator on the struct used to declare the instance layout. This
   struct must include the struct used to declare the base type. In
   other words, "tp_basicsize" must be greater than or equal to the
   base's "tp_basicsize".

   Since every type is a subtype of "object", this struct must include
   "PyObject" or "PyVarObject" (depending on whether "ob_size" should
   be included). These are usually defined by the macro
   "PyObject_HEAD" or "PyObject_VAR_HEAD", respectively.

   The basic size does not include the GC header size, as that header
   is not part of "PyObject_HEAD".

   For cases where struct used to declare the base type is unknown,
   see "PyType_Spec.basicsize" and "PyType_FromMetaclass()".

   Notes about alignment:

   * "tp_basicsize" must be a multiple of "_Alignof(PyObject)". When
     using "sizeof" on a "struct" that includes "PyObject_HEAD", as
     recommended, the compiler ensures this. When not using a C
     "struct", or when using compiler extensions like
     "__attribute__((packed))", it is up to you.

   * If the variable items require a particular alignment,
     "tp_basicsize" and "tp_itemsize" must each be a multiple of that
     alignment. For example, if a type's variable part stores a
     "double", it is your responsibility that both fields are a
     multiple of "_Alignof(double)".

   **Herencia:**

   These fields are inherited separately by subtypes. (That is, if the
   field is set to zero, "PyType_Ready()" will copy the value from the
   base type, indicating that the instances do not need additional
   storage.)

   If the base type has a non-zero "tp_itemsize", it is generally not
   safe to set "tp_itemsize" to a different non-zero value in a
   subtype (though this depends on the implementation of the base
   type).

destructor PyTypeObject.tp_dealloc

   * The corresponding slot ID "Py_tp_dealloc" is part of the Stable
   ABI.*

   A pointer to the instance destructor function.  The function
   signature is:

      void tp_dealloc(PyObject *self);

   The destructor function should remove all references which the
   instance owns (e.g., call "Py_CLEAR()"), free all memory buffers
   owned by the instance, and call the type's "tp_free" function to
   free the object itself.

   If you may call functions that may set the error indicator, you
   must use "PyErr_GetRaisedException()" and
   "PyErr_SetRaisedException()" to ensure you don't clobber a
   preexisting error indicator (the deallocation could have occurred
   while processing a different error):

      static void
      foo_dealloc(foo_object *self)
      {
          PyObject *et, *ev, *etb;
          PyObject *exc = PyErr_GetRaisedException();
          ...
          PyErr_SetRaisedException(exc);
      }

   The dealloc handler itself must not raise an exception; if it hits
   an error case it should call "PyErr_FormatUnraisable()" to log (and
   clear) an unraisable exception.

   No guarantees are made about when an object is destroyed, except:

   * Python will destroy an object immediately or some time after the
     final reference to the object is deleted, unless its finalizer
     ("tp_finalize") subsequently resurrects the object.

   * An object will not be destroyed while it is being automatically
     finalized ("tp_finalize") or automatically cleared ("tp_clear").

   CPython currently destroys an object immediately from "Py_DECREF()"
   when the new reference count is zero, but this may change in a
   future version.

   It is recommended to call "PyObject_CallFinalizerFromDealloc()" at
   the beginning of "tp_dealloc" to guarantee that the object is
   always finalized before destruction.

   If the type supports garbage collection (the "Py_TPFLAGS_HAVE_GC"
   flag is set), the destructor should call "PyObject_GC_UnTrack()"
   before clearing any member fields.

   It is permissible to call "tp_clear" from "tp_dealloc" to reduce
   code duplication and to guarantee that the object is always cleared
   before destruction.  Beware that "tp_clear" might have already been
   called.

   If the type is heap allocated ("Py_TPFLAGS_HEAPTYPE"), the
   deallocator should release the owned reference to its type object
   (via "Py_DECREF()") after calling the type deallocator.  See the
   example code below.:

      static void
      foo_dealloc(PyObject *op)
      {
         foo_object *self = (foo_object *) op;
         PyObject_GC_UnTrack(self);
         Py_CLEAR(self->ref);
         Py_TYPE(self)->tp_free(self);
      }

   "tp_dealloc" must leave the exception status unchanged.  If it
   needs to call something that might raise an exception, the
   exception state must be backed up first and restored later (after
   logging any exceptions with "PyErr_WriteUnraisable()").

   Example:

      static void
      foo_dealloc(PyObject *self)
      {
          PyObject *exc = PyErr_GetRaisedException();

          if (PyObject_CallFinalizerFromDealloc(self) < 0) {
              // self was resurrected.
              goto done;
          }

          PyTypeObject *tp = Py_TYPE(self);

          if (tp->tp_flags & Py_TPFLAGS_HAVE_GC) {
              PyObject_GC_UnTrack(self);
          }

          // Optional, but convenient to avoid code duplication.
          if (tp->tp_clear && tp->tp_clear(self) < 0) {
              PyErr_WriteUnraisable(self);
          }

          // Any additional destruction goes here.

          tp->tp_free(self);
          self = NULL;  // In case PyErr_WriteUnraisable() is called below.

          if (tp->tp_flags & Py_TPFLAGS_HEAPTYPE) {
              Py_CLEAR(tp);
          }

      done:
          // Optional, if something was called that might have raised an
          // exception.
          if (PyErr_Occurred()) {
              PyErr_WriteUnraisable(self);
          }
          PyErr_SetRaisedException(exc);
      }

   "tp_dealloc" may be called from any Python thread, not just the
   thread which created the object (if the object becomes part of a
   refcount cycle, that cycle might be collected by a garbage
   collection on any thread).  This is not a problem for Python API
   calls, since the thread on which "tp_dealloc" is called with an
   *attached thread state*.  However, if the object being destroyed in
   turn destroys objects from some other C library, care should be
   taken to ensure that destroying those objects on the thread which
   called "tp_dealloc" will not violate any assumptions of the
   library.

   **Herencia:**

   Este campo es heredado por subtipos.

   Ver también:

     Object Life Cycle for details about how this slot relates to
     other slots.

Py_ssize_t PyTypeObject.tp_vectorcall_offset

   Un desplazamiento opcional a una función por instancia que
   implementa la llamada al objeto usando vectorcall protocol, una
   alternativa más eficiente del simple "tp_call".

   This field is only used if the flag "Py_TPFLAGS_HAVE_VECTORCALL" is
   set. If so, this must be a positive integer containing the offset
   in the instance of a "vectorcallfunc" pointer.

   The *vectorcallfunc* pointer may be "NULL", in which case the
   instance behaves as if "Py_TPFLAGS_HAVE_VECTORCALL" was not set:
   calling the instance falls back to "tp_call".

   Cualquier clase que establezca "_Py_TPFLAGS_HAVE_VECTORCALL"
   también debe establecer "tp_call" y asegurarse de que su
   comportamiento sea coherente con la función *vectorcallfunc*. Esto
   se puede hacer configurando *tp_call* en "PyVectorcall_Call()".

   Distinto en la versión 3.8: Antes de la versión 3.8, este slot se
   llamaba "tp_print". En Python 2.x, se usó para imprimir en un
   archivo. En Python 3.0 a 3.7, no se usó.

   Distinto en la versión 3.12: Before version 3.12, it was not
   recommended for mutable heap types to implement the vectorcall
   protocol. When a user sets "__call__" in Python code, only
   *tp_call* is updated, likely making it inconsistent with the
   vectorcall function. Since 3.12, setting "__call__" will disable
   vectorcall optimization by clearing the
   "Py_TPFLAGS_HAVE_VECTORCALL" flag.

   **Herencia:**

   This field is always inherited. However, the
   "Py_TPFLAGS_HAVE_VECTORCALL" flag is not always inherited. If it's
   not set, then the subclass won't use vectorcall, except when
   "PyVectorcall_Call()" is explicitly called.

getattrfunc PyTypeObject.tp_getattr

   * The corresponding slot ID "Py_tp_getattr" is part of the Stable
   ABI.*

   Un puntero opcional a la función "obtener atributo cadena de
   caracteres" (*get-attribute-string*).

   Este campo está en desuso. Cuando se define, debe apuntar a una
   función que actúe igual que la función "tp_getattro", pero tomando
   una cadena de caracteres C en lugar de un objeto de cadena Python
   para dar el nombre del atributo.

   **Herencia:**

   Group: "tp_getattr", "tp_getattro"

   Este campo es heredado por los subtipos junto con "tp_getattro": un
   subtipo hereda ambos "tp_getattr" y "tp_getattro" de su base
   escriba cuando los subtipos "tp_getattr" y "tp_getattro" son ambos
   "NULL".

setattrfunc PyTypeObject.tp_setattr

   * The corresponding slot ID "Py_tp_setattr" is part of the Stable
   ABI.*

   Un puntero opcional a la función para configurar y eliminar
   atributos.

   Este campo está en desuso. Cuando se define, debe apuntar a una
   función que actúe igual que la función "tp_setattro", pero tomando
   una cadena de caracteres C en lugar de un objeto de cadena Python
   para dar el nombre del atributo.

   **Herencia:**

   Group: "tp_setattr", "tp_setattro"

   Este campo es heredado por los subtipos junto con "tp_setattro": un
   subtipo hereda ambos "tp_setattr" y "tp_setattro" de su base
   escriba cuando los subtipos "tp_setattr" y "tp_setattro" son ambos
   "NULL".

PyAsyncMethods *PyTypeObject.tp_as_async

   Puntero a una estructura adicional que contiene campos relevantes
   solo para los objetos que implementan los protocolos "esperable"
   (*awaitable*) y "iterador asíncrono" (*asynchronous iterator*) en
   el nivel C. Ver Estructuras de objetos asíncronos para más
   detalles.

   Added in version 3.5: Anteriormente conocidos como "tp_compare" y
   "tp_reserved".

   **Herencia:**

   El campo "tp_as_async" no se hereda, pero los campos contenidos se
   heredan individualmente.

reprfunc PyTypeObject.tp_repr

   * The corresponding slot ID "Py_tp_repr" is part of the Stable
   ABI.*

   Un puntero opcional a una función que implementa la función
   incorporada "repr()".

   La firma es la misma que para "PyObject_Repr()":

      PyObject *tp_repr(PyObject *self);

   La función debe retornar una cadena de caracteres o un objeto
   Unicode. Idealmente, esta función debería retornar una cadena que,
   cuando se pasa a "eval()", dado un entorno adecuado, retorna un
   objeto con el mismo valor. Si esto no es factible, debe retornar
   una cadena que comience con "'<'" y termine con "'>'" desde la cual
   se puede deducir tanto el tipo como el valor del objeto.

   **Herencia:**

   Este campo es heredado por subtipos.

   **Por defecto:**

   Cuando este campo no está configurado, se retorna una cadena de
   caracteres de la forma "<%s object at %p>", donde "%s" se reemplaza
   por el nombre del tipo y "%p" por dirección de memoria del objeto.

PyNumberMethods *PyTypeObject.tp_as_number

   Puntero a una estructura adicional que contiene campos relevantes
   solo para objetos que implementan el protocolo numérico. Estos
   campos están documentados en Estructuras de objetos de números.

   **Herencia:**

   El campo "tp_as_number" no se hereda, pero los campos contenidos se
   heredan individualmente.

PySequenceMethods *PyTypeObject.tp_as_sequence

   Puntero a una estructura adicional que contiene campos relevantes
   solo para objetos que implementan el protocolo de secuencia. Estos
   campos están documentados en estructuras de secuencia.

   **Herencia:**

   El campo "tp_as_sequence" no se hereda, pero los campos contenidos
   se heredan individualmente.

PyMappingMethods *PyTypeObject.tp_as_mapping

   Puntero a una estructura adicional que contiene campos relevantes
   solo para objetos que implementan el protocolo de mapeo. Estos
   campos están documentados en Estructuras de objetos mapeo.

   **Herencia:**

   El campo "tp_as_mapping" no se hereda, pero los campos contenidos
   se heredan individualmente.

hashfunc PyTypeObject.tp_hash

   * The corresponding slot ID "Py_tp_hash" is part of the Stable
   ABI.*

   Un puntero opcional a una función que implementa la función
   incorporada "hash()".

   La firma es la misma que para "PyObject_Hash()":

      Py_hash_t tp_hash(PyObject *);

   El valor "-1" no debe retornarse como un valor de retorno normal;
   Cuando se produce un error durante el cálculo del valor *hash*, la
   función debe establecer una excepción y retornar "-1".

   When this field is not set (*and* "tp_richcompare" is not set), an
   attempt to take the hash of the object raises "TypeError". This is
   the same as setting it to "PyObject_HashNotImplemented()".

   Este campo se puede establecer explícitamente en
   "PyObject_HashNotImplemented()" para bloquear la herencia del
   método *hash* de un tipo primario. Esto se interpreta como el
   equivalente de "__hash__ = None" en el nivel de Python, lo que hace
   que "isinstance(o, collections.Hashable)" retorne correctamente
   "False". Tenga en cuenta que lo contrario también es cierto:
   establecer "__hash__ = None" en una clase en el nivel de Python
   dará como resultado que la ranura "tp_hash" se establezca en
   "PyObject_HashNotImplemented()".

   **Herencia:**

   Group: "tp_hash", "tp_richcompare"

   Este campo es heredado por subtipos junto con "tp_richcompare": un
   subtipo hereda ambos "tp_richcompare" y "tp_hash", cuando los
   subtipos "tp_richcompare" y "tp_hash" son ambos "NULL".

   **Por defecto:**

   "PyBaseObject_Type" uses "PyObject_GenericHash()".

ternaryfunc PyTypeObject.tp_call

   * The corresponding slot ID "Py_tp_call" is part of the Stable
   ABI.*

   Un puntero opcional a una función que implementa la llamada al
   objeto. Esto debería ser "NULL" si el objeto no es invocable. La
   firma es la misma que para "PyObject_Call()":

      PyObject *tp_call(PyObject *self, PyObject *args, PyObject *kwargs);

   **Herencia:**

   Este campo es heredado por subtipos.

reprfunc PyTypeObject.tp_str

   * The corresponding slot ID "Py_tp_str" is part of the Stable ABI.*

   Un puntero opcional a una función que implementa la operación
   integrada "str()". (Tenga en cuenta que "str" es un tipo ahora, y
   "str()" llama al constructor para ese tipo. Este constructor llama
   a "PyObject_Str()" para hacer el trabajo real, y "PyObject_Str()"
   llamará a este controlador.)

   La firma es la misma que para "PyObject_Str()":

      PyObject *tp_str(PyObject *self);

   La función debe retornar una cadena de caracteres o un objeto
   Unicode. Debe ser una representación de cadena "amigable" del
   objeto, ya que esta es la representación que será utilizada, entre
   otras cosas, por la función "print()".

   **Herencia:**

   Este campo es heredado por subtipos.

   **Por defecto:**

   Cuando este campo no está configurado, se llama a "PyObject_Repr()"
   para retornar una representación de cadena de caracteres.

getattrofunc PyTypeObject.tp_getattro

   * The corresponding slot ID "Py_tp_getattro" is part of the Stable
   ABI.*

   Un puntero opcional a la función "obtener atributo" (*get-
   attribute*).

   La firma es la misma que para "PyObject_GetAttr()":

      PyObject *tp_getattro(PyObject *self, PyObject *attr);

   Por lo general, es conveniente establecer este campo en
   "PyObject_GenericGetAttr()", que implementa la forma normal de
   buscar atributos de objeto.

   **Herencia:**

   Group: "tp_getattr", "tp_getattro"

   Este campo es heredado por los subtipos junto con "tp_getattr": un
   subtipo hereda ambos "tp_getattr" y "tp_getattro" de su base
   escriba cuando los subtipos "tp_getattr" y "tp_getattro" son ambos
   "NULL".

   **Por defecto:**

   "PyBaseObject_Type" uses "PyObject_GenericGetAttr()".

setattrofunc PyTypeObject.tp_setattro

   * The corresponding slot ID "Py_tp_setattro" is part of the Stable
   ABI.*

   Un puntero opcional a la función para configurar y eliminar
   atributos.

   La firma es la misma que para "PyObject_SetAttr()":

      int tp_setattro(PyObject *self, PyObject *attr, PyObject *value);

   Además, se debe admitir la configuración de *value* en "NULL" para
   eliminar un atributo. Por lo general, es conveniente establecer
   este campo en "PyObject_GenericSetAttr()", que implementa la forma
   normal de establecer los atributos del objeto.

   **Herencia:**

   Group: "tp_setattr", "tp_setattro"

   Los subtipos heredan este campo junto con "tp_setattr": un subtipo
   hereda ambos "tp_setattr" y "tp_setattro" de su base escriba cuando
   los subtipos "tp_setattr" y "tp_setattro" son ambos "NULL".

   **Por defecto:**

   "PyBaseObject_Type" uses "PyObject_GenericSetAttr()".

PyBufferProcs *PyTypeObject.tp_as_buffer

   Puntero a una estructura adicional que contiene campos relevantes
   solo para objetos que implementan la interfaz del búfer. Estos
   campos están documentados en Estructuras de objetos búfer.

   **Herencia:**

   El campo "tp_as_buffer" no se hereda, pero los campos contenidos se
   heredan individualmente.

unsigned long PyTypeObject.tp_flags

   Este campo es una máscara de bits de varias banderas. Algunas
   banderas indican semántica variante para ciertas situaciones; otros
   se utilizan para indicar que ciertos campos en el tipo de objeto (o
   en las estructuras de extensión a las que se hace referencia a
   través de "tp_as_number", "tp_as_sequence", "tp_as_mapping", y
   "tp_as_buffer") que históricamente no siempre estuvieron presentes
   son válidos; si dicho bit de bandera está claro, no se debe acceder
   a los campos de tipo que protege y se debe considerar que tienen un
   valor cero o "NULL".

   **Herencia:**

   Inheritance of this field is complicated.  Most flag bits are
   inherited individually, i.e. if the base type has a flag bit set,
   the subtype inherits this flag bit.  The flag bits that pertain to
   extension structures are strictly inherited if the extension
   structure is inherited, i.e. the base type's value of the flag bit
   is copied into the subtype together with a pointer to the extension
   structure.  The "Py_TPFLAGS_HAVE_GC" flag bit is inherited together
   with the "tp_traverse" and "tp_clear" fields, i.e. if the
   "Py_TPFLAGS_HAVE_GC" flag bit is clear in the subtype and the
   "tp_traverse" and "tp_clear" fields in the subtype exist and have
   "NULL" values.

   **Por defecto:**

   "PyBaseObject_Type" uses "Py_TPFLAGS_DEFAULT |
   Py_TPFLAGS_BASETYPE".

   **Máscaras de bits:**

   Las siguientes máscaras de bits están definidas actualmente; estos
   se pueden unidos por *OR* usando el operador "|" para formar el
   valor del campo "tp_flags". El macro "PyType_HasFeature()" toma un
   tipo y un valor de banderas, *tp* y *f*, y comprueba si
   "tp->tp_flags & f" no es cero.

   Py_TPFLAGS_HEAPTYPE

      This bit is set when the type object itself is allocated on the
      heap, for example, types created dynamically using
      "PyType_FromSpec()".  In this case, the "ob_type" field of its
      instances is considered a reference to the type, and the type
      object is INCREF'ed when a new instance is created, and
      DECREF'ed when an instance is destroyed (this does not apply to
      instances of subtypes; only the type referenced by the
      instance's ob_type gets INCREF'ed or DECREF'ed). Heap types
      should also support garbage collection as they can form a
      reference cycle with their own module object.

      **Herencia:**

      ???

   Py_TPFLAGS_BASETYPE
       * Part of the Stable ABI.*

      Este bit se establece cuando el tipo se puede usar como el tipo
      base de otro tipo. Si este bit es claro, el tipo no puede
      subtiparse (similar a una clase "final" en Java).

      **Herencia:**

      ???

   Py_TPFLAGS_READY

      Este bit se establece cuando el objeto tipo ha sido
      completamente inicializado por "PyType_Ready()".

      **Herencia:**

      ???

   Py_TPFLAGS_READYING

      Este bit se establece mientras "PyType_Ready()" está en el
      proceso de inicialización del objeto tipo.

      **Herencia:**

      ???

   Py_TPFLAGS_HAVE_GC
       * Part of the Stable ABI.*

      This bit is set when the object supports garbage collection.  If
      this bit is set, memory for new instances (see "tp_alloc") must
      be allocated using "PyObject_GC_New" or "PyType_GenericAlloc()"
      and deallocated (see "tp_free") using "PyObject_GC_Del()".  More
      information in section Apoyo a la recolección de basura cíclica.

      **Herencia:**

      Group: "Py_TPFLAGS_HAVE_GC", "tp_traverse", "tp_clear"

      The "Py_TPFLAGS_HAVE_GC" flag bit is inherited together with the
      "tp_traverse" and "tp_clear" fields, i.e.  if the
      "Py_TPFLAGS_HAVE_GC" flag bit is clear in the subtype and the
      "tp_traverse" and "tp_clear" fields in the subtype exist and
      have "NULL" values.

   Py_TPFLAGS_DEFAULT
       * Part of the Stable ABI.*

      This is a bitmask of all the bits that pertain to the existence
      of certain fields in the type object and its extension
      structures. Currently, it includes the following bits:
      "Py_TPFLAGS_HAVE_STACKLESS_EXTENSION".

      **Herencia:**

      ???

   Py_TPFLAGS_METHOD_DESCRIPTOR
       * Part of the Stable ABI since version 3.8.*

      Este bit indica que los objetos se comportan como métodos
      independientes.

      Si este indicador está configurado para "type(meth)", entonces:

      * "meth.__get__(obj, cls)(*args, **kwds)" (con "obj" no "None")
        debe ser equivalente a "meth(obj, *args, **kwds)".

      * "meth.__get__(None, cls)(*args, **kwds)" debe ser equivalente
        a "meth(*args, **kwds)".

      Este indicador (*flag*) permite una optimización para llamadas a
      métodos típicos como "obj.meth()": evita crear un objeto
      temporal de "método vinculado" para "obj.meth".

      Added in version 3.8.

      **Herencia:**

      This flag is never inherited by types without the
      "Py_TPFLAGS_IMMUTABLETYPE" flag set.  For extension types, it is
      inherited whenever "tp_descr_get" is inherited.

   Py_TPFLAGS_MANAGED_DICT

      This bit indicates that instances of the class have a "__dict__"
      attribute, and that the space for the dictionary is managed by
      the VM.

      If this flag is set, "Py_TPFLAGS_HAVE_GC" should also be set.

      The type traverse function must call
      "PyObject_VisitManagedDict()" and its clear function must call
      "PyObject_ClearManagedDict()".

      Added in version 3.12.

      **Herencia:**

      This flag is inherited unless the "tp_dictoffset" field is set
      in a superclass.

   Py_TPFLAGS_MANAGED_WEAKREF

      This bit indicates that instances of the class should be weakly
      referenceable.

      Added in version 3.12.

      **Herencia:**

      This flag is inherited unless the "tp_weaklistoffset" field is
      set in a superclass.

   Py_TPFLAGS_ITEMS_AT_END
       * Part of the Stable ABI since version 3.12.*

      Only usable with variable-size types, i.e. ones with non-zero
      "tp_itemsize".

      Indicates that the variable-sized portion of an instance of this
      type is at the end of the instance's memory area, at an offset
      of "Py_TYPE(obj)->tp_basicsize" (which may be different in each
      subclass).

      When setting this flag, be sure that all superclasses either use
      this memory layout, or are not variable-sized. Python does not
      check this.

      Added in version 3.12.

      **Herencia:**

      This flag is inherited.

   Py_TPFLAGS_LONG_SUBCLASS

   Py_TPFLAGS_LIST_SUBCLASS

   Py_TPFLAGS_TUPLE_SUBCLASS

   Py_TPFLAGS_BYTES_SUBCLASS

   Py_TPFLAGS_UNICODE_SUBCLASS

   Py_TPFLAGS_DICT_SUBCLASS

   Py_TPFLAGS_BASE_EXC_SUBCLASS

   Py_TPFLAGS_TYPE_SUBCLASS

      Functions such as "PyLong_Check()" will call
      "PyType_FastSubclass()" with one of these flags to quickly
      determine if a type is a subclass of a built-in type; such
      specific checks are faster than a generic check, like
      "PyObject_IsInstance()". Custom types that inherit from built-
      ins should have their "tp_flags" set appropriately, or the code
      that interacts with such types will behave differently depending
      on what kind of check is used.

   Py_TPFLAGS_HAVE_FINALIZE

      Este bit se establece cuando la ranura "tp_finalize" está
      presente en la estructura de tipo.

      Added in version 3.4.

      Obsoleto desde la versión 3.8: Este indicador ya no es
      necesario, ya que el intérprete asume que: el espacio
      "tp_finalize" siempre está presente en la estructura de tipos.

   Py_TPFLAGS_HAVE_VECTORCALL
       * Part of the Stable ABI since version 3.12.*

      Este bit se establece cuando la clase implementa protocolo
      vectorcall. Consulte "tp_vectorcall_offset" para obtener más
      detalles.

      **Herencia:**

      This bit is inherited if "tp_call" is also inherited.

      Added in version 3.8: as "_Py_TPFLAGS_HAVE_VECTORCALL"

      Distinto en la versión 3.9: Renamed to the current name, without
      the leading underscore. The old provisional name is *soft
      deprecated*.

      Distinto en la versión 3.12: This flag is now removed from a
      class when the class's "__call__()" method is reassigned.This
      flag can now be inherited by mutable classes.

   Py_TPFLAGS_IMMUTABLETYPE

      Este bit se establece para objetos de tipo que son inmutables:
      los atributos de tipo no se pueden establecer ni eliminar.

      "PyType_Ready()" aplica automáticamente este indicador a static
      types.

      **Herencia:**

      Este flag no se hereda.

      Added in version 3.10.

   Py_TPFLAGS_DISALLOW_INSTANTIATION

      No permita la creación de instancias del tipo: establezca
      "tp_new" en NULL y no cree la clave "__new__" en el diccionario
      de tipos.

      La bandera debe establecerse antes de crear el tipo, no después.
      Por ejemplo, debe establecerse antes de que se llame a
      "PyType_Ready()" en el tipo.

      La bandera se establece automáticamente en static types si
      "tp_base" es NULL o "&PyBaseObject_Type" y "tp_new" es NULL.

      **Herencia:**

      This flag is not inherited. However, subclasses will not be
      instantiable unless they provide a non-NULL "tp_new" (which is
      only possible via the C API).

      Nota:

        To disallow instantiating a class directly but allow
        instantiating its subclasses (e.g. for an *abstract base
        class*), do not use this flag. Instead, make "tp_new" only
        succeed for subclasses.

      Added in version 3.10.

   Py_TPFLAGS_MAPPING

      Este bit indica que las instancias de la clase pueden coincidir
      con los patrones de correspondencia cuando se utilizan como
      sujeto de un bloque "match". Se configura automáticamente al
      registrar o subclasificar "collections.abc.Mapping", y se
      desarma al registrar "collections.abc.Sequence".

      Nota:

        "Py_TPFLAGS_MAPPING" and "Py_TPFLAGS_SEQUENCE" are mutually
        exclusive; it is an error to enable both flags simultaneously.

      **Herencia:**

      This flag is inherited by types that do not already set
      "Py_TPFLAGS_SEQUENCE".

      Ver también:

        **PEP 634** - Coincidencia de patrones estructurales:
        especificación

      Added in version 3.10.

   Py_TPFLAGS_SEQUENCE

      Este bit indica que las instancias de la clase pueden coincidir
      con los patrones de secuencia cuando se utilizan como sujeto de
      un bloque "match". Se configura automáticamente al registrar o
      subclasificar "collections.abc.Sequence", y se desarma al
      registrar "collections.abc.Mapping".

      Nota:

        "Py_TPFLAGS_MAPPING" and "Py_TPFLAGS_SEQUENCE" are mutually
        exclusive; it is an error to enable both flags simultaneously.

      **Herencia:**

      This flag is inherited by types that do not already set
      "Py_TPFLAGS_MAPPING".

      Ver también:

        **PEP 634** - Coincidencia de patrones estructurales:
        especificación

      Added in version 3.10.

   Py_TPFLAGS_VALID_VERSION_TAG

      Internal. Do not set or unset this flag. To indicate that a
      class has changed call "PyType_Modified()"

      Advertencia:

        This flag is present in header files, but is not be used. It
        will be removed in a future version of CPython

   Py_TPFLAGS_HAVE_VERSION_TAG

      This macro does nothing. Historically, this would indicate that
      the "tp_version_tag" field was available and initialized.

      Soft deprecated since version 3.13.

   Py_TPFLAGS_INLINE_VALUES

      This bit indicates that instances of this type will have an
      "inline values" array (containing the object's attributes)
      placed directly after the end of the object.

      This requires that "Py_TPFLAGS_HAVE_GC" is set.

      **Herencia:**

      Este flag no se hereda.

      Added in version 3.13.

   Py_TPFLAGS_IS_ABSTRACT

      This bit indicates that this is an abstract type and therefore
      cannot be instantiated.

      **Herencia:**

      Este flag no se hereda.

      Ver también: "abc"

   Py_TPFLAGS_HAVE_STACKLESS_EXTENSION

      Internal. Do not set or unset this flag. Historically, this was
      a reserved flag for use in Stackless Python.

      Advertencia:

        This flag is present in header files, but is not be used. This
        may be removed in a future version of CPython.

const char *PyTypeObject.tp_doc

   * The corresponding slot ID "Py_tp_doc" is part of the Stable ABI.*

   An optional pointer to a NUL-terminated C string giving the
   docstring for this type object.  This is exposed as the "__doc__"
   attribute on the type and instances of the type.

   **Herencia:**

   Este campo es *no* heredado por los subtipos.

traverseproc PyTypeObject.tp_traverse

   * The corresponding slot ID "Py_tp_traverse" is part of the Stable
   ABI.*

   An optional pointer to a traversal function for the garbage
   collector.  This is only used if the "Py_TPFLAGS_HAVE_GC" flag bit
   is set.  The signature is:

      int tp_traverse(PyObject *self, visitproc visit, void *arg);

   Se puede encontrar más información sobre el esquema de recolección
   de basura de Python en la sección Apoyo a la recolección de basura
   cíclica.

   The "tp_traverse" pointer is used by the garbage collector to
   detect reference cycles. A typical implementation of a
   "tp_traverse" function simply calls "Py_VISIT()" on each of the
   instance's members that are Python objects that the instance owns.
   For example, this is function "local_traverse()" from the "_thread"
   extension module:

      static int
      local_traverse(PyObject *op, visitproc visit, void *arg)
      {
          localobject *self = (localobject *) op;
          Py_VISIT(self->args);
          Py_VISIT(self->kw);
          Py_VISIT(self->dict);
          return 0;
      }

   Tenga en cuenta que "Py_VISIT()" solo se llama a aquellos miembros
   que pueden participar en los ciclos de referencia. Aunque también
   hay un miembro "self->key", solo puede ser "NULL" o una cadena de
   caracteres de Python y, por lo tanto, no puede ser parte de un
   ciclo de referencia.

   Por otro lado, incluso si sabe que un miembro nunca puede ser parte
   de un ciclo, como ayuda para la depuración puede visitarlo de todos
   modos solo para que la función "get_referents()" del módulo "gc" lo
   incluirá.

   Heap types ("Py_TPFLAGS_HEAPTYPE") must visit their type with:

      Py_VISIT(Py_TYPE(self));

   It is only needed since Python 3.9. To support Python 3.8 and
   older, this line must be conditional:

      #if PY_VERSION_HEX >= 0x03090000
          Py_VISIT(Py_TYPE(self));
      #endif

   If the "Py_TPFLAGS_MANAGED_DICT" bit is set in the "tp_flags"
   field, the traverse function must call
   "PyObject_VisitManagedDict()" like this:

      PyObject_VisitManagedDict((PyObject*)self, visit, arg);

   Advertencia:

     Al implementar "tp_traverse", solo se deben visitar los miembros
     que tienen la instancia *owns* (por tener *referencias fuertes*).
     Por ejemplo, si un objeto admite referencias débiles a través de
     la ranura "tp_weaklist", el puntero que respalda la lista
     vinculada (a lo que apunta *tp_weaklist*) **no** debe visitarse
     ya que la instancia no posee directamente las referencias débiles
     a sí misma (la lista de referencias débiles está ahí para
     respaldar la maquinaria de referencia débil, pero la instancia no
     tiene una fuerte referencia a los elementos dentro de ella, ya
     que pueden eliminarse incluso si la instancia todavía está viva).

   Advertencia:

     The traversal function must not have any side effects.  It must
     not modify the reference counts of any Python objects nor create
     or destroy any Python objects.

   Note that "Py_VISIT()" requires the *visit* and *arg* parameters to
   "local_traverse()" to have these specific names; don't name them
   just anything.

   Las instancias de heap-allocated types contienen una referencia a
   su tipo. Por lo tanto, su función transversal debe visitar
   "Py_TYPE(self)" o delegar esta responsabilidad llamando a
   "tp_traverse" de otro tipo asignado al heap (como una superclase
   asignada al heap). Si no es así, es posible que el objeto de tipo
   no se recolecte como basura.

   Nota:

     The "tp_traverse" function can be called from any thread.

   Distinto en la versión 3.9: Se espera que los tipos asignados al
   heap visiten "Py_TYPE(self)" en "tp_traverse". En versiones
   anteriores de Python, debido al bug 40217, hacer esto puede
   provocar fallas en las subclases.

   **Herencia:**

   Group: "Py_TPFLAGS_HAVE_GC", "tp_traverse", "tp_clear"

   This field is inherited by subtypes together with "tp_clear" and
   the "Py_TPFLAGS_HAVE_GC" flag bit: the flag bit, "tp_traverse", and
   "tp_clear" are all inherited from the base type if they are all
   zero in the subtype.

inquiry PyTypeObject.tp_clear

   * The corresponding slot ID "Py_tp_clear" is part of the Stable
   ABI.*

   An optional pointer to a clear function.  The signature is:

      int tp_clear(PyObject *);

   The purpose of this function is to break reference cycles that are
   causing a *cyclic isolate* so that the objects can be safely
   destroyed.  A cleared object is a partially destroyed object; the
   object is not obligated to satisfy design invariants held during
   normal use.

   "tp_clear" does not need to delete references to objects that can't
   participate in reference cycles, such as Python strings or Python
   integers.  However, it may be convenient to clear all references,
   and write the type's "tp_dealloc" function to invoke "tp_clear" to
   avoid code duplication.  (Beware that "tp_clear" might have already
   been called. Prefer calling idempotent functions like
   "Py_CLEAR()".)

   Any non-trivial cleanup should be performed in "tp_finalize"
   instead of "tp_clear".

   Nota:

     If "tp_clear" fails to break a reference cycle then the objects
     in the *cyclic isolate* may remain indefinitely uncollectable
     ("leak").  See "gc.garbage".

   Nota:

     Referents (direct and indirect) might have already been cleared;
     they are not guaranteed to be in a consistent state.

   Nota:

     The "tp_clear" function can be called from any thread.

   Nota:

     An object is not guaranteed to be automatically cleared before
     its destructor ("tp_dealloc") is called.

   This function differs from the destructor ("tp_dealloc") in the
   following ways:

   * The purpose of clearing an object is to remove references to
     other objects that might participate in a reference cycle.  The
     purpose of the destructor, on the other hand, is a superset: it
     must release *all* resources it owns, including references to
     objects that cannot participate in a reference cycle (e.g.,
     integers) as well as the object's own memory (by calling
     "tp_free").

   * When "tp_clear" is called, other objects might still hold
     references to the object being cleared.  Because of this,
     "tp_clear" must not deallocate the object's own memory
     ("tp_free").  The destructor, on the other hand, is only called
     when no (strong) references exist, and as such, must safely
     destroy the object itself by deallocating it.

   * "tp_clear" might never be automatically called.  An object's
     destructor, on the other hand, will be automatically called some
     time after the object becomes unreachable (i.e., either there are
     no references to the object or the object is a member of a
     *cyclic isolate*).

   No guarantees are made about when, if, or how often Python
   automatically clears an object, except:

   * Python will not automatically clear an object if it is reachable,
     i.e., there is a reference to it and it is not a member of a
     *cyclic isolate*.

   * Python will not automatically clear an object if it has not been
     automatically finalized (see "tp_finalize").  (If the finalizer
     resurrected the object, the object may or may not be
     automatically finalized again before it is cleared.)

   * If an object is a member of a *cyclic isolate*, Python will not
     automatically clear it if any member of the cyclic isolate has
     not yet been automatically finalized ("tp_finalize").

   * Python will not destroy an object until after any automatic calls
     to its "tp_clear" function have returned.  This ensures that the
     act of breaking a reference cycle does not invalidate the "self"
     pointer while "tp_clear" is still executing.

   * Python will not automatically call "tp_clear" multiple times
     concurrently.

   CPython currently only automatically clears objects as needed to
   break reference cycles in a *cyclic isolate*, but future versions
   might clear objects regularly before their destruction.

   Taken together, all "tp_clear" functions in the system must combine
   to break all reference cycles.  This is subtle, and if in any doubt
   supply a "tp_clear" function.  For example, the tuple type does not
   implement a "tp_clear" function, because it's possible to prove
   that no reference cycle can be composed entirely of tuples.
   Therefore the "tp_clear" functions of other types are responsible
   for breaking any cycle containing a tuple.  This isn't immediately
   obvious, and there's rarely a good reason to avoid implementing
   "tp_clear".

   Las implementaciones de "tp_clear" deberían descartar las
   referencias de la instancia a las de sus miembros que pueden ser
   objetos de Python, y establecer sus punteros a esos miembros en
   "NULL", como en el siguiente ejemplo:

      static int
      local_clear(PyObject *op)
      {
          localobject *self = (localobject *) op;
          Py_CLEAR(self->key);
          Py_CLEAR(self->args);
          Py_CLEAR(self->kw);
          Py_CLEAR(self->dict);
          return 0;
      }

   The "Py_CLEAR()" macro should be used, because clearing references
   is delicate:  the reference to the contained object must not be
   released (via "Py_DECREF()") until after the pointer to the
   contained object is set to "NULL".  This is because releasing the
   reference may cause the contained object to become trash,
   triggering a chain of reclamation activity that may include
   invoking arbitrary Python code (due to finalizers, or weakref
   callbacks, associated with the contained object). If it's possible
   for such code to reference *self* again, it's important that the
   pointer to the contained object be "NULL" at that time, so that
   *self* knows the contained object can no longer be used.  The
   "Py_CLEAR()" macro performs the operations in a safe order.

   If the "Py_TPFLAGS_MANAGED_DICT" bit is set in the "tp_flags"
   field, the clear function must call "PyObject_ClearManagedDict()"
   like this:

      PyObject_ClearManagedDict((PyObject*)self);

   Se puede encontrar más información sobre el esquema de recolección
   de basura de Python en la sección Apoyo a la recolección de basura
   cíclica.

   **Herencia:**

   Group: "Py_TPFLAGS_HAVE_GC", "tp_traverse", "tp_clear"

   This field is inherited by subtypes together with "tp_traverse" and
   the "Py_TPFLAGS_HAVE_GC" flag bit: the flag bit, "tp_traverse", and
   "tp_clear" are all inherited from the base type if they are all
   zero in the subtype.

   Ver también:

     Object Life Cycle for details about how this slot relates to
     other slots.

richcmpfunc PyTypeObject.tp_richcompare

   * The corresponding slot ID "Py_tp_richcompare" is part of the
   Stable ABI.*

   Un puntero opcional a la función de comparación enriquecida, cuya
   firma es:

      PyObject *tp_richcompare(PyObject *self, PyObject *other, int op);

   Se garantiza que el primer parámetro será una instancia del tipo
   definido por "PyTypeObject".

   La función debería retornar el resultado de la comparación
   (generalmente "Py_True" o "Py_False"). Si la comparación no está
   definida, debe retornar "Py_NotImplemented", si se produce otro
   error, debe retornar "NULL" y establecer una condición de
   excepción.

   Las siguientes constantes se definen para ser utilizadas como el
   tercer argumento para "tp_richcompare" y para
   "PyObject_RichCompare()":

   +----------------------+--------------+
   | Constante            | Comparación  |
   |======================|==============|
   | Py_LT                | "<"          |
   +----------------------+--------------+
   | Py_LE                | "<="         |
   +----------------------+--------------+
   | Py_EQ                | "=="         |
   +----------------------+--------------+
   | Py_NE                | "!="         |
   +----------------------+--------------+
   | Py_GT                | ">"          |
   +----------------------+--------------+
   | Py_GE                | ">="         |
   +----------------------+--------------+

   El siguiente macro está definido para facilitar la escritura de
   funciones de comparación enriquecidas:

   Py_RETURN_RICHCOMPARE(VAL_A, VAL_B, op)

      Retorna "Py_True" o "Py_False" de la función, según el resultado
      de una comparación. "VAL_A" y "VAL_B" deben ser ordenados por
      operadores de comparación C (por ejemplo, pueden ser enteros o
      punto flotantes de C). El tercer argumento especifica la
      operación solicitada, como por ejemplo "PyObject_RichCompare()".

      The returned value is a new *strong reference*.

      En caso de error, establece una excepción y retorna "NULL" de la
      función.

      Added in version 3.7.

   **Herencia:**

   Group: "tp_hash", "tp_richcompare"

   Este campo es heredado por subtipos junto con "tp_hash": un subtipo
   hereda "tp_richcompare" y "tp_hash" cuando el subtipo
   "tp_richcompare" y "tp_hash" son ambos "NULL".

   **Por defecto:**

   "PyBaseObject_Type" provides a "tp_richcompare" implementation,
   which may be inherited.  However, if only "tp_hash" is defined, not
   even the inherited function is used and instances of the type will
   not be able to participate in any comparisons.

Py_ssize_t PyTypeObject.tp_weaklistoffset

   While this field is still supported, "Py_TPFLAGS_MANAGED_WEAKREF"
   should be used instead, if at all possible.

   If the instances of this type are weakly referenceable, this field
   is greater than zero and contains the offset in the instance
   structure of the weak reference list head (ignoring the GC header,
   if present); this offset is used by "PyObject_ClearWeakRefs()" and
   the "PyWeakref_*" functions.  The instance structure needs to
   include a field of type PyObject* which is initialized to "NULL".

   No confunda este campo con "tp_weaklist"; ese es el encabezado de
   la lista para referencias débiles al objeto de tipo en sí.

   It is an error to set both the "Py_TPFLAGS_MANAGED_WEAKREF" bit and
   "tp_weaklistoffset".

   **Herencia:**

   Este campo es heredado por subtipos, pero consulte las reglas que
   se enumeran a continuación. Un subtipo puede anular este
   desplazamiento; Esto significa que el subtipo utiliza un encabezado
   de lista de referencia débil diferente que el tipo base. Dado que
   el encabezado de la lista siempre se encuentra a través de
   "tp_weaklistoffset", esto no debería ser un problema.

   **Por defecto:**

   If the "Py_TPFLAGS_MANAGED_WEAKREF" bit is set in the "tp_flags"
   field, then "tp_weaklistoffset" will be set to a negative value, to
   indicate that it is unsafe to use this field.

getiterfunc PyTypeObject.tp_iter

   * The corresponding slot ID "Py_tp_iter" is part of the Stable
   ABI.*

   An optional pointer to a function that returns an *iterator* for
   the object.  Its presence normally signals that the instances of
   this type are *iterable* (although sequences may be iterable
   without this function).

   Esta función tiene la misma firma que "PyObject_GetIter()":

      PyObject *tp_iter(PyObject *self);

   **Herencia:**

   Este campo es heredado por subtipos.

iternextfunc PyTypeObject.tp_iternext

   * The corresponding slot ID "Py_tp_iternext" is part of the Stable
   ABI.*

   An optional pointer to a function that returns the next item in an
   *iterator*. The signature is:

      PyObject *tp_iternext(PyObject *self);

   Cuando el iterador está agotado, debe retornar "NULL"; a la
   excepción "StopIteration" puede o no establecerse. Cuando se
   produce otro error, también debe retornar "NULL". Su presencia
   indica que las instancias de este tipo son iteradores.

   Los tipos de iterador también deberían definir la función
   "tp_iter", y esa función debería retornar la instancia de iterador
   en sí (no una nueva instancia de iterador).

   Esta función tiene la misma firma que "PyIter_Next()".

   **Herencia:**

   Este campo es heredado por subtipos.

struct PyMethodDef *PyTypeObject.tp_methods

   * The corresponding slot ID "Py_tp_methods" is part of the Stable
   ABI.*

   Un puntero opcional a un arreglo estático terminado en "NULL" de
   estructuras "PyMethodDef", declarando métodos regulares de este
   tipo.

   Para cada entrada en el arreglo, se agrega una entrada al
   diccionario del tipo (ver "tp_dict" a continuación) que contiene un
   descriptor *method*.

   **Herencia:**

   Los subtipos no heredan este campo (los métodos se heredan mediante
   un mecanismo diferente).

struct PyMemberDef *PyTypeObject.tp_members

   * The corresponding slot ID "Py_tp_members" is part of the Stable
   ABI.*

   Un puntero opcional a un arreglo estático terminado en "NULL" de
   estructuras "PyMemberDef", declarando miembros de datos regulares
   (campos o ranuras) de instancias de este tipo.

   Para cada entrada en el arreglo, se agrega una entrada al
   diccionario del tipo (ver "tp_dict" a continuación) que contiene un
   descriptor *member*.

   **Herencia:**

   Los subtipos no heredan este campo (los miembros se heredan
   mediante un mecanismo diferente).

struct PyGetSetDef *PyTypeObject.tp_getset

   * The corresponding slot ID "Py_tp_getset" is part of the Stable
   ABI.*

   Un puntero opcional a un arreglo estático terminado en "NULL" de
   estructuras "PyGetSetDef", declarando atributos calculados de
   instancias de este tipo.

   Para cada entrada en el arreglo, se agrega una entrada al
   diccionario del tipo (ver "tp_dict" a continuación) que contiene un
   descriptor *getset*.

   **Herencia:**

   Este campo no es heredado por los subtipos (los atributos
   computados se heredan a través de un mecanismo diferente).

PyTypeObject *PyTypeObject.tp_base

   * The corresponding slot ID "Py_tp_base" is part of the Stable
   ABI.*

   Un puntero opcional a un tipo base del que se heredan las
   propiedades de tipo. En este nivel, solo se admite una herencia
   única; La herencia múltiple requiere la creación dinámica de un
   objeto tipo llamando al metatipo.

   Nota:

     La inicialización de ranuras está sujeta a las reglas de
     inicialización de globales. C99 requiere que los inicializadores
     sean "constantes de dirección". Los designadores de funciones
     como "PyType_GenericNew()", con conversión implícita a un
     puntero, son constantes de dirección C99 válidas.However, the
     unary '&' operator applied to a non-static variable like
     "PyBaseObject_Type" is not required to produce an address
     constant.  Compilers may support this (gcc does), MSVC does not.
     Both compilers are strictly standard conforming in this
     particular behavior.En consecuencia, "tp_base" debe establecerse
     en la función *init* del módulo de extensión.

   **Herencia:**

   Este campo no es heredado por los subtipos (obviamente).

   **Por defecto:**

   Este campo predeterminado es "&PyBaseObject_Type" (que para los
   programadores de Python se conoce como el tipo "objeto").

PyObject *PyTypeObject.tp_dict

   El diccionario del tipo se almacena aquí por "PyType_Ready()".

   This field should normally be initialized to "NULL" before
   PyType_Ready is called; it may also be initialized to a dictionary
   containing initial attributes for the type.  Once "PyType_Ready()"
   has initialized the type, extra attributes for the type may be
   added to this dictionary only if they don't correspond to
   overloaded operations (like "__add__()").  Once initialization for
   the type has finished, this field should be treated as read-only.

   Some types may not store their dictionary in this slot. Use
   "PyType_GetDict()" to retrieve the dictionary for an arbitrary
   type.

   Distinto en la versión 3.12: Internals detail: For static builtin
   types, this is always "NULL". Instead, the dict for such types is
   stored on "PyInterpreterState". Use "PyType_GetDict()" to get the
   dict for an arbitrary type.

   **Herencia:**

   Este campo no es heredado por los subtipos (aunque los atributos
   definidos aquí se heredan a través de un mecanismo diferente).

   **Por defecto:**

   Si este campo es "NULL", "PyType_Ready()" le asignará un nuevo
   diccionario.

   Advertencia:

     No es seguro usar "PyDict_SetItem()" en o modificar de otra
     manera a "tp_dict" con el diccionario C-API.

descrgetfunc PyTypeObject.tp_descr_get

   * The corresponding slot ID "Py_tp_descr_get" is part of the Stable
   ABI.*

   Un puntero opcional a una función "obtener descriptor" (*descriptor
   ger*).

   La firma de la función es:

      PyObject * tp_descr_get(PyObject *self, PyObject *obj, PyObject *type);

   **Herencia:**

   Este campo es heredado por subtipos.

descrsetfunc PyTypeObject.tp_descr_set

   * The corresponding slot ID "Py_tp_descr_set" is part of the Stable
   ABI.*

   Un puntero opcional a una función para configurar y eliminar el
   valor de un descriptor.

   La firma de la función es:

      int tp_descr_set(PyObject *self, PyObject *obj, PyObject *value);

   El argumento *value* se establece a "NULL" para borrar el valor.

   **Herencia:**

   Este campo es heredado por subtipos.

Py_ssize_t PyTypeObject.tp_dictoffset

   While this field is still supported, "Py_TPFLAGS_MANAGED_DICT"
   should be used instead, if at all possible.

   Si las instancias de este tipo tienen un diccionario que contiene
   variables de instancia, este campo no es cero y contiene el
   desplazamiento en las instancias del tipo del diccionario de
   variables de instancia; este desplazamiento es utilizado por
   "PyObject_GenericGetAttr()".

   No confunda este campo con "tp_dict"; ese es el diccionario para
   los atributos del tipo de objeto en sí.

   The value specifies the offset of the dictionary from the start of
   the instance structure.

   El "tp_dictoffset" debe considerarse como de solo escritura. Para
   obtener el puntero al diccionario, llame a
   "PyObject_GenericGetDict()". Llamar a "PyObject_GenericGetDict()"
   puede necesitar asignar memoria para el diccionario, por lo que
   puede ser más eficiente llamar a "PyObject_GetAttr()" cuando se
   accede a un atributo en el objeto.

   It is an error to set both the "Py_TPFLAGS_MANAGED_DICT" bit and
   "tp_dictoffset".

   **Herencia:**

   This field is inherited by subtypes. A subtype should not override
   this offset; doing so could be unsafe, if C code tries to access
   the dictionary at the previous offset. To properly support
   inheritance, use "Py_TPFLAGS_MANAGED_DICT".

   **Por defecto:**

   This slot has no default.  For static types, if the field is "NULL"
   then no "__dict__" gets created for instances.

   If the "Py_TPFLAGS_MANAGED_DICT" bit is set in the "tp_flags"
   field, then "tp_dictoffset" will be set to "-1", to indicate that
   it is unsafe to use this field.

initproc PyTypeObject.tp_init

   * The corresponding slot ID "Py_tp_init" is part of the Stable
   ABI.*

   Un puntero opcional a una función de inicialización de instancia.

   This function corresponds to the "__init__()" method of classes.
   Like "__init__()", it is possible to create an instance without
   calling "__init__()", and it is possible to reinitialize an
   instance by calling its "__init__()" method again.

   La firma de la función es:

      int tp_init(PyObject *self, PyObject *args, PyObject *kwds);

   The self argument is the instance to be initialized; the *args* and
   *kwds* arguments represent positional and keyword arguments of the
   call to "__init__()".

   La función "tp_init", si no es "NULL", se llama cuando una
   instancia se crea normalmente llamando a su tipo, después de la
   función "tp_new" del tipo ha retornado una instancia del tipo. Si
   la función "tp_new" retorna una instancia de otro tipo que no es un
   subtipo del tipo original, no se llama la función "tp_init"; if
   "tp_new" retorna una instancia de un subtipo del tipo original, se
   llama al subtipo "tp_init".

   Retorna "0" en caso de éxito, "-1" y establece una excepción en
   caso de error.

   **Herencia:**

   Este campo es heredado por subtipos.

   **Por defecto:**

   Para tipos estáticos, este campo no tiene un valor predeterminado.

allocfunc PyTypeObject.tp_alloc

   * The corresponding slot ID "Py_tp_alloc" is part of the Stable
   ABI.*

   Un puntero opcional a una función de asignación de instancia.

   La firma de la función es:

      PyObject *tp_alloc(PyTypeObject *self, Py_ssize_t nitems);

   **Herencia:**

   Static subtypes inherit this slot, which will be
   "PyType_GenericAlloc()" if inherited from "object".

   Heap subtypes do not inherit this slot.

   **Por defecto:**

   For heap subtypes, this field is always set to
   "PyType_GenericAlloc()".

   For static subtypes, this slot is inherited (see above).

newfunc PyTypeObject.tp_new

   * The corresponding slot ID "Py_tp_new" is part of the Stable ABI.*

   Un puntero opcional a una función de creación de instancias.

   La firma de la función es:

      PyObject *tp_new(PyTypeObject *subtype, PyObject *args, PyObject *kwds);

   El argumento *subtype* es el tipo de objeto que se está creando;
   los argumentos *args* y *kwds* representan argumentos posicionales
   y de palabras clave de la llamada al tipo. Tenga en cuenta que
   *subtype* no tiene que ser igual al tipo cuya función "tp_new" es
   llamada; puede ser un subtipo de ese tipo (pero no un tipo no
   relacionado).

   La función "tp_new" debería llamar a "subtype->tp_alloc(subtype,
   nitems)" para asignar espacio para el objeto, y luego hacer solo la
   inicialización adicional que sea absolutamente necesaria. La
   inicialización que se puede ignorar o repetir de forma segura debe
   colocarse en el controlador "tp_init". Una buena regla general es
   que para los tipos inmutables, toda la inicialización debe tener
   lugar en "tp_new", mientras que para los tipos mutables, la mayoría
   de las inicializaciones se deben diferir a "tp_init".

   Set the "Py_TPFLAGS_DISALLOW_INSTANTIATION" flag to disallow
   creating instances of the type in Python.

   **Herencia:**

   Este campo se hereda por subtipos, excepto que no lo heredan tipos
   estáticos cuyo "tp_base" es "NULL" o "&PyBaseObject_Type".

   **Por defecto:**

   Para tipos estáticos, este campo no tiene ningún valor
   predeterminado. Esto significa que si la ranura se define como
   "NULL", no se puede llamar al tipo para crear nuevas instancias;
   presumiblemente hay alguna otra forma de crear instancias, como una
   función de fábrica.

freefunc PyTypeObject.tp_free

   * The corresponding slot ID "Py_tp_free" is part of the Stable
   ABI.*

   Un puntero opcional a una función de desasignación de instancia. Su
   firma es:

      void tp_free(void *self);

   This function must free the memory allocated by "tp_alloc".

   **Herencia:**

   Static subtypes inherit this slot, which will be "PyObject_Free()"
   if inherited from "object".  Exception: If the type supports
   garbage collection (i.e., the "Py_TPFLAGS_HAVE_GC" flag is set in
   "tp_flags") and it would inherit "PyObject_Free()", then this slot
   is not inherited but instead defaults to "PyObject_GC_Del()".

   Heap subtypes do not inherit this slot.

   **Por defecto:**

   For heap subtypes, this slot defaults to a deallocator suitable to
   match "PyType_GenericAlloc()" and the value of the
   "Py_TPFLAGS_HAVE_GC" flag.

   For static subtypes, this slot is inherited (see above).

inquiry PyTypeObject.tp_is_gc

   * The corresponding slot ID "Py_tp_is_gc" is part of the Stable
   ABI.*

   Un puntero opcional a una función llamada por el recolector de
   basura.

   The garbage collector needs to know whether a particular object is
   collectible or not.  Normally, it is sufficient to look at the
   object's type's "tp_flags" field, and check the
   "Py_TPFLAGS_HAVE_GC" flag bit.  But some types have a mixture of
   statically and dynamically allocated instances, and the statically
   allocated instances are not collectible.  Such types should define
   this function; it should return "1" for a collectible instance, and
   "0" for a non-collectible instance. The signature is:

      int tp_is_gc(PyObject *self);

   (El único ejemplo de esto son los tipos en sí. El metatipo,
   "PyType_Type", define esta función para distinguir entre tipos
   estática y dinámicamente asignados.)

   **Herencia:**

   Este campo es heredado por subtipos.

   **Por defecto:**

   This slot has no default.  If this field is "NULL",
   "Py_TPFLAGS_HAVE_GC" is used as the functional equivalent.

PyObject *PyTypeObject.tp_bases

   * The corresponding slot ID "Py_tp_bases" is part of the Stable
   ABI.*

   Tupla de tipos base.

   This field should be set to "NULL" and treated as read-only. Python
   will fill it in when the type is "initialized".

   For dynamically created classes, the "Py_tp_bases" "slot" can be
   used instead of the *bases* argument of
   "PyType_FromSpecWithBases()". The argument form is preferred.

   Advertencia:

     Multiple inheritance does not work well for statically defined
     types. If you set "tp_bases" to a tuple, Python will not raise an
     error, but some slots will only be inherited from the first base.

   **Herencia:**

   Este campo no se hereda.

PyObject *PyTypeObject.tp_mro

   Tupla que contiene el conjunto expandido de tipos base, comenzando
   con el tipo en sí y terminando con "object", en orden de resolución
   de método.

   This field should be set to "NULL" and treated as read-only. Python
   will fill it in when the type is "initialized".

   **Herencia:**

   Este campo no se hereda; se calcula fresco por "PyType_Ready()".

PyObject *PyTypeObject.tp_cache

   No usado. Solo para uso interno.

   **Herencia:**

   Este campo no se hereda.

void *PyTypeObject.tp_subclasses

   A collection of subclasses.  Internal use only.  May be an invalid
   pointer.

   To get a list of subclasses, call the Python method
   "__subclasses__()".

   Distinto en la versión 3.12: For some types, this field does not
   hold a valid PyObject*. The type was changed to void* to indicate
   this.

   **Herencia:**

   Este campo no se hereda.

PyObject *PyTypeObject.tp_weaklist

   Cabecera de lista de referencia débil, para referencias débiles a
   este tipo de objeto. No heredado Solo para uso interno.

   Distinto en la versión 3.12: Internals detail: For the static
   builtin types this is always "NULL", even if weakrefs are added.
   Instead, the weakrefs for each are stored on "PyInterpreterState".
   Use the public C-API or the internal
   "_PyObject_GET_WEAKREFS_LISTPTR()" macro to avoid the distinction.

   **Herencia:**

   Este campo no se hereda.

destructor PyTypeObject.tp_del

   * The corresponding slot ID "Py_tp_del" is part of the Stable ABI.*

   Este campo está en desuso. Use "tp_finalize" en su lugar.

unsigned int PyTypeObject.tp_version_tag

   Se usa para indexar en el caché de métodos. Solo para uso interno.

   **Herencia:**

   Este campo no se hereda.

destructor PyTypeObject.tp_finalize

   * The corresponding slot ID "Py_tp_finalize" is part of the Stable
   ABI since version 3.5.*

   An optional pointer to an instance finalization function.  This is
   the C implementation of the "__del__()" special method.  Its
   signature is:

      void tp_finalize(PyObject *self);

   The primary purpose of finalization is to perform any non-trivial
   cleanup that must be performed before the object is destroyed,
   while the object and any other objects it directly or indirectly
   references are still in a consistent state.  The finalizer is
   allowed to execute arbitrary Python code.

   Before Python automatically finalizes an object, some of the
   object's direct or indirect referents might have themselves been
   automatically finalized. However, none of the referents will have
   been automatically cleared ("tp_clear") yet.

   Other non-finalized objects might still be using a finalized
   object, so the finalizer must leave the object in a sane state
   (e.g., invariants are still met).

   Nota:

     After Python automatically finalizes an object, Python might
     start automatically clearing ("tp_clear") the object and its
     referents (direct and indirect).  Cleared objects are not
     guaranteed to be in a consistent state; a finalized object must
     be able to tolerate cleared referents.

   Nota:

     An object is not guaranteed to be automatically finalized before
     its destructor ("tp_dealloc") is called.  It is recommended to
     call "PyObject_CallFinalizerFromDealloc()" at the beginning of
     "tp_dealloc" to guarantee that the object is always finalized
     before destruction.

   Nota:

     The "tp_finalize" function can be called from any thread,
     although the *GIL* will be held.

   Nota:

     The "tp_finalize" function can be called during shutdown, after
     some global variables have been deleted.  See the documentation
     of the "__del__()" method for details.

   When Python finalizes an object, it behaves like the following
   algorithm:

   1. Python might mark the object as *finalized*.  Currently, Python
      always marks objects whose type supports garbage collection
      (i.e., the "Py_TPFLAGS_HAVE_GC" flag is set in "tp_flags") and
      never marks other types of objects; this might change in a
      future version.

   2. If the object is not marked as *finalized* and its "tp_finalize"
      finalizer function is non-"NULL", the finalizer function is
      called.

   3. If the finalizer function was called and the finalizer made the
      object reachable (i.e., there is a reference to the object and
      it is not a member of a *cyclic isolate*), then the finalizer is
      said to have *resurrected* the object.  It is unspecified
      whether the finalizer can also resurrect the object by adding a
      new reference to the object that does not make it reachable,
      i.e., the object is (still) a member of a cyclic isolate.

   4. If the finalizer resurrected the object, the object's pending
      destruction is canceled and the object's *finalized* mark might
      be removed if present.  Currently, Python never removes the
      *finalized* mark; this might change in a future version.

   *Automatic finalization* refers to any finalization performed by
   Python except via calls to "PyObject_CallFinalizer()" or
   "PyObject_CallFinalizerFromDealloc()".  No guarantees are made
   about when, if, or how often an object is automatically finalized,
   except:

   * Python will not automatically finalize an object if it is
     reachable, i.e., there is a reference to it and it is not a
     member of a *cyclic isolate*.

   * Python will not automatically finalize an object if finalizing it
     would not mark the object as *finalized*.  Currently, this
     applies to objects whose type does not support garbage
     collection, i.e., the "Py_TPFLAGS_HAVE_GC" flag is not set.  Such
     objects can still be manually finalized by calling
     "PyObject_CallFinalizer()" or
     "PyObject_CallFinalizerFromDealloc()".

   * Python will not automatically finalize any two members of a
     *cyclic isolate* concurrently.

   * Python will not automatically finalize an object after it has
     automatically cleared ("tp_clear") the object.

   * If an object is a member of a *cyclic isolate*, Python will not
     automatically finalize it after automatically clearing (see
     "tp_clear") any other member.

   * Python will automatically finalize every member of a *cyclic
     isolate* before it automatically clears (see "tp_clear") any of
     them.

   * If Python is going to automatically clear an object ("tp_clear"),
     it will automatically finalize the object first.

   Python currently only automatically finalizes objects that are
   members of a *cyclic isolate*, but future versions might finalize
   objects regularly before their destruction.

   To manually finalize an object, do not call this function directly;
   call "PyObject_CallFinalizer()" or
   "PyObject_CallFinalizerFromDealloc()" instead.

   "tp_finalize" should leave the current exception status unchanged.
   The recommended way to write a non-trivial finalizer is to back up
   the exception at the beginning by calling
   "PyErr_GetRaisedException()" and restore the exception at the end
   by calling "PyErr_SetRaisedException()".  If an exception is
   encountered in the middle of the finalizer, log and clear it with
   "PyErr_WriteUnraisable()" or "PyErr_FormatUnraisable()".  For
   example:

      static void
      foo_finalize(PyObject *self)
      {
          // Save the current exception, if any.
          PyObject *exc = PyErr_GetRaisedException();

          // ...

          if (do_something_that_might_raise() != success_indicator) {
              PyErr_WriteUnraisable(self);
              goto done;
          }

      done:
          // Restore the saved exception.  This silently discards any exception
          // raised above, so be sure to call PyErr_WriteUnraisable first if
          // necessary.
          PyErr_SetRaisedException(exc);
      }

   **Herencia:**

   Este campo es heredado por subtipos.

   Added in version 3.4.

   Distinto en la versión 3.8: Before version 3.8 it was necessary to
   set the "Py_TPFLAGS_HAVE_FINALIZE" flags bit in order for this
   field to be used.  This is no longer required.

   Ver también:

     * **PEP 442**: "Safe object finalization"

     * Object Life Cycle for details about how this slot relates to
       other slots.

     * "PyObject_CallFinalizer()"

     * "PyObject_CallFinalizerFromDealloc()"

vectorcallfunc PyTypeObject.tp_vectorcall

   * The corresponding slot ID "Py_tp_vectorcall" is part of the
   Stable ABI since version 3.14.*

   A vectorcall function to use for calls of this type object (rather
   than instances). In other words, "tp_vectorcall" can be used to
   optimize "type.__call__", which typically returns a new instance of
   *type*.

   As with any vectorcall function, if "tp_vectorcall" is "NULL", the
   *tp_call* protocol ("Py_TYPE(type)->tp_call") is used instead.

   Nota:

     The vectorcall protocol requires that the vectorcall function has
     the same behavior as the corresponding "tp_call". This means that
     "type->tp_vectorcall" must match the behavior of
     "Py_TYPE(type)->tp_call".Specifically, if *type* uses the default
     metaclass, "type->tp_vectorcall" must behave the same as
     PyType_Type->tp_call, which:

     * calls "type->tp_new",

     * if the result is a subclass of *type*, calls "type->tp_init" on
       the result of "tp_new", and

     * returns the result of "tp_new".

     Typically, "tp_vectorcall" is overridden to optimize this process
     for specific "tp_new" and "tp_init". When doing this for user-
     subclassable types, note that both can be overridden (using
     "__new__()" and "__init__()", respectively).

   **Herencia:**

   Este campo nunca se hereda.

   Added in version 3.9: (el campo existe desde 3.8 pero solo se usa
   desde 3.9)

unsigned char PyTypeObject.tp_watched

   Internal. Do not use.

   Added in version 3.12.

## Tipos estáticos

Tradicionalmente, los tipos definidos en el código C son *static*, es
decir, una estructura estática "PyTypeObject" se define directamente
en el código y se inicializa usando "PyType_Ready()".

Esto da como resultado tipos que están limitados en relación con los
tipos definidos en Python:

* Los tipos estáticos están limitados a una base, es decir, no pueden
  usar herencia múltiple.

* Los objetos de tipo estático (pero no necesariamente sus instancias)
  son inmutables. No es posible agregar o modificar los atributos del
  objeto tipo desde Python.

* Los objetos de tipo estático se comparten en sub intérpretes, por lo
  que no deben incluir ningún estado específico del sub interpretador.

Also, since "PyTypeObject" is only part of the Limited API as an
opaque struct, any extension modules using static types must be
compiled for a specific Python minor version.

## Tipos Heap

An alternative to static types is *heap-allocated types*, or *heap
types* for short, which correspond closely to classes created by
Python's "class" statement. Heap types have the "Py_TPFLAGS_HEAPTYPE"
flag set.

This is done by filling a "PyType_Spec" structure and calling
"PyType_FromSpec()", "PyType_FromSpecWithBases()",
"PyType_FromModuleAndSpec()", or "PyType_FromMetaclass()".

## Estructuras de objetos de números

type PyNumberMethods

   Esta estructura contiene punteros a las funciones que utiliza un
   objeto para implementar el protocolo numérico. Cada función es
   utilizada por la función de un nombre similar documentado en la
   sección Protocolo de números.

   Aquí está la definición de la estructura:

      typedef struct {
           binaryfunc nb_add;
           binaryfunc nb_subtract;
           binaryfunc nb_multiply;
           binaryfunc nb_remainder;
           binaryfunc nb_divmod;
           ternaryfunc nb_power;
           unaryfunc nb_negative;
           unaryfunc nb_positive;
           unaryfunc nb_absolute;
           inquiry nb_bool;
           unaryfunc nb_invert;
           binaryfunc nb_lshift;
           binaryfunc nb_rshift;
           binaryfunc nb_and;
           binaryfunc nb_xor;
           binaryfunc nb_or;
           unaryfunc nb_int;
           void *nb_reserved;
           unaryfunc nb_float;

           binaryfunc nb_inplace_add;
           binaryfunc nb_inplace_subtract;
           binaryfunc nb_inplace_multiply;
           binaryfunc nb_inplace_remainder;
           ternaryfunc nb_inplace_power;
           binaryfunc nb_inplace_lshift;
           binaryfunc nb_inplace_rshift;
           binaryfunc nb_inplace_and;
           binaryfunc nb_inplace_xor;
           binaryfunc nb_inplace_or;

           binaryfunc nb_floor_divide;
           binaryfunc nb_true_divide;
           binaryfunc nb_inplace_floor_divide;
           binaryfunc nb_inplace_true_divide;

           unaryfunc nb_index;

           binaryfunc nb_matrix_multiply;
           binaryfunc nb_inplace_matrix_multiply;
      } PyNumberMethods;

   Nota:

     Las funciones binarias y ternarias deben verificar el tipo de
     todos sus operandos e implementar las conversiones necesarias (al
     menos uno de los operandos es una instancia del tipo definido).
     Si la operación no está definida para los operandos dados, las
     funciones binarias y ternarias deben retornar
     "Py_NotImplemented", si se produce otro error, deben retornar
     "NULL" y establecer una excepción.

   Nota:

     The "nb_reserved" field should always be "NULL".  It was
     previously called "nb_long", and was renamed in Python 3.0.1.

binaryfunc PyNumberMethods.nb_add

   * The corresponding slot ID "Py_nb_add" is part of the Stable ABI.*

binaryfunc PyNumberMethods.nb_subtract

   * The corresponding slot ID "Py_nb_subtract" is part of the Stable
   ABI.*

binaryfunc PyNumberMethods.nb_multiply

   * The corresponding slot ID "Py_nb_multiply" is part of the Stable
   ABI.*

binaryfunc PyNumberMethods.nb_remainder

   * The corresponding slot ID "Py_nb_remainder" is part of the Stable
   ABI.*

binaryfunc PyNumberMethods.nb_divmod

   * The corresponding slot ID "Py_nb_divmod" is part of the Stable
   ABI.*

ternaryfunc PyNumberMethods.nb_power

   * The corresponding slot ID "Py_nb_power" is part of the Stable
   ABI.*

unaryfunc PyNumberMethods.nb_negative

   * The corresponding slot ID "Py_nb_negative" is part of the Stable
   ABI.*

unaryfunc PyNumberMethods.nb_positive

   * The corresponding slot ID "Py_nb_positive" is part of the Stable
   ABI.*

unaryfunc PyNumberMethods.nb_absolute

   * The corresponding slot ID "Py_nb_absolute" is part of the Stable
   ABI.*

inquiry PyNumberMethods.nb_bool

   * The corresponding slot ID "Py_nb_bool" is part of the Stable
   ABI.*

unaryfunc PyNumberMethods.nb_invert

   * The corresponding slot ID "Py_nb_invert" is part of the Stable
   ABI.*

binaryfunc PyNumberMethods.nb_lshift

   * The corresponding slot ID "Py_nb_lshift" is part of the Stable
   ABI.*

binaryfunc PyNumberMethods.nb_rshift

   * The corresponding slot ID "Py_nb_rshift" is part of the Stable
   ABI.*

binaryfunc PyNumberMethods.nb_and

   * The corresponding slot ID "Py_nb_and" is part of the Stable ABI.*

binaryfunc PyNumberMethods.nb_xor

   * The corresponding slot ID "Py_nb_xor" is part of the Stable ABI.*

binaryfunc PyNumberMethods.nb_or

   * The corresponding slot ID "Py_nb_or" is part of the Stable ABI.*

unaryfunc PyNumberMethods.nb_int

   * The corresponding slot ID "Py_nb_int" is part of the Stable ABI.*

void *PyNumberMethods.nb_reserved

unaryfunc PyNumberMethods.nb_float

   * The corresponding slot ID "Py_nb_float" is part of the Stable
   ABI.*

binaryfunc PyNumberMethods.nb_inplace_add

   * The corresponding slot ID "Py_nb_inplace_add" is part of the
   Stable ABI.*

binaryfunc PyNumberMethods.nb_inplace_subtract

   * The corresponding slot ID "Py_nb_inplace_subtract" is part of the
   Stable ABI.*

binaryfunc PyNumberMethods.nb_inplace_multiply

   * The corresponding slot ID "Py_nb_inplace_multiply" is part of the
   Stable ABI.*

binaryfunc PyNumberMethods.nb_inplace_remainder

   * The corresponding slot ID "Py_nb_inplace_remainder" is part of
   the Stable ABI.*

ternaryfunc PyNumberMethods.nb_inplace_power

   * The corresponding slot ID "Py_nb_inplace_power" is part of the
   Stable ABI.*

binaryfunc PyNumberMethods.nb_inplace_lshift

   * The corresponding slot ID "Py_nb_inplace_lshift" is part of the
   Stable ABI.*

binaryfunc PyNumberMethods.nb_inplace_rshift

   * The corresponding slot ID "Py_nb_inplace_rshift" is part of the
   Stable ABI.*

binaryfunc PyNumberMethods.nb_inplace_and

   * The corresponding slot ID "Py_nb_inplace_and" is part of the
   Stable ABI.*

binaryfunc PyNumberMethods.nb_inplace_xor

   * The corresponding slot ID "Py_nb_inplace_xor" is part of the
   Stable ABI.*

binaryfunc PyNumberMethods.nb_inplace_or

   * The corresponding slot ID "Py_nb_inplace_or" is part of the
   Stable ABI.*

binaryfunc PyNumberMethods.nb_floor_divide

   * The corresponding slot ID "Py_nb_floor_divide" is part of the
   Stable ABI.*

binaryfunc PyNumberMethods.nb_true_divide

   * The corresponding slot ID "Py_nb_true_divide" is part of the
   Stable ABI.*

binaryfunc PyNumberMethods.nb_inplace_floor_divide

   * The corresponding slot ID "Py_nb_inplace_floor_divide" is part of
   the Stable ABI.*

binaryfunc PyNumberMethods.nb_inplace_true_divide

   * The corresponding slot ID "Py_nb_inplace_true_divide" is part of
   the Stable ABI.*

unaryfunc PyNumberMethods.nb_index

   * The corresponding slot ID "Py_nb_index" is part of the Stable
   ABI.*

binaryfunc PyNumberMethods.nb_matrix_multiply

   * The corresponding slot ID "Py_nb_matrix_multiply" is part of the
   Stable ABI since version 3.5.*

binaryfunc PyNumberMethods.nb_inplace_matrix_multiply

   * The corresponding slot ID "Py_nb_inplace_matrix_multiply" is part
   of the Stable ABI since version 3.5.*

## Estructuras de objetos mapeo

type PyMappingMethods

   Esta estructura contiene punteros a las funciones que utiliza un
   objeto para implementar el protocolo de mapeo. Tiene tres miembros:

lenfunc PyMappingMethods.mp_length

   * The corresponding slot ID "Py_mp_length" is part of the Stable
   ABI.*

   Esta función es utilizada por "PyMapping_Size()" y
   "PyObject_Size()", y tiene la misma firma. Esta ranura puede
   establecerse en "NULL" si el objeto no tiene una longitud definida.

binaryfunc PyMappingMethods.mp_subscript

   * The corresponding slot ID "Py_mp_subscript" is part of the Stable
   ABI.*

   Esta función es utilizada por "PyObject_GetItem()" y
   "PySequence_GetSlice()", y tiene la misma firma que
   "PyObject_GetItem()". Este espacio debe llenarse para que la
   función "PyMapping_Check()" retorna "1", de lo contrario puede ser
   "NULL".

objobjargproc PyMappingMethods.mp_ass_subscript

   * The corresponding slot ID "Py_mp_ass_subscript" is part of the
   Stable ABI.*

   This function is used by "PyObject_SetItem()",
   "PyObject_DelItem()", "PySequence_SetSlice()" and
   "PySequence_DelSlice()".  It has the same signature as
   "PyObject_SetItem()", but *v* can also be set to "NULL" to delete
   an item.  If this slot is "NULL", the object does not support item
   assignment and deletion.

## Estructuras de objetos secuencia

type PySequenceMethods

   Esta estructura contiene punteros a las funciones que utiliza un
   objeto para implementar el protocolo de secuencia.

lenfunc PySequenceMethods.sq_length

   * The corresponding slot ID "Py_sq_length" is part of the Stable
   ABI.*

   Esta función es utilizada por "PySequence_Size()" y
   "PyObject_Size()", y tiene la misma firma. También se usa para
   manejar índices negativos a través de los espacios "sq_item" y
   "sq_ass_item".

binaryfunc PySequenceMethods.sq_concat

   * The corresponding slot ID "Py_sq_concat" is part of the Stable
   ABI.*

   Esta función es utilizada por "PySequence_Concat()" y tiene la
   misma firma. También es utilizado por el operador "+", después de
   intentar la suma numérica a través de la ranura "nb_add".

ssizeargfunc PySequenceMethods.sq_repeat

   * The corresponding slot ID "Py_sq_repeat" is part of the Stable
   ABI.*

   Esta función es utilizada por "PySequence_Repeat()" y tiene la
   misma firma. También es utilizado por el operador "*", después de
   intentar la multiplicación numérica a través de la ranura
   "nb_multiply".

ssizeargfunc PySequenceMethods.sq_item

   * The corresponding slot ID "Py_sq_item" is part of the Stable
   ABI.*

   Esta función es utilizada por "PySequence_GetItem()" y tiene la
   misma firma. También es utilizado por "PyObject_GetItem()", después
   de intentar la suscripción a través de la ranura "mp_subscript".
   Este espacio debe llenarse para que la función "PySequence_Check()"
   retorna "1", de lo contrario puede ser "NULL".

   Negative indexes are handled as follows: if the "sq_length" slot is
   filled, it is called and the sequence length is used to compute a
   positive index which is passed to  "sq_item".  If "sq_length" is
   "NULL", the index is passed as is to the function.

ssizeobjargproc PySequenceMethods.sq_ass_item

   * The corresponding slot ID "Py_sq_ass_item" is part of the Stable
   ABI.*

   Esta función es utilizada por "PySequence_SetItem()" y tiene la
   misma firma. También lo usan "PyObject_SetItem()" y
   "PyObject_DelItem()", después de intentar la asignación y
   eliminación del elemento a través de la ranura "mp_ass_subscript".
   Este espacio puede dejarse en "NULL" si el objeto no admite la
   asignación y eliminación de elementos.

objobjproc PySequenceMethods.sq_contains

   * The corresponding slot ID "Py_sq_contains" is part of the Stable
   ABI.*

   Esta función puede ser utilizada por "PySequence_Contains()" y
   tiene la misma firma. Este espacio puede dejarse en "NULL", en este
   caso "PySequence_Contains()" simplemente atraviesa la secuencia
   hasta que encuentra una coincidencia.

binaryfunc PySequenceMethods.sq_inplace_concat

   * The corresponding slot ID "Py_sq_inplace_concat" is part of the
   Stable ABI.*

   Esta función es utilizada por "PySequence_InPlaceConcat()" y tiene
   la misma firma. Debería modificar su primer operando y retornarlo.
   Este espacio puede dejarse en "NULL", en este caso
   "PySequence_InPlaceConcat()" volverá a "PySequence_Concat()".
   También es utilizado por la asignación aumentada "+=", después de
   intentar la suma numérica en el lugar a través de la ranura
   "nb_inplace_add".

ssizeargfunc PySequenceMethods.sq_inplace_repeat

   * The corresponding slot ID "Py_sq_inplace_repeat" is part of the
   Stable ABI.*

   Esta función es utilizada por "PySequence_InPlaceRepeat()" y tiene
   la misma firma. Debería modificar su primer operando y retornarlo.
   Este espacio puede dejarse en "NULL", en este caso
   "PySequence_InPlaceRepeat()" volverá a "PySequence_Repeat()".
   También es utilizado por la asignación aumentada "*=", después de
   intentar la multiplicación numérica en el lugar a través de la
   ranura "nb_inplace_multiply".

## Estructuras de objetos búfer

type PyBufferProcs

   Esta estructura contiene punteros a las funciones requeridas por
   Buffer protocol. El protocolo define cómo un objeto exportador
   puede exponer sus datos internos a objetos de consumo.

getbufferproc PyBufferProcs.bf_getbuffer

   * The corresponding slot ID "Py_bf_getbuffer" is part of the Stable
   ABI since version 3.11.*

   La firma de esta función es:

      int (PyObject *exporter, Py_buffer *view, int flags);

   Maneja una solicitud a *exporter* para completar *view* según lo
   especificado por *flags*. Excepto por el punto (3), una
   implementación de esta función DEBE seguir estos pasos:

   1. Check if the request can be met. If not, raise "BufferError",
      set "view->obj" to "NULL" and return "-1".

   2. Rellene los campos solicitados.

   3. Incrementa un contador interno para el número de exportaciones
      (*exports*).

   4. Set "view->obj" to *exporter* and increment "view->obj".

   5. Retorna "0".

   **Thread safety:**

   In the *free-threaded build*, implementations must ensure:

   * The export counter increment in step (3) is atomic.

   * The underlying buffer data remains valid and at a stable memory
     location for the lifetime of all exports.

   * For objects that support resizing or reallocation (such as
     "bytearray"), the export counter is checked atomically before
     such operations, and "BufferError" is raised if exports exist.

   * The function is safe to call concurrently from multiple threads.

   See also Thread safety for memoryview objects for the Python-level
   thread safety guarantees of "memoryview" objects.

   Si *exporter* es parte de una cadena o árbol de proveedores de
   búfer, se pueden usar dos esquemas principales:

   * Re-export: Each member of the tree acts as the exporting object
     and sets "view->obj" to a new reference to itself.

   * Redirect: The buffer request is redirected to the root object of
     the tree. Here, "view->obj" will be a new reference to the root
     object.

   Los campos individuales de *view* se describen en la sección
   Estructura de búfer, las reglas sobre cómo debe reaccionar un
   exportador a solicitudes específicas se encuentran en la sección
   Tipos de solicitud de búfer.

   Toda la memoria señalada en la estructura "Py_buffer" pertenece al
   exportador y debe permanecer válida hasta que no queden
   consumidores. "format", "shape", "strides", "suboffsets" y
   "internal" son de solo lectura para el consumidor.

   "PyBuffer_FillInfo()" proporciona una manera fácil de exponer un
   búfer de bytes simple mientras se trata correctamente con todos los
   tipos de solicitud.

   "PyObject_GetBuffer()" es la interfaz para el consumidor que
   envuelve esta función.

releasebufferproc PyBufferProcs.bf_releasebuffer

   * The corresponding slot ID "Py_bf_releasebuffer" is part of the
   Stable ABI since version 3.11.*

   La firma de esta función es:

      void (PyObject *exporter, Py_buffer *view);

   Maneja una solicitud para liberar los recursos del búfer. Si no es
   necesario liberar recursos, "PyBufferProcs.bf_releasebuffer" puede
   ser "NULL". De lo contrario, una implementación estándar de esta
   función tomará estos pasos opcionales:

   1. Disminuir un contador interno para el número de exportaciones.

   2. Si el contador es "0", libera toda la memoria asociada con
      *view*.

   **Thread safety:**

   In the *free-threaded build*:

   * The export counter decrement in step (1) must be atomic.

   * Resource cleanup when the counter reaches zero must be done
     atomically, as the final release may race with concurrent
     releases from other threads and deallocation must only happen
     once.

   El exportador DEBE utilizar el campo "internal" para realizar un
   seguimiento de los recursos específicos del búfer. Se garantiza que
   este campo permanecerá constante, mientras que un consumidor PUEDE
   pasar una copia del búfer original como argumento *view*.

   This function MUST NOT decrement "view->obj", since that is done
   automatically in "PyBuffer_Release()" (this scheme is useful for
   breaking reference cycles).

   "PyBuffer_Release()" es la interfaz para el consumidor que envuelve
   esta función.

## Estructuras de objetos asíncronos

Added in version 3.5.

type PyAsyncMethods

   Esta estructura contiene punteros a las funciones requeridas para
   implementar objetos "esperable" (*awaitable*) y "iterador
   asincrónico" (*asynchronous iterator*).

   Aquí está la definición de la estructura:

      typedef struct {
          unaryfunc am_await;
          unaryfunc am_aiter;
          unaryfunc am_anext;
          sendfunc am_send;
      } PyAsyncMethods;

unaryfunc PyAsyncMethods.am_await

   * The corresponding slot ID "Py_am_await" is part of the Stable ABI
   since version 3.5.*

   La firma de esta función es:

      PyObject *am_await(PyObject *self);

   The returned object must be an *iterator*, i.e. "PyIter_Check()"
   must return "1" for it.

   Este espacio puede establecerse en "NULL" si un objeto no es
   *awaitable*.

unaryfunc PyAsyncMethods.am_aiter

   * The corresponding slot ID "Py_am_aiter" is part of the Stable ABI
   since version 3.5.*

   La firma de esta función es:

      PyObject *am_aiter(PyObject *self);

   Must return an *asynchronous iterator* object. See "__anext__()"
   for details.

   Este espacio puede establecerse en "NULL" si un objeto no
   implementa el protocolo de iteración asincrónica.

unaryfunc PyAsyncMethods.am_anext

   * The corresponding slot ID "Py_am_anext" is part of the Stable ABI
   since version 3.5.*

   La firma de esta función es:

      PyObject *am_anext(PyObject *self);

   Must return an *awaitable* object. See "__anext__()" for details.
   This slot may be set to "NULL".

sendfunc PyAsyncMethods.am_send

   * The corresponding slot ID "Py_am_send" is part of the Stable ABI
   since version 3.10.*

   La firma de esta función es:

      PySendResult am_send(PyObject *self, PyObject *arg, PyObject **result);

   Consulte "PyIter_Send()" para obtener más detalles. Esta ranura se
   puede establecer en "NULL".

   Added in version 3.10.

## Tipo Ranura *typedefs*

typedef PyObject *(*allocfunc)(PyTypeObject *cls, Py_ssize_t nitems)
    * Part of the Stable ABI.*

   The purpose of this function is to separate memory allocation from
   memory initialization.  It should return a pointer to a block of
   memory of adequate length for the instance, suitably aligned, and
   initialized to zeros, but with "ob_refcnt" set to "1" and "ob_type"
   set to the type argument.  If the type's "tp_itemsize" is non-zero,
   the object's "ob_size" field should be initialized to *nitems* and
   the length of the allocated memory block should be "tp_basicsize +
   nitems*tp_itemsize", rounded up to a multiple of "sizeof(void*)";
   otherwise, *nitems* is not used and the length of the block should
   be "tp_basicsize".

   Esta función no debe hacer ninguna otra instancia de
   inicialización, ni siquiera para asignar memoria adicional; eso
   debe ser realizado por "tp_new".

typedef void (*destructor)(PyObject*)
    * Part of the Stable ABI.*

typedef void (*freefunc)(void*)

   Consulte "tp_free".

typedef PyObject *(*newfunc)(PyTypeObject*, PyObject*, PyObject*)
    * Part of the Stable ABI.*

   Consulte "tp_new".

typedef int (*initproc)(PyObject*, PyObject*, PyObject*)
    * Part of the Stable ABI.*

   Consulte "tp_init".

typedef PyObject *(*reprfunc)(PyObject*)
    * Part of the Stable ABI.*

   Consulte "tp_repr".

typedef PyObject *(*getattrfunc)(PyObject *self, char *attr)
    * Part of the Stable ABI.*

   Retorna el valor del atributo nombrado para el objeto.

typedef int (*setattrfunc)(PyObject *self, char *attr, PyObject *value)
    * Part of the Stable ABI.*

   Establece el valor del atributo nombrado para el objeto. El
   argumento del valor se establece en "NULL" para eliminar el
   atributo.

typedef PyObject *(*getattrofunc)(PyObject *self, PyObject *attr)
    * Part of the Stable ABI.*

   Retorna el valor del atributo nombrado para el objeto.

   Consulte "tp_getattro".

typedef int (*setattrofunc)(PyObject *self, PyObject *attr, PyObject *value)
    * Part of the Stable ABI.*

   Establece el valor del atributo nombrado para el objeto. El
   argumento del valor se establece en "NULL" para eliminar el
   atributo.

   Consulte "tp_setattro".

typedef PyObject *(*descrgetfunc)(PyObject*, PyObject*, PyObject*)
    * Part of the Stable ABI.*

   See "tp_descr_get".

typedef int (*descrsetfunc)(PyObject*, PyObject*, PyObject*)
    * Part of the Stable ABI.*

   See "tp_descr_set".

typedef Py_hash_t (*hashfunc)(PyObject*)
    * Part of the Stable ABI.*

   Consulte "tp_hash".

typedef PyObject *(*richcmpfunc)(PyObject*, PyObject*, int)
    * Part of the Stable ABI.*

   Consulte "tp_richcompare".

typedef PyObject *(*getiterfunc)(PyObject*)
    * Part of the Stable ABI.*

   Consulte "tp_iter".

typedef PyObject *(*iternextfunc)(PyObject*)
    * Part of the Stable ABI.*

   Consulte "tp_iternext".

typedef Py_ssize_t (*lenfunc)(PyObject*)
    * Part of the Stable ABI.*

typedef int (*getbufferproc)(PyObject*, Py_buffer*, int)
    * Part of the Stable ABI since version 3.12.*

typedef void (*releasebufferproc)(PyObject*, Py_buffer*)
    * Part of the Stable ABI since version 3.12.*

typedef PyObject *(*unaryfunc)(PyObject*)
    * Part of the Stable ABI.*

typedef PyObject *(*binaryfunc)(PyObject*, PyObject*)
    * Part of the Stable ABI.*

typedef PySendResult (*sendfunc)(PyObject*, PyObject*, PyObject**)

   Consulte "am_send".

typedef PyObject *(*ternaryfunc)(PyObject*, PyObject*, PyObject*)
    * Part of the Stable ABI.*

typedef PyObject *(*ssizeargfunc)(PyObject*, Py_ssize_t)
    * Part of the Stable ABI.*

typedef int (*ssizeobjargproc)(PyObject*, Py_ssize_t, PyObject*)
    * Part of the Stable ABI.*

typedef int (*objobjproc)(PyObject*, PyObject*)
    * Part of the Stable ABI.*

typedef int (*objobjargproc)(PyObject*, PyObject*, PyObject*)
    * Part of the Stable ABI.*

## Ejemplos

Los siguientes son ejemplos simples de definiciones de tipo Python.
Incluyen el uso común que puede encontrar. Algunos demuestran casos
difíciles de esquina (*corner cases*). Para obtener más ejemplos,
información práctica y un tutorial, consulte "definiendo nuevos tipos"
(Definición de tipos de extensión: Tutorial) y "tópicos de nuevos
tipos (Definición de tipos de extensión: temas variados).

Un tipo estático básico:

   typedef struct {
       PyObject_HEAD
       const char *data;
   } MyObject;

   static PyTypeObject MyObject_Type = {
       PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "mymod.MyObject",
       .tp_basicsize = sizeof(MyObject),
       .tp_doc = PyDoc_STR("My objects"),
       .tp_new = myobj_new,
       .tp_dealloc = (destructor)myobj_dealloc,
       .tp_repr = (reprfunc)myobj_repr,
   };

También puede encontrar código más antiguo (especialmente en la base
de código CPython) con un inicializador más detallado:

   static PyTypeObject MyObject_Type = {
       PyVarObject_HEAD_INIT(NULL, 0)
       "mymod.MyObject",               /* tp_name */
       sizeof(MyObject),               /* tp_basicsize */
       0,                              /* tp_itemsize */
       (destructor)myobj_dealloc,      /* tp_dealloc */
       0,                              /* tp_vectorcall_offset */
       0,                              /* tp_getattr */
       0,                              /* tp_setattr */
       0,                              /* tp_as_async */
       (reprfunc)myobj_repr,           /* tp_repr */
       0,                              /* tp_as_number */
       0,                              /* tp_as_sequence */
       0,                              /* tp_as_mapping */
       0,                              /* tp_hash */
       0,                              /* tp_call */
       0,                              /* tp_str */
       0,                              /* tp_getattro */
       0,                              /* tp_setattro */
       0,                              /* tp_as_buffer */
       0,                              /* tp_flags */
       PyDoc_STR("My objects"),        /* tp_doc */
       0,                              /* tp_traverse */
       0,                              /* tp_clear */
       0,                              /* tp_richcompare */
       0,                              /* tp_weaklistoffset */
       0,                              /* tp_iter */
       0,                              /* tp_iternext */
       0,                              /* tp_methods */
       0,                              /* tp_members */
       0,                              /* tp_getset */
       0,                              /* tp_base */
       0,                              /* tp_dict */
       0,                              /* tp_descr_get */
       0,                              /* tp_descr_set */
       0,                              /* tp_dictoffset */
       0,                              /* tp_init */
       0,                              /* tp_alloc */
       myobj_new,                      /* tp_new */
   };

Un tipo que admite referencias débiles, instancias de diccionarios
(*dicts*) y *hashing*:

   typedef struct {
       PyObject_HEAD
       const char *data;
   } MyObject;

   static PyTypeObject MyObject_Type = {
       PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "mymod.MyObject",
       .tp_basicsize = sizeof(MyObject),
       .tp_doc = PyDoc_STR("My objects"),
       .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE |
            Py_TPFLAGS_HAVE_GC | Py_TPFLAGS_MANAGED_DICT |
            Py_TPFLAGS_MANAGED_WEAKREF,
       .tp_new = myobj_new,
       .tp_traverse = (traverseproc)myobj_traverse,
       .tp_clear = (inquiry)myobj_clear,
       .tp_alloc = PyType_GenericNew,
       .tp_dealloc = (destructor)myobj_dealloc,
       .tp_repr = (reprfunc)myobj_repr,
       .tp_hash = (hashfunc)myobj_hash,
       .tp_richcompare = PyBaseObject_Type.tp_richcompare,
   };

A str subclass that cannot be subclassed and cannot be called to
create instances (e.g. uses a separate factory func) using
"Py_TPFLAGS_DISALLOW_INSTANTIATION" flag:

   typedef struct {
       PyUnicodeObject raw;
       char *extra;
   } MyStr;

   static PyTypeObject MyStr_Type = {
       PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "mymod.MyStr",
       .tp_basicsize = sizeof(MyStr),
       .tp_base = NULL,  // set to &PyUnicode_Type in module init
       .tp_doc = PyDoc_STR("my custom str"),
       .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_DISALLOW_INSTANTIATION,
       .tp_repr = (reprfunc)myobj_repr,
   };

El tipo estático más simple con instancias de longitud fija:

   typedef struct {
       PyObject_HEAD
   } MyObject;

   static PyTypeObject MyObject_Type = {
       PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "mymod.MyObject",
   };

El tipo estático más simple con instancias de longitud variable:

   typedef struct {
       PyObject_VAR_HEAD
       const char *data[1];
   } MyObject;

   static PyTypeObject MyObject_Type = {
       PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "mymod.MyObject",
       .tp_basicsize = sizeof(MyObject) - sizeof(char *),
       .tp_itemsize = sizeof(char *),
   };
