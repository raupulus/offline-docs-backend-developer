---
title: Protocolo de llamada
source_url: https://docs.python.org/es/3
source_path: c-api/call.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 110
---

# Protocolo de llamada

CPython admite dos protocolos de llamada diferentes: *tp_call* y
vectorcall.

## El protocolo *tp_call*

Las instancias de clases que establecen "tp_call" son invocables. La
firma del slot es:

   PyObject *tp_call(PyObject *callable, PyObject *args, PyObject *kwargs);

Se realiza una llamada usando una tupla para los argumentos
posicionales y un dict para los argumentos de palabras clave, de
manera similar a "callable(*args, **kwargs)" en el código Python.
*args* debe ser no NULL (use una tupla vacía si no hay argumentos)
pero *kwargs* puede ser *NULL* si no hay argumentos de palabra clave.

Esta convención no solo es utilizada por *tp_call*: "tp_new" y
"tp_init" también pasan argumentos de esta manera.

Para llamar a un objeto, use "PyObject_Call()" u otra llamada a la
API.

## El protocolo vectorcall

Added in version 3.9.

El protocolo vectorcall se introdujo en **PEP 590** como un protocolo
adicional para hacer que las llamadas sean más eficientes.

Como regla general, CPython preferirá el vectorcall para llamadas
internas si el invocable lo admite. Sin embargo, esta no es una regla
estricta. Además, algunas extensiones de terceros usan *tp_call*
directamente (en lugar de usar "PyObject_Call()"). Por lo tanto, una
clase que admita vectorcall también debe implementar "tp_call".
Además, el invocable debe comportarse de la misma manera
independientemente del protocolo que se utilice. La forma recomendada
de lograr esto es configurando "tp_call" en "PyVectorcall_Call()".
Vale la pena repetirlo:

Advertencia:

  Una clase que admita vectorcall **debe** también implementar
  "tp_call" con la misma semántica.

Distinto en la versión 3.12: Ahora el indicador
"Py_TPFLAGS_HAVE_VECTORCALL" se elimina de una clase cuando se
reasigna el método de la clase "__call__()". (Esto configura
internamente solo "tp_call" y, por lo tanto, puede hacer que se
comporte de forma diferente a la función vectorcall.) En versiones
anteriores de Python, vectorcall solo debería usarse con tipos
"immutables" o estáticos.

Una clase no debería implementar vectorcall si eso fuera más lento que
*tp_call*. Por ejemplo, si el destinatario de la llamada necesita
convertir los argumentos a una tupla args y un dict kwargs de todos
modos, entonces no tiene sentido implementar vectorcall.

Las clases pueden implementar el protocolo vectorcall habilitando el
indicador "Py_TPFLAGS_HAVE_VECTORCALL" y la configuración
"tp_vectorcall_offset" al desplazamiento dentro de la estructura del
objeto donde aparece un *vectorcallfunc*. Este es un puntero a una
función con la siguiente firma:

typedef PyObject *(*vectorcallfunc)(PyObject *callable, PyObject *const *args, size_t nargsf, PyObject *kwnames)
    * Part of the Stable ABI since version 3.12.*

* *callable* es el objeto siendo invocado.

* *args* es un arreglo en C que consta de los argumentos posicionales
  seguidos por el
     valores de los argumentos de la palabra clave. Puede ser *NULL*
     si no hay argumentos.

* *nargsf* es el número de argumentos posicionales más posiblemente el
     indicador "PY_VECTORCALL_ARGUMENTS_OFFSET". Para obtener el
     número real de argumentos posicionales de *nargsf*, use
     "PyVectorcall_NARGS()".

* *kwnames* es una tupla que contiene los nombres de los argumentos de
  la palabra clave;
     en otras palabras, las claves del diccionario kwargs. Estos
     nombres deben ser cadenas (instancias de "str" o una subclase) y
     deben ser únicos. Si no hay argumentos de palabras clave,
     entonces *kwnames* puede ser *NULL*.

