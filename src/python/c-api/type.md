---
title: Objetos tipo
source_url: https://docs.python.org/es/3
source_path: c-api/type.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 730
---

# Objetos tipo

type PyTypeObject
    * Part of the Limited API (as an opaque struct).*

   La estructura C de los objetos utilizados para describir los tipos
   incorporados.

PyTypeObject PyType_Type
    * Part of the Stable ABI.*

   Este es el objeto tipo para objetos tipo; es el mismo objeto que
   "type" en la capa Python.

int PyType_Check(PyObject *o)

   Retorna un valor distinto de cero si el objeto *o* es un objeto
   tipo, incluidas las instancias de tipos derivados del objeto de
   tipo estándar. Retorna 0 en todos los demás casos. Esta función
   siempre finaliza con éxito.

int PyType_CheckExact(PyObject *o)

   Retorna un valor distinto de cero si el objeto *o* es un objeto
   tipo, pero no un subtipo del objeto tipo estándar. Retorna 0 en
   todos los demás casos. Esta función siempre finaliza con éxito.

unsigned int PyType_ClearCache()
    * Part of the Stable ABI.*

   Borra la caché de búsqueda interna. Retorna la etiqueta (*tag*) de
   la versión actual.

unsigned long PyType_GetFlags(PyTypeObject *type)
    * Part of the Stable ABI.*

   Retorna el miembro "tp_flags" de *type*. Esta función está
   destinada principalmente para su uso con "Py_LIMITED_API"; se
   garantiza que los bits de bandera individuales serán estables en
   las versiones de Python, pero el acceso a "tp_flags" en sí mismo no
   forma parte de la API limitada.

   Added in version 3.2.

   Distinto en la versión 3.4: El tipo de retorno es ahora "unsigned
   long" en vez de "long".

PyObject *PyType_GetDict(PyTypeObject *type)

   Retorna el espacio de nombres interno del objeto tipo, que de otra
   manera solo está expuesto a través de un *proxy* de solo lectura
   ("cls.__dict__"). Esto es un reemplazo para acceder a "tp_dict"
   directamente. El diccionario retornado debe tratarse como de solo
   lectura.

   Esta función está destinada a casos específicos de incrustación y
   vinculación de lenguajes, donde el acceso directo al diccionario es
   necesario y el acceso indirecto (por ejemplo, a través del *proxy*
   o "PyObject_GetAttr()") no es adecuado.

   Los módulos de extensión deben continuar usando "tp_dict", directa
   o indirectamente, al configurar sus propios tipos.

   Added in version 3.12.

void PyType_Modified(PyTypeObject *type)
    * Part of the Stable ABI.*

   Invalida la memoria caché de búsqueda interna para el tipo y todos
   sus subtipos. Esta función debe llamarse después de cualquier
   modificación manual de los atributos o clases base del tipo.

int PyType_AddWatcher(PyType_WatchCallback callback)

   Registra *callback* como un observador de tipo. Retorna un ID
   entero no negativo que debe pasarse a llamadas futuras a
   "PyType_Watch()". En caso de error (por ejemplo, no hay más IDs de
   observador disponibles), retorna "-1" y establece una excepción.

   In free-threaded builds, "PyType_AddWatcher()" is not thread-safe,
   so it must be called at start up (before spawning the first
   thread).

   Added in version 3.12.

int PyType_ClearWatcher(int watcher_id)

   Borra el observador identificado por *watcher_id* (previamente
   retornado de "PyType_AddWatcher()"). Retorna "0" en caso de éxito,
   "-1" en caso de error (por ejemplo, si *watcher_id* nunca fue
   registrado).

   Una extensión nunca debe llamar a "PyType_ClearWatcher" con un
   *watcher_id* que no le fue retornado por una llamada previa a
   "PyType_AddWatcher()".

   Added in version 3.12.

int PyType_Watch(int watcher_id, PyObject *type)

   Marca *type* como observado. El retrollamada (*callback*) otorgado
   *watcher_id* por "PyType_AddWatcher()" será llamado cada vez que
   "PyType_Modified()" reporte un cambio a *type*. (El *callback*
   puede ser llamado solo una vez para una serie de modificaciones
   consecutivas a *type*, si "_PyType_Lookup()" no es llamado en
   *type* entre las modificaciones; esto es un detalle de
   implementación y sujeto a cambios).

   Una extensión nunca debe llamar a "PyType_Watch" con un
   *watcher_id* que no le fue retornado por una llamada previa a
   "PyType_AddWatcher()".

   Added in version 3.12.

