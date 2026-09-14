---
title: Objetos tupla
source_url: https://docs.python.org/es/3
source_path: c-api/tuple.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 720
---

# Objetos tupla

type PyTupleObject

   Este subtipo de "PyObject" representa un objeto tupla de Python.

PyTypeObject PyTuple_Type
    * Part of the Stable ABI.*

   Esta instancia de "PyTypeObject" representa el tipo tupla de
   Python; es el mismo objeto que "tuple" en la capa de Python.

int PyTuple_Check(PyObject *p)

   Retorna verdadero si *p* es un objeto tupla o una instancia de un
   subtipo del tipo tupla. Esta función siempre finaliza con éxito.

int PyTuple_CheckExact(PyObject *p)

   Retorna verdadero si *p* es un objeto tupla pero no una instancia
   de un subtipo del tipo tupla. Esta función siempre finaliza con
   éxito.

PyObject *PyTuple_New(Py_ssize_t len)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un nuevo objeto tupla de tamaño *len*, o "NULL" con una
   excepción establecida en caso de falla.

PyObject *PyTuple_Pack(Py_ssize_t n, ...)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un nuevo objeto tupla de tamaño *n*, o "NULL" con una
   excepción establecida en caso de falla. Los valores de tupla se
   inicializan con los siguientes *n* argumentos C que apuntan a
   objetos de Python. "PyTuple_Pack(2, a, b)" es equivalente a
   "Py_BuildValue("(OO)", a, b)".

Py_ssize_t PyTuple_Size(PyObject *p)
    * Part of the Stable ABI.*

   Take a pointer to a tuple object, and return the size of that
   tuple. On error, return "-1" with an exception set.

Py_ssize_t PyTuple_GET_SIZE(PyObject *p)

   Como "PyTuple_Size()", pero sin verificación de errores.

PyObject *PyTuple_GetItem(PyObject *p, Py_ssize_t pos)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Retorna el objeto en la posición *pos* en la tupla señalada por
   *p*. Si *pos* es negativo o está fuera de los límites, retorna
   "NULL" y establece una excepción "IndexError".

   La referencia retornada es prestada de la tupla *p* (es decir: solo
   es válida mientras mantengas una referencia a *p*). Para obtener
   una *referencia fuerte*, usa "Py_NewRef(PyTuple_GetItem(...))" o
   "PySequence_GetItem()".

PyObject *PyTuple_GET_ITEM(PyObject *p, Py_ssize_t pos)
    *Return value: Borrowed reference.*

   Como "PyTuple_GetItem()", pero no verifica sus argumentos.

PyObject *PyTuple_GetSlice(PyObject *p, Py_ssize_t low, Py_ssize_t high)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna la rebanada de la tupla apuntada por *p* entre *low* y
   *high*, o "NULL" con una excepción establecida en caso de falla.

   Esto es equivalente a la expresión de Python "p[low:high]". La
   indexación desde el final de la tupla no es compatible.

int PyTuple_SetItem(PyObject *p, Py_ssize_t pos, PyObject *o)
    * Part of the Stable ABI.*

   Inserta una referencia al objeto *o* en la posición *pos* de la
   tupla señalada por *p*. Retorna "0" en caso de éxito. Si *pos* está
   fuera de límites, retorna "-1" y establece una excepción
   "IndexError".

   Nota:

     This function "*steals*" a reference to *o* and discards a
     reference to an item already in the tuple at the affected
     position (unless it was NULL).

void PyTuple_SET_ITEM(PyObject *p, Py_ssize_t pos, PyObject *o)

   Al igual que "PyTuple_SetItem()", pero no realiza ninguna
   comprobación de errores, y debe *solo* usarse para completar tuplas
   nuevas.

   La comprobación de límites se realiza como una aserción si Python
   se construye en modo de depuración o "con aserciones".

   Nota:

     This function "*steals*" a reference to *o*, and, unlike
     "PyTuple_SetItem()", does *not* discard a reference to any item
     that is being replaced; any reference in the tuple at position
     *pos* will be leaked.

   Advertencia:

     This macro should *only* be used on tuples that are newly
     created. Using this macro on a tuple that is already in use (or
     in other words, has a refcount > 1) could lead to undefined
     behavior.

