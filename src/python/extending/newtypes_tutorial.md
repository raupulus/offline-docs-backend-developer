---
title: '2. Definición de tipos de extensión: Tutorial'
source_url: https://docs.python.org/es/3
source_path: extending/newtypes_tutorial.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: extending
order: 1020
---

# 2. Definición de tipos de extensión: Tutorial

Python le permite al escritor de un módulo de extensión C definir
nuevos tipos que pueden ser manipulados desde el código Python, al
igual que los tipos incorporados "str" y "list". El código para todos
los tipos de extensión sigue un patrón, pero hay algunos detalles que
debe comprender antes de comenzar. Este documento es una introducción
suave al tema.

## 2.1. Lo básico

The *CPython* runtime sees all Python objects as variables of type
PyObject*, which serves as a "base type" for all Python objects. The
"PyObject" structure itself only contains the object's *reference
count* and a pointer to the object's "type object". This is where the
action is; the type object determines which (C) functions get called
by the interpreter when, for instance, an attribute gets looked up on
an object, a method called, or it is multiplied by another object.
These C functions are called "type methods".

Por lo tanto, si desea definir un nuevo tipo de extensión, debe crear
un nuevo objeto de tipo.

This sort of thing can only be explained by example, so here's a
minimal, but complete, module that defines a new type named "Custom"
inside a C extension module "custom":

Nota:

  Lo que estamos mostrando aquí es la forma tradicional de definir
  tipos de extensión *estáticos*. Debe ser adecuado para la mayoría de
  los usos. La API de C también permite definir tipos de extensiones
  asignadas en el montón utilizando la función "PyType_FromSpec()",
  que no se trata en este tutorial.

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>

   typedef struct {
       PyObject_HEAD
       /* Type-specific fields go here. */
   } CustomObject;

   static PyTypeObject CustomType = {
       .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "custom.Custom",
       .tp_doc = PyDoc_STR("Custom objects"),
       .tp_basicsize = sizeof(CustomObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT,
       .tp_new = PyType_GenericNew,
   };

   static int
   custom_module_exec(PyObject *m)
   {
       if (PyType_Ready(&CustomType) < 0) {
           return -1;
       }

       if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
           return -1;
       }

       return 0;
   }

   static PyModuleDef_Slot custom_module_slots[] = {
       {Py_mod_exec, custom_module_exec},
       // Just use this while using static types
       {Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
       {0, NULL}
   };

   static PyModuleDef custom_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "custom",
       .m_doc = "Example module that creates an extension type.",
       .m_size = 0,
       .m_slots = custom_module_slots,
   };

   PyMODINIT_FUNC
   PyInit_custom(void)
   {
       return PyModuleDef_Init(&custom_module);
   }

Ahora, eso es bastante para asimilar a la vez, pero espero que los
fragmentos le resulten familiares del capítulo anterior. Este archivo
define tres cosas:

1. What a "Custom" **object** contains: this is the "CustomObject"
   struct, which is allocated once for each "Custom" instance.

2. How the "Custom" **type** behaves: this is the "CustomType" struct,
   which defines a set of flags and function pointers that the
   interpreter inspects when specific operations are requested.

3. How to define and execute the "custom" module: this is the
   "PyInit_custom" function and the associated "custom_module" struct
   for defining the module, and the "custom_module_exec" function to
   set up a fresh module object.

La primera parte es:

   typedef struct {
       PyObject_HEAD
   } CustomObject;

This is what a Custom object will contain.  "PyObject_HEAD" is
mandatory at the start of each object struct and defines a field
called "ob_base" of type "PyObject", containing a pointer to a type
object and a reference count (these can be accessed using the macros
"Py_TYPE" and "Py_REFCNT" respectively).  The reason for the macro is
to abstract away the layout and to enable additional fields in debug
builds.

Nota:

  No hay punto y coma (;) arriba después de la macro "PyObject_HEAD".
  Tenga cuidado de agregar uno por accidente: algunos compiladores se
  quejarán.

Por supuesto, los objetos generalmente almacenan datos adicionales
además del estándar "PyObject_HEAD" repetitivo; por ejemplo, aquí está
la definición de puntos flotantes del estándar de Python:

   typedef struct {
       PyObject_HEAD
       double ob_fval;
   } PyFloatObject;

