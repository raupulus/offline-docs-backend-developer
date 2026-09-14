---
title: Objetos módulo
source_url: https://docs.python.org/es/3
source_path: c-api/module.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 500
---

# Objetos módulo

PyTypeObject PyModule_Type
    * Part of the Stable ABI.*

   This instance of "PyTypeObject" represents the Python module type.
   This is exposed to Python programs as "types.ModuleType".

int PyModule_Check(PyObject *p)

   Retorna verdadero si *p* es un objeto de módulo o un subtipo de un
   objeto de módulo. Esta función siempre finaliza con éxito.

int PyModule_CheckExact(PyObject *p)

   Retorna verdadero si *p* es un objeto módulo, pero no un subtipo de
   "PyModule_Type". Esta función siempre finaliza con éxito.

PyObject *PyModule_NewObject(PyObject *name)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Return a new module object with "module.__name__" set to *name*.
   The module's "__name__", "__doc__", "__package__" and "__loader__"
   attributes are filled in (all but "__name__" are set to "None").
   The caller is responsible for setting a "__file__" attribute.

   Return "NULL" with an exception set on error.

   Added in version 3.3.

   Distinto en la versión 3.4: "__package__" and "__loader__" are now
   set to "None".

PyObject *PyModule_New(const char *name)
    *Return value: New reference.** Part of the Stable ABI.*

   Similar a "PyModule_NewObject()", pero el nombre es una cadena de
   caracteres codificada UTF-8 en lugar de un objeto Unicode.

PyObject *PyModule_GetDict(PyObject *module)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Retorna el objeto del diccionario que implementa el espacio de
   nombres de *module*; este objeto es el mismo que el atributo
   "__dict__" del objeto módulo. Si *module* no es un objeto módulo (o
   un subtipo de un objeto de módulo), se lanza "SystemError" y se
   retorna "NULL".

   It is recommended extensions use other "PyModule_*" and
   "PyObject_*" functions rather than directly manipulate a module's
   "__dict__".

   The returned reference is borrowed from the module; it is valid
   until the module is destroyed.

PyObject *PyModule_GetNameObject(PyObject *module)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Return *module*'s "__name__" value.  If the module does not provide
   one, or if it is not a string, "SystemError" is raised and "NULL"
   is returned.

   Added in version 3.3.

const char *PyModule_GetName(PyObject *module)
    * Part of the Stable ABI.*

   Similar a "PyModule_GetNameObject()" pero retorna el nombre
   codificado a "'utf-8'".

   The returned buffer is only valid until the module is renamed or
   destroyed. Note that Python code may rename a module by setting its
   "__name__" attribute.

void *PyModule_GetState(PyObject *module)
    * Part of the Stable ABI.*

   Retorna el "estado" del módulo, es decir, un puntero al bloque de
   memoria asignado en el momento de la creación del módulo, o "NULL".
   Ver "PyModuleDef.m_size".

PyModuleDef *PyModule_GetDef(PyObject *module)
    * Part of the Stable ABI.*

   Retorna un puntero a la estructura "PyModuleDef" a partir de la
   cual se creó el módulo, o "NULL" si el módulo no se creó a partir
   de una definición.

   On error, return "NULL" with an exception set. Use
   "PyErr_Occurred()" to tell this case apart from a missing
   "PyModuleDef".

PyObject *PyModule_GetFilenameObject(PyObject *module)
    *Return value: New reference.** Part of the Stable ABI.*

   Return the name of the file from which *module* was loaded using
   *module*'s "__file__" attribute.  If this is not defined, or if it
   is not a string, raise "SystemError" and return "NULL"; otherwise
   return a reference to a Unicode object.

   Added in version 3.2.

const char *PyModule_GetFilename(PyObject *module)
    * Part of the Stable ABI.*

   Similar a "PyModule_GetFilenameObject()" pero retorna el nombre de
   archivo codificado a 'utf-8'.

   The returned buffer is only valid until the module's "__file__"
   attribute is reassigned or the module is destroyed.

   Obsoleto desde la versión 3.2: "PyModule_GetFilename()" raises
   "UnicodeEncodeError" on unencodable filenames, use
   "PyModule_GetFilenameObject()" instead.

