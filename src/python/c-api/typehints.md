---
title: Objetos para indicaciones de tipado
source_url: https://docs.python.org/es/3
source_path: c-api/typehints.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 740
---

# Objetos para indicaciones de tipado

Se proporcionan varios tipos incorporados para indicaciones de tipado.
Actualmente existen dos tipos -- GenericAlias y Union. Solo
"GenericAlias" es expuesto a C.

PyObject *Py_GenericAlias(PyObject *origin, PyObject *args)
    * Part of the Stable ABI since version 3.9.*

   Crea un objeto GenericAlias. Equivalente a llamar la clase de
   Python "types.GenericAlias". Los argumentos *origin* y *args*
   establecen los atributos "__origin__" y "__args__" de
   "GenericAlias" respectivamente. *origin* debe ser un PyTypeObject*,
   y *args* puede ser un PyTupleObject* o cualquier "PyObject*". Si
   *args* no es una tupla, se construye automáticamente una tupla de
   un elemento y "__args__" se establece como "(args,)". Se realiza
   una verificación mínima para los argumentos, por lo que la función
   tendrá éxito incluso si *origin* no es un tipo. El atributo
   "__parameters__" de "GenericAlias" se construye de manera perezosa
   a partir de "__args__". En caso de falla, se levantará una
   excepción y retorna "NULL".

   Aquí hay un ejemplo sobre cómo hacer un tipo de extensión genérica:

      ...
      static PyMethodDef my_obj_methods[] = {
          // Other methods.
          ...
          {"__class_getitem__", Py_GenericAlias, METH_O|METH_CLASS, "my_obj is generic over its contained type"}
          ...
      }

   Ver también: El método del modelo de datos "__class_getitem__()".

   Added in version 3.9.

PyTypeObject Py_GenericAliasType
    * Part of the Stable ABI since version 3.9.*

   El tipo en C del objeto retornado por "Py_GenericAlias()".
   Equivalente a "types.GenericAlias" en Python.

   Added in version 3.9.