La segunda parte es la definición del tipo de objeto.

   static PyTypeObject CustomType = {
       .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "custom.Custom",
       .tp_doc = PyDoc_STR("Custom objects"),
       .tp_basicsize = sizeof(CustomObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT,
       .tp_new = PyType_GenericNew,
   };

Nota:

  Recomendamos utilizar los inicializadores designados al estilo C99
  como se indica arriba, para evitar enumerar todos los campos
  "PyTypeObject" que no le interesan y también para evitar preocuparse
  por el orden de declaración de los campos.

La definición real de "PyTypeObject" en "object.h" tiene muchos más
campos que la definición anterior. El compilador de C rellenará los
campos restantes con ceros, y es una práctica común no especificarlos
explícitamente a menos que los necesite.

Lo vamos a separar, un campo a la vez:

   .ob_base = PyVarObject_HEAD_INIT(NULL, 0)

Esta línea es obligatoria para inicializar el campo "ob_base"
mencionado anteriormente.

   .tp_name = "custom.Custom",

El nombre de nuestro tipo. Esto aparecerá en la representación textual
predeterminada de nuestros objetos y en algunos mensajes de error, por
ejemplo:

   >>> "" + custom.Custom()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: can only concatenate str (not "custom.Custom") to str

Note that the name is a dotted name that includes both the module name
and the name of the type within the module. The module in this case is
"custom" and the type is "Custom", so we set the type name to
"custom.Custom". Using the real dotted import path is important to
make your type compatible with the "pydoc" and "pickle" modules.

   .tp_basicsize = sizeof(CustomObject),
   .tp_itemsize = 0,

This is so that Python knows how much memory to allocate when creating
new "Custom" instances.  "tp_itemsize" is only used for variable-sized
objects and should otherwise be zero.

Nota:

  If you want your type to be subclassable from Python, and your type
  has the same "tp_basicsize" as its base type, you may have problems
  with multiple inheritance.  A Python subclass of your type will have
  to list your type first in its "__bases__", or else it will not be
  able to call your type's "__new__()" method without getting an
  error.  You can avoid this problem by ensuring that your type has a
  larger value for "tp_basicsize" than its base type does.  Most of
  the time, this will be true anyway, because either your base type
  will be "object", or else you will be adding data members to your
  base type, and therefore increasing its size.

We set the class flags to "Py_TPFLAGS_DEFAULT".

   .tp_flags = Py_TPFLAGS_DEFAULT,

Todos los tipos deben incluir esta constante en sus banderas. Habilita
todos los miembros definidos hasta al menos Python 3.3. Si necesita
más miembros, necesitará O (*OR*) las banderas correspondientes.

Proporcionamos una cadena de documentos para el tipo en "tp_doc".

   .tp_doc = PyDoc_STR("Custom objects"),

To enable object creation, we have to provide a "tp_new" handler.
This is the equivalent of the Python method "__new__()", but has to be
specified explicitly.  In this case, we can just use the default
implementation provided by the API function "PyType_GenericNew()".

   .tp_new = PyType_GenericNew,

Everything else in the file should be familiar, except for some code
in "custom_module_exec()":

   if (PyType_Ready(&CustomType) < 0) {
       return -1;
   }

This initializes the "Custom" type, filling in a number of members to
the appropriate default values, including "ob_type" that we initially
set to "NULL".

   if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
       return -1;
   }

This adds the type to the module dictionary.  This allows us to create
"Custom" instances by calling the "Custom" class:

   >>> import custom
   >>> mycustom = custom.Custom()

That's it!  All that remains is to build it; put the above code in a
file called "custom.c",

   [build-system]
   requires = ["setuptools"]
   build-backend = "setuptools.build_meta"

   [project]
   name = "custom"
   version = "1"

in a file called "pyproject.toml", and

   from setuptools import Extension, setup
   setup(ext_modules=[Extension("custom", ["custom.c"])])

en un archivo llamado "setup.py"; luego escribiendo

   $ python -m pip install .

in a shell should produce a file "custom.so" in a subdirectory and
install it; now fire up Python --- you should be able to "import
custom" and play around with "Custom" objects.

Eso no fue tan difícil, ¿verdad?

Por supuesto, el tipo personalizado actual es bastante poco
interesante. No tiene datos y no hace nada. Ni siquiera se puede
subclasificar.

## 2.2. Agregar datos y métodos al ejemplo básico

Let's extend the basic example to add some data and methods.  Let's
also make the type usable as a base class. We'll create a new module,
"custom2" that adds these capabilities:

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>
   #include <stddef.h> /* for offsetof() */

   typedef struct {
       PyObject_HEAD
       PyObject *first; /* first name */
       PyObject *last;  /* last name */
       int number;
   } CustomObject;

   static void
   Custom_dealloc(PyObject *op)
   {
       CustomObject *self = (CustomObject *) op;
       Py_XDECREF(self->first);
       Py_XDECREF(self->last);
       Py_TYPE(self)->tp_free(self);
   }

   static PyObject *
   Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
   {
       CustomObject *self;
       self = (CustomObject *) type->tp_alloc(type, 0);
       if (self != NULL) {
           self->first = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
           if (self->first == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->last = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
           if (self->last == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->number = 0;
       }
       return (PyObject *) self;
   }

   static int
   Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       CustomObject *self = (CustomObject *) op;
       static char *kwlist[] = {"first", "last", "number", NULL};
       PyObject *first = NULL, *last = NULL;

       if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
                                        &first, &last,
                                        &self->number))
           return -1;

       if (first) {
           Py_XSETREF(self->first, Py_NewRef(first));
       }
       if (last) {
           Py_XSETREF(self->last, Py_NewRef(last));
       }
       return 0;
   }

   static PyMemberDef Custom_members[] = {
       {"first", Py_T_OBJECT_EX, offsetof(CustomObject, first), 0,
        "first name"},
       {"last", Py_T_OBJECT_EX, offsetof(CustomObject, last), 0,
        "last name"},
       {"number", Py_T_INT, offsetof(CustomObject, number), 0,
        "custom number"},
       {NULL}  /* Sentinel */
   };

   static PyObject *
   Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy))
   {
       CustomObject *self = (CustomObject *) op;
       if (self->first == NULL) {
           PyErr_SetString(PyExc_AttributeError, "first");
           return NULL;
       }
       if (self->last == NULL) {
           PyErr_SetString(PyExc_AttributeError, "last");
           return NULL;
       }
       return PyUnicode_FromFormat("%S %S", self->first, self->last);
   }

   static PyMethodDef Custom_methods[] = {
       {"name", Custom_name, METH_NOARGS,
        "Return the name, combining the first and last name"
       },
       {NULL}  /* Sentinel */
   };

   static PyTypeObject CustomType = {
       .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "custom2.Custom",
       .tp_doc = PyDoc_STR("Custom objects"),
       .tp_basicsize = sizeof(CustomObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
       .tp_new = Custom_new,
       .tp_init = Custom_init,
       .tp_dealloc = Custom_dealloc,
       .tp_members = Custom_members,
       .tp_methods = Custom_methods,
   };

   static int
   custom_module_exec(PyObject *m)
   {
       if (PyType_Ready(&CustomType) < 0) {
           return -1;
       }

       if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
           return -1;
       }

       return 0;
   }

   static PyModuleDef_Slot custom_module_slots[] = {
       {Py_mod_exec, custom_module_exec},
       {Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
       {0, NULL}
   };

   static PyModuleDef custom_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "custom2",
       .m_doc = "Example module that creates an extension type.",
       .m_size = 0,
       .m_slots = custom_module_slots,
   };

   PyMODINIT_FUNC
   PyInit_custom2(void)
   {
       return PyModuleDef_Init(&custom_module);
   }

