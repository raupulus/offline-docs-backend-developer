---
title: Los perfiladores de Python
source_url: https://docs.python.org/es/3
source_path: library/profile.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3530
---

# Los perfiladores de Python

**Código fuente:** Lib/profile.py y Lib/pstats.py

======================================================================

## Introducción a los perfiladores

"cProfile" y "profile" proporcionan *deterministic profiling* de los
programas de Python. *profile* es un conjunto de estadísticas que
describe con qué frecuencia y durante cuánto tiempo se ejecutaron
varias partes del programa. Estas estadísticas pueden formatearse en
informes a través del módulo "pstats".

La biblioteca estándar de Python proporciona dos implementaciones
diferentes de la misma interfaz de creación de perfiles:

1. "cProfile" se recomienda para la mayoría de los usuarios; Es una
   extensión C con una sobrecarga razonable que la hace adecuada para
   perfilar programas de larga duración. Basado en "lsprof", aportado
   por Brett Rosen y Ted Czotter.

2. "profile", un módulo Python puro cuya interfaz es imitada por
   "cProfile", pero que agrega una sobrecarga significativa a los
   programas perfilados. Si está intentando extender el generador de
   perfiles de alguna manera, la tarea podría ser más fácil con este
   módulo. Originalmente diseñado y escrito por Jim Roskind.

Nota:

  Los módulos del generador de perfiles están diseñados para
  proporcionar un perfil de ejecución para un programa determinado, no
  para fines de evaluación comparativa (para eso, está "timeit" que
  permite obtener resultados razonablemente precisos). Esto se aplica
  particularmente a la evaluación comparativa del código Python contra
  el código C: los perfiladores introducen gastos generales para el
  código Python, pero no para las funciones de nivel C, por lo que el
  código C parecería más rápido que cualquier Python.

## Manual instantáneo de usuario

Esta sección se proporciona a los usuarios que "no quieren leer el
manual". Proporciona una visión general muy breve y permite a un
usuario realizar perfiles rápidamente en una aplicación existente.

Para perfilar una función que toma un solo argumento, puede hacer:

   import cProfile
   import re
   cProfile.run('re.compile("foo|bar")')

(Use "profile" en lugar de "cProfile" si este último no está
disponible en su sistema.)

La acción anterior ejecutaría "re.compile()" e imprime resultados de
perfil como los siguientes:

         214 function calls (207 primitive calls) in 0.002 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 __init__.py:250(compile)
        1    0.000    0.000    0.001    0.001 __init__.py:289(_compile)
        1    0.000    0.000    0.000    0.000 _compiler.py:759(compile)
        1    0.000    0.000    0.000    0.000 _parser.py:937(parse)
        1    0.000    0.000    0.000    0.000 _compiler.py:598(_code)
        1    0.000    0.000    0.000    0.000 _parser.py:435(_parse_sub)

The first line indicates that 214 calls were monitored.  Of those
calls, 207 were *primitive*, meaning that the call was not induced via
recursion. The next line: "Ordered by: cumulative time" indicates the
output is sorted by the "cumtime" values. The column headings include:

ncalls
   por el número de llamadas.

tottime
   para el tiempo total empleado en la función dada (y excluyendo el
   tiempo realizado en llamadas a subfunciones)

percall
   es el cociente de "tottime" dividido por "ncalls"

cumtime
   es el tiempo acumulado empleado en esta y todas las subfunciones
   (desde la invocación hasta la salida). Esta cifra es precisa
   *incluso* para funciones recursivas.

percall
   es el cociente de "cumtime" dividido por llamadas primitivas

filename:lineno(function)
   proporciona los datos respectivos de cada función

Cuando hay dos números en la primera columna (por ejemplo, "3/1"),
significa que la función se repite. El segundo valor es el número de
llamadas primitivas y el primero es el número total de llamadas. Tenga
en cuenta que cuando la función no se repite, estos dos valores son
iguales y solo se imprime la figura.

En lugar de imprimir la salida al final de la ejecución del perfil,
puede guardar los resultados en un archivo especificando un nombre de
archivo en la función "run()":

   import cProfile
   import re
   cProfile.run('re.compile("foo|bar")', 'restats')

La clase "pstats.Stats" lee los resultados del perfil desde un archivo
y los formatea de varias maneras.

