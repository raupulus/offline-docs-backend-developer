---
title: '3. Definición de tipos de extensión: temas variados'
source_url: https://docs.python.org/es/3
source_path: extending/newtypes.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: extending
order: 1010
---

# 3. Definición de tipos de extensión: temas variados

Esta sección tiene como objetivo dar un vistazo rápido a los diversos
métodos de tipo que puede implementar y lo que hacen.

Aquí está la definición de "PyTypeObject", con algunos campos que solo
se usan en las versiones de depuración omitidas:

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

Esos son *muchos* métodos. Sin embargo, no se preocupe demasiado: si
tiene un tipo que desea definir, es muy probable que solo implemente
un puñado de estos.

Como probablemente espera ahora, vamos a repasar esto y daremos más
información sobre los diversos controladores. No iremos en el orden en
que se definen en la estructura, porque hay mucho equipaje histórico
que afecta el orden de los campos. A menudo es más fácil encontrar un
ejemplo que incluya los campos que necesita y luego cambiar los
valores para adaptarlos a su nuevo tipo.

   const char *tp_name; /* For printing */

El nombre del tipo -- como se mencionó en el capítulo anterior,
aparecerá en varios lugares, casi por completo para fines de
diagnóstico. ¡Intente elegir algo que sea útil en tal situación!

   Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */

Estos campos le dicen al tiempo de ejecución cuánta memoria asignar
cuando se crean nuevos objetos de este tipo. Python tiene algún
soporte incorporado para estructuras de longitud variable (piense:
cadenas, tuplas) que es donde entra el campo "tp_itemsize". Esto se
tratará más adelante.

   const char *tp_doc;

Aquí puede poner una cadena de caracteres (o su dirección) que desea
que se retorne cuando el script de Python haga referencia a
"obj.__doc__" para recuperar el docstring.

Ahora llegamos a los métodos de tipo básicos: los que implementarán la
mayoría de los tipos de extensión.

## 3.1. Finalización y desasignación

   destructor tp_dealloc;

Se llama a esta función cuando el recuento de referencia de la
instancia de su tipo se reduce a cero y el intérprete de Python quiere
reclamarlo. Si su tipo tiene memoria para liberar u otra limpieza para
realizar, puede ponerla aquí. El objeto en sí mismo necesita ser
liberado aquí también. Aquí hay un ejemplo de esta función:

   static void
   newdatatype_dealloc(PyObject *op)
   {
       newdatatypeobject *self = (newdatatypeobject *) op;
       free(self->obj_UnderlyingDatatypePtr);
       Py_TYPE(self)->tp_free(self);
   }

Si su tipo admite la recolección de basura, el destructor debe llamar
a "PyObject_GC_UnTrack()" antes de borrar cualquier campo miembro:

   static void
   newdatatype_dealloc(PyObject *op)
   {
       newdatatypeobject *self = (newdatatypeobject *) op;
       PyObject_GC_UnTrack(op);
       Py_CLEAR(self->other_obj);
       ...
       Py_TYPE(self)->tp_free(self);
   }

Un requisito importante de la función desasignador es que deja solo
las excepciones pendientes. Esto es importante ya que los
desasignadores se llaman con frecuencia cuando el intérprete
desenrolla la pila de Python; cuando la pila se desenrolla debido a
una excepción (en lugar de retornos normales), no se hace nada para
proteger a los desasignadores de memoria (*deallocator*) de ver que ya
se ha establecido una excepción. Cualquier acción que realice un
desasignador que pueda hacer que se ejecute código Python adicional
puede detectar que se ha establecido una excepción. Esto puede
conducir a errores engañosos del intérprete. La forma correcta de
protegerse contra esto es guardar una excepción pendiente antes de
realizar la acción insegura y restaurarla cuando haya terminado. Esto
se puede hacer usando las funciones "PyErr_Fetch()" y
"PyErr_Restore()":

   static void
   my_dealloc(PyObject *obj)
   {
       MyObject *self = (MyObject *) obj;
       PyObject *cbresult;

       if (self->my_callback != NULL) {
           PyObject *err_type, *err_value, *err_traceback;

           /* This saves the current exception state */
           PyErr_Fetch(&err_type, &err_value, &err_traceback);

           cbresult = PyObject_CallNoArgs(self->my_callback);
           if (cbresult == NULL) {
              PyErr_WriteUnraisable(self->my_callback);
           }
           else {
               Py_DECREF(cbresult);
           }

           /* This restores the saved exception state */
           PyErr_Restore(err_type, err_value, err_traceback);

           Py_DECREF(self->my_callback);
       }
       Py_TYPE(self)->tp_free(self);
   }

