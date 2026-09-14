---
title: '"dis" --- Desensamblador para bytecode de Python'
source_url: https://docs.python.org/es/3
source_path: library/dis.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2340
---

# "dis" --- Desensamblador para bytecode de Python

**Código fuente:** Lib/dis.py

======================================================================

The "dis" module supports the analysis of CPython *bytecode* by
disassembling it. The CPython bytecode which this module takes as an
input is defined in the file "Include/opcode.h" and used by the
compiler and the interpreter.

Bytecode es un detalle de implementación del intérprete CPython. No se
garantiza que el bytecode no se agregará, eliminará ni cambiará entre
las versiones de Python. El uso de este módulo no debe considerarse
para trabajar en diferentes máquinas virtuales Python o versiones de
Python.

Distinto en la versión 3.6: Use 2 bytes para cada instrucción.
Anteriormente, el número de bytes variaba según la instrucción.

Distinto en la versión 3.10: El argumento de las instrucciones de
salto, manejo de excepciones y bucle ahora es el desplazamiento de
instrucción en lugar del desplazamiento de byte.

Distinto en la versión 3.11: Some instructions are accompanied by one
or more inline cache entries, which take the form of "CACHE"
instructions. These instructions are hidden by default, but can be
shown by passing "show_caches=True" to any "dis" utility. Furthermore,
the interpreter now adapts the bytecode to specialize it for different
runtime conditions. The adaptive bytecode can be shown by passing
"adaptive=True".

Distinto en la versión 3.12: El argumento de un salto es el
desplazamiento de la instrucción de destino en relación con la
instrucción que aparece inmediatamente después de las entradas "CACHE"
de la instrucción de salto.Como consecuencia, la presencia de las
instrucciones "CACHE" es transparente para los saltos hacia adelante,
pero debe tenerse en cuenta al razonar sobre los saltos hacia atrás.

Distinto en la versión 3.13: La salida muestra etiquetas lógicas en
lugar de desplazamientos de instrucciones para destinos de salto y
controladores de excepciones. Se agregaron la opción de línea de
comandos "-O" y el argumento "show_offsets".

Distinto en la versión 3.14: The "-P" command-line option and the
"show_positions" argument were added.The "-S" command-line option is
added.

Ejemplo: Dada la función "myfunc()":

   def myfunc(alist):
       return len(alist)

El siguiente comando se puede utilizar para mostrar el desmontaje de
"myfunc()":

   >>> dis.dis(myfunc)
     2           RESUME                   0

     3           LOAD_GLOBAL              1 (len + NULL)
                 LOAD_FAST_BORROW         0 (alist)
                 CALL                     1
                 RETURN_VALUE

(El "2" es un número de línea).

## Interfaz de línea de comandos

The "dis" module can be invoked as a script from the command line:

   python -m dis [-h] [-C] [-O] [-P] [-S] [infile]

Se aceptan las siguientes opciones:

-h, --help

   Mostrar uso y salir.

-C, --show-caches

   Mostrar cachés en línea.

   Added in version 3.13.

-O, --show-offsets

   Mostrar desplazamientos de instrucciones.

   Added in version 3.13.

-P, --show-positions

   Show positions of instructions in the source code.

   Added in version 3.14.

-S, --specialized

   Show specialized bytecode.

   Added in version 3.14.

Si se especifica "infile", su código desensamblado se escribirá en la
salida estándar. De lo contrario, el desensamblado se realiza en el
código fuente compilado recibido de la entrada estándar.

## Análisis de bytecode

Added in version 3.4.

La API de análisis de bytecode permite que partes del código Python se
envuelvan en un objeto "Bytecode" que proporciona un fácil acceso a
los detalles del código compilado.

class dis.Bytecode(x, *, first_line=None, current_offset=None, show_caches=False, adaptive=False, show_offsets=False, show_positions=False)

   Analiza el bytecode correspondiente a una función, generador,
   generador asíncrono, corutina, método, cadena de código fuente o un
   objeto de código (como lo retorna "compile()").

   Este es un contenedor conveniente para muchas de las funciones
   enumeradas a continuación, en particular "get_instructions()", ya
   que iterar sobre una instancia de "Bytecode" produce las
   operaciones de bytecode como instancias de "Instruction".

   Si *first_line* no es "None", indica el número de línea que se debe
   informar para la primera línea de origen en el código desmontado.
   De lo contrario, la información de la línea de origen (si la hay)
   se toma directamente del objeto de código desmontado.

   Si *current_offset* no es "None", se refiere a un desplazamiento de
   instrucción en el código desmontado. Establecer esto significa
   "dis()" mostrará un marcador de "instrucción actual" contra el
   código de operación especificado.

   Si *show_caches* es "True", "dis()" mostrará las entradas de caché
   en línea utilizadas por el intérprete para especializar el código
   de bytes.

   Si *adaptive* es "True", "dis()" mostrará un código de bytes
   especializado que puede ser diferente del código de bytes original.

   Si *show_offsets* es "True", "dis()" incluirá desplazamientos de
   instrucciones en la salida.

   If *show_positions* is "True", "dis()" will include instruction
   source code positions in the output.

   classmethod from_traceback(tb, *, show_caches=False)

      Construye una instancia de "Bytecode" a partir del *traceback*
      dado, estableciendo *current_offset* en la instrucción
      responsable de la excepción.

   codeobj

      El objeto de código compilado.

   first_line

      La primera línea de origen del objeto de código (si está
      disponible)

   dis()

      Retorna una vista formateada de las operaciones de bytecode (lo
      mismo que impreso por "dis.dis()", pero retornado como una
      cadena de caracteres multilínea).

   info()

      Retorna una cadena de caracteres multilínea formateada con
      información detallada sobre el objeto de código, como
      "code_info()".

   Distinto en la versión 3.7: Esto ahora puede manejar objetos
   generadores asíncronos y de corutinas.

   Distinto en la versión 3.11: Se agregaron los parámetros
   *show_caches* y *adaptive*.

   Distinto en la versión 3.13: Added the *show_offsets* parameter

   Distinto en la versión 3.14: Added the *show_positions* parameter.

Ejemplo:

   >>> bytecode = dis.Bytecode(myfunc)
   >>> for instr in bytecode:
   ...     print(instr.opname)
   ...
   RESUME
   LOAD_GLOBAL
   LOAD_FAST_BORROW
   CALL
   RETURN_VALUE

## Funciones de análisis

The "dis" module also defines the following analysis functions that
convert the input directly to the desired output. They can be useful
if only a single operation is being performed, so the intermediate
analysis object isn't useful:

dis.code_info(x)

   Retorna una cadena de caracteres multilínea formateada con
   información detallada del objeto de código para la función,
   generador, generador asíncrono, corutina, método, cadena de código
   fuente u objeto de código suministrados.

   Tenga en cuenta que el contenido exacto de las cadenas de
   información de código depende en gran medida de la implementación y
   puede cambiar arbitrariamente en las diferentes máquinas virtuales
   Python o las versiones de Python.

   Added in version 3.2.

   Distinto en la versión 3.7: Esto ahora puede manejar objetos
   generadores asíncronos y de corutinas.

dis.show_code(x, *, file=None)

   Imprime información detallada del objeto de código para la función,
   método, cadena de código fuente u objeto de código suministrado en
   *file* (o "sys.stdout" si *file* no está especificado).

   Esta es una abreviatura conveniente para "print(code_info(x),
   file=file)", destinado a la exploración interactiva en el indicador
   del intérprete (*prompt*).

   Added in version 3.2.

   Distinto en la versión 3.4: Agrega un parámetro *file*.

