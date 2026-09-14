---
title: Protocolo de objeto
source_url: https://docs.python.org/es/3
source_path: c-api/object.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 540
---

# Protocolo de objeto

PyObject *Py_GetConstant(unsigned int constant_id)
    * Part of the Stable ABI since version 3.13.*

   Obtiene una *referencia fuerte* a una constante.

   Establece una excepción y retorna "NULL" si *constant_id* es
   inválido.

   *constant_id* debe ser uno de estos identificadores constantes:

   +------------------------------------------+-------+---------------------------+
   | Identificador de constante               | Valor | Objeto retornado          |
   |==========================================|=======|===========================|
   | Py_CONSTANT_NONE                         | "0"   | "None"                    |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_FALSE                        | "1"   | "False"                   |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_TRUE                         | "2"   | "True"                    |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_ELLIPSIS                     | "3"   | "Ellipsis"                |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_NOT_IMPLEMENTED              | "4"   | "NotImplemented"          |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_ZERO                         | "5"   | "0"                       |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_ONE                          | "6"   | "1"                       |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_EMPTY_STR                    | "7"   | "''"                      |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_EMPTY_BYTES                  | "8"   | "b''"                     |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_EMPTY_TUPLE                  | "9"   | "()"                      |
   +------------------------------------------+-------+---------------------------+

   Los valores numéricos solo se proporcionan para proyectos que no
   pueden usar los identificadores constantes.

   Added in version 3.13.

   En CPython, todas estas constantes son *inmortales*.

PyObject *Py_GetConstantBorrowed(unsigned int constant_id)
    * Part of the Stable ABI since version 3.13.*

   Similar a "Py_GetConstant()", pero retorna una *referencia
   prestada*.

   Esta función está destinada principalmente para compatibilidad
   hacia atrás: se recomienda usar "Py_GetConstant()" para código
   nuevo.

   La referencia es prestada del intérprete, y es válida hasta la
   finalización del intérprete.

   Added in version 3.13.

PyObject *Py_NotImplemented

   El singleton "NotImplemented", se usa para indicar que una
   operación no está implementada para la combinación de tipos dada.

Py_RETURN_NOTIMPLEMENTED

   Maneja adecuadamente el retorno de "Py_NotImplemented" desde una
   función C (es decir, crea una nueva *referencia fuerte* a
   "NotImplemented" y lo retorna).

Py_PRINT_RAW

   Flag to be used with multiple functions that print the object (like
   "PyObject_Print()" and "PyFile_WriteObject()"). If passed, these
   functions use the "str()" of the object instead of the "repr()".

int PyObject_Print(PyObject *o, FILE *fp, int flags)

   Imprime un objeto *o*, en el archivo *fp*. Retorna "-1" en caso de
   error. El argumento de las banderas se usa para habilitar ciertas
   opciones de impresión. La única opción actualmente admitida es
   "Py_PRINT_RAW"; si se proporciona, se escribe "str()" del objeto en
   lugar de "repr()".

int PyObject_HasAttrWithError(PyObject *o, PyObject *attr_name)
    * Part of the Stable ABI since version 3.13.*

   Retorna "1" si *o* tiene el atributo *attr_name*, y "0" en caso
   contrario. Esto es equivalente a la expresión de Python "hasattr(o,
   attr_name)". En caso de error, retorna "-1".

   Added in version 3.13.

int PyObject_HasAttrStringWithError(PyObject *o, const char *attr_name)
    * Part of the Stable ABI since version 3.13.*

   Esto es lo mismo que "PyObject_HasAttrWithError()", pero
   *attr_name* se especifica como una cadena de bytes codificada en
   UTF-8 const char*, en lugar de un PyObject*.

   Added in version 3.13.

