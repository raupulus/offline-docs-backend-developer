---
title: Conteo de referencias
source_url: https://docs.python.org/es/3
source_path: c-api/refcounting.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 590
---

# Conteo de referencias

Las funciones y macros de esta sección se utilizan para administrar
conteos de referencia de objetos en Python.

Py_ssize_t Py_REFCNT(PyObject *o)
    * Part of the Stable ABI since version 3.14.*

   Obtiene el recuento de referencias para el objeto de Python *o*.

   Ten cuenta que el valor devuelto puede que no reflejar cuantas
   referencias al objecto existen realmente. Por ejemplo, algunos
   objetos son *immortal* y tienen un refcount muy alto que no refleja
   el número real de referencias. Por lo tanto, no confíes en que el
   valor devuelto sea preciso, salvo cuando sea 0 o 1.

   Usa la función "Py_SET_REFCNT()" para establecer la cuenta de
   referencias de un objeto.

   Nota:

     On *free-threaded builds* of Python, returning 1 isn't sufficient
     to determine if it's safe to treat *o* as having no access by
     other threads. Use "PyUnstable_Object_IsUniquelyReferenced()" for
     that instead.See also the function
     "PyUnstable_Object_IsUniqueReferencedTemporary()".

   Distinto en la versión 3.10: "Py_REFCNT()" se convierte en una
   función estática en línea.

   Distinto en la versión 3.11: El tipo de parámetro ya no es const
   PyObject*.

void Py_SET_REFCNT(PyObject *o, Py_ssize_t refcnt)

   Establece la cuenta de referencias del objeto *o* al valor
   *refcnt*.

   En compilación de Python con Free Threading, si *refcnt* es mas
   mayor que "UINT32_MAX", el objeto se convierte en *immortal*.

   Esta función no afecta a los objetos *immortal*.

   Added in version 3.9.

   Distinto en la versión 3.12: Los objetos inmortales no se
   modifican.

void Py_INCREF(PyObject *o)

   Indica tomar una nueva *strong reference* al objeto *o*, lo que
   indica que está en uso y no debe ser destruido.

   Esta función no afecta a los objetos *immortal*.

   Esta función se usa generalmente para convertir un *borrowed
   reference* en un *strong reference* en su lugar. La función
   "Py_NewRef()" se puede utilizar para crear un nuevo *strong
   reference*.

   Cuando se termine de usar el objeto, se libera llamando a
   "Py_DECREF()".

   El objeto no debe ser "NULL"; si no está seguro de que no sea
   "NULL", use "Py_XINCREF()".

   No esperes que esta función modifique realmente *o* de ninguna
   manera. Al menos para **algunos objetos**, esta función no tiene
   ningún efecto.

   Distinto en la versión 3.12: Los objetos inmortales no se
   modifican.

void Py_XINCREF(PyObject *o)

   Similar a "Py_INCREF()", pero el objeto *o* puede ser "NULL", en
   cuyo caso esto no tiene efecto.

   Ver también "Py_XNewRef()".

PyObject *Py_NewRef(PyObject *o)
    * Part of the Stable ABI since version 3.10.*

   Crea una nueva *strong reference* a un objeto: llama a
   "Py_INCREF()" sobre *o* y devuelve el objeto *o*.

   Cuando la *strong reference* ya no sea necesaria, se debe llamar a
   "Py_DECREF()" para disminuir el recuento de referencias del objeto.

   El objeto *o* no debe ser "NULL"; use "Py_XNewRef()" si *o* puede
   ser "NULL".

   Por ejemplo:

      Py_INCREF(obj);
      self->attr = obj;

   puede ser escrito como:

      self->attr = Py_NewRef(obj);

   Ver también "Py_INCREF()".

   Added in version 3.10.

PyObject *Py_XNewRef(PyObject *o)
    * Part of the Stable ABI since version 3.10.*

   Similar a "Py_NewRef()", pero el objeto *o* puede ser NULL.

   Si el objeto *o* es "NULL", la función solo retorna "NULL".

   Added in version 3.10.

