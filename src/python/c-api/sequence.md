---
title: Protocolo de secuencia
source_url: https://docs.python.org/es/3
source_path: c-api/sequence.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 610
---

# Protocolo de secuencia

int PySequence_Check(PyObject *o)
    * Part of the Stable ABI.*

   Return "1" if the object provides the sequence protocol, and "0"
   otherwise. Note that it returns "1" for Python classes with a
   "__getitem__()" method, unless they are "dict" subclasses, since in
   general it is impossible to determine what type of keys the class
   supports.  This function always succeeds.

Py_ssize_t PySequence_Size(PyObject *o)
Py_ssize_t PySequence_Length(PyObject *o)
    * Part of the Stable ABI.*

   Retorna el número de objetos en secuencia *o* en caso de éxito y
   "-1" en caso de error. Esto es equivalente a la expresión de Python
   "len(o)".

PyObject *PySequence_Concat(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna la concatenación de *o1* y *o2* en caso de éxito, y "NULL"
   en caso de error. Este es el equivalente de la expresión de Python
   "o1+o2".

PyObject *PySequence_Repeat(PyObject *o, Py_ssize_t count)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resultado de repetir el objeto de secuencia *o* *count*
   veces, o "NULL" en caso de falla. Este es el equivalente de la
   expresión de Python "o*count".

PyObject *PySequence_InPlaceConcat(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna la concatenación de *o1* y *o2* en caso de éxito, y "NULL"
   en caso de error. La operación se realiza en su lugar *in-place*
   cuando *o1* lo admite. Este es el equivalente de la expresión de
   Python "o1+=o2".

PyObject *PySequence_InPlaceRepeat(PyObject *o, Py_ssize_t count)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resultado de repetir el objeto de secuencia *o* *count*
   veces, o "NULL" en caso de falla. La operación se realiza en su
   lugar (*in-place*) cuando *o* lo admite. Este es el equivalente de
   la expresión de Python "o*=count".

PyObject *PySequence_GetItem(PyObject *o, Py_ssize_t i)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el elemento *i*-ésimo de *o* o "NULL" en caso de error.
   Este es el equivalente de la expresión de Python "o[i]".

PyObject *PySequence_GetSlice(PyObject *o, Py_ssize_t i1, Py_ssize_t i2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna la rebanada del objeto secuencia *o* entre *i1* y *i2*, o
   "NULL" en caso de error. Este es el equivalente de la expresión de
   Python "o[i1:i2]".

int PySequence_SetItem(PyObject *o, Py_ssize_t i, PyObject *v)
    * Part of the Stable ABI.*

   Assign object *v* to the *i*th element of *o*.  Raise an exception
   and return "-1" on failure; return "0" on success.  This is the
   equivalent of the Python statement "o[i] = v".  This function *does
   not* "*steal*" a reference to *v*.

   If *v* is "NULL", the element is deleted, but this feature is
   deprecated in favour of using "PySequence_DelItem()".

int PySequence_DelItem(PyObject *o, Py_ssize_t i)
    * Part of the Stable ABI.*

   Elimina el elemento *i*-ésimo del objeto *o*. Retorna "-1" en caso
   de falla. Este es el equivalente de la declaración de Python "del
   o[i]".

int PySequence_SetSlice(PyObject *o, Py_ssize_t i1, Py_ssize_t i2, PyObject *v)
    * Part of the Stable ABI.*

   Asigna el objeto secuencia *v* al segmento en el objeto secuencia
   *o* de *i1* a *i2*. Este es el equivalente de la declaración de
   Python "o[i1:i2]=v".

int PySequence_DelSlice(PyObject *o, Py_ssize_t i1, Py_ssize_t i2)
    * Part of the Stable ABI.*

   Elimina el segmento en el objeto secuencia *o* de *i1* a *i2*.
   Retorna "-1" en caso de falla. Este es el equivalente de la
   declaración de Python "del o[i1:i2]".

Py_ssize_t PySequence_Count(PyObject *o, PyObject *value)
    * Part of the Stable ABI.*

   Retorna el número de apariciones de *value* en *o*, es decir,
   retorna el número de claves para las que "o[clave]==value". En caso
   de fallo, retorna "-1". Esto es equivalente a la expresión de
   Python "o.count(value)".

int PySequence_Contains(PyObject *o, PyObject *value)
    * Part of the Stable ABI.*

   Determine si *o* contiene *valor*. Si un elemento en *o* es igual a
   *value*, retorna "1"; de lo contrario, retorna "0". En caso de
   error, retorna "-1". Esto es equivalente a la expresión de Python
   "value in o".

int PySequence_In(PyObject *o, PyObject *value)
    * Part of the Stable ABI.*

   Alias for "PySequence_Contains()".

   Soft deprecated since version 3.14: The function should no longer
   be used to write new code.

Py_ssize_t PySequence_Index(PyObject *o, PyObject *value)
    * Part of the Stable ABI.*

   Retorna el primer índice *i* para el que "o[i]==value". En caso de
   error, retorna "-1". Esto es equivalente a la expresión de Python
   "o.index(value)".

PyObject *PySequence_List(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un objeto lista con el mismo contenido que la secuencia o
   iterable *o*, o "NULL" en caso de error. La lista retornada está
   garantizada como nueva. Esto es equivalente a la expresión de
   Python "list(o)".

PyObject *PySequence_Tuple(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un objeto tupla con el mismo contenido que la secuencia o
   iterable *o*, o "NULL" en caso de error. Si *o* es una tupla, se
   retornará una nueva referencia; de lo contrario, se construirá una
   tupla con el contenido apropiado. Esto es equivalente a la
   expresión de Python "tupla(o)".

PyObject *PySequence_Fast(PyObject *o, const char *m)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna la secuencia o iterable *o* como un objeto utilizable por
   la otra familia de funciones "PySequence_Fast*". Si el objeto no es
   una secuencia o no es iterable, lanza "TypeError" con *m* como
   texto del mensaje. Retorna "NULL" en caso de falla.

   Las funciones "PySequence_Fast*" se denominan así porque suponen
   que *o* es un "PyTupleObject" o un "PyListObject" y acceden a los
   campos de datos de *o* directamente.

   Como detalle de implementación de CPython, si *o* ya es una
   secuencia o lista, se retornará.

Py_ssize_t PySequence_Fast_GET_SIZE(PyObject *o)

   Returns the length of *o*, assuming that *o* was returned by
   "PySequence_Fast()" and that *o* is not "NULL".  The size can also
   be retrieved by calling "PySequence_Size()" on *o*, but
   "PySequence_Fast_GET_SIZE()" is faster because it can assume *o* is
   a list or tuple.

PyObject *PySequence_Fast_GET_ITEM(PyObject *o, Py_ssize_t i)
    *Return value: Borrowed reference.*

   Retorna el elemento *i*-ésimo de *o*, suponiendo que *o* haya sido
   retornado por "PySequence_Fast()", *o* no es "NULL" y que *i* está
   dentro de los límites.

PyObject **PySequence_Fast_ITEMS(PyObject *o)

   Retorna el arreglo subyacente de punteros *PyObject*. Asume que *o*
   fue retornado por "PySequence_Fast()" y *o* no es "NULL".

   Tenga en cuenta que si una lista cambia de tamaño, la reasignación
   puede reubicar el arreglo de elementos. Por lo tanto, solo use el
   puntero de arreglo subyacente en contextos donde la secuencia no
   puede cambiar.

PyObject *PySequence_ITEM(PyObject *o, Py_ssize_t i)
    *Return value: New reference.*

   Retorna el elemento *i*-ésimo de *o* o "NULL" en caso de error. Es
   la forma más rápida de "PySequence_GetItem()" pero sin verificar
   que "PySequence_Check()" en *o* es verdadero y sin ajuste para
   índices negativos.