dis.dis(x=None, *, file=None, depth=None, show_caches=False, adaptive=False, show_offsets=False, show_positions=False)

   Desensamblar el objeto *x*. *x* puede denotar un módulo, una clase,
   un método, una función, un generador, un generador asincrónico, una
   corrutina, un objeto de código, una cadena de código fuente o una
   secuencia de bytes de código de bytes sin formato. Para un módulo,
   desensamblar todas las funciones. Para una clase, desensamblar
   todos los métodos (incluidos los métodos de clase y estáticos).
   Para un objeto de código o una secuencia de código de bytes sin
   formato, imprime una línea por cada instrucción de código de bytes.
   También desensamblar de forma recursiva objetos de código anidados.
   Estos pueden incluir expresiones de generador, funciones anidadas,
   los cuerpos de clases anidadas y los objetos de código utilizados
   para annotation scopes. Las cadenas se compilan primero en objetos
   de código con la función incorporada "compile()" antes de
   desensamblarse. Si no se proporciona ningún objeto, esta función
   desensamblará el último seguimiento.

   El desensamblaje se escribe como texto en el argumento *file*
   proporcionado si se proporciona y, de lo contrario, "sys.stdout".

   La profundidad máxima de recursión está limitada por *depth* a
   menos que sea "None". "depth=0" significa que no hay recursión.

   Si *show_caches* es "True", esta función mostrará las entradas de
   caché en línea utilizadas por el intérprete para especializar el
   código de bytes.

   Si *adaptive* es "True", esta función mostrará un código de bytes
   especializado que puede ser diferente del código de bytes original.

   Distinto en la versión 3.4: Agrega un parámetro *file*.

   Distinto en la versión 3.7: Desensamblaje recursivo implementado y
   parámetro agregado *depth*.

   Distinto en la versión 3.7: Esto ahora puede manejar objetos
   generadores asíncronos y de corutinas.

   Distinto en la versión 3.11: Se agregaron los parámetros
   *show_caches* y *adaptive*.

   Distinto en la versión 3.13: Se agregó el parámetro *show_offsets*.

   Distinto en la versión 3.14: Added the *show_positions* parameter.

dis.distb(tb=None, *, file=None, show_caches=False, adaptive=False, show_offset=False, show_positions=False)

   Desmonta la función de inicio de pila de un rastreo, utilizando el
   último rastreo si no se pasó ninguno. Se indica la instrucción que
   causa la excepción.

   El desensamblaje se escribe como texto en el argumento *file*
   proporcionado si se proporciona y, de lo contrario, "sys.stdout".

   Distinto en la versión 3.4: Agrega un parámetro *file*.

   Distinto en la versión 3.11: Se agregaron los parámetros
   *show_caches* y *adaptive*.

   Distinto en la versión 3.13: Se agregó el parámetro *show_offsets*.

   Distinto en la versión 3.14: Added the *show_positions* parameter.

dis.disassemble(code, lasti=-1, *, file=None, show_caches=False, adaptive=False, show_offsets=False, show_positions=False)
dis.disco(code, lasti=-1, *, file=None, show_caches=False, adaptive=False, show_offsets=False, show_positions=False)

   Desmonta un objeto de código, que indica la última instrucción si
   se proporcionó *lasti*. La salida se divide en las siguientes
   columnas:

   1. the source code location of the instruction. Complete location
      information is shown if *show_positions* is true. Otherwise (the
      default) only the line number is displayed.

   2. la instrucción actual, indicada como "-->",

   3. una instrucción etiquetada, indicada con ">>",

   4. la dirección de la instrucción,

   5. el nombre del código de operación,

   6. parámetros de operación, y

   7. interpretación de los parámetros entre paréntesis.

   La interpretación de parámetros reconoce nombres de variables
   locales y globales, valores constantes, objetivos de ramificación y
   operadores de comparación.

   El desensamblaje se escribe como texto en el argumento *file*
   proporcionado si se proporciona y, de lo contrario, "sys.stdout".

   Distinto en la versión 3.4: Agrega un parámetro *file*.

   Distinto en la versión 3.11: Se agregaron los parámetros
   *show_caches* y *adaptive*.

   Distinto en la versión 3.13: Se agregó el parámetro *show_offsets*.

   Distinto en la versión 3.14: Added the *show_positions* parameter.

dis.get_instructions(x, *, first_line=None, show_caches=False, adaptive=False)

   Retorna un iterador sobre las instrucciones en la función, método,
   cadena de código fuente u objeto de código suministrado.

   El iterador genera una serie de tuplas con nombre "Instruction" que
   dan los detalles de cada operación en el código suministrado.

   Si *first_line* no es "None", indica el número de línea que se debe
   informar para la primera línea de origen en el código desmontado.
   De lo contrario, la información de la línea de origen (si la hay)
   se toma directamente del objeto de código desmontado.

   El parámetro *adaptive* funciona como lo hace en "dis()".

   Added in version 3.4.

   Distinto en la versión 3.11: Se agregaron los parámetros
   *show_caches* y *adaptive*.

   Distinto en la versión 3.13: El parámetro *show_caches* está
   obsoleto y no tiene efecto. El iterador genera las instancias
   "Instruction" con el campo *cache_info* completado
   (independientemente del valor de *show_caches*) y ya no genera
   elementos separados para las entradas de caché.

dis.findlinestarts(code)

   Esta función generadora utiliza el método "co_lines()" de code
   object y *code* para encontrar los desplazamientos que son inicios
   de líneas en el código fuente. Se generan como pares "(offset,
   lineno)".

   Distinto en la versión 3.6: Los números de línea pueden estar
   disminuyendo. Antes, siempre estaban aumentando.

   Distinto en la versión 3.10: Se utiliza el método **PEP 626**
   "co_lines()" en lugar de los atributos "co_firstlineno" y
   "co_lnotab" del code object.

   Distinto en la versión 3.13: Los números de línea pueden ser "None"
   para el código de bytes que no se asigna a las líneas de origen.

dis.findlabels(code)

   Detecta todos los desplazamientos en la cadena de caracteres de
   código de byte compilada *code* que son objetivos de salto y
   retorna una lista de estos desplazamientos.

dis.stack_effect(opcode, oparg=None, *, jump=None)

   Calcula el efecto de pila de *opcode* con el argumento *oparg*.

   Si el código tiene un objetivo de salto y *jump* es "True",
   "stack_effect()" retornará el efecto de pila del salto. Si *jump*
   es "False", retornará el efecto de acumulación de no saltar. Y si
   *jump* es "None" (predeterminado), retornará el efecto de
   acumulación máxima de ambos casos.

   Added in version 3.4.

   Distinto en la versión 3.8: Agrega un parámetro *jump*.

   Distinto en la versión 3.13: Si se omite "oparg" (o "None"), ahora
   se devuelve el efecto de pila para "oparg=0". Anteriormente, esto
   era un error para los códigos de operación que usan su argumento.
   Tampoco es un error pasar un entero "oparg" cuando "opcode" no lo
   usa; en este caso, se ignora "oparg".

## Instrucciones bytecode de Python

La función "get_instructions()" y clase "Bytecode" proporcionan
detalles de las instrucciones bytecode como instancias "Instruction":