# Module definitions

The functions in the previous section work on any module object,
including modules imported from Python code.

Modules defined using the C API typically use a *module definition*,
"PyModuleDef" -- a statically allocated, constant “description" of how
a module should be created.

The definition is usually used to define an extension's “main” module
object (see Defining extension modules for details). It is also used
to create extension modules dynamically.

Unlike "PyModule_New()", the definition allows management of *module
state* -- a piece of memory that is allocated and cleared together
with the module object. Unlike the module's Python attributes, Python
code cannot replace or delete data stored in module state.

type PyModuleDef
    * Part of the Stable ABI (including all members).*

   The module definition struct, which holds all information needed to
   create a module object. This structure must be statically allocated
   (or be otherwise guaranteed to be valid while any modules created
   from it exist). Usually, there is only one variable of this type
   for each extension module.

   PyModuleDef_Base m_base

      Always initialize this member to "PyModuleDef_HEAD_INIT".

   const char *m_name

      Nombre para el nuevo módulo.

   const char *m_doc

      Docstring para el módulo; por lo general, se usa una variable
      docstring creada con "PyDoc_STRVAR".

   Py_ssize_t m_size

      El estado del módulo se puede mantener en un área de memoria por
      módulo que se puede recuperar con "PyModule_GetState()", en
      lugar de en globales estáticos. Esto hace que los módulos sean
      seguros para su uso en múltiples sub-interpretadores.

      This memory area is allocated based on *m_size* on module
      creation, and freed when the module object is deallocated, after
      the "m_free" function has been called, if present.

      Setting it to a non-negative value means that the module can be
      re-initialized and specifies the additional amount of memory it
      requires for its state.

      Setting "m_size" to "-1" means that the module does not support
      sub-interpreters, because it has global state. Negative "m_size"
      is only allowed when using legacy single-phase initialization or
      when creating modules dynamically.

      Ver **PEP 3121** para más detalles.

   PyMethodDef *m_methods

      Un puntero a una tabla de funciones de nivel de módulo, descrito
      por valores "PyMethodDef". Puede ser "NULL" si no hay funciones
      presentes.

   PyModuleDef_Slot *m_slots

      An array of slot definitions for multi-phase initialization,
      terminated by a "{0, NULL}" entry. When using legacy single-
      phase initialization, *m_slots* must be "NULL".

      Distinto en la versión 3.5: Antes de la versión 3.5, este
      miembro siempre estaba configurado en "NULL" y se definía como:

         inquiry m_reload

   traverseproc m_traverse

      Una función transversal para llamar durante el recorrido GC del
      objeto del módulo, o "NULL" si no es necesario.

      This function is not called if the module state was requested
      but is not allocated yet. This is the case immediately after the
      module is created and before the module is executed
      ("Py_mod_exec" function). More precisely, this function is not
      called if "m_size" is greater than 0 and the module state (as
      returned by "PyModule_GetState()") is "NULL".

      Distinto en la versión 3.9: Ya no se llama antes de que se
      asigne el estado del módulo.

   inquiry m_clear

      Una función clara para llamar durante la limpieza GC del objeto
      del módulo, o "NULL" si no es necesario.

      This function is not called if the module state was requested
      but is not allocated yet. This is the case immediately after the
      module is created and before the module is executed
      ("Py_mod_exec" function). More precisely, this function is not
      called if "m_size" is greater than 0 and the module state (as
      returned by "PyModule_GetState()") is "NULL".

      Tal como "PyTypeObject.tp_clear", esta función no *siempre* es
      llamada antes de la designación de un módulo. Por ejemplo,
      cuando el recuento de referencias está  listo para determinar
      que un objeto no se usa más, la recolección de basura cíclica no
      se involucra y se llama a "m_free" directamente.

      Distinto en la versión 3.9: Ya no se llama antes de que se
      asigne el estado del módulo.

   freefunc m_free

      Una función para llamar durante la desasignación del objeto del
      módulo, o "NULL" si no es necesario.

      This function is not called if the module state was requested
      but is not allocated yet. This is the case immediately after the
      module is created and before the module is executed
      ("Py_mod_exec" function). More precisely, this function is not
      called if "m_size" is greater than 0 and the module state (as
      returned by "PyModule_GetState()") is "NULL".

      Distinto en la versión 3.9: Ya no se llama antes de que se
      asigne el estado del módulo.

