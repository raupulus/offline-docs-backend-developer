---
title: Protocolo búfer
source_url: https://docs.python.org/es/3
source_path: c-api/buffer.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 80
---

# Protocolo búfer

Ciertos objetos disponibles en Python ajustan el acceso a un arreglo
de memoria subyacente o *buffer*. Dichos objetos incluyen el
incorporado "bytes" y "bytearray", y algunos tipos de extensión como
"array.array". Las bibliotecas de terceros pueden definir sus propios
tipos para fines especiales, como el procesamiento de imágenes o el
análisis numérico.

Si bien cada uno de estos tipos tiene su propia semántica, comparten
la característica común de estar respaldados por un búfer de memoria
posiblemente grande. Es deseable, en algunas situaciones, acceder a
ese búfer directamente y sin copia intermedia.

Python provides such a facility at the C and Python level in the form
of the buffer protocol.  This protocol has two sides:

* on the producer side, a type can export a "buffer interface" which
  allows objects of that type to expose information about their
  underlying buffer. This interface is described in the section
  Estructuras de objetos búfer; for Python see Emulando tipos de
  búfer.

* on the consumer side, several means are available to obtain a
  pointer to the raw underlying data of an object (for example a
  method parameter). For Python see "memoryview".

Los objetos simples como "bytes" y "bytearray" exponen su búfer
subyacente en forma orientada a bytes. Otras formas son posibles; por
ejemplo, los elementos expuestos por un "array.array" pueden ser
valores de varios bytes.

An example consumer of the buffer interface is the "write()" method of
file objects: any object that can export a series of bytes through the
buffer interface can be written to a file.  While "write()" only needs
read-only access to the internal contents of the object passed to it,
other methods such as "readinto()" need write access to the contents
of their argument.  The buffer interface allows objects to selectively
allow or reject exporting of read-write and read-only buffers.

Hay dos formas para que un consumidor de la interfaz del búfer
adquiera un búfer sobre un objeto de destino:

* llamar "PyObject_GetBuffer()" con los parámetros correctos;

* llamar "PyArg_ParseTuple()" (o uno de sus hermanos) con uno de los
  "y*", "w*" o "s*" códigos de formato.

En ambos casos, se debe llamar a "PyBuffer_Release()" cuando ya no se
necesita el búfer. De lo contrario, podrían surgir varios problemas,
como pérdidas de recursos.

Added in version 3.12: The buffer protocol is now accessible in
Python, see Emulando tipos de búfer and "memoryview".

## Estructura de búfer

Las estructuras de búfer (o simplemente "búferes") son útiles como una
forma de exponer los datos binarios de otro objeto al programador de
Python. También se pueden usar como un mecanismo de corte de copia
cero. Usando su capacidad para hacer referencia a un bloque de
memoria, es posible exponer cualquier información al programador
Python con bastante facilidad. La memoria podría ser una matriz grande
y constante en una extensión C, podría ser un bloque de memoria sin
procesar para su manipulación antes de pasar a una biblioteca del
sistema operativo, o podría usarse para pasar datos estructurados en
su formato nativo en memoria .

Contrariamente a la mayoría de los tipos de datos expuestos por el
intérprete de Python, los búferes no son punteros "PyObject" sino
estructuras C simples. Esto les permite ser creados y copiados de
manera muy simple. Cuando se necesita un contenedor genérico alrededor
de un búfer, un objeto memoryview puede ser creado.

Para obtener instrucciones breves sobre cómo escribir un objeto de
exportación, consulte Estructuras de objetos búfer. Para obtener un
búfer, consulte "PyObject_GetBuffer()".