Los archivos "cProfile" y "profile" también se pueden invocar como un
script para perfilar otro script. Por ejemplo:

   python -m cProfile [-o output_file] [-s sort_order] (-m module | myscript.py)

-o <output_file>

   Writes the profile results to a file instead of to stdout.

-s <sort_order>

   Specifies one of the "sort_stats()" sort values to sort the output
   by. This only applies when "-o" is not supplied.

-m <module>

   Specifies that a module is being profiled instead of a script.

   Added in version 3.7: Se agregó la opción "-m" a "cProfile".

   Added in version 3.8: Se agregó la opción "-m" a "profile".

Los módulos "pstats" clase "Stats" tienen una variedad de métodos para
manipular e imprimir los datos guardados en un archivo de resultados
de perfil:

   import pstats
   from pstats import SortKey
   p = pstats.Stats('restats')
   p.strip_dirs().sort_stats(-1).print_stats()

El método "strip_dirs()" eliminó la ruta extraña de todos los nombres
de módulos. El método "sort_stats()" clasificó todas las entradas de
acuerdo con el módulo/línea/nombre de cadena de caracteres estándar
que se imprime. El método "print_stats()" imprimió todas las
estadísticas. Puede intentar las siguientes llamadas de clasificación:

   p.sort_stats(SortKey.NAME)
   p.print_stats()

La primera llamada realmente ordenará la lista por nombre de función,
y la segunda llamada imprimirá las estadísticas. Las siguientes son
algunas llamadas interesantes para experimentar:

   p.sort_stats(SortKey.CUMULATIVE).print_stats(10)

Esto ordena el perfil por tiempo acumulado en una función y luego solo
imprime las diez líneas más significativas. Si desea comprender qué
algoritmos están tomando tiempo, la línea anterior es lo que usaría.

Si estuviera buscando ver qué funciones se repetían mucho y toman
mucho tiempo, usted haría:

   p.sort_stats(SortKey.TIME).print_stats(10)

para ordenar según el tiempo dedicado a cada función y luego imprimir
las estadísticas de las diez funciones principales.

También puedes probar:

   p.sort_stats(SortKey.FILENAME).print_stats('__init__')

Esto ordenará todas las estadísticas por nombre de archivo y luego
imprimirá estadísticas solo para los métodos de inicio de clase (ya
que están escritos con "__init__" en ellos). Como último ejemplo,
puedes probar:

   p.sort_stats(SortKey.TIME, SortKey.CUMULATIVE).print_stats(.5, 'init')

Esta línea clasifica las estadísticas con una clave primaria de tiempo
y una clave secundaria de tiempo acumulado, y luego imprime algunas de
las estadísticas. Para ser específicos, la lista primero se reduce al
50% (re: ".5") de su tamaño original, luego solo se mantienen las
líneas que contienen "`init" y se imprime esa sub-sublista.

Si se preguntó qué funciones denominaban las funciones anteriores,
ahora podría ("p" todavía está ordenada según el último criterio)
hacer:

   p.print_callers(.5, 'init')

y obtendría una lista de llamadas para cada una de las funciones
enumeradas.

Si desea más funcionalidad, tendrá que leer el manual o adivinar lo
que hacen las siguientes funciones:

   p.print_callees()
   p.add('restats')

Invocado como un script, el módulo "pstats" es un navegador de
estadísticas para leer y examinar volcados de perfil. Tiene una
interfaz simple orientada a la línea de comandos (implementada usando
"cmd") y ayuda interactiva.

## "profile" and "cProfile" Module Reference

Both the "profile" and "cProfile" modules provide the following
functions:

profile.run(command, filename=None, sort=-1)

   Esta función toma un único argumento que se puede pasar a la
   función "exec()" y un nombre de archivo opcional. En todos los
   casos esta rutina ejecuta:

      exec(command, __main__.__dict__, __main__.__dict__)

   y recopila estadísticas de perfiles de la ejecución. Si no hay
   ningún nombre de archivo, esta función crea automáticamente una
   instancia de "Stats" e imprime un informe de perfil simple. Si se
   especifica el valor de clasificación, se pasa a esta instancia
   "Stats" para controlar cómo se ordenan los resultados.