Esta versión del módulo tiene una serie de cambios.

The  "Custom" type now has three data attributes in its C struct,
*first*, *last*, and *number*.  The *first* and *last* variables are
Python strings containing first and last names.  The *number*
attribute is a C integer.

La estructura del objeto se actualiza en consecuencia:

   typedef struct {
       PyObject_HEAD
       PyObject *first; /* first name */
       PyObject *last;  /* last name */
       int number;
   } CustomObject;

Debido a que ahora tenemos datos para administrar, debemos ser más
cuidadosos con la asignación de objetos y la desasignación. Como
mínimo, necesitamos un método de desasignación:

   static void
   Custom_dealloc(PyObject *op)
   {
       CustomObject *self = (CustomObject *) op;
       Py_XDECREF(self->first);
       Py_XDECREF(self->last);
       Py_TYPE(self)->tp_free(self);
   }

que se asigna al miembro "tp_dealloc":

   .tp_dealloc = Custom_dealloc,

This method first clears the reference counts of the two Python
attributes. "Py_XDECREF()" correctly handles the case where its
argument is "NULL" (which might happen here if "tp_new" failed
midway).  It then calls the "tp_free" member of the object's type
(computed by "Py_TYPE(self)") to free the object's memory.  Note that
the object's type might not be "CustomType", because the object may be
an instance of a subclass.

Nota:

  The explicit cast to "CustomObject *" above is needed because we
  defined "Custom_dealloc" to take a "PyObject *" argument, as the
  "tp_dealloc" function pointer expects to receive a "PyObject *"
  argument. By assigning to the "tp_dealloc" slot of a type, we
  declare that it can only be called with instances of our
  "CustomObject" class, so the cast to "(CustomObject *)" is safe.
  This is object-oriented polymorphism, in C!In existing code, or in
  previous versions of this tutorial, you might see similar functions
  take a pointer to the subtype object structure ("CustomObject*")
  directly, like this:

     Custom_dealloc(CustomObject *self)
     {
         Py_XDECREF(self->first);
         Py_XDECREF(self->last);
         Py_TYPE(self)->tp_free((PyObject *) self);
     }
     ...
     .tp_dealloc = (destructor) Custom_dealloc,

  This does the same thing on all architectures that CPython supports,
  but according to the C standard, it invokes undefined behavior.

Queremos asegurarnos de que el nombre y el apellido se inicialicen en
cadenas de caracteres vacías, por lo que proporcionamos una
implementación "tp_new":

   static PyObject *
   Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
   {
       CustomObject *self;
       self = (CustomObject *) type->tp_alloc(type, 0);
       if (self != NULL) {
           self->first = PyUnicode_FromString("");
           if (self->first == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->last = PyUnicode_FromString("");
           if (self->last == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->number = 0;
       }
       return (PyObject *) self;
   }

e instalarlo en el miembro "tp_new":

   .tp_new = Custom_new,

The "tp_new" handler is responsible for creating (as opposed to
initializing) objects of the type.  It is exposed in Python as the
"__new__()" method. It is not required to define a "tp_new" member,
and indeed many extension types will simply reuse
"PyType_GenericNew()" as done in the first version of the "Custom"
type above.  In this case, we use the "tp_new" handler to initialize
the "first" and "last" attributes to non-"NULL" default values.

"tp_new" se pasa el tipo que se instancia (no necesariamente
"CustomType", si se instancia una subclase) y cualquier argumento
pasado cuando se llamó al tipo, y se espera que retorna la instancia
creada. Los manejadores "tp_new" siempre aceptan argumentos
posicionales y de palabras clave, pero a menudo ignoran los
argumentos, dejando el manejo de argumentos al inicializador (también
conocido como, "tp_init" en C o "__init__" en Python).

Nota:

  "tp_new" no debería llamar explícitamente a "tp_init", ya que el
  intérprete lo hará por sí mismo.

La implementación "tp_new" llama al "tp_alloc" para asignar memoria:

   self = (CustomObject *) type->tp_alloc(type, 0);

Como la asignación de memoria puede fallar, debemos verificar el
resultado "tp_alloc" contra "NULL" antes de continuar.

Nota:

  No llenamos la ranura "tp_alloc" nosotros mismos. Más bien
  "PyType_Ready()" lo llena para nosotros al heredarlo de nuestra
  clase base, que es "object" por defecto. La mayoría de los tipos
  utilizan la estrategia de asignación predeterminada.

Nota:

  If you are creating a co-operative "tp_new" (one that calls a base
  type's "tp_new" or "__new__()"), you must *not* try to determine
  what method to call using method resolution order at runtime.
  Always statically determine what type you are going to call, and
  call its "tp_new" directly, or via "type->tp_base->tp_new".  If you
  do not do this, Python subclasses of your type that also inherit
  from other Python-defined classes may not work correctly.
  (Specifically, you may not be able to create instances of such
  subclasses without getting a "TypeError".)

También definimos una función de inicialización que acepta argumentos
para proporcionar valores iniciales para nuestra instancia:

   static int
   Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       CustomObject *self = (CustomObject *) op;
       static char *kwlist[] = {"first", "last", "number", NULL};
       PyObject *first = NULL, *last = NULL, *tmp;

       if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
                                        &first, &last,
                                        &self->number))
           return -1;

       if (first) {
           tmp = self->first;
           Py_INCREF(first);
           self->first = first;
           Py_XDECREF(tmp);
       }
       if (last) {
           tmp = self->last;
           Py_INCREF(last);
           self->last = last;
           Py_XDECREF(tmp);
       }
       return 0;
   }