PY_VECTORCALL_ARGUMENTS_OFFSET
    * Part of the Stable ABI since version 3.12.*

   Si este indicador se establece en un argumento vectorcall *nargsf*,
   el destinatario de la llamada puede cambiar temporalmente
   "args[-1]". En otras palabras, *args* apunta al argumento 1 (no 0)
   en el vector asignado. El destinatario de la llamada debe restaurar
   el valor de "args[-1]" antes de regresar.

   Para "PyObject_VectorcallMethod()", este indicador significa en
   cambio que "args[0]" puede cambiarse.

   Siempre que puedan hacerlo de forma económica (sin asignación
   adicional), se anima a las personas que llaman a utilizar
   "PY_VECTORCALL_ARGUMENTS_OFFSET". Si lo hace, permitirá que las
   personas que llaman, como los métodos enlazados, realicen sus
   llamadas posteriores (que incluyen un argumento *self* antepuesto)
   de manera muy eficiente.

   Added in version 3.8.

Para llamar a un objeto que implementa vectorcall, use una función
call API como con cualquier otro invocable. "PyObject_Vectorcall()"
normalmente será más eficiente.

### Control de recursión

Cuando se usa *tp_call*, los destinatarios no necesitan preocuparse
por recursividad: CPython usa "Py_EnterRecursiveCall()" y
"Py_LeaveRecursiveCall()" para llamadas realizadas usando *tp_call*.

Por eficiencia, este no es el caso de las llamadas realizadas mediante
vectorcall: el destinatario de la llamada debe utilizar
*Py_EnterRecursiveCall* y *Py_LeaveRecursiveCall* si es necesario.

### API de soporte para vectorcall

Py_ssize_t PyVectorcall_NARGS(size_t nargsf)
    * Part of the Stable ABI since version 3.12.*

   Dado un argumento vectorcall *nargsf*, retorna el número real de
   argumentos. Actualmente equivalente a:

      (Py_ssize_t)(nargsf & ~PY_VECTORCALL_ARGUMENTS_OFFSET)

   Sin embargo, la función "PyVectorcall_NARGS" debe usarse para
   permitir futuras extensiones.

   Added in version 3.8.

vectorcallfunc PyVectorcall_Function(PyObject *op)

   Si *op* no admite el protocolo vectorcall (ya sea porque el tipo no
   lo hace o porque la instancia específica no lo hace), retorna
   *NULL*. De lo contrario, retorna el puntero de la función
   vectorcall almacenado en *op*. Esta función nunca lanza una
   excepción.

   Esto es principalmente útil para verificar si *op* admite
   vectorcall, lo cual se puede hacer marcando
   "PyVectorcall_Function(op) != NULL".

   Added in version 3.9.

PyObject *PyVectorcall_Call(PyObject *callable, PyObject *tuple, PyObject *dict)
    * Part of the Stable ABI since version 3.12.*

   Llama a la "vectorcallfunc" de *callable* con argumentos
   posicionales y de palabras clave dados en una tupla y dict,
   respectivamente.

   Esta es una función especializada, destinada a colocarse en el slot
   "tp_call" o usarse en una implementación de "tp_call". No comprueba
   el indicador "Py_TPFLAGS_HAVE_VECTORCALL" y no vuelve a "tp_call".

   Added in version 3.8.

## API para invocar objetos

Hay varias funciones disponibles para llamar a un objeto Python. Cada
una convierte sus argumentos a una convención respaldada por el objeto
llamado, ya sea *tp_call* o vectorcall. Para realizar la menor
conversión posible, elija la que mejor se adapte al formato de datos
que tiene disponible.

La siguiente tabla resume las funciones disponibles; consulte la
documentación individual para obtener más detalles.

+--------------------------------------------+--------------------+----------------------+-----------------+
| Función                                    | invocable          | args                 | kwargs          |
|============================================|====================|======================|=================|
## | "PyObject_Call()"                          | "PyObject *"       | tupla                | dict/"NULL"     |

## | "PyObject_CallNoArgs()"                    | "PyObject *"       | ---                  | ---             |

## | "PyObject_CallOneArg()"                    | "PyObject *"       | 1 objeto             | ---             |

## | "PyObject_CallObject()"                    | "PyObject *"       | tuple/"NULL"         | ---             |

## | "PyObject_CallFunction()"                  | "PyObject *"       | formato              | ---             |

## | "PyObject_CallMethod()"                    | obj + "char*"      | formato              | ---             |

## | "PyObject_CallFunctionObjArgs()"           | "PyObject *"       | variadica            | ---             |

## | "PyObject_CallMethodObjArgs()"             | obj + nombre       | variadica            | ---             |

## | "PyObject_CallMethodNoArgs()"              | obj + nombre       | ---                  | ---             |

## | "PyObject_CallMethodOneArg()"              | obj + nombre       | 1 objeto             | ---             |