type Py_buffer
    * Part of the Stable ABI (including all members) since version
   3.11.*

   void *buf

      Un puntero al inicio de la estructura lógica descrita por los
      campos del búfer. Puede ser cualquier ubicación dentro del
      bloque de memoria física subyacente del exportador. Por ejemplo,
      con negativo "strides" el valor puede apuntar al final del
      bloque de memoria.

      Para arreglos *contiguous*, el valor apunta al comienzo del
      bloque de memoria.

   PyObject *obj

      A new reference to the exporting object. The reference is owned
      by the consumer and automatically released (i.e. reference count
      decremented) and set to "NULL" by "PyBuffer_Release()". The
      field is the equivalent of the return value of any standard
      C-API function.

      Como un caso especial, para los búferes *temporary* que están
      envueltos por "PyMemoryView_FromBuffer()" o
      "PyBuffer_FillInfo()" este campo es "NULL". En general, los
      objetos de exportación NO DEBEN usar este esquema.

   Py_ssize_t len

      "product(shape) * itemize". Para arreglos contiguos, esta es la
      longitud del bloque de memoria subyacente. Para arreglos no
      contiguos, es la longitud que tendría la estructura lógica si se
      copiara en una representación contigua.

      Accede a "((char *)buf)[0] hasta ((char *)buf)[len-1]" solo es
      válido si el búfer se ha obtenido mediante una solicitud que
      garantiza la contigüidad. En la mayoría de los casos, dicha
      solicitud será "PyBUF_SIMPLE" o "PyBUF_WRITABLE".

   int readonly

      Un indicador de si el búfer es de solo lectura. Este campo está
      controlado por el indicador "PyBUF_WRITABLE".

   Py_ssize_t itemsize

      Tamaño del elemento en bytes de un solo elemento. Igual que el
      valor de "struct.calcsize()" invocado en valores no "NULL"
      "format".

      Excepción importante: si un consumidor solicita un búfer sin el
      indicador "PyBUF_FORMAT", "format" se establecerá en "NULL",
      pero "itemsize" todavía tiene el valor para el formato original.

      Si "shape" está presente, la igualdad "product(shape) * itemsize
      == len" aún se mantiene y el consumidor puede usar "itemsize"
      para navegar el búfer.

      Si "shape" es "NULL" como resultado de un "PyBUF_SIMPLE" o un
      "PyBUF_WRITABLE", el consumidor debe ignorar "itemsize" y asume
      "itemsize == 1".

   char *format

      A *NULL* terminated string in "struct" module style syntax
      describing the contents of a single item. If this is "NULL",
      ""B"" (unsigned bytes) is assumed.

      Este campo está controlado por el indicador "PyBUF_FORMAT".

   int ndim

      The number of dimensions the memory represents as an
      n-dimensional array. If it is "0", "buf" points to a single item
      representing a scalar. In this case, "shape", "strides" and
      "suboffsets" MUST be "NULL". The maximum number of dimensions is
      given by "PyBUF_MAX_NDIM".

   Py_ssize_t *shape

      Un arreglo de "Py_ssize_t" de longitud "ndim" que indica la
      forma de la memoria como un arreglo n-dimensional. Tenga en
      cuenta que "shape[0] * ... * shape[ndim-1] * itemsize" DEBE ser
      igual a "len".

      Los valores de forma están restringidos a "shape[n] >= 0". El
      caso "shape[n] == 0" requiere atención especial. Vea arreglos
      complejos (complex arrays) para más información.

      El arreglo de formas es de sólo lectura para el consumidor.

   Py_ssize_t *strides

      Un arreglo de "Py_ssize_t" de longitud "ndim" que proporciona el
      número de bytes que se omiten para llegar a un nuevo elemento en
      cada dimensión.

      Los valores de *stride* pueden ser cualquier número entero. Para
      los arreglos regulares, los pasos son generalmente positivos,
      pero un consumidor DEBE ser capaz de manejar el caso "strides[n]
      <= 0". Ver complex arrays para más información.

      El arreglo *strides* es de sólo lectura para el consumidor.

   Py_ssize_t *suboffsets

      Un arreglo de "Py_ssize_t" de longitud "ndim". Si "suboffsets[n]
      >= 0", los valores almacenados a lo largo de la enésima
      dimensión son punteros y el valor del *suboffsets* dicta cuántos
      bytes agregar a cada puntero después de desreferenciarlos. Un
      valor de *suboffsets* negativo indica que no debe producirse una
      desreferenciación (*striding* en un bloque de memoria contiguo).

      Si todos los *suboffsets* son negativos (es decir, no se
      necesita desreferenciar), entonces este campo debe ser "NULL"
      (el valor predeterminado).

      *Python Imaging Library (PIL)* utiliza este tipo de
      representación de arreglos. Consulte complex arrays para obtener
      más información sobre cómo acceder a los elementos de dicho
      arreglo.

      El arreglo de *suboffsets* es de sólo lectura para el
      consumidor.

   void *internal

      Esto es para uso interno del objeto exportador. Por ejemplo, el
      exportador podría volver a emitirlo como un número entero y
      utilizarlo para almacenar indicadores sobre si las matrices de
      forma, *strides* y *suboffsets* deben liberarse cuando se libera
      el búfer. El consumidor NO DEBE alterar este valor.