int PyType_Unwatch(int watcher_id, PyObject *type)

   Mark *type* as not watched. This undoes a previous call to
   "PyType_Watch()". *type* must not be "NULL".

   An extension should never call this function with a *watcher_id*
   that was not returned to it by a previous call to
   "PyType_AddWatcher()".

   On success, this function returns "0". On failure, this function
   returns "-1" with an exception set.

   Added in version 3.12.

typedef int (*PyType_WatchCallback)(PyObject *type)

   Tipo de una función de retrollamada (*callback*) de observador de
   tipo.

   El retrollamada (*callback*) no debe modificar *type* o causar que
   "PyType_Modified()" sea llamado en *type* o cualquier tipo en su
   MRO; violar esta regla podría causar recursión infinita.

   Added in version 3.12.

int PyType_HasFeature(PyTypeObject *o, int feature)

   Retorna un valor distinto de cero si el tipo objeto *o* establece
   la característica *feature*. Las características de tipo se indican
   mediante flags de un solo bit.

int PyType_FastSubclass(PyTypeObject *type, int flag)

   Return non-zero if the type object *type* sets the subclass flag
   *flag*. Subclass flags are denoted by "Py_TPFLAGS_*_SUBCLASS". This
   function is used by many "_Check" functions for common types.

   Ver también:

     "PyObject_TypeCheck()", which is used as a slower alternative in
     "_Check" functions for types that don't come with subclass flags.

int PyType_IS_GC(PyTypeObject *o)

   Retorna verdadero si el objeto tipo incluye soporte para el
   detector de ciclos; esto prueba el indicador de tipo
   "Py_TPFLAGS_HAVE_GC".

int PyType_IsSubtype(PyTypeObject *a, PyTypeObject *b)
    * Part of the Stable ABI.*

   Retorna verdadero si *a* es un subtipo de *b*.

   Esta función solo busca subtipos reales, lo que significa que
   "__subclasscheck__()" no se llama en *b*. Llama
   "PyObject_IsSubclass()" para hacer la misma verificación que
   "issubclass()" haría.

PyObject *PyType_GenericAlloc(PyTypeObject *type, Py_ssize_t nitems)
    *Return value: New reference.** Part of the Stable ABI.*

   Generic handler for the "tp_alloc" slot of a type object.  Uses
   Python's default memory allocation mechanism to allocate memory for
   a new instance, zeros the memory, then initializes the memory as if
   by calling "PyObject_Init()" or "PyObject_InitVar()".

   Do not call this directly to allocate memory for an object; call
   the type's "tp_alloc" slot instead.

   For types that support garbage collection (i.e., the
   "Py_TPFLAGS_HAVE_GC" flag is set), this function behaves like
   "PyObject_GC_New" or "PyObject_GC_NewVar" (except the memory is
   guaranteed to be zeroed before initialization), and should be
   paired with "PyObject_GC_Del()" in "tp_free". Otherwise, it behaves
   like "PyObject_New" or "PyObject_NewVar" (except the memory is
   guaranteed to be zeroed before initialization) and should be paired
   with "PyObject_Free()" in "tp_free".

PyObject *PyType_GenericNew(PyTypeObject *type, PyObject *args, PyObject *kwds)
    *Return value: New reference.** Part of the Stable ABI.*

   Generic handler for the "tp_new" slot of a type object.  Creates a
   new instance using the type's "tp_alloc" slot and returns the
   resulting object.

int PyType_Ready(PyTypeObject *type)
    * Part of the Stable ABI.*

   Finalizar un objeto tipo. Se debe llamar a todos los objetos tipo
   para finalizar su inicialización. Esta función es responsable de
   agregar ranuras heredadas de la clase base de un tipo. Retorna "0"
   en caso de éxito o retorna "-1" y establece una excepción en caso
   de error.

   Nota:

     Si algunas de las clases base implementan el protocolo GC y el
     tipo proporcionado no incluye "Py_TPFLAGS_HAVE_GC" en sus
     banderas, entonces el protocolo GC se implementará
     automáticamente desde sus padres. Por el contrario, si el tipo
     que se está creando incluye "Py_TPFLAGS_HAVE_GC" en sus banderas,
     entonces **debe** implementar el protocolo GC por sí mismo
     implementando al menos el manejador "tp_traverse".