int PyObject_HasAttr(PyObject *o, PyObject *attr_name)
    * Part of the Stable ABI.*

   Retorna "1" si *o* tiene el atributo *attr_name*, y "0" en caso
   contrario. Esta función siempre tiene éxito.

   Nota:

     Exceptions that occur when this calls "__getattr__()" and
     "__getattribute__()" methods aren't propagated, but instead given
     to "sys.unraisablehook()". For proper error handling, use
     "PyObject_HasAttrWithError()", "PyObject_GetOptionalAttr()" or
     "PyObject_GetAttr()" instead.

int PyObject_HasAttrString(PyObject *o, const char *attr_name)
    * Part of the Stable ABI.*

   Esto es lo mismo que "PyObject_HasAttr()", pero *attr_name* se
   especifica como una cadena de bytes codificada en UTF-8 const
   char*, en lugar de un PyObject*.

   Nota:

     Las excepciones que ocurren cuando esto llama a los métodos
     "__getattr__()" y "__getattribute__()" o mientras se crea el
     objeto "str" temporal se ignoran silenciosamente. Para un manejo
     adecuado de errores, usa "PyObject_HasAttrStringWithError()",
     "PyObject_GetOptionalAttrString()" o "PyObject_GetAttrString()"
     en su lugar.

PyObject *PyObject_GetAttr(PyObject *o, PyObject *attr_name)
    *Return value: New reference.** Part of the Stable ABI.*

   Recupera un atributo llamado *attr_name* del objeto *o*. Retorna el
   valor del atributo en caso de éxito o "NULL" en caso de error. Este
   es el equivalente de la expresión de Python "o.attr_name".

   Si el atributo faltante no debe tratarse como un error, puedes usar
   "PyObject_GetOptionalAttr()" en su lugar.

PyObject *PyObject_GetAttrString(PyObject *o, const char *attr_name)
    *Return value: New reference.** Part of the Stable ABI.*

   Esto es lo mismo que "PyObject_GetAttr()", pero *attr_name* se
   especifica como una cadena de bytes codificada en UTF-8 const
   char*, en lugar de un PyObject*.

   Si el atributo faltante no debe tratarse como un error, puedes usar
   "PyObject_GetOptionalAttrString()" en su lugar.

int PyObject_GetOptionalAttr(PyObject *obj, PyObject *attr_name, PyObject **result);
    * Part of the Stable ABI since version 3.13.*

   Variante de "PyObject_GetAttr()" que no lanza "AttributeError" si
   el atributo no se encuentra.

   Si se encuentra el atributo, retorna "1" y establece **result* a
   una nueva *referencia fuerte* al atributo. Si no se encuentra el
   atributo, retorna "0" y establece **result* a "NULL"; el
   "AttributeError" se silencia. Si se lanza un error distinto de
   "AttributeError", retorna "-1" y establece **result* a "NULL".

   Added in version 3.13.

int PyObject_GetOptionalAttrString(PyObject *obj, const char *attr_name, PyObject **result);
    * Part of the Stable ABI since version 3.13.*

   Esto es lo mismo que "PyObject_GetOptionalAttr()", pero *attr_name*
   se especifica como una cadena de bytes codificada en UTF-8 const
   char*, en lugar de un PyObject*.

   Added in version 3.13.

PyObject *PyObject_GenericGetAttr(PyObject *o, PyObject *name)
    *Return value: New reference.** Part of the Stable ABI.*

   Función *getter* de atributo genérico que debe colocarse en la
   ranura "tp_getattro" de un objeto tipo. Busca un descriptor en el
   diccionario de clases en el MRO del objeto, así como un atributo en
   el objeto "__dict__" (si está presente). Como se describe en
   Implementando descriptores, los descriptores de datos tienen
   preferencia sobre los atributos de instancia, mientras que los
   descriptores que no son de datos no lo hacen. De lo contrario, se
   lanza un "AttributeError".