PyTypeObject PyModuleDef_Type
    * Part of the Stable ABI since version 3.5.*

   The type of "PyModuleDef" objects.

## Module slots

type PyModuleDef_Slot
    * Part of the Stable ABI (including all members) since version
   3.5.*

   int slot

      Una ranura ID, elegida entre los valores disponibles que se
      explican a continuación.

   void *value

      Valor de la ranura, cuyo significado depende de la ID de la
      ranura.

   Added in version 3.5.

Los tipos de ranura disponibles son:

Py_mod_create
    * Part of the Stable ABI since version 3.5.*

   Especifica una función que se llama para crear el objeto del módulo
   en sí. El puntero *value* de este espacio debe apuntar a una
   función de la firma:

   PyObject *create_module(PyObject *spec, PyModuleDef *def)

   La función recibe una instancia de "ModuleSpec", como se define en
   **PEP 451**, y la definición del módulo. Debería retornar un nuevo
   objeto de módulo, o establecer un error y retornar "NULL".

   Esta función debe mantenerse mínima. En particular, no debería
   llamar a código arbitrario de Python, ya que intentar importar el
   mismo módulo nuevamente puede dar como resultado un bucle infinito.

   Múltiples ranuras "Py_mod_create" no pueden especificarse en una
   definición de módulo.

   Si no se especifica "Py_mod_create", la maquinaria de importación
   creará un objeto de módulo normal usando "PyModule_New()". El
   nombre se toma de *spec*, no de la definición, para permitir que
   los módulos de extensión se ajusten dinámicamente a su lugar en la
   jerarquía de módulos y se importen bajo diferentes nombres a través
   de enlaces simbólicos, todo mientras se comparte una definición de
   módulo único.

   No es necesario que el objeto retornado sea una instancia de
   "PyModule_Type". Se puede usar cualquier tipo, siempre que admita
   la configuración y la obtención de atributos relacionados con la
   importación. Sin embargo, solo se pueden retornar instancias
   "PyModule_Type" si el "PyModuleDef" no tiene "NULL" "m_traverse",
   "m_clear", "m_free"; "m_size" distinto de cero; o ranuras que no
   sean "Py_mod_create".

   Added in version 3.5.

Py_mod_exec
    * Part of the Stable ABI since version 3.5.*

   Especifica una función que se llama para ejecutar (*execute*) el
   módulo. Esto es equivalente a ejecutar el código de un módulo
   Python: por lo general, esta función agrega clases y constantes al
   módulo. La firma de la función es:

   int exec_module(PyObject *module)

   Si se especifican varias ranuras "Py_mod_exec", se procesan en el
   orden en que aparecen en el arreglo *m_slots*.

   Added in version 3.5.

Py_mod_multiple_interpreters
    * Part of the Stable ABI since version 3.12.*

   Specifies one of the following values:

   Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED

      The module does not support being imported in subinterpreters.

   Py_MOD_MULTIPLE_INTERPRETERS_SUPPORTED

      The module supports being imported in subinterpreters, but only
      when they share the main interpreter's GIL. (See Aislamiento de
      módulos de extensión.)

   Py_MOD_PER_INTERPRETER_GIL_SUPPORTED

      The module supports being imported in subinterpreters, even when
      they have their own GIL. (See Aislamiento de módulos de
      extensión.)

   This slot determines whether or not importing this module in a
   subinterpreter will fail.

   Multiple "Py_mod_multiple_interpreters" slots may not be specified
   in one module definition.

   If "Py_mod_multiple_interpreters" is not specified, the import
   machinery defaults to "Py_MOD_MULTIPLE_INTERPRETERS_SUPPORTED".

   Added in version 3.12.