PyObject *PyType_GetName(PyTypeObject *type)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.11.*

   Retorna el nombre del tipo. Equivalente a obtener el atributo
   "__name__" del tipo.

   Added in version 3.11.

PyObject *PyType_GetQualName(PyTypeObject *type)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.11.*

   Retorna el nombre calificado del tipo. Equivalente a obtener el
   atributo "__qualname__" del tipo.

   Added in version 3.11.

PyObject *PyType_GetFullyQualifiedName(PyTypeObject *type)
    * Part of the Stable ABI since version 3.13.*

   Retorna el nombre completamente calificado del tipo. Equivalente a
   "f"{type.__module__}.{type.__qualname__}"", o "type.__qualname__"
   si "type.__module__" no es una cadena de caracteres o es igual a
   ""builtins"".

   Added in version 3.13.

PyObject *PyType_GetModuleName(PyTypeObject *type)
    * Part of the Stable ABI since version 3.13.*

   Retorna el nombre del módulo del tipo. Equivalente a obtener el
   atributo "type.__module__".

   Added in version 3.13.

void *PyType_GetSlot(PyTypeObject *type, int slot)
    * Part of the Stable ABI since version 3.4.*

   Retorna el puntero de función almacenado en la ranura dada. Si el
   resultado es "NULL", esto indica que la ranura es "NULL" o que la
   función se llamó con parámetros no válidos. Las personas que llaman
   suelen convertir el puntero de resultado en el tipo de función
   apropiado.

   Consulte "PyType_Slot.slot" para conocer los posibles valores del
   argumento *slot*.

   Added in version 3.4.

   Distinto en la versión 3.10: "PyType_GetSlot()" ahora puede aceptar
   todos los tipos. Anteriormente, estaba limitado a heap types.

PyObject *PyType_GetModule(PyTypeObject *type)
    *Return value: Borrowed reference.** Part of the Stable ABI since
   version 3.10.*

   Retorna el objeto módulo asociado con el tipo dado cuando se creó
   el tipo usando "PyType_FromModuleAndSpec()".

   The returned reference is *borrowed* from *type*, and will be valid
   as long as you hold a reference to *type*. Do not release it with
   "Py_DECREF()" or similar.

   Si no hay ningún módulo asociado con el tipo dado, establece
   "TypeError" y retorna "NULL".

   Esta función se suele utilizar para obtener el módulo en el que se
   define un método. Tenga en cuenta que en un método de este tipo, es
   posible que "PyType_GetModule(Py_TYPE(self))" no retorne el
   resultado deseado. "Py_TYPE(self)" puede ser una *subclass* de la
   clase deseada, y las subclases no están necesariamente definidas en
   el mismo módulo que su superclase. Consulte "PyCMethod" para
   obtener la clase que define el método. Consulte
   "PyType_GetModuleByDef()" para los casos en los que no se puede
   usar "PyCMethod".

   Added in version 3.9.

void *PyType_GetModuleState(PyTypeObject *type)
    * Part of the Stable ABI since version 3.10.*

   Retorna el estado del objeto de módulo asociado con el tipo dado.
   Este es un atajo para llamar "PyModule_GetState()" en el resultado
   de "PyType_GetModule()".

   Si no hay ningún módulo asociado con el tipo dado, establece
   "TypeError" y retorna "NULL".

   Si el tipo *type* tiene un módulo asociado pero su estado es
   "NULL", retorna "NULL" sin establecer una excepción.

   Added in version 3.9.