class dis.Instruction

   Detalles para una operación de bytecode

   opcode

      código numérico para la operación, correspondiente a los valores
      del opcode listados a continuación y los valores de bytecode en
      Colecciones opcode.

   opname

      nombre legible por humanos para la operación

   baseopcode

      código numérico para la operación base si la operación es
      especializada; en caso contrario, igual a "opcode"

   baseopname

      Nombre legible para humanos para la operación base si la
      operación es especializada; de lo contrario, es igual a "opname"

   arg

      argumento numérico para la operación (si existe), de lo
      contrario "None"

   oparg

      alias para "arg"

   argval

      valor de argumento resuelto (si lo hay); de lo contrario, "None"

   argrepr

      descripción legible por humanos del argumento de la operación
      (si lo hay); de lo contrario, una cadena vacía.

   offset

      índice de inicio de operación dentro de la secuencia de bytecode

   start_offset

      índice de inicio de la operación dentro de la secuencia de
      bytecode, incluidas las operaciones con prefijo "EXTENDED_ARG"
      si están presentes; de lo contrario, igual a "offset"

   cache_offset

      índice de inicio de las entradas de caché después de la
      operación

   end_offset

      índice final de las entradas de caché después de la operación

   starts_line

      "True" si este código de operación inicia una línea de origen,
      de lo contrario "False"

   line_number

      número de línea de origen asociado con este código de operación
      (si lo hay), de lo contrario "None"

   is_jump_target

      "True" si otro código salta aquí, de lo contrario, "False"

   jump_target

      índice de código de bytes del objetivo del salto si se trata de
      una operación de salto, de lo contrario "None"

   positions

      Objeto "dis.Positions" que contiene las ubicaciones de inicio y
      finalización cubiertas por esta instrucción.

   cache_info

      Information about the cache entries of this instruction, as
      triplets of the form "(name, size, data)", where the "name" and
      "size" describe the cache format and data is the contents of the
      cache. "cache_info" is "None" if the instruction does not have
      caches.

   Added in version 3.4.

   Distinto en la versión 3.11: Se agrega el campo "positions".

   Distinto en la versión 3.13: Se modificó el campo "starts_line".Se
   agregaron los campos "start_offset", "cache_offset", "end_offset",
   "baseopname", "baseopcode", "jump_target", "oparg", "line_number" y
   "cache_info".

class dis.Positions

   En caso de que la información no esté disponible, algunos campos
   pueden ser "None".

   lineno

   end_lineno

   col_offset

   end_col_offset

   Added in version 3.11.

El compilador de Python actualmente genera las siguientes
instrucciones de bytecode.

**Instrucciones generales**

A continuación, nos referiremos a la pila del intérprete como "STACK"
y describiremos las operaciones en ella como si fuera una lista de
Python. La parte superior de la pila corresponde a "STACK[-1]" en este
lenguaje.

NOP

   Código que no hace nada. Utilizado como marcador de posición por el
   optimizador de bytecode y para generar eventos de seguimiento de
   línea.

NOT_TAKEN

   Do nothing code. Used by the interpreter to record "BRANCH_LEFT"
   and "BRANCH_RIGHT" events for "sys.monitoring".

   Added in version 3.14.

POP_ITER

   Removes the iterator from the top of the stack.

   Added in version 3.14.

POP_TOP

   Elimina el elemento de la parte superior de la pila:

      STACK.pop()

END_FOR

   Elimina el elemento superior de la pila. Equivale a "POP_TOP". Se
   utiliza para limpiar al final de los bucles, de ahí el nombre.

   Added in version 3.12.

END_SEND

   Implementa "del STACK[-2]". Se utiliza para limpiar cuando finaliza
   un generador.

   Added in version 3.12.

COPY(i)

   Empuja el elemento i-ésimo hacia la parte superior de la pila sin
   quitarlo de su ubicación original:

      assert i > 0
      STACK.append(STACK[-i])

   Added in version 3.11.

SWAP(i)

   Intercambia la parte superior de la pila con el elemento i-ésimo:

      STACK[-i], STACK[-1] = STACK[-1], STACK[-i]

   Added in version 3.11.

CACHE

   En lugar de ser una instrucción real, este código de operación se
   usa para marcar espacio adicional para que el intérprete almacene
   en caché datos útiles directamente en el bytecode. Todas las
   utilidades "dis" lo ocultan automáticamente, pero se puede ver con
   "show_caches=True".

   Lógicamente, este espacio forma parte de la instrucción anterior.
   Muchos códigos de operación esperan ser seguidos por un número
   exacto de cachés y le indicarán al intérprete que los omita en
   tiempo de ejecución.

   Los cachés poblados pueden parecer instrucciones arbitrarias, por
   lo que se debe tener mucho cuidado al leer o modificar el bytecode
   adaptativo sin procesar que contiene datos acelerados.

   Added in version 3.11.

**Operaciones unarias**

Las operaciones unarias toman la parte superior de la pila, aplican la
operación y retornan el resultado a la pila.

UNARY_NEGATIVE

   Implementa "STACK[-1] = -STACK[-1]".

UNARY_NOT

   Implementa "STACK[-1] = not STACK[-1]".

   Distinto en la versión 3.13: Esta instrucción ahora requiere un
   operando "bool" exacto.

UNARY_INVERT

   Implementa "STACK[-1] = ~STACK[-1]".

GET_ITER

   Implementa "STACK[-1] = iter(STACK[-1])".

GET_YIELD_FROM_ITER

   Si "STACK[-1]" es un objeto *generator iterator* o *coroutine*, se
   deja como está. De lo contrario, se implementa "STACK[-1] =
   iter(STACK[-1])".

   Added in version 3.5.

TO_BOOL

   Implementa "STACK[-1] = bool(STACK[-1])".

   Added in version 3.13.

**Operaciones binarias e in situ**

Las operaciones binarias eliminan los dos elementos superiores de la
pila ("STACK[-1]" y "STACK[-2]"). Realizan la operación y luego
vuelven a colocar el resultado en la pila.

Las operaciones en el lugar son como operaciones binarias, pero la
operación se realiza en el lugar cuando "STACK[-2]" la admite, y el
"STACK[-1]" resultante puede ser (pero no tiene que ser) el
"STACK[-2]" original.

BINARY_OP(op)

   Implementa los operadores binarios y locales (según el valor de
   *op*):

      rhs = STACK.pop()
      lhs = STACK.pop()
      STACK.append(lhs op rhs)

   Added in version 3.11.

   Distinto en la versión 3.14: With oparg :"NB_SUBSCR", implements
   binary subscript (replaces opcode "BINARY_SUBSCR")

STORE_SUBSCR

   Implementos:

      key = STACK.pop()
      container = STACK.pop()
      value = STACK.pop()
      container[key] = value

DELETE_SUBSCR

   Implementos:

      key = STACK.pop()
      container = STACK.pop()
      del container[key]

BINARY_SLICE

   Implementos:

      end = STACK.pop()
      start = STACK.pop()
      container = STACK.pop()
      STACK.append(container[start:end])

   Added in version 3.12.

STORE_SLICE

   Implementos:

      end = STACK.pop()
      start = STACK.pop()
      container = STACK.pop()
      value = STACK.pop()
      container[start:end] = value

   Added in version 3.12.

**Opcodes de corutinas**

GET_AWAITABLE(where)

   Implementa "STACK[-1] = get_awaitable(STACK[-1])", donde
   "get_awaitable(o)" devuelve "o" si "o" es un objeto de corrutina o
   un objeto generador con el indicador "CO_ITERABLE_COROUTINE", o
   resuelve "o.__await__".

      Si el operando "where" es distinto de cero, indica dónde ocurre
      la instrucción:

      * "1": Después de una llamada a "__aenter__"

      * "2": Después de una llamada a "__aexit__"

   Added in version 3.5.

   Distinto en la versión 3.11: Anteriormente, esta instrucción no
   tenía un oparg.

GET_AITER

   Implementa "STACK[-1] = STACK[-1].__aiter__()".

   Added in version 3.5.

   Distinto en la versión 3.7: Ya no se admite el retorno de objetos
   *awaitable* de "__aiter__".

GET_ANEXT

   Implemente "STACK.append(get_awaitable(STACK[-1].__anext__()))" en
   la pila. Consulte "GET_AWAITABLE" para obtener más detalles sobre
   "get_awaitable".

   Added in version 3.5.

END_ASYNC_FOR

   Finaliza un bucle "async for". Controla una excepción generada al
   esperar un elemento siguiente. La pila contiene el iterable
   asincrónico en "STACK[-2]" y la excepción generada en "STACK[-1]".
   Ambos se eliminan. Si la excepción no es "StopAsyncIteration", se
   vuelve a generar.

   Added in version 3.8.

   Distinto en la versión 3.11: La representación de excepciones en la
   pila ahora consta de uno, no de tres elementos.