Py_mod_gil
    * Part of the Stable ABI since version 3.13.*

   Specifies one of the following values:

   Py_MOD_GIL_USED

      The module depends on the presence of the global interpreter
      lock (GIL), and may access global state without synchronization.

   Py_MOD_GIL_NOT_USED

      The module is safe to run without an active GIL.

   This slot is ignored by Python builds not configured with "--
   disable-gil".  Otherwise, it determines whether or not importing
   this module will cause the GIL to be automatically enabled. See
   Free-threaded CPython for more detail.

   Multiple "Py_mod_gil" slots may not be specified in one module
   definition.

   If "Py_mod_gil" is not specified, the import machinery defaults to
   "Py_MOD_GIL_USED".

   Added in version 3.13.

# Creating extension modules dynamically

The following functions may be used to create a module outside of an
extension's initialization function. They are also used in single-
phase initialization.

PyObject *PyModule_Create(PyModuleDef *def)
    *Return value: New reference.*

   Create a new module object, given the definition in *def*. This is
   a macro that calls "PyModule_Create2()" with *module_api_version*
   set to "PYTHON_API_VERSION", or to "PYTHON_ABI_VERSION" if using
   the limited API.

PyObject *PyModule_Create2(PyModuleDef *def, int module_api_version)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un nuevo objeto de módulo, dada la definición en *def*,
   asumiendo la versión de API *module_api_version*. Si esa versión no
   coincide con la versión del intérprete en ejecución, se emite un
   "RuntimeWarning".

   Return "NULL" with an exception set on error.

   This function does not support slots. The "m_slots" member of *def*
   must be "NULL".

   Nota:

     La mayoría de los usos de esta función deberían usar
     "PyModule_Create()" en su lugar; solo use esto si está seguro de
     que lo necesita.

PyObject *PyModule_FromDefAndSpec(PyModuleDef *def, PyObject *spec)
    *Return value: New reference.*

   This macro calls "PyModule_FromDefAndSpec2()" with
   *module_api_version* set to "PYTHON_API_VERSION", or to
   "PYTHON_ABI_VERSION" if using the limited API.

   Added in version 3.5.

PyObject *PyModule_FromDefAndSpec2(PyModuleDef *def, PyObject *spec, int module_api_version)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Create a new module object, given the definition in *def* and the
   ModuleSpec *spec*, assuming the API version *module_api_version*.
   If that version does not match the version of the running
   interpreter, a "RuntimeWarning" is emitted.

   Return "NULL" with an exception set on error.

   Note that this does not process execution slots ("Py_mod_exec").
   Both "PyModule_FromDefAndSpec" and "PyModule_ExecDef" must be
   called to fully initialize a module.

   Nota:

     La mayoría de los usos de esta función deberían usar
     "PyModule_FromDefAndSpec()" en su lugar; solo use esto si está
     seguro de que lo necesita.

   Added in version 3.5.

int PyModule_ExecDef(PyObject *module, PyModuleDef *def)
    * Part of the Stable ABI since version 3.7.*

   Procesa cualquier ranura de ejecución ("Py_mod_exec") dado en
   *def*.

   Added in version 3.5.

PYTHON_API_VERSION

   The C API version. Defined for backwards compatibility.

   Currently, this constant is not updated in new Python versions, and
   is not useful for versioning. This may change in the future.

PYTHON_ABI_VERSION

   Defined as "3" for backwards compatibility.

   Currently, this constant is not updated in new Python versions, and
   is not useful for versioning. This may change in the future.

# Funciones de soporte

The following functions are provided to help initialize a module
state. They are intended for a module's execution slots
("Py_mod_exec"), the initialization function for legacy single-phase
initialization, or code that creates modules dynamically.