## | "PyObject_Vectorcall()"                    | "PyObject *"       | vectorcall           | vectorcall      |

## | "PyObject_VectorcallDict()"                | "PyObject *"       | vectorcall           | dict/"NULL"     |

## | "PyObject_VectorcallMethod()"              | arg + nombre       | vectorcall           | vectorcall      |

PyObject *PyObject_Call(PyObject *callable, PyObject *args, PyObject *kwargs)
    *Return value: New reference.** Part of the Stable ABI.*

   Llama a un objeto de Python invocable *callable*, con argumentos
   dados por la tupla *args*, y argumentos con nombre dados por el
   diccionario *kwargs*.

   *args* no debe ser *NULL*; use una tupla vacía si no se necesitan
   argumentos. Si no se necesitan argumentos con nombre, *kwargs*
   puede ser *NULL*.

   Retorna el resultado de la llamada en caso de éxito o lanza una
   excepción y retorna *NULL* en caso de error.

   Este es el equivalente de la expresión de Python: "callable(*args,
   **kwargs)".

PyObject *PyObject_CallNoArgs(PyObject *callable)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.10.*

   Llama a un objeto de Python invocable *callable* sin ningún
   argumento. Es la forma más eficiente de llamar a un objeto Python
   invocable sin ningún argumento.

   Retorna el resultado de la llamada en caso de éxito o lanza una
   excepción y retorna *NULL* en caso de error.

   Added in version 3.9.

PyObject *PyObject_CallOneArg(PyObject *callable, PyObject *arg)
    *Return value: New reference.*

   Llama a un objeto de Python invocable *callable* con exactamente 1
   argumento posicional *arg* y sin argumentos de palabra clave.

   Retorna el resultado de la llamada en caso de éxito o lanza una
   excepción y retorna *NULL* en caso de error.

   Added in version 3.9.

PyObject *PyObject_CallObject(PyObject *callable, PyObject *args)
    *Return value: New reference.** Part of the Stable ABI.*

   Llama a un objeto de Python invocable *callable*, con argumentos
   dados por la tupla *args*. Si no se necesitan argumentos, entonces
   *args* puede ser *NULL*.

   Retorna el resultado de la llamada en caso de éxito o lanza una
   excepción y retorna *NULL* en caso de error.

   Este es el equivalente de la expresión de Python:
   "callable(*args)".

PyObject *PyObject_CallFunction(PyObject *callable, const char *format, ...)
    *Return value: New reference.** Part of the Stable ABI.*

   Llama a un objeto de Python invocable *callable*, con un número
   variable de argumentos C. Los argumentos de C se describen usando
   una cadena de caracteres de formato de estilo "Py_BuildValue()". El
   formato puede ser *NULL*, lo que indica que no se proporcionan
   argumentos.

   Retorna el resultado de la llamada en caso de éxito o lanza una
   excepción y retorna *NULL* en caso de error.

   Este es el equivalente de la expresión de Python:
   "callable(*args)".

   Tenga en cuenta que si solo pasa PyObject* args,
   "PyObject_CallFunctionObjArgs()" es una alternativa más rápida.

   Distinto en la versión 3.4: El tipo de *format* se cambió desde
   "char *".

PyObject *PyObject_CallMethod(PyObject *obj, const char *name, const char *format, ...)
    *Return value: New reference.** Part of the Stable ABI.*

   Llama al método llamado *name* del objeto *obj* con un número
   variable de argumentos en C. Los argumentos de C se describen
   mediante una cadena de formato "Py_BuildValue()" que debería
   producir una tupla.

   El formato puede ser *NULL*, lo que indica que no se proporcionan
   argumentos.

   Retorna el resultado de la llamada en caso de éxito o lanza una
   excepción y retorna *NULL* en caso de error.

   Este es el equivalente de la expresión de Python: "obj.name(arg1,
   arg2, ...)".

   Tenga en cuenta que si solo pasa PyObject* args,
   "PyObject_CallMethodObjArgs()" es una alternativa más rápida.

   Distinto en la versión 3.4: Los tipos de *name* y *format* se
   cambiaron desde "char *".

PyObject *PyObject_CallFunctionObjArgs(PyObject *callable, ...)
    *Return value: New reference.** Part of the Stable ABI.*

   Llama a un objeto de Python invocable *callable*, con un número
   variable de argumentos PyObject*. Los argumentos se proporcionan
   como un número variable de parámetros seguidos de *NULL*.

   Retorna el resultado de la llamada en caso de éxito o lanza una
   excepción y retorna *NULL* en caso de error.

   Este es el equivalente de la expresión de Python: "callable(arg1,
   arg2, ...)".

