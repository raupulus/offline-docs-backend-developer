---
title: Cápsulas
source_url: https://docs.python.org/es/3
source_path: c-api/capsule.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 120
---

# Cápsulas

Consulta Proporcionar una API C para un módulo de extensión para
obtener más información sobre el uso de estos objetos.

Added in version 3.1.

type PyCapsule

   This subtype of "PyObject" represents an opaque value, useful for C
   extension modules which need to pass an opaque value (as a void*
   pointer) through Python code to other C code.  It is often used to
   make a C function pointer defined in one module available to other
   modules, so the regular import mechanism can be used to access C
   APIs defined in dynamically loaded modules.

PyTypeObject PyCapsule_Type
    * Part of the Stable ABI.*

   The type object corresponding to capsule objects. This is the same
   object as "types.CapsuleType" in the Python layer.

type PyCapsule_Destructor
    * Part of the Stable ABI.*

   El tipo de devolución de llamada de un destructor para una cápsula.
   Definido como:

      typedef void (*PyCapsule_Destructor)(PyObject *);

   Consulte "PyCapsule_New()" para conocer la semántica de las
   devoluciones de llamada de *PyCapsule_Destructor*.

int PyCapsule_CheckExact(PyObject *p)
    * Thread safety: Atomic.*

   Retorna verdadero si su argumento es a "PyCapsule". Esta función
   siempre finaliza con éxito.

PyObject *PyCapsule_New(void *pointer, const char *name, PyCapsule_Destructor destructor)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Crea un "PyCapsule" encapsulando el *pointer*. El argumento
   *pointer* puede no ser "NULL".

   En caso de falla, establece una excepción y retorna "NULL".

   La cadena de caracteres *name* puede ser "NULL" o un puntero a una
   cadena C válida. Si no es "NULL", esta cadena de caracteres debe
   sobrevivir a la cápsula. (Aunque está permitido liberarlo dentro
   del *destructor*).

   Si el argumento *destructor* no es "NULL", se llamará con la
   cápsula como argumento cuando se destruya.

   Si esta cápsula se almacenará como un atributo de un módulo, el
   nombre *name* debe especificarse como "modulename.attributename".
   Esto permitirá que otros módulos importen la cápsula usando
   "PyCapsule_Import()".

void *PyCapsule_GetPointer(PyObject *capsule, const char *name)
    * Part of the Stable ABI.** Thread safety: Safe to call without
   external synchronization on distinct objects.*

   Recupera el *pointer* almacenado en la cápsula. En caso de falla,
   establece una excepción y retorna  "NULL".

   El parámetro *name* debe coincidir exactamente con el nombre
   almacenado en la cápsula. Si el nombre almacenado en la cápsula es
   "NULL", el *name* también debe ser "NULL". Python utiliza la
   función C "strcmp()" para comparar los nombres de las cápsulas.

PyCapsule_Destructor PyCapsule_GetDestructor(PyObject *capsule)
    * Part of the Stable ABI.** Thread safety: Safe to call without
   external synchronization on distinct objects.*

   Retorna el destructor actual almacenado en la cápsula. En caso de
   falla, establece una excepción y retorna "NULL".

   Es legal que una cápsula tenga un destructor "NULL". Esto hace que
   un código de retorno "NULL" sea algo ambiguo; use
   "PyCapsule_IsValid()" o "PyErr_Occurred()" para desambiguar.

void *PyCapsule_GetContext(PyObject *capsule)
    * Part of the Stable ABI.** Thread safety: Safe to call without
   external synchronization on distinct objects.*

   Retorna el contexto actual almacenado en la cápsula. En caso de
   falla, establece una excepción y retorna "NULL".

   Es legal que una cápsula tenga un contexto "NULL". Esto hace que un
   código de retorno "NULL" sea algo ambiguo; use
   "PyCapsule_IsValid()" o "PyErr_Occurred()" para desambiguar.