Constants:

PyBUF_MAX_NDIM
    * Part of the Stable ABI since version 3.11.*

   The maximum number of dimensions the memory represents. Exporters
   MUST respect this limit, consumers of multi-dimensional buffers
   SHOULD be able to handle up to "PyBUF_MAX_NDIM" dimensions.
   Currently set to 64.

## Tipos de solicitud búfer

Los búferes obtienen generalmente enviando una solicitud de búfer a un
objeto de exportación a través de "PyObject_GetBuffer()". Dado que la
complejidad de la estructura lógica de la memoria puede variar
drásticamente, el consumidor usa el argumento *flags* para especificar
el tipo de búfer exacto que puede manejar.

All "Py_buffer" fields are unambiguously defined by the request type.

### campos independientes de solicitud

Los siguientes campos no están influenciados por *flags* y siempre
deben completarse con los valores correctos: "obj", "buf", "len",
"itemsize", "ndim".

### formato de sólo lectura

   PyBUF_WRITABLE
       * Part of the Stable ABI since version 3.11.*

      Controls the "readonly" field. If set, the exporter MUST provide
      a writable buffer or else report failure. Otherwise, the
      exporter MAY provide either a read-only or writable buffer, but
      the choice MUST be consistent for all consumers. For example,
      PyBUF_SIMPLE | PyBUF_WRITABLE can be used to request a simple
      writable buffer.

   PyBUF_WRITEABLE

      This is an alias to "PyBUF_WRITABLE".

      Soft deprecated since version 3.13.

   PyBUF_FORMAT
       * Part of the Stable ABI since version 3.11.*

      Controla el campo "format". Si se establece, este campo DEBE
      completarse correctamente. De lo contrario, este campo DEBE ser
      "NULL".

"PyBUF_WRITABLE" puede ser |'d a cualquiera de las banderas en la
siguiente sección. Dado que "PyBUF_SIMPLE" se define como 0,
"PyBUF_WRITABLE" puede usarse como un indicador independiente para
solicitar un búfer de escritura simple.

"PyBUF_FORMAT" must be |'d to any of the flags except "PyBUF_SIMPLE",
because the latter already implies format "B" (unsigned bytes).
"PyBUF_FORMAT" cannot be used on its own.

### formas, *strides*, *suboffsets*

Las banderas que controlan la estructura lógica de la memoria se
enumeran en orden decreciente de complejidad. Tenga en cuenta que cada
bandera contiene todos los bits de las banderas debajo de ella.

+-------------------------------+---------+-----------+--------------+
| Solicitud                     | forma   | *strides* | *suboffsets* |
|===============================|=========|===========|==============|
| PyBUF_INDIRECT  * Part of the | sí      | sí        | si es        |
| Stable ABI since version      |         |           | necesario    |
## | 3.11.*                        |         |           |              |

| PyBUF_STRIDES  * Part of the  | sí      | sí        | NULL         |
| Stable ABI since version      |         |           |              |
## | 3.11.*                        |         |           |              |

| PyBUF_ND  * Part of the       | sí      | NULL      | NULL         |
| Stable ABI since version      |         |           |              |
## | 3.11.*                        |         |           |              |