int PyModule_AddObjectRef(PyObject *module, const char *name, PyObject *value)
    * Part of the Stable ABI since version 3.10.*

   Agrega un objeto a *module* como *name*. Esta es una función de
   conveniencia que se puede usar desde la función de inicialización
   del módulo.

   En caso de éxito, retorna "0". En caso de error, lanza una
   excepción y retorna "-1".

   Ejemplo de uso

      static int
      add_spam(PyObject *module, int value)
      {
          PyObject *obj = PyLong_FromLong(value);
          if (obj == NULL) {
              return -1;
          }
          int res = PyModule_AddObjectRef(module, "spam", obj);
          Py_DECREF(obj);
          return res;
       }

   To be convenient, the function accepts "NULL" *value* with an
   exception set. In this case, return "-1" and just leave the raised
   exception unchanged.

   El ejemplo puede también ser escrito sin verificar explicitamente
   si *obj* es "NULL":

      static int
      add_spam(PyObject *module, int value)
      {
          PyObject *obj = PyLong_FromLong(value);
          int res = PyModule_AddObjectRef(module, "spam", obj);
          Py_XDECREF(obj);
          return res;
       }

   Note que "Py_XDECREF()" debería ser usado en vez de "Py_DECREF()"
   en este caso, ya que *obj* puede ser "NULL".

   The number of different *name* strings passed to this function
   should be kept small, usually by only using statically allocated
   strings as *name*. For names that aren't known at compile time,
   prefer calling "PyUnicode_FromString()" and "PyObject_SetAttr()"
   directly. For more details, see "PyUnicode_InternFromString()",
   which may be used internally to create a key object.

   Added in version 3.10.

int PyModule_Add(PyObject *module, const char *name, PyObject *value)
    * Part of the Stable ABI since version 3.13.*

   Similar to "PyModule_AddObjectRef()", but "*steals*" a reference to
   *value* (even on error). It can be called with a result of function
   that returns a new reference without bothering to check its result
   or even saving it to a variable.

   Ejemplo de uso

      if (PyModule_Add(module, "spam", PyBytes_FromString(value)) < 0) {
          goto error;
      }

   Added in version 3.13.

int PyModule_AddObject(PyObject *module, const char *name, PyObject *value)
    * Part of the Stable ABI.*

   Similar to "PyModule_AddObjectRef()", but *steals* a reference to
   *value* on success (if it returns "0").

   The new "PyModule_Add()" or "PyModule_AddObjectRef()" functions are
   recommended, since it is easy to introduce reference leaks by
   misusing the "PyModule_AddObject()" function.

   Nota:

     Unlike other functions that steal references,
     "PyModule_AddObject()" only releases the reference to *value*
     **on success**.This means that its return value must be checked,
     and calling code must "Py_XDECREF()" *value* manually on error.

   Ejemplo de uso

      PyObject *obj = PyBytes_FromString(value);
      if (PyModule_AddObject(module, "spam", obj) < 0) {
          // If 'obj' is not NULL and PyModule_AddObject() failed,
          // 'obj' strong reference must be deleted with Py_XDECREF().
          // If 'obj' is NULL, Py_XDECREF() does nothing.
          Py_XDECREF(obj);
          goto error;
      }
      // PyModule_AddObject() stole a reference to obj:
      // Py_XDECREF(obj) is not needed here.

   Soft deprecated since version 3.13.

int PyModule_AddIntConstant(PyObject *module, const char *name, long value)
    * Part of the Stable ABI.*

   Add an integer constant to *module* as *name*.  This convenience
   function can be used from the module's initialization function.
   Return "-1" with an exception set on error, "0" on success.

   This is a convenience function that calls "PyLong_FromLong()" and
   "PyModule_AddObjectRef()"; see their documentation for details.

int PyModule_AddStringConstant(PyObject *module, const char *name, const char *value)
    * Part of the Stable ABI.*

   Add a string constant to *module* as *name*.  This convenience
   function can be used from the module's initialization function.
   The string *value* must be "NULL"-terminated. Return "-1" with an
   exception set on error, "0" on success.

   This is a convenience function that calls
   "PyUnicode_InternFromString()" and "PyModule_AddObjectRef()"; see
   their documentation for details.

PyModule_AddIntMacro(module, macro)

   Add an int constant to *module*. The name and the value are taken
   from *macro*. For example "PyModule_AddIntMacro(module, AF_INET)"
   adds the int constant *AF_INET* with the value of *AF_INET* to
   *module*. Return "-1" with an exception set on error, "0" on
   success.

PyModule_AddStringMacro(module, macro)

   Agrega una constante de cadena de caracteres a *module*.