profile.runctx(command, globals, locals, filename=None, sort=-1)

   This function is similar to "run()", with added arguments to supply
   the globals and locals mappings for the *command* string. This
   routine executes:

      exec(command, globals, locals)

   y recopila estadísticas de perfiles como en la función "run()"
   anterior.

class profile.Profile(timer=None, timeunit=0.0, subcalls=True, builtins=True)

   Esta clase normalmente solo es usada si se necesita un control más
   preciso sobre la creación de perfiles que el que proporciona la
   función "cProfile.run()".

   Se puede suministrar un temporizador personalizado para medir
   cuánto tiempo tarda el código en ejecutarse mediante el argumento
   *timer*. Esta debe ser una función que retorna un solo número que
   representa la hora actual. Si el número es un entero, la *timeunit*
   especifica un multiplicador que especifica la duración de cada
   unidad de tiempo. Por ejemplo, si el temporizador retorna tiempos
   medidos en miles de segundos, la unidad de tiempo sería ".001".

   El uso directo de la clase "Profile" permite formatear los
   resultados del perfil sin escribir los datos del perfil en un
   archivo:

      import cProfile, pstats, io
      from pstats import SortKey
      pr = cProfile.Profile()
      pr.enable()
      # ... do something ...
      pr.disable()
      s = io.StringIO()
      sortby = SortKey.CUMULATIVE
      ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
      ps.print_stats()
      print(s.getvalue())

   The "Profile" class can also be used as a context manager
   (supported only in "cProfile" module. see Tipos gestores de
   contexto):

      import cProfile

      with cProfile.Profile() as pr:
          # ... do something ...

          pr.print_stats()

   Distinto en la versión 3.8: Se agregó soporte de administrador de
   contexto.

   enable()

      Start collecting profiling data. Only in "cProfile".

   disable()

      Stop collecting profiling data. Only in "cProfile".

   create_stats()

      Deja de recopilar datos de perfiles y registre los resultados
      internamente como el perfil actual.

   print_stats(sort=-1)

      Crea un objeto "Stats" en función del perfil actual e imprima
      los resultados en *stdout*.

      The *sort* parameter specifies the sorting order of the
      displayed statistics. It accepts a single key or a tuple of keys
      to enable multi-level sorting, as in "Stats.sort_stats".

      Added in version 3.13: "print_stats()" now accepts a tuple of
      keys.

   dump_stats(filename)

      Escribe los resultados del perfil actual en *filename*.

   run(cmd)

      Perfila el cmd a través de "exec()".

   runctx(cmd, globals, locals)

      Perfila el cmd a través de "exec()" con el entorno global y
      local especificado.

   runcall(func, /, *args, **kwargs)

      Perfila "func(*args, **kwargs)"

Tenga en cuenta que la creación de perfiles solo funcionará si el
comando/función llamado realmente regresa. Si el intérprete se termina
(por ejemplo, a través de una llamada a "sys.exit()" durante la
ejecución del comando/función llamado) no se imprimirán resultados de
generación de perfiles.

## La clase "Stats"

El análisis de los datos del generador de perfiles es realizado
utilizando la clase "Stats".