PyObject *PyObject_CallMethodObjArgs(PyObject *obj, PyObject *name, ...)
    *Return value: New reference.** Part of the Stable ABI.*

   Llama a un método del objeto de Python *obj*, donde el nombre del
   método se proporciona como un objeto de cadena de caracteres de
   Python en *name*. Se llama con un número variable de argumentos
   PyObject*. Los argumentos se proporcionan como un número variable
   de parámetros seguidos de *NULL*.

   Retorna el resultado de la llamada en caso de éxito o lanza una
   excepción y retorna *NULL* en caso de error.

PyObject *PyObject_CallMethodNoArgs(PyObject *obj, PyObject *name)

   Llama a un método del objeto de Python *obj* sin argumentos, donde
   el nombre del método se da como un objeto de cadena de caracteres
   de Python en *name*.

   Retorna el resultado de la llamada en caso de éxito o lanza una
   excepción y retorna *NULL* en caso de error.

   Added in version 3.9.

PyObject *PyObject_CallMethodOneArg(PyObject *obj, PyObject *name, PyObject *arg)

   Llama a un método del objeto de Python *obj* con un único argumento
   posicional *arg*, donde el nombre del método se proporciona como un
   objeto de cadena de caracteres de Python en *name*.

   Retorna el resultado de la llamada en caso de éxito o lanza una
   excepción y retorna *NULL* en caso de error.

   Added in version 3.9.

PyObject *PyObject_Vectorcall(PyObject *callable, PyObject *const *args, size_t nargsf, PyObject *kwnames)
    * Part of the Stable ABI since version 3.12.*

   Llama a un objeto de Python invocable *callable*. Los argumentos
   son los mismos que para "vectorcallfunc". Si *callable* admite
   vectorcall, esto llama directamente a la función vectorcall
   almacenada en *callable*.

   Retorna el resultado de la llamada en caso de éxito o lanza una
   excepción y retorna *NULL* en caso de error.

   Added in version 3.8: as "_PyObject_Vectorcall"

   Distinto en la versión 3.9: Renamed to the current name, without
   the leading underscore. The old provisional name is *soft
   deprecated*.

PyObject *PyObject_VectorcallDict(PyObject *callable, PyObject *const *args, size_t nargsf, PyObject *kwdict)

   Llamada *invocable* con argumentos posicionales pasados exactamente
   como en el protocolo vectorcall, pero con argumentos de palabras
   clave pasados como un diccionario *kwdict*. El arreglo *args*
   contiene solo los argumentos posicionales.

   Independientemente del protocolo que se utilice internamente, es
   necesario realizar una conversión de argumentos. Por lo tanto, esta
   función solo debe usarse si la persona que llama ya tiene un
   diccionario listo para usar para los argumentos de palabras clave,
   pero no una tupla para los argumentos posicionales.

   Added in version 3.9.

PyObject *PyObject_VectorcallMethod(PyObject *name, PyObject *const *args, size_t nargsf, PyObject *kwnames)
    * Part of the Stable ABI since version 3.12.*

   Llama a un método usando la convención de llamada vectorcall. El
   nombre del método se proporciona como una cadena de caracteres de
   Python *name*. El objeto cuyo método se llama es *args[0]*, y el
   arreglo *args* que comienza en *args [1]* representa los argumentos
   de la llamada. Debe haber al menos un argumento posicional.
   *nargsf* es el número de argumentos posicionales que incluyen *args
   [0]*, más "PY_VECTORCALL_ARGUMENTS_OFFSET" si el valor de "args[0]"
   puede cambiarse temporalmente. Los argumentos de palabras clave se
   pueden pasar como en "PyObject_Vectorcall()".

   Si el objeto tiene la característica
   "Py_TPFLAGS_METHOD_DESCRIPTOR", esto llamará al objeto de método
   independiente con el vector *args* completo como argumentos.

   Retorna el resultado de la llamada en caso de éxito o lanza una
   excepción y retorna *NULL* en caso de error.

   Added in version 3.9.

## API de soporte de llamadas

int PyCallable_Check(PyObject *o)
    * Part of the Stable ABI.*

   Determina si el objeto *o* es invocable. Retorna "1" si el objeto
   es invocable y "0" en caso contrario. Esta función siempre finaliza
   con éxito.