CLEANUP_THROW

   Maneja una excepción generada durante una llamada "throw()" o
   "close()" a través del marco actual. Si "STACK[-1]" es una
   instancia de "StopIteration", extrae tres valores de la pila y
   envía su miembro "value". De lo contrario, vuelve a generar
   "STACK[-1]".

   Added in version 3.12.

**Opcodes misceláneos**

SET_ADD(i)

   Implementos:

      item = STACK.pop()
      set.add(STACK[-i], item)

   Se utiliza para implementar comprensiones de conjuntos.

LIST_APPEND(i)

   Implementos:

      item = STACK.pop()
      list.append(STACK[-i], item)

   Se utiliza para implementar listas por comprensión.

MAP_ADD(i)

   Implementos:

      value = STACK.pop()
      key = STACK.pop()
      dict.__setitem__(STACK[-i], key, value)

   Se utiliza para implementar comprensiones de diccionarios.

   Added in version 3.1.

   Distinto en la versión 3.8: El valor del mapa es "STACK[-1]" y la
   clave del mapa es "STACK[-2]". Antes, estaban invertidos.

Para todas las instrucciones "SET_ADD", "LIST_APPEND" y "MAP_ADD",
mientras el valor agregado o el par clave/valor aparece, el objeto
contenedor permanece en la pila para que quede disponible para futuras
iteraciones del bucle.

RETURN_VALUE

   Regresa con "STACK[-1]" al llamador de la función.

YIELD_VALUE

   Produce "STACK.pop()" a partir de un *generator*.

   Distinto en la versión 3.11: oparg establecido para ser la
   profundidad de la pila.

   Distinto en la versión 3.12: oparg está configurado para ser la
   profundidad del bloque de excepción, para el cierre eficiente de
   los generadores.

   Distinto en la versión 3.13: oparg es "1" si esta instrucción es
   parte de un yield-from o await, y "0" en caso contrario.

SETUP_ANNOTATIONS

   Comprueba si "__anotaciones__" está definido en "locals()", si no
   está configurado como un "dict" vacío. Este código de operación
   solo se emite si el cuerpo de una clase o módulo contiene
   *anotaciones de variables* estáticamente.

   Added in version 3.6.

POP_EXCEPT

   Extrae un valor de la pila, que se utiliza para restaurar el estado
   de excepción.

   Distinto en la versión 3.11: La representación de excepciones en la
   pila ahora consta de uno, no de tres elementos.

RERAISE

   Vuelve a generar la excepción que se encuentra actualmente en la
   parte superior de la pila. Si oparg no es cero, extrae un valor
   adicional de la pila que se utiliza para establecer "f_lasti" del
   marco actual.

   Added in version 3.9.

   Distinto en la versión 3.11: La representación de excepciones en la
   pila ahora consta de uno, no de tres elementos.

PUSH_EXC_INFO

   Extrae un valor de la pila. Agrega la excepción actual a la parte
   superior de la pila. Agrega el valor que apareció originalmente de
   vuelta a la pila. Se utiliza en los controladores de excepciones.

   Added in version 3.11.

CHECK_EXC_MATCH

   Realiza una comparación de excepciones para "except". Comprueba si
   "STACK[-2]" es una comparación de excepciones con "STACK[-1]".
   Extrae "STACK[-1]" y envía el resultado booleano de la prueba.

   Added in version 3.11.

CHECK_EG_MATCH

   Realiza la coincidencia de excepciones para "except*". Aplica
   "split(STACK[-1])" en el grupo de excepciones que representa a
   "STACK[-2]".

   En caso de coincidencia, extrae dos elementos de la pila y agrega
   el subgrupo que no coincide ("None" en caso de coincidencia total)
   seguido del subgrupo coincidente. Cuando no hay ninguna
   coincidencia, muestra un elemento (el tipo de coincidencia) y
   presiona "None".

   Added in version 3.11.

WITH_EXCEPT_START

   Llama a la función en la posición 4 de la pila con argumentos
   (tipo, val, tb) que representan la excepción en la parte superior
   de la pila. Se utiliza para implementar la llamada
   "context_manager.__exit__(*exc_info())" cuando se ha producido una
   excepción en una sentencia "with".

   Added in version 3.9.

   Distinto en la versión 3.11: La función "__exit__" está en la
   posición 4 de la pila en lugar de la 7. La representación de
   excepciones en la pila ahora consta de uno, no de tres, elementos.

LOAD_COMMON_CONSTANT

   Pushes a common constant onto the stack. The interpreter contains a
   hardcoded list of constants supported by this instruction.  Used by
   the "assert" statement to load "AssertionError".

   Added in version 3.14.

LOAD_BUILD_CLASS

   Coloca "builtins.__build_class__()" en la pila. Luego se lo llama
   para construir una clase.

GET_LEN

   Perform "STACK.append(len(STACK[-1]))". Used in "match" statements
   where comparison with structure of pattern is needed.

   Added in version 3.10.

MATCH_MAPPING

   Si "STACK[-1]" es una instancia de "collections.abc.Mapping" (o,
   más técnicamente: si tiene el indicador "Py_TPFLAGS_MAPPING"
   establecido en su "tp_flags"), inserte "True" en la pila. De lo
   contrario, inserte "False".

   Added in version 3.10.

MATCH_SEQUENCE

   Si "STACK[-1]" es una instancia de "collections.abc.Sequence" y
   *not* es una instancia de "str"/"bytes"/"bytearray" (o, más
   técnicamente: si tiene el indicador "Py_TPFLAGS_SEQUENCE"
   establecido en su "tp_flags"), inserte "True" en la pila. De lo
   contrario, inserte "False".

   Added in version 3.10.

MATCH_KEYS

   "STACK[-1]" es una tupla de claves de mapeo y "STACK[-2]" es el
   sujeto de la coincidencia. Si "STACK[-2]" contiene todas las claves
   de "STACK[-1]", inserte un "tuple" que contenga los valores
   correspondientes. De lo contrario, inserte "None".

   Added in version 3.10.

   Distinto en la versión 3.11: Anteriormente, esta instrucción
   también generaba un valor booleano que indicaba éxito ("True") o
   falla ("False").

STORE_NAME(namei)

   Implementa "name = STACK.pop()". *namei* es el índice de *name* en
   el atributo "co_names" de code object. El compilador intenta
   utilizar "STORE_FAST" o "STORE_GLOBAL" si es posible.

DELETE_NAME(namei)

   Implementa "del name", donde *namei* es el índice en el atributo
   "co_names" del code object.

UNPACK_SEQUENCE(count)

   Descomprime "STACK[-1]" en valores individuales *count*, que se
   colocan en la pila de derecha a izquierda. Requiere que haya
   exactamente valores *count*.:

      assert(len(STACK[-1]) == count)
      STACK.extend(STACK.pop()[:-count-1:-1])

UNPACK_EX(counts)

   Implementa la asignación con un objetivo destacado: descomprime un
   iterable en "STACK[-1]" en valores individuales, donde la cantidad
   total de valores puede ser menor que la cantidad de elementos en el
   iterable: uno de los nuevos valores será una lista de todos los
   elementos restantes.

   El número de valores antes y después del valor de la lista está
   limitado a 255.

   La cantidad de valores antes del valor de la lista se codifica en
   el argumento del código de operación. La cantidad de valores
   después de la lista, si los hay, se codifica utilizando un
   "EXTENDED_ARG". Como consecuencia, el argumento puede verse como
   valores de dos bytes, donde el byte bajo de *counts* es la cantidad
   de valores antes del valor de la lista y el byte alto de *counts*,
   la cantidad de valores después de este.

   Los valores extraídos se colocan en la pila de derecha a izquierda,
   es decir, "a, *b, c = d" se almacenará después de la ejecución como
   "STACK.extend((a, b, c))".

STORE_ATTR(namei)

   Implementos:

      obj = STACK.pop()
      value = STACK.pop()
      obj.name = value

   donde *namei* es el índice del nombre en "co_names" del code
   object.