rellenando la ranura "tp_init".

   .tp_init = Custom_init,

The "tp_init" slot is exposed in Python as the "__init__()" method.
It is used to initialize an object after it's created.  Initializers
always accept positional and keyword arguments, and they should return
either "0" on success or "-1" on error.

Unlike the "tp_new" handler, there is no guarantee that "tp_init" is
called at all (for example, the "pickle" module by default doesn't
call "__init__()" on unpickled instances).  It can also be called
multiple times.  Anyone can call the "__init__()" method on our
objects.  For this reason, we have to be extra careful when assigning
the new attribute values.  We might be tempted, for example to assign
the "first" member like this:

   if (first) {
       Py_XDECREF(self->first);
       Py_INCREF(first);
       self->first = first;
   }

But this would be risky.  Our type doesn't restrict the type of the
"first" member, so it could be any kind of object.  It could have a
destructor that causes code to be executed that tries to access the
"first" member; or that destructor could detach the *thread state* and
let arbitrary code run in other threads that accesses and modifies our
object.

Para ser paranoicos y protegernos de esta posibilidad, casi siempre
reasignamos miembros antes de disminuir sus recuentos de referencias.
¿Cuándo no tenemos que hacer esto?

* cuando sabemos absolutamente que el recuento de referencia es mayor
  que 1;

* when we know that deallocation of the object [1] will neither detach
  the *thread state* nor cause any calls back into our type's code;

* al disminuir un recuento de referencias en un manejador "tp_dealloc"
  en un tipo que no admite la recolección de basura cíclica [2].

Queremos exponer nuestras variables de instancia como atributos. Hay
varias formas de hacerlo. La forma más simple es definir definiciones
de miembros:

   static PyMemberDef Custom_members[] = {
       {"first", Py_T_OBJECT_EX, offsetof(CustomObject, first), 0,
        "first name"},
       {"last", Py_T_OBJECT_EX, offsetof(CustomObject, last), 0,
        "last name"},
       {"number", Py_T_INT, offsetof(CustomObject, number), 0,
        "custom number"},
       {NULL}  /* Sentinel */
   };

y poner las definiciones en la ranura "tp_members":

   .tp_members = Custom_members,

Cada definición de miembro tiene un nombre de miembro, tipo,
desplazamiento, banderas de acceso y cadena de caracteres de
documentación. Consulte la sección Gestión de atributos genéricos a
continuación para obtener más detalles.

Una desventaja de este enfoque es que no proporciona una forma de
restringir los tipos de objetos que se pueden asignar a los atributos
de Python. Esperamos que el nombre y el apellido sean cadenas, pero se
pueden asignar objetos de Python. Además, los atributos se pueden
eliminar, configurando los punteros C en "NULL". Si bien podemos
asegurarnos de que los miembros se inicialicen en valores que no sean
"NULL", los miembros se pueden establecer en "NULL" si se eliminan los
atributos.

We define a single method, "Custom.name()", that outputs the objects
name as the concatenation of the first and last names.

   static PyObject *
   Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy))
   {
       CustomObject *self = (CustomObject *) op;
       if (self->first == NULL) {
           PyErr_SetString(PyExc_AttributeError, "first");
           return NULL;
       }
       if (self->last == NULL) {
           PyErr_SetString(PyExc_AttributeError, "last");
           return NULL;
       }
       return PyUnicode_FromFormat("%S %S", self->first, self->last);
   }

The method is implemented as a C function that takes a "Custom" (or
"Custom" subclass) instance as the first argument.  Methods always
take an instance as the first argument. Methods often take positional
and keyword arguments as well, but in this case we don't take any and
don't need to accept a positional argument tuple or keyword argument
dictionary. This method is equivalent to the Python method:

   def name(self):
       return "%s %s" % (self.first, self.last)

Note that we have to check for the possibility that our "first" and
"last" members are "NULL".  This is because they can be deleted, in
which case they are set to "NULL".  It would be better to prevent
deletion of these attributes and to restrict the attribute values to
be strings.  We'll see how to do that in the next section.

Ahora que hemos definido el método, necesitamos crear un arreglo de
definiciones de métodos:

   static PyMethodDef Custom_methods[] = {
       {"name", Custom_name, METH_NOARGS,
        "Return the name, combining the first and last name"
       },
       {NULL}  /* Sentinel */
   };

(note that we used the "METH_NOARGS" flag to indicate that the method
is expecting no arguments other than *self*)

y asignarlo a la ranura "tp_methods":

   .tp_methods = Custom_methods,

Finally, we'll make our type usable as a base class for subclassing.
We've written our methods carefully so far so that they don't make any
assumptions about the type of the object being created or used, so all
we need to do is to add the "Py_TPFLAGS_BASETYPE" to our class flag
definition:

   .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,

We rename "PyInit_custom()" to "PyInit_custom2()", update the module
name in the "PyModuleDef" struct, and update the full class name in
the "PyTypeObject" struct.

Finally, we update our "setup.py" file to include the new module,

   from setuptools import Extension, setup
   setup(ext_modules=[
       Extension("custom", ["custom.c"]),
       Extension("custom2", ["custom2.c"]),
   ])

and then we re-install so that we can "import custom2":

   $ python -m pip install .

