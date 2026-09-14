---
title: Apoyo a la recolección de basura cíclica
source_url: https://docs.python.org/es/3
source_path: c-api/gcsupport.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 310
---

# Apoyo a la recolección de basura cíclica

El soporte de Python para detectar y recolectar basura que involucra
referencias circulares requiere el soporte de tipos de objetos que son
"contenedores" para otros objetos que también pueden ser contenedores.
Los tipos que no almacenan referencias a otros objetos, o que solo
almacenan referencias a tipos atómicos (como números o cadenas), no
necesitan proporcionar ningún soporte explícito para la recolección de
basura.

Para crear un tipo de contenedor, el campo "tp_flags" del objeto tipo
debe incluir "Py_TPFLAGS_HAVE_GC" y proporcionar una implementación
del manejador "tp_traverse". Si las instancias del tipo son mutables,
también se debe proporcionar una implementación a "tp_clear".

"Py_TPFLAGS_HAVE_GC"
   Los objetos con un tipo con este indicador establecido deben
   cumplir con las reglas documentadas aquí. Por conveniencia, estos
   objetos se denominarán objetos contenedor.

Los constructores para tipos de contenedores deben cumplir con dos
reglas:

1. La memoria para el objeto debe asignarse usando "PyObject_GC_New" o
   "PyObject_GC_NewVar".

2. Una vez que se inicializan todos los campos que pueden contener
   referencias a otros contenedores, debe llamar a
   "PyObject_GC_Track()".

Del mismo modo, el desasignador (*deallocator*) para el objeto debe
cumplir con un par similar de reglas:

1. Antes de invalidar los campos que se refieren a otros contenedores,
   debe llamarse "PyObject_GC_UnTrack()".

2. La memoria del objeto debe ser desasignada (*deallocated*) usando
   "PyObject_GC_Del()".

   Advertencia:

     Si un tipo añade el Py_TPFLAGS_HAVE_GC, entonces *must*
     implementar al menos un manejado "tp_traverse" o usar
     explícitamente uno de su subclase o subclases.Al llamar a
     "PyType_Ready()" o alguna de las APIs que indirectamente lo
     llaman como "PyType_FromSpecWithBases()" o "PyType_FromSpec()" el
     intérprete automáticamente llenara los campos "tp_flags",
     "tp_traverse" y "tp_clear" si el tipo hereda de una clase que
     implementa el protocolo del recolector de basura y la clase
     secundaria *no* incluye el *flag* "Py_TPFLAGS_HAVE_GC".

PyObject_GC_New(TYPE, typeobj)

   Análogo a "PyObject_New" pero para objetos de contenedor con el
   *flag* "Py_TPFLAGS_HAVE_GC" establecido.

   Do not call this directly to allocate memory for an object; call
   the type's "tp_alloc" slot instead.

   When populating a type's "tp_alloc" slot, "PyType_GenericAlloc()"
   is preferred over a custom function that simply calls this macro.

   Memory allocated by this macro must be freed with
   "PyObject_GC_Del()" (usually called via the object's "tp_free"
   slot).

   Ver también:

     * "PyObject_GC_Del()"

     * "PyObject_New"

     * "PyType_GenericAlloc()"

     * "tp_alloc"

PyObject_GC_NewVar(TYPE, typeobj, size)

   Análogo a "PyObject_NewVar" pero para objetos de contenedor con el
   *flag* "Py_TPFLAGS_HAVE_GC" establecido.

   Do not call this directly to allocate memory for an object; call
   the type's "tp_alloc" slot instead.

   When populating a type's "tp_alloc" slot, "PyType_GenericAlloc()"
   is preferred over a custom function that simply calls this macro.

   Memory allocated by this macro must be freed with
   "PyObject_GC_Del()" (usually called via the object's "tp_free"
   slot).

   Ver también:

     * "PyObject_GC_Del()"

     * "PyObject_NewVar"

     * "PyType_GenericAlloc()"

     * "tp_alloc"

PyObject *PyUnstable_Object_GC_NewWithExtraData(PyTypeObject *type, size_t extra_size)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Análogo a "PyObject_GC_New" pero asigna *extra_size* bytes al final
   del objeto (en el desplazamiento "tp_basicsize"). La memoria
   asignada se inicializa a ceros, excepto para el "encabezado del
   objeto Python".

   Los datos extras se desasignarán con el objeto, pero por lo demás
   no se gestionan por Python.

   Memory allocated by this function must be freed with
   "PyObject_GC_Del()" (usually called via the object's "tp_free"
   slot).

   Advertencia:

     La función está marcada como inestable porque aún no se ha
     decidido el mecanismo final para reservar datos extra después de
     una instancia. Para asignar un número variable de campos, se
     recomienda usar en su lugar "PyVarObject" y "tp_itemsize".

   Added in version 3.12.