class pstats.Stats(*filenames or profile, stream=sys.stdout)

   Este constructor de clase crea una instancia de un "objeto de
   estadísticas" a partir de un *filename* (o una lista de nombres de
   archivo) o de una instancia "Profile". La salida se imprimirá en la
   secuencia especificada por *stream*.

   El archivo seleccionado por el constructor anterior debe haber sido
   creado por la versión correspondiente de "profile" o "cProfile".
   Para ser específicos, *no* hay compatibilidad de archivos
   garantizada con futuras versiones de este generador de perfiles, y
   no hay compatibilidad con archivos producidos por otros
   perfiladores, o el mismo generador de perfiles ejecutado en un
   sistema operativo diferente. Si se proporcionan varios archivos, se
   combinarán todas las estadísticas para funciones idénticas, de modo
   que se pueda considerar una vista general de varios procesos en un
   solo informe. Si es necesario combinar archivos adicionales con
   datos en un objeto existente "Stats", se puede usar el método
   "add()".

   En lugar de leer los datos del perfil de un archivo, se puede usar
   un objeto "cProfile.Profile" o "profile.Profile" como fuente de
   datos del perfil.

   los objetos "Stats" tienen los siguientes métodos:

   strip_dirs()

      Este método para la clase "Stats" elimina toda la información de
      ruta principal de los nombres de archivo. Es muy útil para
      reducir el tamaño de la impresión para que quepa en (cerca de)
      80 columnas. Este método modifica el objeto y se pierde la
      información eliminada. Después de realizar una operación de
      tira, se considera que el objeto tiene sus entradas en un orden
      "aleatorio", como lo fue justo después de la inicialización y
      carga del objeto. Si "strip_dirs()" hace que dos nombres de
      funciones no se puedan distinguir (están en la misma línea del
      mismo nombre de archivo y tienen el mismo nombre de función),
      entonces las estadísticas para estas dos entradas se acumulan en
      un sola entrada.

   add(*filenames)

      Este método de la clase "Stats" acumula información de perfil
      adicional en el objeto de perfil actual. Sus argumentos deben
      referirse a los nombres de archivo creados por la versión
      correspondiente de "profile.run()" or "cProfile.run()". Las
      estadísticas para funciones con nombre idéntico (re: archivo,
      línea, nombre) se acumulan automáticamente en estadísticas de
      función única.

   dump_stats(filename)

      Guarda los datos cargados en el objeto "Stats" en un archivo
      llamado *filename*. El archivo se crea si no existe y se
      sobrescribe si ya existe. Esto es equivalente al método del
      mismo nombre en las clases: class "profile.Profile" y
      "cProfile.Profile".

   sort_stats(*keys)

      Este método modifica el objeto "Stats" ordenándolo de acuerdo
      con los criterios proporcionados. El argumento puede ser una
      cadena de caracteres o una enumeración SortKey que identifica la
      base de una clasificación (ejemplo: "'time'", "'name'",
      "SortKey.TIME" o "SortKey.NAME"). El argumento enumeraciones
      SortKey tiene ventaja sobre el argumento de cadena de caracteres
      en que es más robusto y menos propenso a errores.

      Cuando se proporciona más de una llave, se utilizan llaves
      adicionales como criterios secundarios cuando hay igualdad en
      todas las llaves seleccionadas antes que ellas. Por ejemplo,
      "sort_stats(SortKey.NAME, SortKey.FILE)" ordenará todas las
      entradas de acuerdo con el nombre de su función y resolverá
      todos los vínculos (nombres de función idénticos)
      clasificándolos por nombre de archivo.

      Para el argumento de cadena de caracteres, se pueden usar
      abreviaturas para cualquier nombre de llaves, siempre que la
      abreviatura no sea ambigua.

      Los siguientes son la cadena de caracteres válida y SortKey:

      +--------------------+-----------------------+------------------------+
      | Arg de cadena de   | Arg de enumeración    | Significado            |
      | caracteres válido  | válido                |                        |
      |====================|=======================|========================|
      | "'calls'"          | SortKey.CALLS         | recuento de llamadas   |
      +--------------------+-----------------------+------------------------+
      | "'cumulative'"     | SortKey.CUMULATIVE    | tiempo acumulado       |
      +--------------------+-----------------------+------------------------+
      | "'cumtime'"        | N/A                   | tiempo acumulado       |
      +--------------------+-----------------------+------------------------+
      | "'file'"           | N/A                   | nombre de archivo      |
      +--------------------+-----------------------+------------------------+
      | "'filename'"       | SortKey.FILENAME      | nombre de archivo      |
      +--------------------+-----------------------+------------------------+
      | "'module'"         | N/A                   | nombre de archivo      |
      +--------------------+-----------------------+------------------------+
      | "'ncalls'"         | N/A                   | recuento de llamadas   |
      +--------------------+-----------------------+------------------------+
      | "'pcalls'"         | SortKey.PCALLS        | recuento de llamadas   |
      |                    |                       | primitivas             |
      +--------------------+-----------------------+------------------------+
      | "'line'"           | SortKey.LINE          | número de línea        |
      +--------------------+-----------------------+------------------------+
      | "'name'"           | SortKey.NAME          | nombre de la función   |
      +--------------------+-----------------------+------------------------+
      | "'nfl'"            | SortKey.NFL           | nombre/archivo/línea   |
      +--------------------+-----------------------+------------------------+
      | "'stdname'"        | SortKey.STDNAME       | nombre estándar        |
      +--------------------+-----------------------+------------------------+
      | "'time'"           | SortKey.TIME          | tiempo interno         |
      +--------------------+-----------------------+------------------------+
      | "'tottime'"        | N/A                   | tiempo interno         |
      +--------------------+-----------------------+------------------------+

      Tenga en cuenta que todos los tipos de estadísticas están en
      orden descendente (colocando primero los elementos que requieren
      más tiempo), donde las búsquedas de nombre, archivo y número de
      línea están en orden ascendente (alfabético). La sutil
      distinción entre "SortKey.NFL" y "SortKey.STDNAME" es que el
      nombre estándar es una especie de nombre tal como está impreso,
      lo que significa que los números de línea incrustados se
      comparan de manera extraña. Por ejemplo, las líneas 3, 20 y 40
      aparecerían (si los nombres de los archivos fueran los mismos)
      en el orden de las cadenas 20, 3 y 40. En contraste,
      "SortKey.NFL" hace una comparación numérica de los números de
      línea. De hecho, "sort_stats(SortKey.NFL)" es lo mismo que
      "sort_stats(SortKey.NAME, SortKey.FILENAME, SortKey.LINE)".

      Por razones de compatibilidad con versiones anteriores, se
      permiten los argumentos numéricos "-1", "0", "1", y "2". Se
      interpretan como "'stdname'", "'calls'", "'time'", y
      "'cumulative'" respectivamente. Si se usa este formato de estilo
      antiguo (numérico), solo se usará una clave de clasificación (la
      tecla numérica) y los argumentos adicionales se ignorarán en
      silencio.

      Added in version 3.7: Enumeración SortKey añadida.

   reverse_order()

      Este método para la clase "Stats" invierte el orden de la lista
      básica dentro del objeto. Tenga en cuenta que, de forma
      predeterminada, el orden ascendente vs descendente se selecciona
      correctamente en función de la llave de clasificación elegida.

   print_stats(*restrictions)

      Este método para la clase "Stats" imprime un informe como se
      describe en la definición "profile.run()".

      El orden de la impresión se basa en la última operación
      "sort_stats()" realizada en el objeto (sujeto a advertencias en
      "add()" y "strip_dirs()").

      The arguments provided (if any) can be used to limit the list
      down to the significant entries.  Initially, the list is taken
      to be the complete set of profiled functions.  Each restriction
      is either an integer (to select a count of lines), or a decimal
      fraction between 0.0 and 1.0 inclusive (to select a percentage
      of lines), or a string that will be interpreted as a regular
      expression (to pattern match the standard name that is printed).
      If several restrictions are provided, then they are applied
      sequentially. For example:

         print_stats(.1, 'foo:')

      primero limitaría la impresión al primer 10% de la lista, y
      luego solo imprimiría las funciones que formaban parte del
      nombre del archivo ".*foo:". En contraste, el comando:

         print_stats('foo:', .1)

      limitaría la lista a todas las funciones que tengan nombres de
      archivo: archivo ".*foo:", y luego procedería a imprimir solo el
      primer 10% de ellas.

   print_callers(*restrictions)

      Este método para la clase "Stats" imprime una lista de todas las
      funciones que llamaron a cada función en la base de datos
      perfilada. El orden es idéntico al proporcionado por
      "print_stats()", y la definición del argumento de restricción
      también es idéntica. Cada persona que llama se informa en su
      propia línea. El formato difiere ligeramente según el generador
      de perfiles que produjo las estadísticas:

      * Con "profile", se muestra un número entre paréntesis después
        de cada llamada para mostrar cuántas veces se realizó esta
        llamada específica. Por conveniencia, un segundo número sin
        paréntesis repite el tiempo acumulado empleado en la función
        de la derecha.

      * Con "cProfile", cada persona que llama está precedida por tres
        números: la cantidad de veces que se realizó esta llamada
        específica y los tiempos totales y acumulativos gastados en la
        función actual mientras fue invocada por esta persona que
        llama.

   print_callees(*restrictions)

      Este método para la clase "Stats" imprime una lista de todas las
      funciones que fueron llamadas por la función indicada. Aparte de
      esta inversión de la dirección de las llamadas (re: llamado vs
      fue llamado por), los argumentos y el orden son idénticos al
      método "print_callers()".

   get_stats_profile()

      Este método retorna una instancia de StatsProfile, la cual
      contiene un mapeo de nombres de función a instancias de
      FunctionProfile. Cada instancia de FunctionProfile mantiene
      información relacionada al perfil de la función, como cuánto
      demoró la función en ejecutarse, cuantas veces fue llamada,
      etc...

      Added in version 3.9: Añadidas las siguientes clases de datos:
      StatsProfile, FunctionProfile. Añadida la siguiente función:
      get_stats_profile.