## 2.3. Proporcionar un control más preciso sobre los atributos de datos

In this section, we'll provide finer control over how the "first" and
"last" attributes are set in the "Custom" example. In the previous
version of our module, the instance variables "first" and "last" could
be set to non-string values or even deleted. We want to make sure that
these attributes always contain strings.

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>
   #include <stddef.h> /* for offsetof() */

   typedef struct {
       PyObject_HEAD
       PyObject *first; /* first name */
       PyObject *last;  /* last name */
       int number;
   } CustomObject;

   static void
   Custom_dealloc(PyObject *op)
   {
       CustomObject *self = (CustomObject *) op;
       Py_XDECREF(self->first);
       Py_XDECREF(self->last);
       Py_TYPE(self)->tp_free(self);
   }

   static PyObject *
   Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
   {
       CustomObject *self;
       self = (CustomObject *) type->tp_alloc(type, 0);
       if (self != NULL) {
           self->first = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
           if (self->first == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->last = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
           if (self->last == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->number = 0;
       }
       return (PyObject *) self;
   }

   static int
   Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       CustomObject *self = (CustomObject *) op;
       static char *kwlist[] = {"first", "last", "number", NULL};
       PyObject *first = NULL, *last = NULL;

       if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                        &first, &last,
                                        &self->number))
           return -1;

       if (first) {
           Py_SETREF(self->first, Py_NewRef(first));
       }
       if (last) {
           Py_SETREF(self->last, Py_NewRef(last));
       }
       return 0;
   }

   static PyMemberDef Custom_members[] = {
       {"number", Py_T_INT, offsetof(CustomObject, number), 0,
        "custom number"},
       {NULL}  /* Sentinel */
   };

   static PyObject *
   Custom_getfirst(PyObject *op, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       return Py_NewRef(self->first);
   }

   static int
   Custom_setfirst(PyObject *op, PyObject *value, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       if (value == NULL) {
           PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
           return -1;
       }
       if (!PyUnicode_Check(value)) {
           PyErr_SetString(PyExc_TypeError,
                           "The first attribute value must be a string");
           return -1;
       }
       Py_SETREF(self->first, Py_NewRef(value));
       return 0;
   }

   static PyObject *
   Custom_getlast(PyObject *op, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       return Py_NewRef(self->last);
   }

   static int
   Custom_setlast(PyObject *op, PyObject *value, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       if (value == NULL) {
           PyErr_SetString(PyExc_TypeError, "Cannot delete the last attribute");
           return -1;
       }
       if (!PyUnicode_Check(value)) {
           PyErr_SetString(PyExc_TypeError,
                           "The last attribute value must be a string");
           return -1;
       }
       Py_SETREF(self->last, Py_NewRef(value));
       return 0;
   }

   static PyGetSetDef Custom_getsetters[] = {
       {"first", Custom_getfirst, Custom_setfirst,
        "first name", NULL},
       {"last", Custom_getlast, Custom_setlast,
        "last name", NULL},
       {NULL}  /* Sentinel */
   };

   static PyObject *
   Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy))
   {
       CustomObject *self = (CustomObject *) op;
       return PyUnicode_FromFormat("%S %S", self->first, self->last);
   }

   static PyMethodDef Custom_methods[] = {
       {"name", Custom_name, METH_NOARGS,
        "Return the name, combining the first and last name"
       },
       {NULL}  /* Sentinel */
   };

   static PyTypeObject CustomType = {
       .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "custom3.Custom",
       .tp_doc = PyDoc_STR("Custom objects"),
       .tp_basicsize = sizeof(CustomObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
       .tp_new = Custom_new,
       .tp_init = Custom_init,
       .tp_dealloc = Custom_dealloc,
       .tp_members = Custom_members,
       .tp_methods = Custom_methods,
       .tp_getset = Custom_getsetters,
   };

   static int
   custom_module_exec(PyObject *m)
   {
       if (PyType_Ready(&CustomType) < 0) {
           return -1;
       }

       if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
           return -1;
       }

       return 0;
   }

   static PyModuleDef_Slot custom_module_slots[] = {
       {Py_mod_exec, custom_module_exec},
       {Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
       {0, NULL}
   };

   static PyModuleDef custom_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "custom3",
       .m_doc = "Example module that creates an extension type.",
       .m_size = 0,
       .m_slots = custom_module_slots,
   };

   PyMODINIT_FUNC
   PyInit_custom3(void)
   {
       return PyModuleDef_Init(&custom_module);
   }

To provide greater control, over the "first" and "last" attributes,
we'll use custom getter and setter functions.  Here are the functions
for getting and setting the "first" attribute:

   static PyObject *
   Custom_getfirst(PyObject *op, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       Py_INCREF(self->first);
       return self->first;
   }

   static int
   Custom_setfirst(PyObject *op, PyObject *value, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       PyObject *tmp;
       if (value == NULL) {
           PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
           return -1;
       }
       if (!PyUnicode_Check(value)) {
           PyErr_SetString(PyExc_TypeError,
                           "The first attribute value must be a string");
           return -1;
       }
       tmp = self->first;
       Py_INCREF(value);
       self->first = value;
       Py_DECREF(tmp);
       return 0;
   }

The getter function is passed a "Custom" object and a "closure", which
is a void pointer.  In this case, the closure is ignored.  (The
closure supports an advanced usage in which definition data is passed
to the getter and setter. This could, for example, be used to allow a
single set of getter and setter functions that decide the attribute to
get or set based on data in the closure.)

The setter function is passed the "Custom" object, the new value, and
the closure.  The new value may be "NULL", in which case the attribute
is being deleted.  In our setter, we raise an error if the attribute
is deleted or if its new value is not a string.