| PyBUF_SIMPLE  * Part of the   | NULL    | NULL      | NULL         |
| Stable ABI since version      |         |           |              |
## | 3.11.*                        |         |           |              |

### solicitudes de contigüidad

La *contigüidad* C o Fortran se puede solicitar explícitamente, con y
sin información de paso. Sin información de paso, el búfer debe ser
C-contiguo.

+-------------------------------------+---------+-----------+--------------+----------+
| Solicitud                           | forma   | *strides* | *suboffsets* | contig   |
|=====================================|=========|===========|==============|==========|
| PyBUF_C_CONTIGUOUS  * Part of the   | sí      | sí        | NULL         | C        |
## | Stable ABI since version 3.11.*     |         |           |              |          |

| PyBUF_F_CONTIGUOUS  * Part of the   | sí      | sí        | NULL         | F        |
## | Stable ABI since version 3.11.*     |         |           |              |          |

| PyBUF_ANY_CONTIGUOUS  * Part of the | sí      | sí        | NULL         | C o F    |
## | Stable ABI since version 3.11.*     |         |           |              |          |

## | "PyBUF_ND"                          | sí      | NULL      | NULL         | C        |

### solicitudes compuestas

Todas las solicitudes posibles están completamente definidas por
alguna combinación de las banderas en la sección anterior. Por
conveniencia, el protocolo de memoria intermedia proporciona
combinaciones de uso frecuente como indicadores únicos.

En la siguiente tabla *U* significa contigüidad indefinida. El
consumidor tendría que llamar a "PyBuffer_IsContiguous()" para
determinar la contigüidad.

+---------------------------------+---------+-----------+--------------+----------+------------+----------+
| Solicitud                       | forma   | *strides* | *suboffsets* | contig   | sólo       | formato  |
|                                 |         |           |              |          | lectura    |          |
|=================================|=========|===========|==============|==========|============|==========|
| PyBUF_FULL  * Part of the       | sí      | sí        | si es        | U        | 0          | sí       |
## | Stable ABI since version 3.11.* |         |           | necesario    |          |            |          |

| PyBUF_FULL_RO  * Part of the    | sí      | sí        | si es        | U        | 1 o 0      | sí       |
## | Stable ABI since version 3.11.* |         |           | necesario    |          |            |          |

| PyBUF_RECORDS  * Part of the    | sí      | sí        | NULL         | U        | 0          | sí       |
## | Stable ABI since version 3.11.* |         |           |              |          |            |          |

| PyBUF_RECORDS_RO  * Part of the | sí      | sí        | NULL         | U        | 1 o 0      | sí       |
## | Stable ABI since version 3.11.* |         |           |              |          |            |          |

| PyBUF_STRIDED  * Part of the    | sí      | sí        | NULL         | U        | 0          | NULL     |
## | Stable ABI since version 3.11.* |         |           |              |          |            |          |

| PyBUF_STRIDED_RO  * Part of the | sí      | sí        | NULL         | U        | 1 o 0      | NULL     |
## | Stable ABI since version 3.11.* |         |           |              |          |            |          |

| PyBUF_CONTIG  * Part of the     | sí      | NULL      | NULL         | C        | 0          | NULL     |
## | Stable ABI since version 3.11.* |         |           |              |          |            |          |

| PyBUF_CONTIG_RO  * Part of the  | sí      | NULL      | NULL         | C        | 1 o 0      | NULL     |
## | Stable ABI since version 3.11.* |         |           |              |          |            |          |

## Arreglos complejos

### Estilo NumPy: forma y *strides*

La estructura lógica de las matrices de estilo NumPy está definida por
"itemsize", "ndim", "shape" y "strides".

Si "ndim == 0", la ubicación de memoria señalada por "buf" se
interpreta como un escalar de tamaño "itemsize". En ese caso, tanto
"shape" como "strides" son "NULL".