Nota:

  Existen limitaciones para lo que puede hacer de manera segura en una
  función de desasignación. Primero, si su tipo admite la recolección
  de basura (usando "tp_traverse" o "tp_clear"), algunos de los
  miembros del objeto pueden haber sido borrados o finalizados por el
  time "tp_dealloc" es llamado. Segundo, en "tp_dealloc", su objeto
  está en un estado inestable: su recuento de referencia es igual a
  cero. Cualquier llamada a un objeto o API no trivial (como en el
  ejemplo anterior) podría terminar llamando "tp_dealloc" nuevamente,
  causando una doble liberación y un bloqueo.Comenzando con Python
  3.4, se recomienda no poner ningún código de finalización complejo
  en "tp_dealloc", y en su lugar use el nuevo método de tipo
  "tp_finalize".

  Ver también: **PEP 442** explica el nuevo esquema de finalización.

## 3.2. Presentación de objetos

En Python, hay dos formas de generar una representación textual de un
objeto: la función "repr()", y la función "str()". (La función
"print()" solo llama a "str()".) Estos controladores son opcionales.

   reprfunc tp_repr;
   reprfunc tp_str;

El manejador "tp_repr" debe retornar un objeto de cadena que contenga
una representación de la instancia para la que se llama. Aquí hay un
ejemplo simple:

   static PyObject *
   newdatatype_repr(PyObject *op)
   {
       newdatatypeobject *self = (newdatatypeobject *) op;
       return PyUnicode_FromFormat("Repr-ified_newdatatype{{size:%d}}",
                                   self->obj_UnderlyingDatatypePtr->size);
   }

Si no se especifica un controlador "tp_repr", el intérprete
proporcionará una representación que utiliza el "tp_name" del tipo y
un valor de identificación exclusivo para el objeto.

El manejador "tp_str" es para "str()" lo que el manejador "tp_repr"
descrito arriba es para "repr()"; es decir, se llama cuando el código
Python llama "str()" en una instancia de su objeto. Su implementación
es muy similar a la función "tp_repr", pero la cadena resultante está
destinada al consumo humano. Si "tp_str" no se especifica, en su lugar
se utiliza el controlador "tp_repr".

Aquí hay un ejemplo simple:

   static PyObject *
   newdatatype_str(PyObject *op)
   {
       newdatatypeobject *self = (newdatatypeobject *) op;
       return PyUnicode_FromFormat("Stringified_newdatatype{{size:%d}}",
                                   self->obj_UnderlyingDatatypePtr->size);
   }

## 3.3. Gestión de atributos

Para cada objeto que puede soportar atributos, el tipo correspondiente
debe proporcionar las funciones que controlan cómo se resuelven los
atributos. Es necesario que haya una función que pueda recuperar
atributos (si hay alguna definida), y otra para establecer atributos
(si se permite establecer atributos). La eliminación de un atributo es
un caso especial, para el cual el nuevo valor pasado al controlador es
"NULL".

Python admite dos pares de controladores de atributos; un tipo que
admite atributos solo necesita implementar las funciones para un par.
La diferencia es que un par toma el nombre del atributo como char*,
mientras que el otro acepta un PyObject*. Cada tipo puede usar
cualquier par que tenga más sentido para la conveniencia de la
implementación.

   getattrfunc  tp_getattr;        /* char * version */
   setattrfunc  tp_setattr;
   /* ... */
   getattrofunc tp_getattro;       /* PyObject * version */
   setattrofunc tp_setattro;

Si acceder a los atributos de un objeto siempre es una operación
simple (esto se explicará en breve), existen implementaciones
genéricas que se pueden usar para proporcionar la versión PyObject* de
las funciones de administración de atributos. La necesidad real de
controladores de atributos específicos de tipo desapareció casi por
completo a partir de Python 2.2, aunque hay muchos ejemplos que no se
han actualizado para usar algunos de los nuevos mecanismos genéricos
disponibles.

### 3.3.1. Gestión de atributos genéricos

La mayoría de los tipos de extensión solo usan atributos *simple*.
Entonces, ¿qué hace que los atributos sean simples? Solo hay un par de
condiciones que se deben cumplir:

1. El nombre de los atributos debe ser conocido cuando
   "PyType_Ready()" es llamado.

2. No se necesita un procesamiento especial para registrar que un
   atributo se buscó o se configuró, ni se deben tomar acciones
   basadas en el valor.

Tenga en cuenta que esta lista no impone restricciones a los valores
de los atributos, cuándo se calculan los valores o cómo se almacenan
los datos relevantes.