int PyObject_SetAttr(PyObject *o, PyObject *attr_name, PyObject *v)
    * Part of the Stable ABI.*

   Establece el valor del atributo llamado *attr_name*, para el objeto
   *o*, en el valor *v*. Lanza una excepción y retorna "-1" en caso de
   falla; retorna "0" en caso de éxito. Este es el equivalente de la
   declaración de Python "o.attr_name = v".

   Si *v* es "NULL", el atributo se elimina. Este comportamiento está
   deprecado en favor de usar "PyObject_DelAttr()", pero por el
   momento no hay planes de quitarlo.

int PyObject_SetAttrString(PyObject *o, const char *attr_name, PyObject *v)
    * Part of the Stable ABI.*

   Esto es lo mismo que "PyObject_SetAttr()", pero *attr_name* se
   especifica como una cadena de bytes codificada en UTF-8 const
   char*, en lugar de un PyObject*.

   Si *v* es "NULL", el atributo se elimina, sin embargo, esta
   característica está deprecada en favor de usar
   "PyObject_DelAttrString()".

   El número de diferentes nombres de atributos pasados a esta función
   debe mantenerse pequeño, generalmente usando una cadena asignada
   estáticamente como *attr_name*. Para nombres de atributos que no se
   conocen en tiempo de compilación, prefiere llamar directamente a
   "PyUnicode_FromString()" y "PyObject_SetAttr()". Para más detalles,
   consulta "PyUnicode_InternFromString()", que puede usarse
   internamente para crear un objeto clave.

int PyObject_GenericSetAttr(PyObject *o, PyObject *name, PyObject *value)
    * Part of the Stable ABI.*

   Establecimiento de atributo genérico y función de eliminación que
   está destinada a colocarse en la ranura de un objeto tipo
   "tp_setattro". Busca un descriptor de datos en el diccionario de
   clases en el MRO del objeto y, si se encuentra, tiene preferencia
   sobre la configuración o eliminación del atributo en el diccionario
   de instancias. De lo contrario, el atributo se establece o elimina
   en el objeto "__dict__" (si está presente). En caso de éxito, se
   retorna "0"; de lo contrario, se lanza un "AttributeError" y se
   retorna "-1".

int PyObject_DelAttr(PyObject *o, PyObject *attr_name)
    * Part of the Stable ABI since version 3.13.*

   Elimina el atributo llamado *attr_name*, para el objeto *o*.
   Retorna "-1" en caso de falla. Este es el equivalente de la
   declaración de Python "del o.attr_name".

int PyObject_DelAttrString(PyObject *o, const char *attr_name)
    * Part of the Stable ABI since version 3.13.*

   Esto es lo mismo que "PyObject_DelAttr()", pero *attr_name* se
   especifica como una cadena de bytes codificada en UTF-8 const
   char*, en lugar de un PyObject*.

   El número de diferentes nombres de atributos pasados a esta función
   debe mantenerse pequeño, generalmente usando una cadena asignada
   estáticamente como *attr_name*. Para nombres de atributos que no se
   conocen en tiempo de compilación, prefiere llamar directamente a
   "PyUnicode_FromString()" y "PyObject_DelAttr()". Para más detalles,
   consulta "PyUnicode_InternFromString()", que puede usarse
   internamente para crear un objeto clave para la búsqueda.

PyObject *PyObject_GenericGetDict(PyObject *o, void *context)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.10.*

   Una implementación genérica para obtener un descriptor "__dict__".
   Crea el diccionario si es necesario.

   Esta función también puede ser llamada para obtener el "__dict__"
   del objeto *o*. Se pasa *context* igual a "NULL" cuando se lo
   llama. Dado que esta función puede necesitar asignar memoria para
   el diccionario, puede ser más eficiente llamar a
   "PyObject_GetAttr()" para acceder a un atributo del objeto.

   En caso de fallo, retorna "NULL" con una excepción establecida.

   Added in version 3.3.