const char *PyCapsule_GetName(PyObject *capsule)
    * Part of the Stable ABI.** Thread safety: Safe to call without
   external synchronization on distinct objects.*

   Retorna el nombre actual almacenado en la cápsula. En caso de
   falla, establece una excepción y retorna "NULL".

   Es legal que una cápsula tenga un nombre "NULL". Esto hace que un
   código de retorno "NULL" sea algo ambiguo; use
   "PyCapsule_IsValid()" o "PyErr_Occurred()" para desambiguar.

void *PyCapsule_Import(const char *name, int no_block)
    * Part of the Stable ABI.** Thread safety: Safe to call from
   multiple threads with external synchronization only.*

   Importa un puntero a un objeto C desde un atributo cápsula en un
   módulo. El parámetro *name* debe especificar el nombre completo del
   atributo, como en "module.attribute". El nombre *name* almacenado
   en la cápsula debe coincidir exactamente con esta cadena de
   caracteres.

   This function splits *name* on the "." character, and imports the
   first element. It then processes further elements using attribute
   lookups.

   Retorna el puntero *pointer* interno de la cápsula en caso de
   éxito. En caso de falla, establece una excepción y retorna "NULL".

   Nota:

     If *name* points to an attribute of some submodule or subpackage,
     this submodule or subpackage must be previously imported using
     other means (for example, by using "PyImport_ImportModule()") for
     the attribute lookups to succeed.

   Distinto en la versión 3.3: *no_block* ya no tiene efecto.

int PyCapsule_IsValid(PyObject *capsule, const char *name)
    * Part of the Stable ABI.** Thread safety: Safe to call without
   external synchronization on distinct objects.*

   Determina si *capsule* es o no una cápsula válida. Una cápsula
   válida no es "NULL", pasa "PyCapsule_CheckExact()", tiene un
   puntero no "NULL" almacenado y su nombre interno coincide con el
   parámetro *name*. (Consulte "PyCapsule_GetPointer()" para obtener
   información sobre cómo se comparan los nombres de las cápsulas).

   En otras palabras, si "PyCapsule_IsValid()" retorna un valor
   verdadero, se garantiza que las llamadas a cualquiera de las
   funciones de acceso (cualquier función que comience con
   "PyCapsule_Get") tendrán éxito.

   Retorna un valor distinto de cero si el objeto es válido y coincide
   con el nombre pasado. Retorna "0" de lo contrario. Esta función no
   fallará.

int PyCapsule_SetContext(PyObject *capsule, void *context)
    * Part of the Stable ABI.** Thread safety: Safe to call without
   external synchronization on distinct objects.*

   Establece el puntero de contexto dentro de *capsule* a *context*.

   Retorna "0" en caso de éxito. Retorna distinto de cero y establece
   una excepción en caso de error.

int PyCapsule_SetDestructor(PyObject *capsule, PyCapsule_Destructor destructor)
    * Part of the Stable ABI.** Thread safety: Safe to call without
   external synchronization on distinct objects.*

   Establece el destructor dentro de *capsule* en *destructor*.

   Retorna "0" en caso de éxito. Retorna distinto de cero y establece
   una excepción en caso de error.

int PyCapsule_SetName(PyObject *capsule, const char *name)
    * Part of the Stable ABI.** Thread safety: Safe to call without
   external synchronization on distinct objects.*

   Establece el nombre dentro de *capsule* a *name*. Si no es "NULL",
   el nombre debe sobrevivir a la cápsula. Si el *name* anterior
   almacenado en la cápsula no era "NULL", no se intenta liberarlo.

   Retorna "0" en caso de éxito. Retorna distinto de cero y establece
   una excepción en caso de error.

int PyCapsule_SetPointer(PyObject *capsule, void *pointer)
    * Part of the Stable ABI.** Thread safety: Safe to call without
   external synchronization on distinct objects.*

   Establece el puntero vacío dentro de *capsule* a *pointer*. El
   puntero puede no ser "NULL".

   Retorna "0" en caso de éxito. Retorna distinto de cero y establece
   una excepción en caso de error.