Cuando se llama a "PyType_Ready()", utiliza tres tablas a las que hace
referencia el objeto de tipo para crear *descriptor* que se colocan en
el diccionario del objeto de tipo. Cada descriptor controla el acceso
a un atributo del objeto de instancia. Cada una de las tablas es
opcional; si los tres son "NULL", las instancias del tipo solo tendrán
atributos que se heredan de su tipo base, y deberían dejar
"tp_getattro" y los campos "tp_setattro" "NULL" también, permitiendo
que el tipo base maneje los atributos.

Las tablas se declaran como tres campos del tipo objeto:

   struct PyMethodDef *tp_methods;
   struct PyMemberDef *tp_members;
   struct PyGetSetDef *tp_getset;

Si "tp_methods" no es "NULL", debe referirse a un arreglo de
estructuras "PyMethodDef". Cada entrada en la tabla es una instancia
de esta estructura:

   typedef struct PyMethodDef {
       const char  *ml_name;       /* method name */
       PyCFunction  ml_meth;       /* implementation function */
       int          ml_flags;      /* flags */
       const char  *ml_doc;        /* docstring */
   } PyMethodDef;

One entry should be defined for each method provided by the type; no
entries are needed for methods inherited from a base type.  One
additional entry is needed at the end; it is a sentinel that marks the
end of the array.  The "ml_name" field of the sentinel must be "NULL".

La segunda tabla se utiliza para definir atributos que se asignan
directamente a los datos almacenados en la instancia. Se admite una
variedad de tipos C primitivos, y el acceso puede ser de solo lectura
o lectura-escritura. Las estructuras en la tabla se definen como:

   typedef struct PyMemberDef {
       const char *name;
       int         type;
       int         offset;
       int         flags;
       const char *doc;
   } PyMemberDef;

For each entry in the table, a *descriptor* will be constructed and
added to the type which will be able to extract a value from the
instance structure.  The "type" field should contain a type code like
"Py_T_INT" or "Py_T_DOUBLE"; the value will be used to determine how
to convert Python values to and from C values.  The "flags" field is
used to store flags which control how the attribute can be accessed:
you can set it to "Py_READONLY" to prevent Python code from setting
it.

An interesting advantage of using the "tp_members" table to build
descriptors that are used at runtime is that any attribute defined
this way can have an associated doc string simply by providing the
text in the table.  An application can use the introspection API to
retrieve the descriptor from the class object, and get the doc string
using its "__doc__" attribute.

As with the "tp_methods" table, a sentinel entry with a "ml_name"
value of "NULL" is required.

### 3.3.2. Gestión de atributos específicos de tipo

Para simplificar, solo la versión char* será demostrada aquí; el tipo
del parámetro con nombre es la única diferencia entre char* y
PyObject* de la interfaz. Este ejemplo efectivamente hace lo mismo que
el ejemplo genérico anterior, pero no usa el soporte genérico agregado
en Python 2.2. Explica cómo se llaman las funciones del controlador,
de modo que si necesita ampliar su funcionalidad, comprenderá lo que
debe hacerse.

The "tp_getattr" handler is called when the object requires an
attribute look-up.  It is called in the same situations where the
"__getattr__()" method of a class would be called.

Aquí hay un ejemplo:

   static PyObject *
   newdatatype_getattr(PyObject *op, char *name)
   {
       newdatatypeobject *self = (newdatatypeobject *) op;
       if (strcmp(name, "data") == 0) {
           return PyLong_FromLong(self->data);
       }

       PyErr_Format(PyExc_AttributeError,
                    "'%.100s' object has no attribute '%.400s'",
                    Py_TYPE(self)->tp_name, name);
       return NULL;
   }

The "tp_setattr" handler is called when the "__setattr__()" or
"__delattr__()" method of a class instance would be called.  When an
attribute should be deleted, the third parameter will be "NULL".  Here
is an example that simply raises an exception; if this were really all
you wanted, the "tp_setattr" handler should be set to "NULL".

   static int
   newdatatype_setattr(PyObject *op, char *name, PyObject *v)
   {
       PyErr_Format(PyExc_RuntimeError, "Read-only attribute: %s", name);
       return -1;
   }

## 3.4. Comparación de Objetos

   richcmpfunc tp_richcompare;

The "tp_richcompare" handler is called when comparisons are needed.
It is analogous to the rich comparison methods, like "__lt__()", and
also called by "PyObject_RichCompare()" and
"PyObject_RichCompareBool()".