## ¿Qué es el perfil determinista?

*Deterministic profiling* está destinada a reflejar el hecho de que se
supervisan todos los eventos *function call*, *function return*, y
*exception*, y se realizan temporizaciones precisas para los
intervalos entre estos eventos (durante los cuales el código del
usuario se está ejecutando). Por el contrario, *statistical profiling*
(que no se realiza en este módulo) muestrea aleatoriamente el puntero
de instrucción efectivo y deduce dónde se está gastando el tiempo. La
última técnica tradicionalmente implica menos sobrecarga (ya que el
código no necesita ser instrumentado), pero proporciona solo
indicaciones relativas de dónde se está gastando el tiempo.

En Python, dado que hay un intérprete activo durante la ejecución, no
se requiere la presencia de código instrumentado para realizar un
perfil determinista. Python proporciona automáticamente un *hook*
(retrollamada  opcional) para cada evento. Además, la naturaleza
interpretada de Python tiende a agregar tanta sobrecarga a la
ejecución, que los perfiles deterministas tienden a agregar solo una
pequeña sobrecarga de procesamiento en aplicaciones típicas. El
resultado es que el perfil determinista no es tan costoso, pero
proporciona estadísticas extensas de tiempo de ejecución sobre la
ejecución de un programa Python.

Las estadísticas de recuento de llamadas se pueden usar para
identificar errores en el código (recuentos sorprendentes) e
identificar posibles puntos de expansión en línea (recuentos altos de
llamadas). Las estadísticas de tiempo interno se pueden utilizar para
identificar "bucles activos" que deben optimizarse cuidadosamente. Las
estadísticas de tiempo acumulativo deben usarse para identificar
errores de alto nivel en la selección de algoritmos. Tenga en cuenta
que el manejo inusual de los tiempos acumulativos en este generador de
perfiles permite que las estadísticas de implementaciones recursivas
de algoritmos se comparen directamente con implementaciones
iterativas.