PyObject *PyType_GetModuleByDef(PyTypeObject *type, struct PyModuleDef *def)
    *Return value: Borrowed reference.** Part of the Stable ABI since
   version 3.13.*

   Encuentra la primer superclase cuyo módulo fue creado a partir del
   "PyModuleDef" *def* dado, y retorna ese módulo.

   Si no se encuentra ningún módulo, lanza "TypeError" y retorna
   "NULL".

   Esta función está pensada para ser utilizada junto con
   "PyModule_GetState()" para obtener el estado del módulo de los
   métodos de ranura (como "tp_init" o "nb_add") y en otros lugares
   donde la clase que define a un método no se puede pasar utilizando
   la convención de llamada "PyCMethod".

   The returned reference is *borrowed* from *type*, and will be valid
   as long as you hold a reference to *type*. Do not release it with
   "Py_DECREF()" or similar.

   Added in version 3.11.

int PyType_GetBaseByToken(PyTypeObject *type, void *token, PyTypeObject **result)
    * Part of the Stable ABI since version 3.14.*

   Find the first superclass in *type*'s *method resolution order*
   whose "Py_tp_token" token is equal to the given one.

   * If found, set **result* to a new *strong reference* to it and
     return "1".

   * If not found, set **result* to "NULL" and return "0".

   * On error, set **result* to "NULL" and return "-1" with an
     exception set.

   The *result* argument may be "NULL", in which case **result* is not
   set. Use this if you need only the return value.

   The *token* argument may not be "NULL".

   Added in version 3.14.

int PyUnstable_Type_AssignVersionTag(PyTypeObject *type)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Intenta asignar una etiqueta (*tag*) de versión al tipo dado.

   Retorna 1 si el tipo ya tenía una etiqueta (*tag*) de versión
   válida o se asignó una nueva, o 0 si no se pudo asignar una nueva
   etiqueta.

   Added in version 3.12.

int PyType_SUPPORTS_WEAKREFS(PyTypeObject *type)

   Return true if instances of *type* support creating weak
   references, false otherwise. This function always succeeds. *type*
   must not be "NULL".

   Ver también:

     * Objetos de referencia débil

     * "weakref"

## Crear tipos asignados en montículo (*heap*)

Las siguientes funciones y estructuras se utilizan para crear heap
types.

PyObject *PyType_FromMetaclass(PyTypeObject *metaclass, PyObject *module, PyType_Spec *spec, PyObject *bases)
    * Part of the Stable ABI since version 3.12.*

   Crea y retorna un tipo heap a partir del *spec* (ver
   "Py_TPFLAGS_HEAPTYPE").

   La metaclase *metaclass* se usa para construir el objeto tipo
   resultante. Cuando *metaclass* es "NULL", la metaclase se deriva de
   *bases* (o ranuras *Py_tp_base[s]* si *bases* es "NULL", ver
   abajo).

   Metaclasses that override "tp_new" are not supported, except if
   "tp_new" is "NULL".

   The *bases* argument can be used to specify base classes; it can
   either be only one class or a tuple of classes. If *bases* is
   "NULL", the "Py_tp_bases" slot is used instead. If that also is
   "NULL", the "Py_tp_base" slot is used instead. If that also is
   "NULL", the new type derives from "object".

   El argumento *module* se puede utilizar para registrar el módulo en
   el que se define la nueva clase. Debe ser un objeto de módulo o
   "NULL". Si no es "NULL", el módulo se asocia con el nuevo tipo y
   luego se puede recuperar con "PyType_GetModule()". El módulo
   asociado no es heredado por subclases; debe especificarse para cada
   clase individualmente.

   Esta función llama "PyType_Ready()" en el tipo nuevo.

   Nota que esta función *no* coincide completamente con el
   comportamiento de llamar "type()" o usar la sentencia "class". Con
   tipos base o metaclases proporcionados por el usuario, prefiera
   llamar "type" (o la metaclase) sobre las funciones "PyType_From*".
   Específicamente:

   * "__new__()" no es llamado en la nueva clase (y debe ser
     establecido a "type.__new__").

   * "__init__()" no es llamado en la nueva clase.

   * "__init_subclass__()" no es llamado en ninguna base.

   * "__set_name__()" no es llamado en nuevos descriptores.

   Added in version 3.12.