Esta función se llama con dos objetos de Python y el operador como
argumentos, donde el operador es uno de "Py_EQ", "Py_NE", "Py_LE",
"Py_GE", "Py_LT" o "Py_GT". Debe comparar los dos objetos con respecto
al operador especificado y retornar "Py_True" o "Py_False" si la
comparación es exitosa, "Py_NotImplemented" para indicar que la
comparación no está implementada y se debe probar el método de
comparación del otro objeto, o "NULL" si se estableció una excepción.

Aquí hay una implementación de muestra, para un tipo de datos que se
considera igual si el tamaño de un puntero interno es igual:

   static PyObject *
   newdatatype_richcmp(PyObject *lhs, PyObject *rhs, int op)
   {
       newdatatypeobject *obj1 = (newdatatypeobject *) lhs;
       newdatatypeobject *obj2 = (newdatatypeobject *) rhs;
       PyObject *result;
       int c, size1, size2;

       /* code to make sure that both arguments are of type
          newdatatype omitted */

       size1 = obj1->obj_UnderlyingDatatypePtr->size;
       size2 = obj2->obj_UnderlyingDatatypePtr->size;

       switch (op) {
       case Py_LT: c = size1 <  size2; break;
       case Py_LE: c = size1 <= size2; break;
       case Py_EQ: c = size1 == size2; break;
       case Py_NE: c = size1 != size2; break;
       case Py_GT: c = size1 >  size2; break;
       case Py_GE: c = size1 >= size2; break;
       }
       result = c ? Py_True : Py_False;
       return Py_NewRef(result);
    }

## 3.5. Soporte de protocolo abstracto

Python admite una variedad de protocolos *abstractos*; las interfaces
específicas proporcionadas para usar estas interfaces están
documentadas en Capa de objetos abstractos.

Varias de estas interfaces abstractas se definieron temprano en el
desarrollo de la implementación de Python. En particular, los
protocolos de número, mapeo y secuencia han sido parte de Python desde
el principio. Se han agregado otros protocolos con el tiempo. Para los
protocolos que dependen de varias rutinas de controlador de la
implementación de tipo, los protocolos más antiguos se han definido
como bloques opcionales de controladores a los que hace referencia el
objeto de tipo. Para los protocolos más nuevos, hay espacios
adicionales en el objeto de tipo principal, con un bit de marca que se
establece para indicar que los espacios están presentes y el
intérprete debe verificarlos. (El bit de indicador no indica que los
valores de intervalo no son "NULL". El indicador puede establecerse
para indicar la presencia de un intervalo, pero un intervalo aún puede
estar vacío.):

   PyNumberMethods   *tp_as_number;
   PySequenceMethods *tp_as_sequence;
   PyMappingMethods  *tp_as_mapping;

Si desea que su objeto pueda actuar como un número, una secuencia o un
objeto de mapeo, entonces coloca la dirección de una estructura que
implementa el tipo C "PyNumberMethods", "PySequenceMethods", o
"PyMappingMethods", respectivamente. Depende de usted completar esta
estructura con los valores apropiados. Puede encontrar ejemplos del
uso de cada uno de estos en el directorio "Objects" de la distribución
fuente de Python.

   hashfunc tp_hash;

Esta función, si elige proporcionarla, debería retornar un número hash
para una instancia de su tipo de datos. Aquí hay un ejemplo simple:

   static Py_hash_t
   newdatatype_hash(PyObject *op)
   {
       newdatatypeobject *self = (newdatatypeobject *) op;
       Py_hash_t result;
       result = self->some_size + 32767 * self->some_number;
       if (result == -1) {
           result = -2;
       }
       return result;
   }

"Py_hash_t" es un tipo entero con signo con un ancho que varia
dependiendo de la plataforma.retornar "-1" de "tp_hash" indica un
error, por lo que debe tener cuidado de evitar retornarlo cuando el
cálculo de hash sea exitoso, como se vio anteriormente.

   ternaryfunc tp_call;

Esta función se llama cuando una instancia de su tipo de datos se
"llama", por ejemplo, si "obj1" es una instancia de su tipo de datos y
el script de Python contiene "obj1('hello')", el controlador "tp_call"
se invoca.

Esta función toma tres argumentos:

1. *self* es la instancia del tipo de datos que es el sujeto de la
   llamada. Si la llamada es "obj1('hola')", entonces *self* es
   "obj1".

2. *args* es una tupla que contiene los argumentos de la llamada.
   Puede usar "PyArg_ParseTuple()" para extraer los argumentos.

3. *kwds* es un diccionario de argumentos de palabras clave que se
   pasaron. Si no es "NULL" y admite argumentos de palabras clave, use
   "PyArg_ParseTupleAndKeywords()" para extraer los argumentos. Si no
   desea admitir argumentos de palabras clave y esto no es "NULL",
   genere un "TypeError" con un mensaje que indique que los argumentos
   de palabras clave no son compatibles.