Si "strides" es "NULL", el arreglo se interpreta como un arreglo C
n-dimensional estándar. De lo contrario, el consumidor debe acceder a
un arreglo n-dimensional de la siguiente manera:

   ptr = (char *)buf + indices[0] * strides[0] + ... + indices[n-1] * strides[n-1];
   item = *((typeof(item) *)ptr);

Como se señaló anteriormente, "buf" puede apuntar a cualquier
ubicación dentro del bloque de memoria real. Un exportador puede
verificar la validez de un búfer con esta función:

   def verify_structure(memlen, itemsize, ndim, shape, strides, offset):
       """Verify that the parameters represent a valid array within
          the bounds of the allocated memory:
              char *mem: start of the physical memory block
              memlen: length of the physical memory block
              offset: (char *)buf - mem
       """
       if offset % itemsize:
           return False
       if offset < 0 or offset+itemsize > memlen:
           return False
       if any(v % itemsize for v in strides):
           return False

       if ndim <= 0:
           return ndim == 0 and not shape and not strides
       if 0 in shape:
           return True

       imin = sum(strides[j]*(shape[j]-1) for j in range(ndim)
                  if strides[j] <= 0)
       imax = sum(strides[j]*(shape[j]-1) for j in range(ndim)
                  if strides[j] > 0)

       return 0 <= offset+imin and offset+imax+itemsize <= memlen

### Estilo PIL: forma, *strides* y *suboffsets*

Además de los elementos normales, los arreglos de estilo PIL pueden
contener punteros que deben seguirse para llegar al siguiente elemento
en una dimensión. Por ejemplo, el arreglo C tridimensional regular
"char v[2][2][3]" también se puede ver como un arreglo de 2 punteros a
2 arreglos bidimensionales: "char (*v[2])[2][3]". En la representación
de *suboffsets*, esos dos punteros pueden incrustarse al comienzo de
"buf", apuntando a dos matrices "char x[2][3]" que pueden ubicarse en
cualquier lugar de la memoria.

Aquí hay una función que retorna un puntero al elemento en un arreglo
N-D a la que apunta un índice N-dimensional cuando hay *strides* y
*suboffsets* no "NULL":

   void *get_item_pointer(int ndim, void *buf, Py_ssize_t *strides,
                          Py_ssize_t *suboffsets, Py_ssize_t *indices) {
       char *pointer = (char*)buf;
       int i;
       for (i = 0; i < ndim; i++) {
           pointer += strides[i] * indices[i];
           if (suboffsets[i] >=0 ) {
               pointer = *((char**)pointer) + suboffsets[i];
           }
       }
       return (void*)pointer;
   }

## Funciones relacionadas a búfer

int PyObject_CheckBuffer(PyObject *obj)
    * Part of the Stable ABI since version 3.11.*

   Retorna "1" si *obj* admite la interfaz de búfer; de lo contrario,
   "0" cuando se retorna "1", no garantiza que "PyObject_GetBuffer()"
   tenga éxito. Esta función siempre finaliza con éxito.

int PyObject_GetBuffer(PyObject *exporter, Py_buffer *view, int flags)
    * Part of the Stable ABI since version 3.11.*

   Send a request to *exporter* to fill in *view* as specified by
   *flags*. If the exporter cannot provide a buffer of the exact type,
   it MUST raise "BufferError", set "view->obj" to "NULL" and return
   "-1".

   Si tiene éxito, completa *view*, establece "view->obj" en una nueva
   referencia a *exporter* y retorna 0. En el caso de proveedores de
   búfer encadenados que redirigen las solicitudes a un solo objeto,
   "view->obj" PUEDE referirse a este objeto en lugar de *exporter*
   (Ver Estructuras de objetos de búfer).

   Las llamadas exitosas a "PyObject_GetBuffer()" deben combinarse con
   las llamadas a "PyBuffer_Release()", similar a "malloc()" y
   "free()". Por lo tanto, después de que el consumidor haya terminado
   con el búfer, "PyBuffer_Release()" debe llamarse exactamente una
   vez.