Creamos un arreglo de estructuras "PyGetSetDef":

   static PyGetSetDef Custom_getsetters[] = {
       {"first", Custom_getfirst, Custom_setfirst,
        "first name", NULL},
       {"last", Custom_getlast, Custom_setlast,
        "last name", NULL},
       {NULL}  /* Sentinel */
   };

y lo registra en la ranura "tp_getset":

   .tp_getset = Custom_getsetters,

El último elemento en la estructura "PyGetSetDef" es el "cierre"
(*closure*) mencionado anteriormente. En este caso, no estamos usando
un cierre, por lo que simplemente pasamos "NULL".

También eliminamos las definiciones de miembro para estos atributos:

   static PyMemberDef Custom_members[] = {
       {"number", Py_T_INT, offsetof(CustomObject, number), 0,
        "custom number"},
       {NULL}  /* Sentinel */
   };

También necesitamos actualizar el manejador "tp_init" para permitir
que solo se pasen las cadenas [3]:

   static int
   Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       CustomObject *self = (CustomObject *) op;
       static char *kwlist[] = {"first", "last", "number", NULL};
       PyObject *first = NULL, *last = NULL, *tmp;

       if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                        &first, &last,
                                        &self->number))
           return -1;

       if (first) {
           tmp = self->first;
           Py_INCREF(first);
           self->first = first;
           Py_DECREF(tmp);
       }
       if (last) {
           tmp = self->last;
           Py_INCREF(last);
           self->last = last;
           Py_DECREF(tmp);
       }
       return 0;
   }

Con estos cambios, podemos asegurar que los miembros "primero" y
"último" nunca sean "NULL", por lo que podemos eliminar las
comprobaciones de los valores "NULL" en casi todos los casos. Esto
significa que la mayoría de las llamadas "Py_XDECREF()" se pueden
convertir en llamadas "Py_DECREF()". El único lugar donde no podemos
cambiar estas llamadas es en la implementación "tp_dealloc", donde
existe la posibilidad de que la inicialización de estos miembros falle
en "tp_new".

También cambiamos el nombre de la función de inicialización del módulo
y el nombre del módulo en la función de inicialización, como lo
hicimos antes, y agregamos una definición adicional al archivo
"setup.py".

## 2.4. Apoyo a la recolección de basura cíclica

Python tiene un *recolector de basura cíclico (GC)* que puede
identificar objetos innecesarios incluso cuando sus recuentos de
referencia no son cero. Esto puede suceder cuando los objetos están
involucrados en ciclos. Por ejemplo, considere:

   >>> l = []
   >>> l.append(l)
   >>> del l

En este ejemplo, creamos una lista que se contiene a sí misma. Cuando
lo eliminamos, todavía tiene una referencia de sí mismo. Su recuento
de referencia no cae a cero. Afortunadamente, el recolector cíclico de
basura de Python finalmente descubrirá que la lista es basura y la
liberará.

In the second version of the "Custom" example, we allowed any kind of
object to be stored in the "first" or "last" attributes [4]. Besides,
in the second and third versions, we allowed subclassing "Custom", and
subclasses may add arbitrary attributes.  For any of those two
reasons, "Custom" objects can participate in cycles:

   >>> import custom3
   >>> class Derived(custom3.Custom): pass
   ...
   >>> n = Derived()
   >>> n.some_attribute = n

To allow a "Custom" instance participating in a reference cycle to be
properly detected and collected by the cyclic GC, our "Custom" type
needs to fill two additional slots and to enable a flag that enables
these slots:

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>
   #include <stddef.h> /* for offsetof() */

   typedef struct {
       PyObject_HEAD
       PyObject *first; /* first name */
       PyObject *last;  /* last name */
       int number;
   } CustomObject;

   static int
   Custom_traverse(PyObject *op, visitproc visit, void *arg)
   {
       CustomObject *self = (CustomObject *) op;
       Py_VISIT(self->first);
       Py_VISIT(self->last);
       return 0;
   }

   static int
   Custom_clear(PyObject *op)
   {
       CustomObject *self = (CustomObject *) op;
       Py_CLEAR(self->first);
       Py_CLEAR(self->last);
       return 0;
   }

   static void
   Custom_dealloc(PyObject *op)
   {
       PyObject_GC_UnTrack(op);
       (void)Custom_clear(op);
       Py_TYPE(op)->tp_free(op);
   }

   static PyObject *
   Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
   {
       CustomObject *self;
       self = (CustomObject *) type->tp_alloc(type, 0);
       if (self != NULL) {
           self->first = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
           if (self->first == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->last = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
           if (self->last == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->number = 0;
       }
       return (PyObject *) self;
   }

   static int
   Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       CustomObject *self = (CustomObject *) op;
       static char *kwlist[] = {"first", "last", "number", NULL};
       PyObject *first = NULL, *last = NULL;

       if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                        &first, &last,
                                        &self->number))
           return -1;

       if (first) {
           Py_SETREF(self->first, Py_NewRef(first));
       }
       if (last) {
           Py_SETREF(self->last, Py_NewRef(last));
       }
       return 0;
   }

   static PyMemberDef Custom_members[] = {
       {"number", Py_T_INT, offsetof(CustomObject, number), 0,
        "custom number"},
       {NULL}  /* Sentinel */
   };

   static PyObject *
   Custom_getfirst(PyObject *op, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       return Py_NewRef(self->first);
   }

   static int
   Custom_setfirst(PyObject *op, PyObject *value, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       if (value == NULL) {
           PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
           return -1;
       }
       if (!PyUnicode_Check(value)) {
           PyErr_SetString(PyExc_TypeError,
                           "The first attribute value must be a string");
           return -1;
       }
       Py_XSETREF(self->first, Py_NewRef(value));
       return 0;
   }

   static PyObject *
   Custom_getlast(PyObject *op, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       return Py_NewRef(self->last);
   }

   static int
   Custom_setlast(PyObject *op, PyObject *value, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       if (value == NULL) {
           PyErr_SetString(PyExc_TypeError, "Cannot delete the last attribute");
           return -1;
       }
       if (!PyUnicode_Check(value)) {
           PyErr_SetString(PyExc_TypeError,
                           "The last attribute value must be a string");
           return -1;
       }
       Py_XSETREF(self->last, Py_NewRef(value));
       return 0;
   }

   static PyGetSetDef Custom_getsetters[] = {
       {"first", Custom_getfirst, Custom_setfirst,
        "first name", NULL},
       {"last", Custom_getlast, Custom_setlast,
        "last name", NULL},
       {NULL}  /* Sentinel */
   };

   static PyObject *
   Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy))
   {
       CustomObject *self = (CustomObject *) op;
       return PyUnicode_FromFormat("%S %S", self->first, self->last);
   }

   static PyMethodDef Custom_methods[] = {
       {"name", Custom_name, METH_NOARGS,
        "Return the name, combining the first and last name"
       },
       {NULL}  /* Sentinel */
   };

   static PyTypeObject CustomType = {
       .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "custom4.Custom",
       .tp_doc = PyDoc_STR("Custom objects"),
       .tp_basicsize = sizeof(CustomObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,
       .tp_new = Custom_new,
       .tp_init = Custom_init,
       .tp_dealloc = Custom_dealloc,
       .tp_traverse = Custom_traverse,
       .tp_clear = Custom_clear,
       .tp_members = Custom_members,
       .tp_methods = Custom_methods,
       .tp_getset = Custom_getsetters,
   };

   static int
   custom_module_exec(PyObject *m)
   {
       if (PyType_Ready(&CustomType) < 0) {
           return -1;
       }

       if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
           return -1;
       }

       return 0;
   }

   static PyModuleDef_Slot custom_module_slots[] = {
       {Py_mod_exec, custom_module_exec},
       {Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
       {0, NULL}
   };

   static PyModuleDef custom_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "custom4",
       .m_doc = "Example module that creates an extension type.",
       .m_size = 0,
       .m_slots = custom_module_slots,
   };

   PyMODINIT_FUNC
   PyInit_custom4(void)
   {
       return PyModuleDef_Init(&custom_module);
   }