Aquí hay una implementación de juguete "tp_call":

   static PyObject *
   newdatatype_call(PyObject *op, PyObject *args, PyObject *kwds)
   {
       newdatatypeobject *self = (newdatatypeobject *) op;
       PyObject *result;
       const char *arg1;
       const char *arg2;
       const char *arg3;

       if (!PyArg_ParseTuple(args, "sss:call", &arg1, &arg2, &arg3)) {
           return NULL;
       }
       result = PyUnicode_FromFormat(
           "Returning -- value: [%d] arg1: [%s] arg2: [%s] arg3: [%s]\n",
           self->obj_UnderlyingDatatypePtr->size,
           arg1, arg2, arg3);
       return result;
   }

   /* Iterators */
   getiterfunc tp_iter;
   iternextfunc tp_iternext;

These functions provide support for the iterator protocol.  Both
handlers take exactly one parameter, the instance for which they are
being called, and return a new reference.  In the case of an error,
they should set an exception and return "NULL".  "tp_iter" corresponds
to the Python "__iter__()" method, while "tp_iternext" corresponds to
the Python "__next__()" method.

Cualquier objeto *iterable* debe implementar el manejador "tp_iter",
que debe retornar un objeto *iterator*. Aquí se aplican las mismas
pautas que para las clases de Python:

* Para colecciones (como listas y tuplas) que pueden admitir múltiples
  iteradores independientes, cada llamada debe crear y retornar un
  nuevo iterador a "tp_iter".

* Los objetos que solo se pueden iterar una vez (generalmente debido a
  los efectos secundarios de la iteración, como los objetos de
  archivo) pueden implementar "tp_iter" retornando una nueva
  referencia a ellos mismos y, por lo tanto, también deben implementar
  el manejador "tp_iternext".

Cualquier objeto *iterator* debe implementar tanto "tp_iter" como
"tp_iternext". El manejador de un iterador "tp_iter" debería retornar
una nueva referencia al iterador. Su controlador "tp_iternext" debería
retornar una nueva referencia al siguiente objeto en la iteración, si
hay uno. Si la iteración ha llegado al final, "tp_iternext" puede
retornar "NULL" sin establecer una excepción, o puede establecer
"StopIteration" *además* para retornar "NULL"; evitar la excepción
puede producir un rendimiento ligeramente mejor. Si se produce un
error real, "tp_iternext" siempre debe establecer una excepción y
retornar "NULL".

## 3.6. Soporte de referencia débil

Uno de los objetivos de la implementación de referencia débil de
Python es permitir que cualquier tipo participe en el mecanismo de
referencia débil sin incurrir en la sobrecarga de objetos críticos
para el rendimiento (como los números).

Ver también: Documentación para el módulo "weakref".

For an object to be weakly referenceable, the extension type must set
the "Py_TPFLAGS_MANAGED_WEAKREF" bit of the "tp_flags" field. The
legacy "tp_weaklistoffset" field should be left as zero.

Concretely, here is how the statically declared type object would
look:

   static PyTypeObject TrivialType = {
       PyVarObject_HEAD_INIT(NULL, 0)
       /* ... other members omitted for brevity ... */
       .tp_flags = Py_TPFLAGS_MANAGED_WEAKREF | ...,
   };

The only further addition is that "tp_dealloc" needs to clear any weak
references (by calling "PyObject_ClearWeakRefs()"):

   static void
   Trivial_dealloc(PyObject *op)
   {
       /* Clear weakrefs first before calling any destructors */
       PyObject_ClearWeakRefs(op);
       /* ... remainder of destruction code omitted for brevity ... */
       Py_TYPE(op)->tp_free(op);
   }

## 3.7. Más Sugerencias

Para aprender a implementar cualquier método específico para su nuevo
tipo de datos, obtenga el código fuente *CPython*. Vaya al directorio
"Objects", luego busque en los archivos fuente C "tp_" más la función
que desee (por ejemplo, "tp_richcompare"). Encontrará ejemplos de la
función que desea implementar.

Cuando necesite verificar que un objeto es una instancia concreta del
tipo que está implementando, use la función "PyObject_TypeCheck()".
Una muestra de su uso podría ser algo como lo siguiente:

   if (!PyObject_TypeCheck(some_object, &MyType)) {
       PyErr_SetString(PyExc_TypeError, "arg #1 not a mything");
       return NULL;
   }

Ver también:

  Descargue las versiones de origen de CPython.
     https://www.python.org/downloads/source/

  El proyecto CPython en GitHub, donde se desarrolla el código fuente
  de CPython.
     https://github.com/python/cpython