void PyBuffer_Release(Py_buffer *view)
    * Part of the Stable ABI since version 3.11.*

   Release the buffer *view* and release the *strong reference* (i.e.
   decrement the reference count) to the view's supporting object,
   "view->obj". This function MUST be called when the buffer is no
   longer being used, otherwise reference leaks may occur.

   Es un error llamar a esta función en un búfer que no se obtuvo a
   través de "PyObject_GetBuffer()".

Py_ssize_t PyBuffer_SizeFromFormat(const char *format)
    * Part of the Stable ABI since version 3.11.*

   Return the implied "itemsize" from "format". On error, raise an
   exception and return -1.

   Added in version 3.9.

int PyBuffer_IsContiguous(const Py_buffer *view, char order)
    * Part of the Stable ABI since version 3.11.*

   Retorna "1" si la memoria definida por *view* es de estilo C
   (*order* es "'C'") o de estilo Fortran (*order* es "'F'")
   *contiguous* o uno cualquiera (*order* es "'A'"). Retorna "0" de lo
   contrario. Esta función siempre finaliza con éxito.

void *PyBuffer_GetPointer(const Py_buffer *view, const Py_ssize_t *indices)
    * Part of the Stable ABI since version 3.11.*

   Obtiene el área de memoria señalada por los *indices* dentro del
   *view* dado. *indices* deben apuntar a un arreglo de índices
   "view->ndim".

int PyBuffer_FromContiguous(const Py_buffer *view, const void *buf, Py_ssize_t len, char fort)
    * Part of the Stable ABI since version 3.11.*

   Copia *len* bytes contiguos de *buf* a *view*. *fort* puede ser
   "'C'" o "'F'" (para pedidos al estilo C o al estilo Fortran). "0"
   se retorna en caso de éxito, "-1" en caso de error.

int PyBuffer_ToContiguous(void *buf, const Py_buffer *src, Py_ssize_t len, char order)
    * Part of the Stable ABI since version 3.11.*

   Copia *len* bytes de *src* a su representación contigua en *buf*.
   *order* puede ser "'C'" o "'F'" o "''A'" (para pedidos al estilo C
   o al estilo Fortran o cualquiera) "0" se retorna en caso de éxito,
   "-1" en caso de error.

   Esta función falla si *len* != *src->len*.

int PyObject_CopyData(PyObject *dest, PyObject *src)
    * Part of the Stable ABI since version 3.11.*

   Copiar datos del búfer *src* al *dest*. Puede convertir entre
   búferes de estilo C o Fortran.

   Se retorna "0" en caso de éxito, "-1" en caso de error.

void PyBuffer_FillContiguousStrides(int ndims, Py_ssize_t *shape, Py_ssize_t *strides, int itemsize, char order)
    * Part of the Stable ABI since version 3.11.*

   Rellena el arreglo *strides* con bytes de paso de un *contiguous*
   (estilo C si *order* es "'C'" o estilo Fortran si *order* es "'F '"
   ) arreglo de la forma dada con el número dado de bytes por
   elemento.

int PyBuffer_FillInfo(Py_buffer *view, PyObject *exporter, void *buf, Py_ssize_t len, int readonly, int flags)
    * Part of the Stable ABI since version 3.11.*

   Maneje las solicitudes de búfer para un exportador que quiera
   exponer *buf* de tamaño *len* con capacidad de escritura
   establecida de acuerdo con *readonly*. *buf* se interpreta como una
   secuencia de bytes sin signo.

   El argumento *flags* indica el tipo de solicitud. Esta función
   siempre llena *view* según lo especificado por *flags*, a menos que
   *buf* haya sido designado como solo lectura y "PyBUF_WRITABLE" esté
   configurado en *flags*.

   On success, set "view->obj" to a new reference to *exporter* and
   return 0. Otherwise, raise "BufferError", set "view->obj" to "NULL"
   and return "-1";

   Si esta función se usa como parte de a getbufferproc, *exporter*
   DEBE establecerse en el objeto exportador y *flags* deben pasarse
   sin modificaciones. De lo contrario, *exporter* DEBE ser "NULL".