int _PyTuple_Resize(PyObject **p, Py_ssize_t newsize)

   Se puede usar para cambiar el tamaño de una tupla. *newsize* será
   el nuevo tamaño de la tupla. Debido a que se *supone* que las
   tuplas son inmutables, esto solo debe usarse si solo hay una
   referencia al objeto. *No* use esto si la tupla ya puede ser
   conocida por alguna otra parte del código. La tupla siempre crecerá
   o disminuirá al final. Piense en esto como destruir la antigua
   tupla y crear una nueva, solo que de manera más eficiente. Retorna
   "0" en caso de éxito. El código del cliente nunca debe suponer que
   el valor resultante de "*p" será el mismo que antes de llamar a
   esta función. Si se reemplaza el objeto referenciado por "*p", se
   destruye el original "*p". En caso de fallo, retorna "-1" y
   establece "*p" en "NULL", y lanza "MemoryError" o "SystemError".

# Objetos de secuencia de estructura

Los objetos de secuencia de estructura son el equivalente en C de los
objetos "namedtuple()", es decir, una secuencia a cuyos elementos
también se puede acceder a través de atributos. Para crear una
secuencia de estructura, primero debe crear un tipo de secuencia de
estructura específico.

PyTypeObject *PyStructSequence_NewType(PyStructSequence_Desc *desc)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un nuevo tipo de secuencia de estructura a partir de los datos
   en *desc*, que se describen a continuación. Las instancias del tipo
   resultante se pueden crear con "PyStructSequence_New()".

   Retorna "NULL" con una excepción establecida en caso de falla.

void PyStructSequence_InitType(PyTypeObject *type, PyStructSequence_Desc *desc)

   Inicializa una secuencia de estructura tipo *type* desde *desc* en
   su lugar.

int PyStructSequence_InitType2(PyTypeObject *type, PyStructSequence_Desc *desc)

   Como "PyStructSequence_InitType()", pero retorna "0" en caso de
   éxito y "-1" con una excepción establecida en caso de falla.

   Added in version 3.4.

type PyStructSequence_Desc
    * Part of the Stable ABI (including all members).*

   Contiene la meta información de un tipo de secuencia de estructura
   para crear.

   const char *name

      Fully qualified name of the type; null-terminated UTF-8 encoded.
      The name must contain the module name.

   const char *doc

      Puntero al *docstring* para el tipo o "NULL" para omitir

   PyStructSequence_Field *fields

      Puntero al arreglo terminado en "NULL" con nombres de campo del
      nuevo tipo

   int n_in_sequence

      Cantidad de campos visibles para el lado de Python (si se usa
      como tupla)

type PyStructSequence_Field
    * Part of the Stable ABI (including all members).*

   Describe un campo de una secuencia de estructura. Como una
   secuencia de estructura se modela como una tupla, todos los campos
   se escriben como PyObject*. El índice en el arreglo "fields" de
   "PyStructSequence_Desc" determina qué campo de la secuencia de
   estructura se describe.

   const char *name

      Nombre para el campo o "NULL" para finalizar la lista de campos
      con nombre, establece en "PyStructSequence_UnnamedField" para
      dejar sin nombre

   const char *doc

      Campo *docstring* o "NULL" para omitir

const char *const PyStructSequence_UnnamedField
    * Part of the Stable ABI since version 3.11.*

   Valor especial para un nombre de campo para dejarlo sin nombre.

   Distinto en la versión 3.9: El tipo se cambió de "char *".

PyObject *PyStructSequence_New(PyTypeObject *type)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea una instancia de *type*, que debe haberse creado con
   "PyStructSequence_NewType()".

   Retorna "NULL" con una excepción establecida en caso de falla.

PyObject *PyStructSequence_GetItem(PyObject *p, Py_ssize_t pos)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Retorna el objeto en la posición *pos* en la secuencia de
   estructura apuntada por *p*.

   La comprobación de límites se realiza como una aserción si Python
   se construye en modo de depuración o "con aserciones".

PyObject *PyStructSequence_GET_ITEM(PyObject *p, Py_ssize_t pos)
    *Return value: Borrowed reference.*

   Alias de "PyStructSequence_GetItem()".

   Distinto en la versión 3.13: Ahora implementado como un alias de
   "PyStructSequence_GetItem()".

void PyStructSequence_SetItem(PyObject *p, Py_ssize_t pos, PyObject *o)
    * Part of the Stable ABI.*

   Establece el campo en el índice *pos* de la secuencia de estructura
   *p* en el valor *o*. Como "PyTuple_SET_ITEM()", esto solo debe
   usarse para completar instancias nuevas.

   La comprobación de límites se realiza como una aserción si Python
   se construye en modo de depuración o "con aserciones".

   Nota:

     This function "*steals*" a reference to *o*.

void PyStructSequence_SET_ITEM(PyObject *p, Py_ssize_t *pos, PyObject *o)

   Alias de "PyStructSequence_SetItem()".

   Distinto en la versión 3.13: Ahora implementado como un alias de
   "PyStructSequence_SetItem()".