## Limitaciones

Una limitación tiene que ver con la precisión de la información de
sincronización. Hay un problema fundamental con los perfiladores
deterministas que implican precisión. La restricción más obvia es que
el "reloj" subyacente solo funciona a una velocidad (típicamente) de
aproximadamente 0,001 segundos. Por lo tanto, ninguna medición será
más precisa que el reloj subyacente. Si se toman suficientes medidas,
entonces el "error" tenderá a promediar. Desafortunadamente, eliminar
este primer error induce una segunda fuente de error.

El segundo problema es que "lleva un tiempo" desde que se distribuye
un evento hasta que la llamada del generador de perfiles para obtener
la hora en realidad *obtiene* el estado del reloj. Del mismo modo, hay
un cierto retraso al salir del controlador de eventos del generador de
perfiles desde el momento en que se obtuvo el valor del reloj (y luego
se retiró), hasta que el código del usuario se está ejecutando
nuevamente. Como resultado, las funciones que se llaman muchas veces,
o llaman a muchas funciones, generalmente acumularán este error. El
error que se acumula de esta manera es típicamente menor que la
precisión del reloj (menos de un tic de reloj), pero *puede*
acumularse y volverse muy significativo.

El problema es más importante con "profile" que con la sobrecarga
inferior "cProfile". Por esta razón, "profile" proporciona un medio
para calibrarse a sí mismo para una plataforma dada para que este
error pueda ser eliminado probabilísticamente (en promedio). Después
de calibrar el generador de perfiles, será más preciso (en un sentido
al menos cuadrado), pero a veces producirá números negativos (cuando
el recuento de llamadas es excepcionalmente bajo y los dioses de la
probabilidad trabajan en su contra :-) ) *No* se alarme por los
números negativos en el perfil. Deberían aparecer *solo* si ha
calibrado su generador de perfiles, y los resultados son realmente
mejores que sin calibración.