int PyObject_GenericSetDict(PyObject *o, PyObject *value, void *context)
    * Part of the Stable ABI since version 3.7.*

   Una implementación genérica para el creador de un descriptor
   "__dict__". Esta implementación no permite que se elimine el
   diccionario.

   Added in version 3.3.

PyObject **_PyObject_GetDictPtr(PyObject *obj)

   Retorna un puntero al "__dict__" del objeto *obj*. Si no hay
   "__dict__", retorna "NULL" sin establecer una excepción.

   Esta función puede necesitar asignar memoria para el diccionario,
   por lo que puede ser más eficiente llamar a "PyObject_GetAttr()"
   para acceder a un atributo del objeto.

PyObject *PyObject_RichCompare(PyObject *o1, PyObject *o2, int opid)
    *Return value: New reference.** Part of the Stable ABI.*

   Compara los valores de *o1* y *o2* utilizando la operación
   especificada por *opid*, que debe ser uno de "Py_LT", "Py_LE",
   "Py_EQ", "Py_NE", "Py_GT", o "Py_GE", correspondiente a "<", "<=",
   "==", "!=", ">" o ">=" respectivamente. Este es el equivalente de
   la expresión de Python "o1 op o2", donde "op" es el operador
   correspondiente a *opid*. Retorna el valor de la comparación en
   caso de éxito o "NULL" en caso de error.

int PyObject_RichCompareBool(PyObject *o1, PyObject *o2, int opid)
    * Part of the Stable ABI.*

   Compara los valores de *o1* y *o2* usando la operación especificada
   por *opid*, como "PyObject_RichCompare()", pero retorna "-1" en
   caso de error, "0" si el resultado es falso, "1" en caso contrario.

Nota:

  Si *o1* y *o2* son el mismo objeto, "PyObject_RichCompareBool()"
  siempre retornará "1" para "Py_EQ" y "0" para "Py_NE".

PyObject *PyObject_Format(PyObject *obj, PyObject *format_spec)
    * Part of the Stable ABI.*

   Formatea *obj* usando *format_spec*. Esto es equivalente a la
   expresión de Python "format(obj, format_spec)".

   *format_spec* puede ser "NULL". En este caso, la llamada es
   equivalente a "format(obj)". Retorna la cadena formateada en caso
   de éxito, "NULL" en caso de fallo.