Primero, el método transversal permite que el GC cíclico conozca los
subobjetos que podrían participar en los ciclos:

   static int
   Custom_traverse(PyObject *op, visitproc visit, void *arg)
   {
       CustomObject *self = (CustomObject *) op;
       int vret;
       if (self->first) {
           vret = visit(self->first, arg);
           if (vret != 0)
               return vret;
       }
       if (self->last) {
           vret = visit(self->last, arg);
           if (vret != 0)
               return vret;
       }
       return 0;
   }

For each subobject that can participate in cycles, we need to call the
"visit()" function, which is passed to the traversal method. The
"visit()" function takes as arguments the subobject and the extra
argument *arg* passed to the traversal method.  It returns an integer
value that must be returned if it is non-zero.

Python proporciona una macro "Py_VISIT()" que automatiza las funciones
de visita de llamada. Con "Py_VISIT()", podemos minimizar la cantidad
de repeticiones en "Custom_traverse":

   static int
   Custom_traverse(PyObject *op, visitproc visit, void *arg)
   {
       CustomObject *self = (CustomObject *) op;
       Py_VISIT(self->first);
       Py_VISIT(self->last);
       return 0;
   }

Nota:

  La implementación "tp_traverse" debe nombrar sus argumentos
  exactamente *visit* y *arg* para usar "Py_VISIT()".

En segundo lugar, debemos proporcionar un método para borrar cualquier
subobjeto que pueda participar en los ciclos:

   static int
   Custom_clear(PyObject *op)
   {
       CustomObject *self = (CustomObject *) op;
       Py_CLEAR(self->first);
       Py_CLEAR(self->last);
       return 0;
   }

Observe el uso de la macro "Py_CLEAR()". Es la forma recomendada y
segura de borrar los atributos de datos de tipos arbitrarios al tiempo
que disminuye sus recuentos de referencia. Si tuviera que llamar a
"Py_XDECREF()" en lugar del atributo antes de establecerlo en "NULL",
existe la posibilidad de que el destructor del atributo vuelva a
llamar al código que lee el atributo nuevamente (*especialmente* si
hay un ciclo de referencia).

Nota:

  Puede emular "Py_CLEAR()" escribiendo:

     PyObject *tmp;
     tmp = self->first;
     self->first = NULL;
     Py_XDECREF(tmp);

  Sin embargo, es mucho más fácil y menos propenso a errores usar
  siempre "Py_CLEAR()" al eliminar un atributo. ¡No intentes micro-
  optimizar a expensas de la robustez!

El desasignador "Custom_dealloc" puede llamar a un código arbitrario
al borrar los atributos. Significa que el GC circular se puede activar
dentro de la función. Dado que el GC asume que el recuento de
referencias no es cero, debemos destrabar el objeto del GC llamando a
"PyObject_GC_UnTrack()" antes de borrar los miembros. Aquí está
nuestro reubicador reimplementado usando "PyObject_GC_UnTrack()" y
"Custom_clear":

   static void
   Custom_dealloc(PyObject *op)
   {
       PyObject_GC_UnTrack(op);
       (void)Custom_clear(op);
       Py_TYPE(op)->tp_free(op);
   }

Finally, we add the "Py_TPFLAGS_HAVE_GC" flag to the class flags:

   .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,