DELETE_ATTR(namei)

   Implementos:

      obj = STACK.pop()
      del obj.name

   donde *namei* es el índice del nombre en "co_names" del code
   object.

STORE_GLOBAL(namei)

   Funciona como "STORE_NAME", pero almacena el nombre como global.

DELETE_GLOBAL(namei)

   Funciona como "DELETE_NAME", pero elimina un nombre global.

LOAD_CONST(consti)

   Apila "co_consts[consti]" en la pila.

LOAD_SMALL_INT(i)

   Pushes the integer "i" onto the stack. "i" must be in "range(256)"

   Added in version 3.14.

LOAD_NAME(namei)

   Introduce el valor asociado con "co_names[namei]" en la pila. El
   nombre se busca en las variables locales, luego en las variables
   globales y luego en las integradas.

LOAD_LOCALS

   Introduce una referencia al diccionario de variables locales en la
   pila. Esto se utiliza para preparar diccionarios de espacios de
   nombres para "LOAD_FROM_DICT_OR_DEREF" y
   "LOAD_FROM_DICT_OR_GLOBALS".

   Added in version 3.12.

LOAD_FROM_DICT_OR_GLOBALS(i)

   Extrae una asignación de la pila y busca el valor de
   "co_names[namei]". Si no se encuentra el nombre allí, lo busca en
   las variables globales y luego en las integradas, de forma similar
   a "LOAD_GLOBAL". Esto se utiliza para cargar variables globales en
   annotation scopes dentro de los cuerpos de clase.

   Added in version 3.12.

BUILD_TEMPLATE

   Constructs a new "Template" instance from a tuple of strings and a
   tuple of interpolations and pushes the resulting object onto the
   stack:

      interpolations = STACK.pop()
      strings = STACK.pop()
      STACK.append(_build_template(strings, interpolations))

   Added in version 3.14.

BUILD_INTERPOLATION(format)

   Constructs a new "Interpolation" instance from a value and its
   source expression and pushes the resulting object onto the stack.

   If no conversion or format specification is present, "format" is
   set to "2".

   If the low bit of "format" is set, it indicates that the
   interpolation contains a format specification.

   If "format >> 2" is non-zero, it indicates that the interpolation
   contains a conversion. The value of "format >> 2" is the conversion
   type ("0" for no conversion, "1" for "!s", "2" for "!r", and "3"
   for "!a"):

      conversion = format >> 2
      if format & 1:
          format_spec = STACK.pop()
      else:
          format_spec = None
      expression = STACK.pop()
      value = STACK.pop()
      STACK.append(_build_interpolation(value, expression, conversion, format_spec))

   Added in version 3.14.

BUILD_TUPLE(count)

   Crea una tupla que consume elementos *count* de la pila y envía la
   tupla resultante a la pila:

      if count == 0:
          value = ()
      else:
          value = tuple(STACK[-count:])
          STACK = STACK[:-count]

      STACK.append(value)

BUILD_LIST(count)

   Funciona como "BUILD_TUPLE", pero crea una lista.

BUILD_SET(count)

   Funciona como "BUILD_TUPLE", pero crea un conjunto.

BUILD_MAP(count)

   Inserta un nuevo objeto de diccionario en la pila. Extrae elementos
   "2 * count" para que el diccionario contenga entradas *count*:
   "{..., STACK[-4]: STACK[-3], STACK[-2]: STACK[-1]}".

   Distinto en la versión 3.5: El diccionario se crea a partir de
   elementos de la pila en lugar de crear un diccionario vacío
   dimensionado previamente para contener *count* elementos.

BUILD_STRING(count)

   Concatena *count* cadenas de caracteres de la pila y empuja la
   cadena de caracteres resultante en la pila.

   Added in version 3.6.

LIST_EXTEND(i)

   Implementos:

      seq = STACK.pop()
      list.extend(STACK[-i], seq)

   Se utiliza para crear listas.

   Added in version 3.9.

SET_UPDATE(i)

   Implementos:

      seq = STACK.pop()
      set.update(STACK[-i], seq)

   Se utiliza para construir decorados.

   Added in version 3.9.

DICT_UPDATE(i)

   Implementos:

      map = STACK.pop()
      dict.update(STACK[-i], map)

   Se utiliza para crear diccionarios.

   Added in version 3.9.

DICT_MERGE(i)

   Como "DICT_UPDATE" pero lanza una excepción para claves duplicadas.

   Added in version 3.9.

LOAD_ATTR(namei)

   Si el bit bajo de "namei" no está configurado, esto reemplaza
   "STACK[-1]" con "getattr(STACK[-1], co_names[namei>>1])".

   Si se establece el bit bajo de "namei", se intentará cargar un
   método llamado "co_names[namei>>1]" desde el objeto "STACK[-1]". Se
   extrae "STACK[-1]". Este código de bytes distingue dos casos: si
   "STACK[-1]" tiene un método con el nombre correcto, el código de
   bytes inserta el método no vinculado y "STACK[-1]". "CALL" o
   "CALL_KW" utilizarán "STACK[-1]" como primer argumento ("self") al
   llamar al método no vinculado. De lo contrario, se insertan "NULL"
   y el objeto devuelto por la búsqueda de atributos.

   Distinto en la versión 3.12: Si se establece el bit bajo de
   "namei", entonces se inserta un "NULL" o "self" en la pila antes
   del atributo o el método no vinculado respectivamente.

LOAD_SUPER_ATTR(namei)

   Este código de operación implementa "super()", tanto en su forma de
   cero argumentos como de dos argumentos (por ejemplo,
   "super().method()", "super().attr" y "super(cls, self).method()",
   "super(cls, self).attr").

   Extrae tres valores de la pila (desde la parte superior de la pila
   hacia abajo):

   * "self": el primer argumento del método actual

   * "cls": la clase dentro de la cual se definió el método actual

   * El "super" global

   Con respecto a su argumento, funciona de manera similar a
   "LOAD_ATTR", excepto que "namei" se desplaza hacia la izquierda 2
   bits en lugar de 1.

   El bit bajo de "namei" indica que se debe intentar cargar un
   método, como en el caso de "LOAD_ATTR", lo que da como resultado la
   inserción de "NULL" y el método cargado. Cuando no está
   configurado, se inserta un solo valor en la pila.

   El segundo bit bajo de "namei", si está configurado, significa que
   esta fue una llamada de dos argumentos a "super()" (si no está
   configurado significa cero argumentos).

   Added in version 3.12.

COMPARE_OP(opname)

   Realiza una operación booleana. El nombre de la operación se puede
   encontrar en "cmp_op[opname >> 5]". Si se establece el quinto bit
   más bajo de "opname" ("opname & 16"), el resultado se debe
   convertir a "bool".

   Distinto en la versión 3.13: El quinto bit más bajo del oparg ahora
   indica una conversión forzada a "bool".

IS_OP(invert)

   Realiza una comparación "is" o "is not" si "invert" es 1.

   Added in version 3.9.

CONTAINS_OP(invert)

   Realiza una comparación "in" o "not in" si "invert" es 1.

   Added in version 3.9.

IMPORT_NAME(namei)

   Importa el módulo "co_names[namei]". Se extraen "STACK[-1]" y
   "STACK[-2]" y proporcionan los argumentos *fromlist* y *level* de
   "__import__()". El objeto del módulo se coloca en la pila. El
   espacio de nombres actual no se ve afectado: para una declaración
   de importación adecuada, una instrucción "STORE_FAST" posterior
   modifica el espacio de nombres.

IMPORT_FROM(namei)

   Carga el atributo "co_names[namei]" del módulo que se encuentra en
   "STACK[-1]". El objeto resultante se coloca en la pila para ser
   almacenado posteriormente mediante una instrucción "STORE_FAST".

JUMP_FORWARD(delta)

   Incrementa el contador de bytecode en *delta*.

JUMP_BACKWARD(delta)

   Decrementa el contador de bytecode en *delta*. Comprueba si hay
   interrupciones.

   Added in version 3.11.