## Calibración

El generador de perfiles del módulo "profile" resta una constante de
cada tiempo de manejo de eventos para compensar la sobrecarga de
llamar a la función de tiempo y eliminar los resultados. Por defecto,
la constante es 0. El siguiente procedimiento se puede usar para
obtener una mejor constante para una plataforma dada (ver
Limitaciones).

   import profile
   pr = profile.Profile()
   for i in range(5):
       print(pr.calibrate(10000))

El método ejecuta la cantidad de llamadas de Python dadas por el
argumento, directamente y nuevamente bajo el generador de perfiles,
midiendo el tiempo para ambos. Luego, calcula la sobrecarga oculta por
evento del generador de perfiles y la retorna como un valor flotante.
Por ejemplo, en un Intel Core i5 de 1.8Ghz que ejecuta macOS y usa el
time.process_time () de Python como temporizador, el número mágico es
aproximadamente 4.04e-6.

El objetivo de este ejercicio es obtener un resultado bastante
consistente. Si su computadora es *muy* rápida, o su función de
temporizador tiene una resolución pobre, es posible que tenga que
pasar 100000, o incluso 1000000, para obtener resultados consistentes.

Cuando tiene una respuesta consistente, hay tres formas de usarla:

   import profile

   # 1. Apply computed bias to all Profile instances created hereafter.
   profile.Profile.bias = your_computed_bias

   # 2. Apply computed bias to a specific Profile instance.
   pr = profile.Profile()
   pr.bias = your_computed_bias

   # 3. Specify computed bias in instance constructor.
   pr = profile.Profile(bias=your_computed_bias)

Si tiene una opción, es mejor que elija una constante más pequeña, y
luego sus resultados "con menos frecuencia" se mostrarán como
negativos en las estadísticas del perfil.

## Usando un temporizador personalizado

Si desea cambiar la forma en que se determina el tiempo actual (por
ejemplo, para forzar el uso del tiempo del reloj de pared o el tiempo
transcurrido del proceso), pase la función de temporización que desee
a la clase constructora "Profile":

   pr = profile.Profile(your_time_func)

El generador de perfiles resultante llamará a "your_time_func".
Dependiendo de si está utilizando "profile.Profile" o
"cProfile.Profile", el valor de retorno de "your_time_func" se
interpretará de manera diferente:

"profile.Profile"
   "your_time_func" debería retornar un solo número o una lista de
   números cuya suma es la hora actual (como lo que "os.times()"
   retorna). Si la función retorna un número de tiempo único o la
   lista de números retornados tiene una longitud de 2, obtendrá una
   versión especialmente rápida de la rutina de envío.

   Be warned that you should calibrate the profiler class for the
   timer function that you choose (see Calibración).  For most
   machines, a timer that returns a lone integer value will provide
   the best results in terms of low overhead during profiling.
   ("os.times()" is *pretty* bad, as it returns a tuple of floating-
   point values).  If you want to substitute a better timer in the
   cleanest fashion, derive a class and hardwire a replacement
   dispatch method that best handles your timer call, along with the
   appropriate calibration constant.

"cProfile.Profile"
   "your_time_func" debería retornar un solo número. Si retorna
   enteros, también puede invocar al constructor de la clase con un
   segundo argumento que especifique la duración real de una unidad de
   tiempo. Por ejemplo, si "your_integer_time_func" retorna tiempos
   medidos en miles de segundos, construiría la instancia "Profile" de
   la siguiente manera:

      pr = cProfile.Profile(your_integer_time_func, 0.001)

   As the "cProfile.Profile" class cannot be calibrated, custom timer
   functions should be used with care and should be as fast as
   possible.  For the best results with a custom timer, it might be
   necessary to hard-code it in the C source of the internal "_lsprof"
   module.

Python 3.3 agrega varias funciones nuevas en "time" que se puede usar
para realizar mediciones precisas del proceso o el tiempo del reloj de
pared (*wall-clock time*). Por ejemplo, vea "time.perf_counter()".