PyObject *PyType_FromModuleAndSpec(PyObject *module, PyType_Spec *spec, PyObject *bases)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.10.*

   Equivalente a "PyType_FromMetaclass(NULL, module, spec, bases)".

   Added in version 3.9.

   Distinto en la versión 3.10: La función ahora acepta una sola clase
   como argumento *bases* y "NULL" como ranura "tp_doc".

   Distinto en la versión 3.12: La función ahora encuentra y usa una
   metaclase correspondiente a las clases base proporcionadas.
   Anteriormente, sólo se retornaban instancias de "type".The "tp_new"
   of the metaclass is *ignored*. which may result in incomplete
   initialization. Creating classes whose metaclass overrides "tp_new"
   is deprecated.

   Distinto en la versión 3.14: Creating classes whose metaclass
   overrides "tp_new" is no longer allowed.

PyObject *PyType_FromSpecWithBases(PyType_Spec *spec, PyObject *bases)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.3.*

   Equivalente a "PyType_FromMetaclass(NULL, NULL, spec, bases)".

   Added in version 3.3.

   Distinto en la versión 3.12: La función ahora encuentra y usa una
   metaclase correspondiente a las clases base proporcionadas.
   Anteriormente, sólo se retornaban instancias de "type".The "tp_new"
   of the metaclass is *ignored*. which may result in incomplete
   initialization. Creating classes whose metaclass overrides "tp_new"
   is deprecated.

   Distinto en la versión 3.14: Creating classes whose metaclass
   overrides "tp_new" is no longer allowed.

PyObject *PyType_FromSpec(PyType_Spec *spec)
    *Return value: New reference.** Part of the Stable ABI.*

   Equivalente a "PyType_FromMetaclass(NULL, NULL, spec, NULL)".

   Distinto en la versión 3.12: La función ahora encuentra y usa una
   metaclase correspondiente a las clases base proporcionadas en las
   ranuras *Py_tp_base[s]*. Anteriormente, sólo se retornaban
   instancias de "type".The "tp_new" of the metaclass is *ignored*.
   which may result in incomplete initialization. Creating classes
   whose metaclass overrides "tp_new" is deprecated.

   Distinto en la versión 3.14: Creating classes whose metaclass
   overrides "tp_new" is no longer allowed.

int PyType_Freeze(PyTypeObject *type)
    * Part of the Stable ABI since version 3.14.*

   Make a type immutable: set the "Py_TPFLAGS_IMMUTABLETYPE" flag.

   All base classes of *type* must be immutable.

   On success, return "0". On error, set an exception and return "-1".

   The type must not be used before it's made immutable. For example,
   type instances must not be created before the type is made
   immutable.

   Added in version 3.14.

type PyType_Spec
    * Part of the Stable ABI (including all members).*

   Estructura que define el comportamiento de un tipo.

   const char *name

      Nombre del tipo, utilizado para establecer
      "PyTypeObject.tp_name".

   int basicsize

      Si es positivo, especifica el tamaño de la instancia en bytes.
      Se utiliza para establecer "PyTypeObject.tp_basicsize".

      Si es cero, especifica que "tp_basicsize" debe ser heredado.

      If negative, the absolute value specifies how much space
      instances of the class need *in addition* to the superclass. Use
      "PyObject_GetTypeData()" to get a pointer to subclass-specific
      memory reserved this way. For negative "basicsize", Python will
      insert padding when needed to meet "tp_basicsize"'s alignment
      requirements.

      Distinto en la versión 3.12: Anteriormente, este campo no podía
      ser negativo.

   int itemsize

      Tamaño de un elemento de un tipo de tamaño variable, en bytes.
      Utilizado para establecer "PyTypeObject.tp_itemsize". Consulte
      la documentación de "tp_itemsize" para conocer las advertencias.

      Si es cero, "tp_itemsize" se hereda. Extender clases de tamaño
      variable arbitrario es peligroso, ya que algunos tipos usan un
      desplazamiento fijo para memoria de tamaño variable, que puede
      entonces superponerse con memoria de tamaño fijo usada por una
      subclase. Para ayudar a prevenir errores, heredar "itemsize"
      sólo es posible en las siguientes situaciones:

      * The base is not variable-sized (its "tp_itemsize" is zero).

      * El "PyType_Spec.basicsize" solicitado es positivo, sugiriendo
        que la distribución de memoria de la clase base es conocida.

      * El "PyType_Spec.basicsize" solicitado es cero, sugiriendo que
        la subclase no accede a la memoria de la instancia
        directamente.

      * Con la bandera "Py_TPFLAGS_ITEMS_AT_END".

   unsigned int flags

      Banderas (*flags*) del tipo, que se usan para establecer
      "PyTypeObject.tp_flags".

      Si el indicador "Py_TPFLAGS_HEAPTYPE" no está establecido,
      "PyType_FromSpecWithBases()" lo establece automáticamente.

   PyType_Slot *slots

      Arreglo de estructuras "PyType_Slot". Terminado por el valor de
      ranura especial "{0, NULL}".

      Cada ID de ranura debe especificarse como máximo una vez.