Eso es prácticamente todo. Si hubiéramos escrito controladores
personalizados "tp_alloc" o "tp_free", tendríamos que modificarlos
para la recolección de basura cíclica. La mayoría de las extensiones
usarán las versiones proporcionadas automáticamente.

## 2.5. Subclases de otros tipos

Es posible crear nuevos tipos de extensión que se derivan de los tipos
existentes. Es más fácil heredar de los tipos incorporados, ya que una
extensión puede usar fácilmente "PyTypeObject" que necesita. Puede ser
difícil compartir estas estructuras "PyTypeObject" entre módulos de
extensión.

In this example we will create a "SubList" type that inherits from the
built-in "list" type. The new type will be completely compatible with
regular lists, but will have an additional "increment()" method that
increases an internal counter:

   >>> import sublist
   >>> s = sublist.SubList(range(3))
   >>> s.extend(s)
   >>> print(len(s))
   6
   >>> print(s.increment())
   1
   >>> print(s.increment())
   2

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>

   typedef struct {
       PyListObject list;
       int state;
   } SubListObject;

   static PyObject *
   SubList_increment(PyObject *op, PyObject *Py_UNUSED(dummy))
   {
       SubListObject *self = (SubListObject *) op;
       self->state++;
       return PyLong_FromLong(self->state);
   }

   static PyMethodDef SubList_methods[] = {
       {"increment", SubList_increment, METH_NOARGS,
        PyDoc_STR("increment state counter")},
       {NULL},
   };

   static int
   SubList_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       SubListObject *self = (SubListObject *) op;
       if (PyList_Type.tp_init(op, args, kwds) < 0)
           return -1;
       self->state = 0;
       return 0;
   }

   static PyTypeObject SubListType = {
       .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "sublist.SubList",
       .tp_doc = PyDoc_STR("SubList objects"),
       .tp_basicsize = sizeof(SubListObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
       .tp_init = SubList_init,
       .tp_methods = SubList_methods,
   };

   static int
   sublist_module_exec(PyObject *m)
   {
       SubListType.tp_base = &PyList_Type;
       if (PyType_Ready(&SubListType) < 0) {
           return -1;
       }

       if (PyModule_AddObjectRef(m, "SubList", (PyObject *) &SubListType) < 0) {
           return -1;
       }

       return 0;
   }

   static PyModuleDef_Slot sublist_module_slots[] = {
       {Py_mod_exec, sublist_module_exec},
       {Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
       {0, NULL}
   };

   static PyModuleDef sublist_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "sublist",
       .m_doc = "Example module that creates an extension type.",
       .m_size = 0,
       .m_slots = sublist_module_slots,
   };

   PyMODINIT_FUNC
   PyInit_sublist(void)
   {
       return PyModuleDef_Init(&sublist_module);
   }

As you can see, the source code closely resembles the "Custom"
examples in previous sections. We will break down the main differences
between them.

   typedef struct {
       PyListObject list;
       int state;
   } SubListObject;

La diferencia principal para los objetos de tipo derivado es que la
estructura de objeto del tipo base debe ser el primer valor. El tipo
base ya incluirá "PyObject_HEAD()" al comienzo de su estructura.

When a Python object is a "SubList" instance, its "PyObject *" pointer
can be safely cast to both "PyListObject *" and "SubListObject *":

   static int
   SubList_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       SubListObject *self = (SubListObject *) op;
       if (PyList_Type.tp_init(op, args, kwds) < 0)
           return -1;
       self->state = 0;
       return 0;
   }

We see above how to call through to the "__init__()" method of the
base type.

Este patrón es importante cuando se escribe un tipo con miembros
personalizados "tp_new" y "tp_dealloc". El manejador "tp_new" no
debería crear realmente la memoria para el objeto con su "tp_alloc",
pero deja que la clase base lo maneje llamando a su propio "tp_new".

The "PyTypeObject" struct supports a "tp_base" specifying the type's
concrete base class.  Due to cross-platform compiler issues, you can't
fill that field directly with a reference to "PyList_Type"; it should
be done in the "Py_mod_exec" function:

   static int
   sublist_module_exec(PyObject *m)
   {
       SubListType.tp_base = &PyList_Type;
       if (PyType_Ready(&SubListType) < 0) {
           return -1;
       }

       if (PyModule_AddObjectRef(m, "SubList", (PyObject *) &SubListType) < 0) {
           return -1;
       }

       return 0;
   }

Antes de llamar a "PyType_Ready()", la estructura de tipo debe tener
el espacio "tp_base" rellenado. Cuando derivamos un tipo existente, no
es necesario completar el "tp_alloc" ranura con "PyType_GenericNew()"
-- la función de asignación del tipo base será heredada.

After that, calling "PyType_Ready()" and adding the type object to the
module is the same as with the basic "Custom" examples.

-[ Notas al pie ]-

[1] Esto es cierto cuando sabemos que el objeto es un tipo básico,
    como una cadena o un flotador.

[2] Nos basamos en esto en el manejador "tp_dealloc" en este ejemplo,
    porque nuestro tipo no admite la recolección de basura.

[3] Ahora sabemos que el primer y el último miembro son cadenas de
    caracteres, por lo que quizás podríamos ser menos cuidadosos al
    disminuir sus recuentos de referencia, sin embargo, aceptamos
    instancias de subclases de cadenas. A pesar de que la
    desasignación de cadenas normales no volverá a llamar a nuestros
    objetos, no podemos garantizar que la desasignación de una
    instancia de una subclase de cadena de caracteres no vuelva a
    llamar a nuestros objetos.

[4] Además, incluso con nuestros atributos restringidos a instancias
    de cadenas, el usuario podría pasar subclases arbitrarias "str" y,
    por lo tanto, seguir creando ciclos de referencia.