JUMP_BACKWARD_NO_INTERRUPT(delta)

   Decrementa el contador de bytecode en *delta*. No busca
   interrupciones.

   Added in version 3.11.

POP_JUMP_IF_TRUE(delta)

   Si "STACK[-1]" es verdadero, incrementa el contador de bytecode en
   *delta*. Se elimina "STACK[-1]".

   Distinto en la versión 3.11: El oparg ahora es un delta relativo en
   lugar de un objetivo absoluto. Este código de operación es una
   pseudoinstrucción, reemplazada en el bytecode final por las
   versiones dirigidas (hacia adelante/hacia atrás).

   Distinto en la versión 3.12: Esto ya no es una pseudoinstrucción.

   Distinto en la versión 3.13: Esta instrucción ahora requiere un
   operando "bool" exacto.

POP_JUMP_IF_FALSE(delta)

   Si "STACK[-1]" es falso, incrementa el contador de bytecode en
   *delta*. Se elimina "STACK[-1]".

   Distinto en la versión 3.11: El oparg ahora es un delta relativo en
   lugar de un objetivo absoluto. Este código de operación es una
   pseudoinstrucción, reemplazada en el bytecode final por las
   versiones dirigidas (hacia adelante/hacia atrás).

   Distinto en la versión 3.12: Esto ya no es una pseudoinstrucción.

   Distinto en la versión 3.13: Esta instrucción ahora requiere un
   operando "bool" exacto.

POP_JUMP_IF_NOT_NONE(delta)

   Si "STACK[-1]" no es "None", incrementa el contador de bytecode en
   *delta*. Se elimina "STACK[-1]".

   Added in version 3.11.

   Distinto en la versión 3.12: Esto ya no es una pseudoinstrucción.

POP_JUMP_IF_NONE(delta)

   Si "STACK[-1]" es "None", incrementa el contador de bytecode en
   *delta*. Se elimina "STACK[-1]".

   Added in version 3.11.

   Distinto en la versión 3.12: Esto ya no es una pseudoinstrucción.

FOR_ITER(delta)

   "STACK[-1]" es un *iterator*. Llama a su método "__next__()". Si
   esto produce un nuevo valor, colócalo en la pila (dejando el
   iterador debajo de él). Si el iterador indica que está agotado, el
   contador de código de bytes se incrementa en *delta*.

   Distinto en la versión 3.12: Hasta la versión 3.11, el iterador se
   activaba cuando se agotaba.

LOAD_GLOBAL(namei)

   Carga el "co_names[namei>>1]" global llamado en la pila.

   Distinto en la versión 3.11: Si se establece el bit bajo de
   "namei", se agrega un "NULL" a la pila antes de la variable global.

LOAD_FAST(var_num)

   Apila una referencia al local "co_varnames[var_num]" sobre la pila.

   Distinto en la versión 3.12: Este código de operación ahora solo se
   utiliza en situaciones en las que se garantiza que la variable
   local se inicializará. No puede generar "UnboundLocalError".

LOAD_FAST_BORROW(var_num)

   Pushes a borrowed reference to the local "co_varnames[var_num]"
   onto the stack.

   Added in version 3.14.

LOAD_FAST_LOAD_FAST(var_nums)

   Pushes references to "co_varnames[var_nums >> 4]" and
   "co_varnames[var_nums & 15]" onto the stack.

   Added in version 3.13.

LOAD_FAST_BORROW_LOAD_FAST_BORROW(var_nums)

   Pushes borrowed references to "co_varnames[var_nums >> 4]" and
   "co_varnames[var_nums & 15]" onto the stack.

   Added in version 3.14.

LOAD_FAST_CHECK(var_num)

   Inserta una referencia al "co_varnames[var_num]" local en la pila y
   genera un "UnboundLocalError" si la variable local no se ha
   inicializado.

   Added in version 3.12.

LOAD_FAST_AND_CLEAR(var_num)

   Inserta una referencia al "co_varnames[var_num]" local en la pila
   (o inserta "NULL" en la pila si la variable local no se ha
   inicializado) y establece "co_varnames[var_num]" en "NULL".

   Added in version 3.12.

STORE_FAST(var_num)

   Almacena "STACK.pop()" en el "co_varnames[var_num]" local.

STORE_FAST_STORE_FAST(var_nums)

   Stores "STACK[-1]" into "co_varnames[var_nums >> 4]" and
   "STACK[-2]" into "co_varnames[var_nums & 15]".

   Added in version 3.13.

STORE_FAST_LOAD_FAST(var_nums)

   Stores "STACK.pop()" into the local "co_varnames[var_nums >> 4]"
   and pushes a reference to the local "co_varnames[var_nums & 15]"
   onto the stack.

   Added in version 3.13.

DELETE_FAST(var_num)

   Elimina la "co_varnames[var_num]" local.

MAKE_CELL(i)

   Crea una nueva celda en la ranura "i". Si esa ranura no está vacía,
   ese valor se almacena en la nueva celda.

   Added in version 3.11.

LOAD_DEREF(i)

   Carga la celda contenida en el slot "i" del almacenamiento "fast
   locals". Agrega una referencia al objeto que contiene la celda en
   la pila.

   Distinto en la versión 3.11: "i" ya no está compensado por la
   longitud de "co_varnames".

LOAD_FROM_DICT_OR_DEREF(i)

   Pops a mapping off the stack and looks up the name associated with
   slot "i" of the "fast locals" storage in this mapping. If the name
   is not found there, loads it from the cell contained in slot "i",
   similar to "LOAD_DEREF". This is used for loading *closure
   variables* in class bodies (which previously used
   "LOAD_CLASSDEREF") and in annotation scopes within class bodies.

   Added in version 3.12.

STORE_DEREF(i)

   Almacena "STACK.pop()" en la celda contenida en la ranura "i" del
   almacenamiento de "locales rápidos".

   Distinto en la versión 3.11: "i" ya no está compensado por la
   longitud de "co_varnames".

DELETE_DEREF(i)

   Vacía la celda contenida en la ranura "i" del almacenamiento de
   "locales rápidos". Utilizado por la instrucción "del".

   Added in version 3.2.

   Distinto en la versión 3.11: "i" ya no está compensado por la
   longitud de "co_varnames".

COPY_FREE_VARS(n)

   Copies the "n" *free (closure) variables* from the closure into the
   frame. Removes the need for special code on the caller's side when
   calling closures.

   Added in version 3.11.

RAISE_VARARGS(argc)

   Provoca una excepción utilizando una de las 3 formas de la
   declaración "raise", dependiendo del valor de *argc*:

   * 0: "raise" (vuelve a lanzar la excepción anterior)

   * 1: "raise STACK[-1]" (generar instancia o tipo de excepción en
     "STACK[-1]")

   * 2: "raise STACK[-2] from STACK[-1]" (generar una instancia o tipo
     de excepción en "STACK[-2]" con "__cause__" establecido en
     "STACK[-1]")

CALL(argc)

   Llama a un objeto invocable con la cantidad de argumentos
   especificados por "argc". En la pila se encuentran (en orden
   ascendente):

   * El llamable

   * "self" o "NULL"

   * Los argumentos posicionales restantes

   "argc" es el total de los argumentos posicionales, excluyendo
   "self".

   "CALL" extrae todos los argumentos y el objeto invocable de la
   pila, llama al objeto invocable con esos argumentos y agrega el
   valor retornado por el objeto invocable.

   Added in version 3.11.

   Distinto en la versión 3.13: El objeto invocable ahora siempre
   aparece en la misma posición en la pila.

   Distinto en la versión 3.13: Las llamadas con argumentos de
   palabras clave ahora son manejadas por "CALL_KW".