void Py_DECREF(PyObject *o)

   Libera una *strong reference* al objeto *o*, indicando que la
   referencia ya no se usa.

   Esta función no afecta a los objetos *immortal*.

   Una vez que la última *strong reference* sea liberada (por ejemplo,
   cuando la cuenta de referencias del objeto llegue a 0), se invoca
   la función de desasignación del tipo de objeto (la cual no debe ser
   "NULL").

   Esta función se usa generalmente para eliminar un *strong
   reference* antes de salir de su alcance.

   El objeto no debe ser "NULL"; si no está seguro de que no sea
   "NULL", use "Py_XINCREF()".

   No esperes que esta función modifique realmente *o* de ninguna
   manera. Al menos para **algunos objetos**, esta función no tiene
   ningún efecto.

   Advertencia:

     La función de desasignación puede hacer que se invoque un código
     arbitrario de Python (por ejemplo, cuando se desasigna una
     instancia de clase con el método "__del__()"). Mientras las
     excepciones en dicho código no sean propagadas, el código
     ejecutado tendrá acceso libre a todas las variables globales de
     Python. Esto significa que cualquier objeto al que se pueda
     acceder desde una variable global debería estar en un estado
     coherente antes de invocar a "Py_DECREF()". Por ejemplo, el
     código para eliminar un objeto de una lista debe copiar una
     referencia al objeto eliminado en una variable temporal,
     actualizar la estructura de datos de la lista y luego llamar a
     "Py_DECREF()" para la variable temporal.

   Distinto en la versión 3.12: Los objetos inmortales no se
   modifican.

void Py_XDECREF(PyObject *o)

   Similar a "Py_DECREF()", pero el objeto *o* puede ser "NULL", en
   cuyo caso esto no tendría efecto alguno. El mismo aviso de
   "Py_DECREF()" aplica aquí también.

void Py_CLEAR(PyObject *o)

   Libera una *strong reference* del objeto *o*. El objeto puede ser
   "NULL", en cuyo caso el macro no tiene efecto; de lo contrario, el
   efecto es el mismo que el de "Py_DECREF()", excepto que el
   argumento también se establece en "NULL". La advertencia de
   "Py_DECREF()" no se aplica en este caso, ya que el macro usa
   cuidadosamente una variable temporal y asigna "NULL" al argumento
   antes de liberar la referencia.

   Es buena idea usar este macro al liberar una referencia de un
   objeto que podría ser recorrido durante la recolección de basura.

   Distinto en la versión 3.12: Ahora, el macro argumento solo se
   evalúa una vez. Si el argumento tiene efectos secundarios, estos ya
   no se duplican.

void Py_IncRef(PyObject *o)
    * Part of the Stable ABI.*

   Indica la toma de una nueva *strong reference* al objeto *o*. Es
   una versión en forma de función de "Py_XINCREF()". Puede utilizarse
   para la integración dinámica de Python en tiempo de ejecución.

void Py_DecRef(PyObject *o)
    * Part of the Stable ABI.*

   Libera una *strong reference* al objeto *o*. Una versión en forma
   de función de "Py_XDECREF()". Puede utilizarse para la integración
   dinámica de Python en tiempo de ejecución.

Py_SETREF(dst, src)

   Un macro que libera de forma segura un *strong reference* al objeto
   *dst* y establece *dst* al valor *src*.

   Como en el caso de "Py_CLEAR()", el código "obvio" puede ser
   mortal:

      Py_DECREF(dst);
      dst = src;

   La forma segura es:

      Py_SETREF(dst, src);

   That arranges to set *dst* to *src* *before* releasing the
   reference to the old value of *dst*, so that any code triggered as
   a side-effect of *dst* getting torn down no longer believes *dst*
   points to a valid object.

   Added in version 3.6.

   Distinto en la versión 3.12: Los macro argumentos ahora solo se
   evalúan una vez. Si algún argumento tiene efectos secundarios,
   estos ya no se duplican.

Py_XSETREF(dst, src)

   Un variante del macro "Py_SETREF" que usa "Py_XDECREF()" en lugar
   de "Py_DECREF()".

   Added in version 3.6.

   Distinto en la versión 3.12: Los macro argumentos ahora solo se
   evalúan una vez. Si algún argumento tiene efectos secundarios,
   estos ya no se duplican.