PyObject *PyObject_Repr(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Calcula una representación de cadena de caracteres del objeto *o*.
   Retorna la representación de cadena de caracteres en caso de éxito,
   "NULL" en caso de error. Este es el equivalente de la expresión de
   Python "repr(o)". Llamado por la función incorporada "repr()".

   If argument is "NULL", return the string "'<NULL>'".

   Distinto en la versión 3.4: Esta función ahora incluye una
   afirmación de depuración para ayudar a garantizar que no descarte
   silenciosamente una excepción activa.

PyObject *PyObject_ASCII(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Como "PyObject_Repr()", calcula una representación de cadena de
   caracteres del objeto *o*, pero escapa los caracteres no ASCII en
   la cadena de caracteres retornada por "PyObject_Repr()" con "\x",
   "\u" o "\U" escapa. Esto genera una cadena de caracteres similar a
   la que retorna "PyObject_Repr()" en Python 2. Llamado por la
   función incorporada "ascii()".

   If argument is "NULL", return the string "'<NULL>'".

PyObject *PyObject_Str(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Calcula una representación de cadena de caracteres del objeto *o*.
   Retorna la representación de cadena de caracteres en caso de éxito,
   "NULL" en caso de error. Llamado por la función incorporada "str()"
   y, por lo tanto, por la función "print()".

   If argument is "NULL", return the string "'<NULL>'".

   Distinto en la versión 3.4: Esta función ahora incluye una
   afirmación de depuración para ayudar a garantizar que no descarte
   silenciosamente una excepción activa.

PyObject *PyObject_Bytes(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Calcula una representación de bytes del objeto *o*. "NULL" se
   retorna en caso de error y un objeto de bytes en caso de éxito.
   Esto es equivalente a la expresión de Python "bytes(o)", cuando *o*
   no es un número entero. A diferencia de "bytes(o)", se lanza un
   TypeError cuando *o* es un entero en lugar de un objeto de bytes
   con inicialización cero.

   If argument is "NULL", return the "bytes" object "b'<NULL>'".

int PyObject_IsSubclass(PyObject *derived, PyObject *cls)
    * Part of the Stable ABI.*

   Retorna "1" si la clase *derived* es idéntica o derivada de la
   clase *cls*; de lo contrario, retorna "0". En caso de error,
   retorna "-1".

   Si *cls* es una tupla, la verificación se realizará con cada
   entrada en *cls*. El resultado será "1" cuando al menos una de las
   verificaciones retorne "1", de lo contrario será "0".

   Si *cls* tiene un método "__subclasscheck__()", se llamará para
   determinar el estado de la subclase como se describe en **PEP
   3119**. De lo contrario, *derived* es una subclase de *cls* si es
   una subclase directa o indirecta, es decir, contenida en
   "cls.__mro__".

   Normalmente, solo los objetos de clase, es decir, instancias de
   "type" o una clase derivada, se consideran clases. Sin embargo, los
   objetos pueden anular esto al tener un atributo "__bases__" (que
   debe ser una tupla de clases base).

int PyObject_IsInstance(PyObject *inst, PyObject *cls)
    * Part of the Stable ABI.*

   Retorna "1" si *inst* es una instancia de la clase *cls* o una
   subclase de *cls*, o "0" si no. En caso de error, retorna "-1" y
   establece una excepción.

   Si *cls* es una tupla, la verificación se realizará con cada
   entrada en *cls*. El resultado será "1" cuando al menos una de las
   verificaciones retorne "1", de lo contrario será "0".

   Si *cls* tiene un método "__instancecheck__()", se llamará para
   determinar el estado de la subclase como se describe en **PEP
   3119**. De lo contrario, *inst* es una instancia de *cls* si su
   clase es una subclase de *cls*.

   Una instancia *inst* puede anular lo que se considera su clase al
   tener un atributo "__class__".

   Un objeto *cls* puede anular si se considera una clase, y cuáles
   son sus clases base, al tener un atributo "__bases__" (que debe ser
   una tupla de clases base).

Py_hash_t PyObject_Hash(PyObject *o)
    * Part of the Stable ABI.*

   Calcula y retorna el valor hash de un objeto *o*. En caso de fallo,
   retorna "-1". Este es el equivalente de la expresión de Python
   "hash(o)".

   Distinto en la versión 3.2: El tipo de retorno ahora es
   *Py_hash_t*. Este es un entero con signo del mismo tamaño que
   "Py_ssize_t".

Py_hash_t PyObject_HashNotImplemented(PyObject *o)
    * Part of the Stable ABI.*

   Establece un "TypeError" indicando que "type(o)" no es *hashable* y
   retorna "-1". Esta función recibe un tratamiento especial cuando se
   almacena en una ranura "tp_hash", lo que permite que un tipo
   indique explícitamente al intérprete que no es hashable.

int PyObject_IsTrue(PyObject *o)
    * Part of the Stable ABI.*

   Retorna "1" si el objeto *o* se considera verdadero y "0" en caso
   contrario. Esto es equivalente a la expresión de Python "not not
   o". En caso de error, retorna "-1".

int PyObject_Not(PyObject *o)
    * Part of the Stable ABI.*

   Retorna "0" si el objeto *o* se considera verdadero, y "1" de lo
   contrario. Esto es equivalente a la expresión de Python "not o". En
   caso de error, retorna "-1".

PyObject *PyObject_Type(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Cuando *o* es non-"NULL", retorna un objeto de tipo correspondiente
   al tipo de objeto del objeto *o*. En caso de fallo, lanza
   "SystemError" y retorna "NULL". Esto es equivalente a la expresión
   de Python "type(o)". Esta función crea una nueva *referencia
   fuerte* al valor de retorno. Realmente no hay razón para usar esta
   función en lugar de la función "Py_TYPE()", que retorna un puntero
   de tipo PyTypeObject*, excepto cuando se necesita una nueva
   *referencia fuerte*.

int PyObject_TypeCheck(PyObject *o, PyTypeObject *type)

   Retorna un valor no-nulo si el objeto *o* es de tipo *type* o un
   subtipo de *type*, y "0" en cualquier otro caso. Ninguno de los dos
   parámetros debe ser "NULL".

Py_ssize_t PyObject_Size(PyObject *o)
Py_ssize_t PyObject_Length(PyObject *o)
    * Part of the Stable ABI.*

   Retorna la longitud del objeto *o*. Si el objeto *o* proporciona
   los protocolos de secuencia y mapeo, se retorna la longitud de la
   secuencia. En caso de error, se retorna "-1". Este es el
   equivalente a la expresión de Python "len(o)".

Py_ssize_t PyObject_LengthHint(PyObject *o, Py_ssize_t defaultvalue)

   Retorna una longitud estimada para el objeto *o*. Primero intenta
   retornar su longitud real, luego una estimación usando
   "__length_hint__()", y finalmente retorna el valor predeterminado.
   En caso de error, retorna "-1". Este es el equivalente a la
   expresión de Python "operator.length_hint(o, defaultvalue)".

   Added in version 3.4.

PyObject *PyObject_GetItem(PyObject *o, PyObject *key)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el elemento de *o* correspondiente a la clave *key* del
   objeto o "NULL" en caso de error. Este es el equivalente de la
   expresión de Python "o[key]".

int PyObject_SetItem(PyObject *o, PyObject *key, PyObject *v)
    * Part of the Stable ABI.*

   Asigna el objeto *key* al valor *v*. Lanza una excepción y retorna
   "-1" en caso de error; retorna "0" en caso de éxito. Este es el
   equivalente de la declaración de Python "o[key] = v". Esta función
   *no* roba una referencia a *v*.

int PyObject_DelItem(PyObject *o, PyObject *key)
    * Part of the Stable ABI.*

   Elimina la asignación para el objeto *key* del objeto *o*. Retorna
   "-1" en caso de falla. Esto es equivalente a la declaración de
   Python "del o[key]".

int PyObject_DelItemString(PyObject *o, const char *key)
    * Part of the Stable ABI.*

   This is the same as "PyObject_DelItem()", but *key* is specified as
   a const char* UTF-8 encoded bytes string, rather than a PyObject*.

PyObject *PyObject_Dir(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   This is equivalent to the Python expression "dir(o)", returning a
   (possibly empty) list of strings appropriate for the object
   argument, or "NULL" if there was an error.  If the argument is
   "NULL", this is like the Python "dir()", returning the names of the
   current locals; in this case, if no execution frame is active then
   "NULL" is returned but "PyErr_Occurred()" will return false.

PyObject *PyObject_GetIter(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   This is equivalent to the Python expression "iter(o)". It returns a
   new iterator for the object argument, or the object  itself if the
   object is already an iterator.  Raises "TypeError" and returns
   "NULL" if the object cannot be iterated.

PyObject *PyObject_SelfIter(PyObject *obj)
    *Return value: New reference.** Part of the Stable ABI.*

   This is equivalent to the Python "__iter__(self): return self"
   method. It is intended for *iterator* types, to be used in the
   "PyTypeObject.tp_iter" slot.

PyObject *PyObject_GetAIter(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.10.*

   Esto es equivalente a la expresión de Python "aiter(o)". Toma un
   objeto "AsyncIterable" y retorna un "AsyncIterator". Este es
   típicamente un nuevo iterador, pero si el argumento es un
   "AsyncIterator", se retornará a sí mismo. Lanza "TypeError" y
   retorna "NULL" si el objeto no puede ser iterado.

   Added in version 3.10.

void *PyObject_GetTypeData(PyObject *o, PyTypeObject *cls)
    * Part of the Stable ABI since version 3.12.*

   Obtiene un puntero a datos específicos de subclase reservados para
   *cls*.

   El objeto *o* debe ser una instancia de *cls*, y *cls* debe haberse
   creado usando "PyType_Spec.basicsize" negativo. Python no verifica
   esto.

   En caso de error, establece una excepción y retorna "NULL".

   Added in version 3.12.

Py_ssize_t PyType_GetTypeDataSize(PyTypeObject *cls)
    * Part of the Stable ABI since version 3.12.*

   Retorna el tamaño del espacio de memoria de instancia reservado
   para *cls*, es decir, el tamaño de la memoria que retorna
   "PyObject_GetTypeData()".

   Esto puede ser mayor de lo solicitado usando
   "-PyType_Spec.basicsize"; es seguro usar este tamaño mayor (por
   ejemplo, con "memset()").

   El tipo *cls* **debe** haberse creado usando
   "PyType_Spec.basicsize" negativo. Python no verifica esto.

   En caso de error, establece una excepción y retorna un valor
   negativo.

   Added in version 3.12.

void *PyObject_GetItemData(PyObject *o)

   Obtiene un puntero a datos por elemento para una clase con
   "Py_TPFLAGS_ITEMS_AT_END".

   En caso de error, establece una excepción y retorna "NULL". Se
   lanza "TypeError" si *o* no tiene establecido
   "Py_TPFLAGS_ITEMS_AT_END".

   Added in version 3.12.

int PyObject_VisitManagedDict(PyObject *obj, visitproc visit, void *arg)

   Visita el diccionario gestionado de *obj*.

   Esta función solo debe llamarse en una función de recorrido del
   tipo que tiene la bandera "Py_TPFLAGS_MANAGED_DICT" establecida.

   Added in version 3.13.

void PyObject_ClearManagedDict(PyObject *obj)

   Limpia el diccionario gestionado de *obj*.

   This function must only be called in a clear function of the type
   which has the "Py_TPFLAGS_MANAGED_DICT" flag set.

   Added in version 3.13.

int PyUnstable_Object_EnableDeferredRefcount(PyObject *obj)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Enable deferred reference counting on *obj*, if supported by the
   runtime.  In the *free-threaded* build, this allows the interpreter
   to avoid reference count adjustments to *obj*, which may improve
   multi-threaded performance.  The tradeoff is that *obj* will only
   be deallocated by the tracing garbage collector, and not when the
   interpreter no longer has any references to it.

   This function returns "1" if deferred reference counting is enabled
   on *obj*, and "0" if deferred reference counting is not supported
   or if the hint was ignored by the interpreter, such as when
   deferred reference counting is already enabled on *obj*. This
   function is thread-safe, and cannot fail.

   This function does nothing on builds with the *GIL* enabled, which
   do not support deferred reference counting. This also does nothing
   if *obj* is not an object tracked by the garbage collector (see
   "gc.is_tracked()" and "PyObject_GC_IsTracked()").

   This function is intended to be used soon after *obj* is created,
   by the code that creates it, such as in the object's "tp_new" slot.

   Added in version 3.14.

int PyUnstable_Object_IsUniqueReferencedTemporary(PyObject *obj)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Check if *obj* is a unique temporary object. Returns "1" if *obj*
   is known to be a unique temporary object, and "0" otherwise.  This
   function cannot fail, but the check is conservative, and may return
   "0" in some cases even if *obj* is a unique temporary object.

   If an object is a unique temporary, it is guaranteed that the
   current code has the only reference to the object. For arguments to
   C functions, this should be used instead of checking if the
   reference count is "1". Starting with Python 3.14, the interpreter
   internally avoids some reference count modifications when loading
   objects onto the operands stack by *borrowing* references when
   possible, which means that a reference count of "1" by itself does
   not guarantee that a function argument uniquely referenced.

   In the example below, "my_func" is called with a unique temporary
   object as its argument:

      my_func([1, 2, 3])

   In the example below, "my_func" is **not** called with a unique
   temporary object as its argument, even if its refcount is "1":

      my_list = [1, 2, 3]
      my_func(my_list)

   See also the function "Py_REFCNT()".

   Added in version 3.14.

int PyUnstable_IsImmortal(PyObject *obj)

   *This is Unstable API. It may change without warning in minor
   releases.*

   This function returns non-zero if *obj* is *immortal*, and zero
   otherwise. This function cannot fail.

   Nota:

     Objects that are immortal in one CPython version are not
     guaranteed to be immortal in another.

   Added in version 3.14.

int PyUnstable_TryIncRef(PyObject *obj)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Increments the reference count of *obj* if it is not zero.  Returns
   "1" if the object's reference count was successfully incremented.
   Otherwise, this function returns "0".

   "PyUnstable_EnableTryIncRef()" must have been called earlier on
   *obj* or this function may spuriously return "0" in the *free-
   threaded build*.

   This function is logically equivalent to the following C code,
   except that it behaves atomically in the *free-threaded build*:

      if (Py_REFCNT(op) > 0) {
         Py_INCREF(op);
         return 1;
      }
      return 0;

   This is intended as a building block for managing weak references
   without the overhead of a Python weak reference object.

   Typically, correct use of this function requires support from
   *obj*'s deallocator ("tp_dealloc"). For example, the following
   sketch could be adapted to implement a "weakmap" that works like a
   "WeakValueDictionary" for a specific type:

      PyMutex mutex;

      PyObject *
      add_entry(weakmap_key_type *key, PyObject *value)
      {
          PyUnstable_EnableTryIncRef(value);
          weakmap_type weakmap = ...;
          PyMutex_Lock(&mutex);
          weakmap_add_entry(weakmap, key, value);
          PyMutex_Unlock(&mutex);
          Py_RETURN_NONE;
      }

      PyObject *
      get_value(weakmap_key_type *key)
      {
          weakmap_type weakmap = ...;
          PyMutex_Lock(&mutex);
          PyObject *result = weakmap_find(weakmap, key);
          if (PyUnstable_TryIncRef(result)) {
              // `result` is safe to use
              PyMutex_Unlock(&mutex);
              return result;
          }
          // if we get here, `result` is starting to be garbage-collected,
          // but has not been removed from the weakmap yet
          PyMutex_Unlock(&mutex);
          return NULL;
      }

      // tp_dealloc function for weakmap values
      void
      value_dealloc(PyObject *value)
      {
          weakmap_type weakmap = ...;
          PyMutex_Lock(&mutex);
          weakmap_remove_value(weakmap, value);

          ...
          PyMutex_Unlock(&mutex);
      }

   Added in version 3.14.

void PyUnstable_EnableTryIncRef(PyObject *obj)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Enables subsequent uses of "PyUnstable_TryIncRef()" on *obj*.  The
   caller must hold a *strong reference* to *obj* when calling this.

   Added in version 3.14.

int PyUnstable_Object_IsUniquelyReferenced(PyObject *op)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Determine if *op* only has one reference.

   On GIL-enabled builds, this function is equivalent to Py_REFCNT(op)
   == 1.

   On a *free-threaded build*, this checks if *op*'s *reference count*
   is equal to one and additionally checks if *op* is only used by
   this thread. Py_REFCNT(op) == 1 is **not** thread-safe on free-
   threaded builds; prefer this function.

   The caller must hold an *attached thread state*, despite the fact
   that this function doesn't call into the Python interpreter. This
   function cannot fail.

   Added in version 3.14.