CALL_KW(argc)

   Llama a un objeto invocable con la cantidad de argumentos
   especificados por "argc", incluidos uno o más argumentos nombrados.
   En la pila se encuentran (en orden ascendente):

   * El llamable

   * "self" o "NULL"

   * Los argumentos posicionales restantes

   * Los argumentos nombrados

   * Un "tuple" de nombres de argumentos de palabras clave

   "argc" es el total de argumentos posicionales y nombrados, excluido
   "self". La longitud de la tupla de nombres de argumentos de
   palabras clave es la cantidad de argumentos nombrados.

   "CALL_KW" extrae todos los argumentos, los nombres de palabras
   clave y el objeto invocable de la pila, llama al objeto invocable
   con esos argumentos y envía el valor de retorno devuelto por el
   objeto invocable.

   Added in version 3.13.

CALL_FUNCTION_EX(flags)

   Llama a un objeto invocable con un conjunto variable de argumentos
   posicionales y de palabras clave. Si se establece el bit más bajo
   de *flags*, la parte superior de la pila contiene un objeto de
   mapeo que contiene argumentos de palabras clave adicionales. Antes
   de que se llame al invocable, el objeto de mapeo y el objeto
   iterable se "desempaquetan" y su contenido se pasa como palabra
   clave y argumentos posicionales, respectivamente.
   "CALL_FUNCTION_EX" saca todos los argumentos y el objeto invocable
   de la pila, llama al objeto invocable con esos argumentos y empuja
   el valor de retorno retornado por el objeto invocable.

   Added in version 3.6.

PUSH_NULL

   Pushes a "NULL" to the stack. Used in the call sequence to match
   the "NULL" pushed by "LOAD_METHOD" for non-method calls.

   Added in version 3.11.

MAKE_FUNCTION

   Pushes a new function object on the stack built from the code
   object at "STACK[-1]".

   Distinto en la versión 3.10: El valor indicador "0x04" es una tupla
   de cadena de caracteres en vez de un diccionario

   Distinto en la versión 3.11: Se eliminó el nombre calificado en
   "STACK[-1]".

   Distinto en la versión 3.13: Se eliminaron los atributos de
   funciones adicionales en la pila, señalados por indicadores oparg.
   Ahora utilizan "SET_FUNCTION_ATTRIBUTE".

SET_FUNCTION_ATTRIBUTE(flag)

   Establece un atributo en un objeto de función. Espera que la
   función esté en "STACK[-1]" y que el valor del atributo esté
   establecido en "STACK[-2]"; consume ambos y deja la función en
   "STACK[-1]". El indicador determina qué atributo se debe
   establecer:

   * "0x01", una tupla de valores predeterminados para solo parámetros
     posicionales y posicionales o de palabras clave en orden
     posicional

   * "0x02" un diccionario de valores predeterminados de solo palabras
     clave

   * "0x04" una tupla de cadenas de caracteres que contiene
     anotaciones de parámetros

   * "0x08" una tupla que contiene celdas para variables libres,
     haciendo un cierre (*closure*)

   * "0x10" the *annotate function* for the function object

   Added in version 3.13.

   Distinto en la versión 3.14: Added "0x10" to indicate the annotate
   function for the function object.

BUILD_SLICE(argc)

   Coloca un objeto de segmento en la pila. *argc* debe ser 2 o 3. Si
   es 2, implementa:

      end = STACK.pop()
      start = STACK.pop()
      STACK.append(slice(start, end))

   Si es 3, implementa:

      step = STACK.pop()
      end = STACK.pop()
      start = STACK.pop()
      STACK.append(slice(start, end, step))

   Consulte la función incorporada "slice()" para obtener más
   información.

EXTENDED_ARG(ext)

   Prefija cualquier código de operación que tenga un argumento
   demasiado grande para caber en el byte predeterminado. *ext*
   contiene un byte adicional que actúa como bits más altos en el
   argumento. Para cada opcode, como máximo se permiten tres prefijos
   "EXTENDED_ARG", formando un argumento de dos bytes a cuatro bytes.

CONVERT_VALUE(oparg)

   Convertir valor a cadena, dependiendo de "oparg":

      value = STACK.pop()
      result = func(value)
      STACK.append(result)

   * "oparg == 1": llama "str()" con *value*

   * "oparg == 2": llama "repr()" con *value*

   * "oparg == 3": llama "ascii()" con *value*

   Used for implementing formatted string literals (f-strings).

   Added in version 3.13.

FORMAT_SIMPLE

   Formatea el valor en la parte superior de la pila:

      value = STACK.pop()
      result = value.__format__("")
      STACK.append(result)

   Used for implementing formatted string literals (f-strings).

   Added in version 3.13.

FORMAT_WITH_SPEC

   Formatea el valor dado con la especificación de formato dada:

      spec = STACK.pop()
      value = STACK.pop()
      result = value.__format__(spec)
      STACK.append(result)

   Used for implementing formatted string literals (f-strings).

   Added in version 3.13.

MATCH_CLASS(count)

   "STACK[-1]" es una tupla de nombres de atributos de palabras clave,
   "STACK[-2]" es la clase con la que se realiza la comparación y
   "STACK[-3]" es el sujeto de la comparación. *count* es la cantidad
   de subpatrones posicionales.

   Inserte "STACK[-1]", "STACK[-2]" y "STACK[-3]". Si "STACK[-3]" es
   una instancia de "STACK[-2]" y tiene los atributos posicionales y
   de palabras clave requeridos por *count* y "STACK[-1]", inserte una
   tupla de atributos extraídos. De lo contrario, inserte "None".

   Added in version 3.10.

   Distinto en la versión 3.11: Anteriormente, esta instrucción
   también generaba un valor booleano que indicaba éxito ("True") o
   falla ("False").

RESUME(context)

   Un no-op. Realiza comprobaciones internas de seguimiento,
   depuración y optimización.

   The "context" operand consists of two parts. The lowest two bits
   indicate where the "RESUME" occurs:

   * "0" El inicio de una función, que no es un generador, ni una
     corrutina ni un generador asíncrono

   * "1" Después de una expresión "yield"

   * "2" Después de una expresión "yield from"

   * "3" Después de una expresión "await"

   El siguiente bit es "1" si RESUME está en la profundidad de
   excepción "1", y "0" en caso contrario.

   Added in version 3.11.

   Distinto en la versión 3.13: El valor de oparg cambió para incluir
   información sobre except-depth

RETURN_GENERATOR

   Crea un generador, una corrutina o un generador asincrónico a
   partir del marco actual. Se utiliza como primer código de operación
   del objeto de código para los elementos invocables mencionados
   anteriormente. Borra el marco actual y devuelve el generador recién
   creado.

   Added in version 3.11.

SEND(delta)

   Equivalente a "STACK[-1] = STACK[-2].send(STACK[-1])". Se utiliza
   en las instrucciones "yield from" y "await".

   Si la llamada genera "StopIteration", extrae el valor superior de
   la pila, inserta el atributo "value" de la excepción e incrementa
   el contador de bytecode en *delta*.

   Added in version 3.11.

