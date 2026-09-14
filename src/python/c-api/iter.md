---
title: Protocolo iterador
source_url: https://docs.python.org/es/3
source_path: c-api/iter.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 400
---

# Protocolo iterador

Hay dos funciones específicas para trabajar con iteradores.

int PyIter_Check(PyObject *o)
    * Part of the Stable ABI since version 3.8.*

   Return non-zero if the object *o* can be safely passed to
   "PyIter_NextItem()" and "0" otherwise. This function always
   succeeds.

int PyAIter_Check(PyObject *o)
    * Part of the Stable ABI since version 3.10.*

   Retorna un valor distinto de cero si el objeto *o* proporciona el
   protocolo "AsyncIterator", y "0" en caso contrario. Esta función
   siempre tiene éxito.

   Added in version 3.10.

int PyIter_NextItem(PyObject *iter, PyObject **item)
    * Part of the Stable ABI since version 3.14.*

   Return "1" and set *item* to a *strong reference* of the next value
   of the iterator *iter* on success. Return "0" and set *item* to
   "NULL" if there are no remaining values. Return "-1", set *item* to
   "NULL" and set an exception on error.

   Added in version 3.14.

PyObject *PyIter_Next(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   This is an older version of "PyIter_NextItem()", which is retained
   for backwards compatibility. Prefer "PyIter_NextItem()".

   Retorna el siguiente valor del iterador *o*. El objeto debe ser un
   iterador según "PyIter_Check()" (depende del llamador verificar
   esto). Si no hay valores restantes, retorna "NULL" sin establecer
   una excepción. Si ocurre un error al recuperar el elemento,
   devuelve "NULL" y envía la excepción.

type PySendResult

   El valor de enumeración utilizado para representar diferentes
   resultados de "PyIter_Send()".

   Added in version 3.10.

PySendResult PyIter_Send(PyObject *iter, PyObject *arg, PyObject **presult)
    * Part of the Stable ABI since version 3.10.*

   Envía el valor *arg* al iterador *iter*. Retorna:

   * "PYGEN_RETURN" si el iterador regresa. El valor de retorno se
     retorna a través de *presult*.

   * "PYGEN_NEXT" si el iterador cede. El valor cedido se retorna a
     través de *presult*.

   * "PYGEN_ERROR" si el iterador ha lanzado una excepción. *presult*
     se establece en "NULL".

   Added in version 3.10.