int PyModule_AddType(PyObject *module, PyTypeObject *type)
    * Part of the Stable ABI since version 3.10.*

   Add a type object to *module*. The type object is finalized by
   calling internally "PyType_Ready()". The name of the type object is
   taken from the last component of "tp_name" after dot. Return "-1"
   with an exception set on error, "0" on success.

   Added in version 3.9.

int PyModule_AddFunctions(PyObject *module, PyMethodDef *functions)
    * Part of the Stable ABI since version 3.7.*

   Add the functions from the "NULL" terminated *functions* array to
   *module*. Refer to the "PyMethodDef" documentation for details on
   individual entries (due to the lack of a shared module namespace,
   module level "functions" implemented in C typically receive the
   module as their first parameter, making them similar to instance
   methods on Python classes).

   This function is called automatically when creating a module from
   "PyModuleDef" (such as when using Multi-phase initialization,
   "PyModule_Create", or "PyModule_FromDefAndSpec"). Some module
   authors may prefer defining functions in multiple "PyMethodDef"
   arrays; in that case they should call this function directly.

   The *functions* array must be statically allocated (or otherwise
   guaranteed to outlive the module object).

   Added in version 3.5.

int PyModule_SetDocString(PyObject *module, const char *docstring)
    * Part of the Stable ABI since version 3.7.*

   Set the docstring for *module* to *docstring*. This function is
   called automatically when creating a module from "PyModuleDef"
   (such as when using Multi-phase initialization, "PyModule_Create",
   or "PyModule_FromDefAndSpec").

   Return "0" on success. Return "-1" with an exception set on error.

   Added in version 3.5.

int PyUnstable_Module_SetGIL(PyObject *module, void *gil)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Indicate that *module* does or does not support running without the
   global interpreter lock (GIL), using one of the values from
   "Py_mod_gil". It must be called during *module*'s initialization
   function when using Legacy single-phase initialization. If this
   function is not called during module initialization, the import
   machinery assumes the module does not support running without the
   GIL. This function is only available in Python builds configured
   with "--disable-gil". Return "-1" with an exception set on error,
   "0" on success.

   Added in version 3.13.

## Module lookup (single-phase initialization)

The legacy single-phase initialization initialization scheme creates
singleton modules that can be looked up in the context of the current
interpreter. This allows the module object to be retrieved later with
only a reference to the module definition.

Estas funciones no funcionarán en módulos creados mediante la
inicialización de múltiples fases, ya que se pueden crear múltiples
módulos de este tipo desde una sola definición.

PyObject *PyState_FindModule(PyModuleDef *def)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Retorna el objeto módulo que se creó a partir de *def* para el
   intérprete actual. Este método requiere que el objeto módulo se
   haya adjuntado al estado del intérprete con "PyState_AddModule()"
   de antemano. En caso de que el objeto módulo correspondiente no se
   encuentre o no se haya adjuntado al estado del intérprete,
   retornará "NULL".

int PyState_AddModule(PyObject *module, PyModuleDef *def)
    * Part of the Stable ABI since version 3.3.*

   Adjunta el objeto del módulo pasado a la función al estado del
   intérprete. Esto permite que se pueda acceder al objeto del módulo
   a través de "PyState_FindModule()".

   Solo es efectivo en módulos creados con la inicialización
   monofásica.

   Python calls "PyState_AddModule" automatically after importing a
   module that uses single-phase initialization, so it is unnecessary
   (but harmless) to call it from module initialization code. An
   explicit call is needed only if the module's own init code
   subsequently calls "PyState_FindModule". The function is mainly
   intended for implementing alternative import mechanisms (either by
   calling it directly, or by referring to its implementation for
   details of the required state updates).

   If a module was attached previously using the same *def*, it is
   replaced by the new *module*.

   The caller must have an *attached thread state*.

   Return "-1" with an exception set on error, "0" on success.

   Added in version 3.3.

int PyState_RemoveModule(PyModuleDef *def)
    * Part of the Stable ABI since version 3.3.*

   Removes the module object created from *def* from the interpreter
   state. Return "-1" with an exception set on error, "0" on success.

   The caller must have an *attached thread state*.

   Added in version 3.3.