HAVE_ARGUMENT

   En realidad, no se trata de un código de operación. Identifica la
   línea divisoria entre los códigos de operación en el rango [0,255]
   que no utilizan su argumento y los que sí lo hacen ("<
   HAVE_ARGUMENT" y ">= HAVE_ARGUMENT", respectivamente).

   Si su aplicación utiliza pseudoinstrucciones o instrucciones
   especializadas, utilice la colección "hasarg" en su lugar.

   Distinto en la versión 3.6: Ahora cada instrucción tiene un
   argumento, pero los códigos de operación "<HAVE_ARGUMENT" la
   ignoran. Antes, solo los códigos de operación "> = HAVE_ARGUMENT"
   tenían un argumento.

   Distinto en la versión 3.12: Pseudo instructions were added to the
   "dis" module, and for them it is not true that comparison with
   "HAVE_ARGUMENT" indicates whether they use their arg.

   Obsoleto desde la versión 3.13: Utilice "hasarg" en su lugar.

CALL_INTRINSIC_1

   Llama a una función intrínseca con un argumento. Pasa "STACK[-1]"
   como argumento y establece "STACK[-1]" como resultado. Se utiliza
   para implementar una funcionalidad que no es crítica para el
   rendimiento.

   El operando determina qué función intrínseca se llama:

   +-------------------------------------+-------------------------------------+
   | Operando                            | Descripción                         |
   |=====================================|=====================================|
   | "INTRINSIC_1_INVALID"               | No válido                           |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_PRINT"                   | Imprime el argumento en la salida   |
   |                                     | estándar. Se utiliza en REPL.       |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_IMPORT_STAR"             | Ejecuta "import *" para el módulo   |
   |                                     | nombrado.                           |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_STOPITERATION_ERROR"     | Extrae el valor de retorno de una   |
   |                                     | excepción "StopIteration".          |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_ASYNC_GEN_WRAP"          | Envuelve un valor de generador      |
   |                                     | asincrónico                         |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_UNARY_POSITIVE"          | Realiza la operación unaria "+"     |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_LIST_TO_TUPLE"           | Convierte una lista en una tupla    |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_TYPEVAR"                 | Crea un "typing.TypeVar"            |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_PARAMSPEC"               | Crea un "typing.ParamSpec"          |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_TYPEVARTUPLE"            | Crea un "typing.TypeVarTuple"       |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_SUBSCRIPT_GENERIC"       | Devuelve "typing.Generic" subíndice |
   |                                     | con el argumento                    |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_TYPEALIAS"               | Crea un "typing.TypeAliasType"; se  |
   |                                     | utiliza en la declaración "type".   |
   |                                     | El argumento es una tupla con el    |
   |                                     | nombre del alias de tipo, los       |
   |                                     | parámetros de tipo y el valor.      |
   +-------------------------------------+-------------------------------------+

   Added in version 3.12.

CALL_INTRINSIC_2

   Llama a una función intrínseca con dos argumentos. Se utiliza para
   implementar una funcionalidad que no es crítica para el
   rendimiento:

      arg2 = STACK.pop()
      arg1 = STACK.pop()
      result = intrinsic2(arg1, arg2)
      STACK.append(result)

   El operando determina qué función intrínseca se llama:

   +------------------------------------------+-------------------------------------+
   | Operando                                 | Descripción                         |
   |==========================================|=====================================|
   | "INTRINSIC_2_INVALID"                    | No válido                           |
   +------------------------------------------+-------------------------------------+
   | "INTRINSIC_PREP_RERAISE_STAR"            | Calcula el "ExceptionGroup" que se  |
   |                                          | debe aumentar desde un "try-        |
   |                                          | except*".                           |
   +------------------------------------------+-------------------------------------+
   | "INTRINSIC_TYPEVAR_WITH_BOUND"           | Crea un "typing.TypeVar" con un     |
   |                                          | límite.                             |
   +------------------------------------------+-------------------------------------+
   | "INTRINSIC_TYPEVAR_WITH_CONSTRAINTS"     | Crea un "typing.TypeVar" con        |
   |                                          | restricciones.                      |
   +------------------------------------------+-------------------------------------+
   | "INTRINSIC_SET_FUNCTION_TYPE_PARAMS"     | Establece el atributo               |
   |                                          | "__type_params__" de una función.   |
   +------------------------------------------+-------------------------------------+

   Added in version 3.12.

LOAD_SPECIAL

   Performs special method lookup on "STACK[-1]". If
   "type(STACK[-1]).__xxx__" is a method, leave
   "type(STACK[-1]).__xxx__; STACK[-1]" on the stack. If
   "type(STACK[-1]).__xxx__" is not a method, leave
   "STACK[-1].__xxx__; NULL" on the stack.

   Added in version 3.14.

**Pseudo-instrucciones**

Estos códigos de operación no aparecen en el código de bytes de
Python. El compilador los utiliza, pero se reemplazan por códigos de
operación reales o se eliminan antes de que se genere el código de
bytes.

SETUP_FINALLY(target)

   Configure un controlador de excepciones para el siguiente bloque de
   código. Si se produce una excepción, el nivel de pila de valores se
   restaura a su estado actual y el control se transfiere al
   controlador de excepciones en "target".

SETUP_CLEANUP(target)

   Como "SETUP_FINALLY", pero en caso de excepción también envía la
   última instrucción ("lasti") a la pila para que "RERAISE" pueda
   restaurarla. Si se produce una excepción, el nivel de pila de
   valores y la última instrucción del marco se restauran a su estado
   actual y el control se transfiere al controlador de excepciones en
   "target".

SETUP_WITH(target)

   Como "SETUP_CLEANUP", pero en caso de una excepción, se extrae un
   elemento más de la pila antes de que el control se transfiera al
   controlador de excepciones en "target".

   Esta variante se utiliza en las construcciones "with" y "async
   with", que envían el valor de retorno de "__enter__()" o
   "__aenter__()" del administrador de contexto a la pila.

POP_BLOCK

   Marca el final del bloque de código asociado con el último
   "SETUP_FINALLY", "SETUP_CLEANUP" o "SETUP_WITH".

LOAD_CONST_IMMORTAL(consti)

   Works as "LOAD_CONST", but is more efficient for immortal objects.

JUMP
JUMP_NO_INTERRUPT

   Instrucciones de salto relativo no dirigido que son reemplazadas
   por sus contrapartes dirigidas (hacia adelante/hacia atrás) por el
   ensamblador.

JUMP_IF_TRUE
JUMP_IF_FALSE

   Conditional jumps which do not impact the stack. Replaced by the
   sequence "COPY 1", "TO_BOOL", "POP_JUMP_IF_TRUE/FALSE".

LOAD_CLOSURE(i)

   Envía una referencia a la celda contenida en la ranura "i" del
   almacenamiento de "valores locales rápidos".

   Tenga en cuenta que "LOAD_CLOSURE" se reemplaza con "LOAD_FAST" en
   el ensamblador.

   Distinto en la versión 3.13: Este código de operación ahora es una
   pseudoinstrucción.

## Colecciones opcode

Estas colecciones se proporcionan para la introspección automática de
instrucciones de bytecode:

Distinto en la versión 3.12: Las colecciones ahora también contienen
pseudoinstrucciones e instrucciones instrumentadas. Se trata de
códigos de operación con valores ">= MIN_PSEUDO_OPCODE" y ">=
MIN_INSTRUMENTED_OPCODE".

dis.opname

   Secuencia de nombres de operaciones, indexable utilizando el
   bytecode.

dis.opmap

   Nombres de operaciones de mapeo de diccionario a bytecodes.

dis.cmp_op

   Secuencia de todos los nombres de operaciones de comparación.

dis.hasarg

   Secuencia de códigos de bytes que utilizan su argumento.

   Added in version 3.12.

dis.hasconst

   Secuencia de bytecodes que acceden a una constante.

dis.hasfree

   Sequence of bytecodes that access a *free (closure) variable*.
   'free' in this context refers to names in the current scope that
   are referenced by inner scopes or names in outer scopes that are
   referenced from this scope.  It does *not* include references to
   global or builtin scopes.

dis.hasname

   Secuencia de bytecodes que acceden a un atributo por nombre.

dis.hasjump

   Secuencia de códigos de bytes que tienen un destino de salto. Todos
   los saltos son relativos.

   Added in version 3.13.

dis.haslocal

   Secuencia de códigos de bytes que acceden a una variable local.

dis.hascompare

   Secuencia de bytecodes de operaciones booleanas.

dis.hasexc

   Secuencia de códigos de bytes que establecen un controlador de
   excepciones.

   Added in version 3.12.

dis.hasjrel

   Secuencia de bytecodes que tienen un objetivo de salto relativo.

   Obsoleto desde la versión 3.13: Ahora todos los saltos son
   relativos. Utilice "hasjump".

dis.hasjabs

   Secuencia de bytecodes que tienen un objetivo de salto absoluto.

   Obsoleto desde la versión 3.13: Ahora todos los saltos son
   relativos. Esta lista está vacía.