type PyType_Slot
    * Part of the Stable ABI (including all members).*

   Estructura que define la funcionalidad opcional de un tipo, que
   contiene una ranura ID y un puntero de valor.

   int slot

      Una ranura ID.

      Las ranuras IDs se nombran como los nombres de campo de las
      estructuras "PyTypeObject", "PyNumberMethods",
      "PySequenceMethods", "PyMappingMethods" y "PyAsyncMethods" con
      un prefijo "Py_" agregado. Por ejemplo, use:

      * "Py_tp_dealloc" to set "PyTypeObject.tp_dealloc"

      * "Py_nb_add" to set "PyNumberMethods.nb_add"

      * "Py_sq_length" to set "PySequenceMethods.sq_length"

      An additional slot is supported that does not correspond to a
      "PyTypeObject" struct field:

      * "Py_tp_token"

      The following “offset” fields cannot be set using "PyType_Slot":

      * "tp_weaklistoffset" (use "Py_TPFLAGS_MANAGED_WEAKREF" en su
        lugar si es posible)

      * "tp_dictoffset" (use "Py_TPFLAGS_MANAGED_DICT" en su lugar si
        es posible)

      * "tp_vectorcall_offset" (use ""__vectorcalloffset__"" en
        PyMemberDef)

      If it is not possible to switch to a "MANAGED" flag (for
      example, for vectorcall or to support Python older than 3.12),
      specify the offset in "Py_tp_members". See PyMemberDef
      documentation for details.

      The following internal fields cannot be set at all when creating
      a heap type:

      * "tp_dict", "tp_mro", "tp_cache", "tp_subclasses", and
        "tp_weaklist".

      Establecer "Py_tp_bases" o "Py_tp_base" puede ser problemático
      en algunas plataformas. Para evitar problemas, use el argumento
      *bases* de "PyType_FromSpecWithBases()" en su lugar.

      Distinto en la versión 3.9: Las ranuras en "PyBufferProcs" se
      pueden configurar en la API ilimitada.

      Distinto en la versión 3.11: "bf_getbuffer" y "bf_releasebuffer"
      ahora están disponibles bajo la API limitada.

      Distinto en la versión 3.14: The field "tp_vectorcall" can now
      be set using "Py_tp_vectorcall".  See the field's documentation
      for details.

   void *pfunc

      El valor deseado de la ranura. En la mayoría de los casos, este
      es un puntero a una función.

      *pfunc* values may not be "NULL", except for the following
      slots:

      * "Py_tp_doc"

      * "Py_tp_token" (for clarity, prefer "Py_TP_USE_SPEC" rather
        than "NULL")

Py_tp_token
    * Part of the Stable ABI since version 3.14.*

   A "slot" that records a static memory layout ID for a class.

   If the "PyType_Spec" of the class is statically allocated, the
   token can be set to the spec using the special value
   "Py_TP_USE_SPEC":

      static PyType_Slot foo_slots[] = {
         {Py_tp_token, Py_TP_USE_SPEC},

   It can also be set to an arbitrary pointer, but you must ensure
   that:

   * The pointer outlives the class, so it's not reused for something
     else while the class exists.

   * It "belongs" to the extension module where the class lives, so it
     will not clash with other extensions.

   Use "PyType_GetBaseByToken()" to check if a class's superclass has
   a given token -- that is, check whether the memory layout is
   compatible.

   To get the token for a given class (without considering
   superclasses), use "PyType_GetSlot()" with "Py_tp_token".

   Added in version 3.14.

   Py_TP_USE_SPEC
       * Part of the Stable ABI since version 3.14.*

      Used as a value with "Py_tp_token" to set the token to the
      class's "PyType_Spec". Expands to "NULL".

      Added in version 3.14.