PyObject_GC_Resize(TYPE, op, newsize)

   Cambia el tamaño de un objeto asignado por "PyObject_NewVar".
   Retorna el objeto redimensionado de tipo "TYPE*" (se refiere a
   cualquier tipo de C) o "NULL" en caso de falla.

   *op* debe ser de tipo PyVarObject* y aún no debe ser rastreado por
   el recolector. *newsize* debe ser de tipo "Py_ssize_t".

void PyObject_GC_Track(PyObject *op)
    * Part of the Stable ABI.*

   Agrega el objeto *op* al conjunto de objetos contenedor seguidos
   por el recolector de basura. El recolector puede ejecutarse en
   momentos inesperados, por lo que los objetos deben ser válidos
   durante el seguimiento. Esto debería llamarse una vez que todos los
   campos seguidos por "tp_traverse" se vuelven válidos, generalmente
   cerca del final del constructor.

int PyObject_IS_GC(PyObject *obj)

   Retorna un valor distinto de cero si el objeto implementa el
   protocolo del recolector de basura; de lo contrario, retorna 0.

   El recolector de basura no puede rastrear el objeto si esta función
   retorna 0.

int PyObject_GC_IsTracked(PyObject *op)
    * Part of the Stable ABI since version 3.9.*

   Retorna 1 si el tipo de objeto de *op* implementa el protocolo GC y
   el recolector de basura está rastreando *op* y 0 en caso contrario.

   Esto es análogo a la función de Python "gc.is_tracked()".

   Added in version 3.9.

int PyObject_GC_IsFinalized(PyObject *op)
    * Part of the Stable ABI since version 3.9.*

   Retorna 1 si el tipo de objeto de *op* implementa el protocolo GC y
   *op* ya ha sido finalizado por el recolector de basura y 0 en caso
   contrario.

   Esto es análogo a la función de Python "gc.is_finalized()".

   Added in version 3.9.

void PyObject_GC_Del(void *op)
    * Part of the Stable ABI.*

   Libera memoria asignada a un objeto usando "PyObject_GC_New" o
   "PyObject_GC_NewVar".

   Do not call this directly to free an object's memory; call the
   type's "tp_free" slot instead.

   Do not use this for memory allocated by "PyObject_New",
   "PyObject_NewVar", or related allocation functions; use
   "PyObject_Free()" instead.

   Ver también:

     * "PyObject_Free()" is the non-GC equivalent of this function.

     * "PyObject_GC_New"

     * "PyObject_GC_NewVar"

     * "PyType_GenericAlloc()"

     * "tp_free"

void PyObject_GC_UnTrack(void *op)
    * Part of the Stable ABI.*

   Elimina el objeto *op* del conjunto de objetos contenedor
   rastreados por el recolector de basura. Tenga en cuenta que
   "PyObject_GC_Track()" puede ser llamado nuevamente en este objeto
   para agregarlo nuevamente al conjunto de objetos rastreados. El
   desasignador (el manejador "tp_dealloc") debería llamarlo para el
   objeto antes de que cualquiera de los campos utilizados por el
   manejador "tp_traverse" no sea válido.

Distinto en la versión 3.8: Los macros "_PyObject_GC_TRACK()" y
"_PyObject_GC_UNTRACK()" se han eliminado de la API pública de C.

El manejador "tp_traverse" acepta un parámetro de función de este
tipo:

typedef int (*visitproc)(PyObject *object, void *arg)
    * Part of the Stable ABI.*

   Tipo de la función visitante que se pasa al manejador
   "tp_traverse". La función debe llamarse con un objeto para
   atravesar como *object* y el tercer parámetro para el manejador
   "tp_traverse" como *arg*. El núcleo de Python utiliza varias
   funciones visitantes para implementar la detección de basura
   cíclica; No se espera que los usuarios necesiten escribir sus
   propias funciones visitante.

El manejador "tp_traverse" debe tener el siguiente tipo:

typedef int (*traverseproc)(PyObject *self, visitproc visit, void *arg)
    * Part of the Stable ABI.*

   Función transversal para un objeto contenedor. Las implementaciones
   deben llamar a la función *visit* para cada objeto directamente
   contenido por *self*, siendo los parámetros a *visit* el objeto
   contenido y el valor *arg* pasado al controlador. La función
   *visit* no debe llamarse con un argumento de objeto "NULL". Si
   *visit* retorna un valor distinto de cero, ese valor debe
   retornarse inmediatamente.

   The traversal function must not have any side effects.
   Implementations may not modify the reference counts of any Python
   objects nor create or destroy any Python objects.

Para simplificar la escritura de los manejadores "tp_traverse", se
proporciona un macro a "Py_VISIT()". Para usar este macro, la
implementación "tp_traverse" debe nombrar sus argumentos exactamente
*visit* y *arg*:

Py_VISIT(o)

   If the PyObject* *o* is not "NULL", call the *visit* callback, with
   arguments *o* and *arg*.  If *visit* returns a non-zero value, then
   return it. Using this macro, "tp_traverse" handlers look like:

      static int
      my_traverse(Noddy *self, visitproc visit, void *arg)
      {
          Py_VISIT(self->foo);
          Py_VISIT(self->bar);
          return 0;
      }

El manejador "tp_clear" debe ser del tipo "query", o "NULL" si el
objeto es inmutable.

typedef int (*inquiry)(PyObject *self)
    * Part of the Stable ABI.*

   Descarta referencias que pueden haber creado ciclos de referencia.
   Los objetos inmutables no tienen que definir este método ya que
   nunca pueden crear directamente ciclos de referencia. Tenga en
   cuenta que el objeto aún debe ser válido después de llamar a este
   método (no solo llame a "Py_DECREF()" en una referencia). El
   recolector de basura llamará a este método si detecta que este
   objeto está involucrado en un ciclo de referencia.

## Controlar el estado del recolector de basura

La C-API proporciona las siguientes funciones para controlar las
ejecuciones de recolección de basura.

Py_ssize_t PyGC_Collect(void)
    * Part of the Stable ABI.*

   Realiza una recolección de basura completa, si el recolector de
   basura está habilitado. (Tenga en cuenta que "gc.collect()" lo
   ejecuta incondicionalmente).

   Retorna el número de objetos recolectados e inalcanzables que no se
   pueden recolectar. Si el recolector de basura está deshabilitado o
   ya está recolectando, retorna "0" inmediatamente. Los errores
   durante la recolección de basura se pasan a "sys.unraisablehook".
   Esta función no genera excepciones.

int PyGC_Enable(void)
    * Part of the Stable ABI since version 3.10.*

   Habilita el recolector de basura: similar a "gc.enable()". Retorna
   el estado anterior, 0 para deshabilitado y 1 para habilitado.

   Added in version 3.10.

int PyGC_Disable(void)
    * Part of the Stable ABI since version 3.10.*

   Deshabilita el recolector de basura: similar a "gc.disable()".
   Retorna el estado anterior, 0 para deshabilitado y 1 para
   habilitado.

   Added in version 3.10.

int PyGC_IsEnabled(void)
    * Part of the Stable ABI since version 3.10.*

   Consulta el estado del recolector de basura: similar a
   "gc.isenabled()". Retorna el estado actual, 0 para deshabilitado y
   1 para habilitado.

   Added in version 3.10.

## Consultar el estado del recolector de basura

La C-API proporciona la siguiente interfaz para consultar información
sobre el recolector de basura.

void PyUnstable_GC_VisitObjects(gcvisitobjects_t callback, void *arg)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Ejecuta la *callback* suministrada en todos los objetos activos con
   capacidad para GC. *arg* se pasa a todas las invocaciones de
   *callback*.

   Advertencia:

     Si la devolución de llamada (des)asigna nuevos objetos, no está
     definido si serán visitados.La recolección de basura está
     deshabilitada durante la operación. Ejecutar una recolección
     explícitamente en la devolución de llamada puede provocar un
     comportamiento indefinido, por ejemplo, visitar los mismos
     objetos varias veces o no visitarlos en absoluto.

   Added in version 3.12.

typedef int (*gcvisitobjects_t)(PyObject *object, void *arg)

   Type of the visitor function to be passed to
   "PyUnstable_GC_VisitObjects()". *arg* is the same as the *arg*
   passed to "PyUnstable_GC_VisitObjects". Return "1" to continue
   iteration, return "0" to stop iteration. Other return values are
   reserved for now so behavior on returning anything else is
   undefined.

   Added in version 3.12.
