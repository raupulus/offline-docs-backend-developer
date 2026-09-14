---
title: '"difflib" --- Helpers for computing deltas'
source_url: https://docs.python.org/es/3
source_path: library/difflib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2330
---

# "difflib" --- Helpers for computing deltas

**Código fuente:** Lib/difflib.py

======================================================================

This module provides classes and functions for comparing sequences.
Most of them compare sequences of text lines (for example lists of
strings, or *file objects*) and produce *diffs* -- reports on the
differences. Diffs can be produced in in various formats, including
HTML and context and unified diffs -- formats produced by tools like
*diff* and *git diff*.

Comparisons are done using a matching algorithm implemented in
"SequenceMatcher" -- a flexible class for comparing pairs of sequences
of any type, not just text, so long as the sequence elements are
*hashable*.

## Junk heuristic

"difflib" uses a *junk* heuristic: some items are deemed to be *junk*,
and ignored when searching for similarities. Ideally, these are
uninteresting or common items, such as blank lines or whitespace.

This heuristic can speed the algorithm up (because it reduces the
number of possible combinations) and it can produce results that are
more understandable for humans (typically breaking on whitespace). But
it can also cause pathological cases:

* Inappropriately chosen junk items can cause an unexpectedly
  **large** (but still correct) result.

* The default heuristic is **asymmetric**: only the second sequence is
  inspected when determining what is considered junk, so comparing A
  to B can give different results than comparing B to A and reversing
  the result.

By default, if the second input sequence is at least 200 items long,
items that account for more than 1% it are considered *junk*.

Depending on your data, you should consider turning this heuristic off
(setting "SequenceMatcher"'s *autojunk* argument to  to "False") or
tuning it (using the *isjunk* argument, perhaps to one of the
predefined functions).

## The "difflib" algorithm

The algorithm used in "SequenceMatcher" predates, and is a little
fancier than, an algorithm published in the late 1980s by Ratcliff and
Obershelp under the hyperbolic name "gestalt pattern matching." The
idea is to find the longest contiguous subsequence common to both
inputs, then recursively handle the pieces of the sequences to the
left and to the right of the matching subsequence.

Ver también:

  Pattern Matching: The Gestalt Approach
     Discussion of a similar algorithm by John W. Ratcliff and D. E.
     Metzener. This was published in Dr. Dobb's Journal in July, 1988.

As an extension to the Ratcliff and Obershelp algorithm, "difflib"
searches for the longest *junk-free* contiguous subsequence. See the
Junk heuristic section for details.

**Detalles de implementación de CPython:** Timing

The basic Ratcliff-Obershelp algorithm is cubic time in the worst case
and quadratic time in the expected case. "difflib"'s algorithm is
quadratic time for the worst case and has expected-case behavior
dependent in a complicated way on how many elements the sequences have
in common; best case time is linear.

## Diff generation

class difflib.Differ

   Esta clase se utiliza para comparar secuencias de lineas de texto y
   producir diferencias o deltas en una forma legible por humanos.
   Differ usa "SequenceMatcher" tanto para comparar secuencias de
   lineas, como para comparar secuencias de caracteres entre lineas
   similares.

   Cada linea de un delta de "Differ" comienza con un código de dos
   letras:

   +------------+---------------------------------------------+
   | Código     | Significado                                 |
   |============|=============================================|
   | "'- '"     | línea única para la secuencia 1             |
   +------------+---------------------------------------------+
   | "'+ '"     | línea única para la secuencia 2             |
   +------------+---------------------------------------------+
   | "'  '"     | línea común a ambas secuencias              |
   +------------+---------------------------------------------+
   | "'? '"     | línea ausente en todas las secuencias de    |
   |            | entrada                                     |
   +------------+---------------------------------------------+

   Lines beginning with '"?"' attempt to guide the eye to intraline
   differences, and were not present in either input sequence. These
   lines can be confusing if the sequences contain whitespace
   characters, such as spaces, tabs or line breaks.

   Note that "Differ"-generated deltas make no claim to be **minimal**
   diffs. To the contrary, minimal diffs are often counter-intuitive
   for humans, because they synch up anywhere possible, sometimes at
   accidental matches 100 pages apart. Restricting synch points to
   contiguous matches preserves some notion of locality, at the
   occasional cost of producing a longer diff.

   La clase "Differ" tiene el siguiente constructor:

   __init__(linejunk=None, charjunk=None)

      Parámetros de palabra clave opcionales *linejunk* y *charjunk*
      son para funciones de filtrado (o "None"):

      *linejunk*: Una función que acepta una sola cadena de texto como
      argumento y retorna verdadero si la cadena de texto es un
      elemento no deseado. Su valor por defecto es "None", lo que
      significa que ninguna línea es considerada no deseada.

      *charjunk*: Una función que acepta un solo carácter como
      argumento (una cadena de caracteres de longitud 1) y retorna
      verdadero si el carácter es un elemento no deseado. Su valor por
      defecto es "None", lo que significa que ningún carácter es
      considerado no deseado.

      Estas funciones de elementos no deseados aceleran la
      coincidencia para encontrar diferencies y no hacen que se
      ignoren líneas o caracteres diferentes. Lea la descripción del
      parámetro *isjunk* en el método "find_longest_match()" para una
      explicación mas detallada.

   Los objetos "Differ" son usados (una vez generados los deltas)
   mediante un solo método:

   compare(a, b)

      Compara dos secuencias de líneas y genera el delta
      correspondiente (una secuencia de líneas).

      Each sequence must contain individual single-line strings ending
      with newlines.  Such sequences can be obtained from the
      "readlines()" method of file-like objects.  The generated delta
      also consists of newline-terminated strings, ready to be printed
      as-is via the "writelines()" method of a file-like object.

class difflib.HtmlDiff

   Esta clase puede ser usada para crear una tabla HTML (o un archivo
   HTML completo que contenga la tabla) mostrando comparaciones lado a
   lado y linea por linea del texto, con cambios interlineales e
   intralineales. La tabla se puede generar en modo de diferencia
   completa o contextual.

   Advertencia:

     The trailing newlines get stripped before the diff, so the result
     can be incomplete. See gh-71896 for details.

   El constructor de esta clase es:

   __init__(tabsize=8, wrapcolumn=None, linejunk=None, charjunk=IS_CHARACTER_JUNK)

      Inicializa una instancia de "HtmlDiff".

      *tabsize* es un argumento por palabra clave opcional para
      especificar el espaciado de tabulación. Su valor predeterminado
      es "8".

      *wrapcolumn* es un argumento por palabra clave opcional para
      especificar el número de columnas donde las lineas serán
      divididas y ajustadas al ancho de columna, su valor por defecto
      es "None", donde las lineas no son ajustadas.

      *linejunk* y *charjunk* son argumentos por palabra clave
      opcionales que serán pasados a "ndiff()" (que es utilizado por
      "HtmlDiff" para generar las diferencias lado a lado en HTML).
      Refiérase a la documentación de "ndiff()" para conocer los
      detalles y valores por defecto de sus argumentos.

   Los siguientes métodos son públicos:

   make_file(fromlines, tolines, fromdesc='', todesc='', context=False, numlines=5, *, charset='utf-8')

      Compara *fromlines* y *tolines* (listas de cadenas de texto) y
      retorna una cadena de caracteres que representa un archivo HTML
      completo que contiene una tabla mostrando diferencias línea por
      línea del texto con cambios interlineales e intralineales
      resaltados.

      *fromdesc* y *todesc* son argumentos por palabra clave
      opcionales para especificar los encabezados de las columnas
      desde *fromdesc* hasta *todesc* en el archivo (ambas cadenas
      están vacías por defecto).

      *context* y *numlines* son parámetros opcionales. Establezca
      *context* como "True" para mostrar diferencias contextuales, de
      lo contrario su valor por defecto es "False" que muestra los
      archivos completos. El valor por defecto de *numlines* es "5".
      Cuando *context* es "True", *numlines* controla el número de
      lineas de contexto que rodean las diferencias resaltadas. Cuando
      *context* es "False", *numlines* controla el número de líneas
      que se muestran antes de una diferencia resaltada cuando se usan
      los hipervínculos "next" (un valor de cero produce que los
      hipervínculos "next" ubiquen el siguiente resaltado en la parte
      superior del navegador, sin ningún contexto principal).

      Nota:

        *fromdesc* y *todesc* se interpretan como HTML no escapado y
        se deben escapar correctamente si los datos son recibidos de
        fuentes no confiables.

      Distinto en la versión 3.5: Se agregó el argumento sólo de
      palabra clave *charset*.  La codificación de caracteres por
      defecto para documentos HTML se cambió de "'ISO-8859-1'" a
      "'utf-8'".

   make_table(fromlines, tolines, fromdesc='', todesc='', context=False, numlines=5)

      Compara *fromlines* y *tolines* (listas de cadenas de texto) y
      retorna una cadena de caracteres que representa una tabla HTML
      mostrando comparaciones lado a lado y línea por línea del texto
      con cambios interlineales e intralineales.

      Los argumentos para este método son los mismos que los del
      método "make_file()".

difflib.context_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\n')

   Compara *a* y *b* (listas de cadenas de texto); retorna un delta
   (un *generator* que genera las lineas delta) en formato de
   diferencias de contexto.

   El formato de diferencias de contexto es una forma compacta de
   mostrar solamente las líneas que fueron modificadas y algunas
   líneas adicionales de contexto.  Los cambios son mostrados
   utilizando el estilo antes/después.  El número de líneas de
   contexto es determinado por *n*, cuyo valor por defecto es "3".

   Por defecto, las líneas de control (aquellas que comienzan con
   "***" o "---") son creadas con una línea nueva. Esto es de ayuda
   para que las entradas creadas por "io.IOBase.readlines()" generen
   diferencias que puedan ser utilizadas con "io.IOBase.writelines()"
   ya que ambas, la entrada y la salida, tienen líneas nuevas al
   final.

   Para entradas que no tienen nuevas líneas finales, establezca el
   argumento *lineterm* como """" de forma que la salida sea uniforme
   y libre de nuevas líneas.

   El formato de diferencias de contexto normalmente tiene un
   encabezado para nombres de archivos y tiempos de modificaciones.
   Alguno o todos estos debe ser especificado utilizando las cadenas
   de texto para *fromfile*, *tofile*, *fromfiledate* y *tofiledate*.
   Los tiempos de modificación son normalmente expresados en formato
   ISO 8601. Si no es especificado las cadenas por defecto son
   espacios en blanco.

   >>> import sys
   >>> from difflib import *
   >>> s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
   >>> s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
   >>> sys.stdout.writelines(context_diff(s1, s2, fromfile='before.py',
   ...                        tofile='after.py'))
   *** before.py
   --- after.py
   ***************
   *** 1,4 ****
   ! bacon
   ! eggs
   ! ham
     guido
   --- 1,4 ----
   ! python
   ! eggy
   ! hamster
     guido

   Vea Una interfaz de línea de comandos para difflib para un ejemplo
   mas detallado.

difflib.get_close_matches(word, possibilities, n=3, cutoff=0.6)

   Retorna una lista de las mejores coincidencias "lo suficientemente
   buenas". *word* es una secuencia para la cual coincidencias
   cercanas son deseadas (usualmente una cadena de texto), y
   *possibilities* es una lista de secuencias contra la cual se
   compara *word* (comúnmente una lista de cadenas de caracteres).

   Argumento opcional *n* (por defecto "3") es el máximo número de
   coincidencias cercanas a retornar; *n* debe ser mayor que "0".

   Argumento opcional *cutoff* (por defecto "0.6") es un flotante en
   el rango [0, 1]. Las posibilidades que no alcanzan un puntaje al
   menos similar al de *word* son ignoradas.

   Las mejores (no mas de *n*) coincidencias entre las posibilidades
   son retornadas en una lista, ordenadas por similitud de puntaje,
   las mas similares primero.

   >>> get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])
   ['apple', 'ape']
   >>> import keyword
   >>> get_close_matches('wheel', keyword.kwlist)
   ['while']
   >>> get_close_matches('pineapple', keyword.kwlist)
   []
   >>> get_close_matches('accept', keyword.kwlist)
   ['except']

difflib.ndiff(a, b, linejunk=None, charjunk=IS_CHARACTER_JUNK)

   Compara *a* y *b* (listas de cadenas de texto); retorna un delta
   del estilo "Differ" (un *generator* que genera los deltas de las
   líneas).

   Parámetros de palabra clave opcional *linejunk* y *charjunk* son
   funciones de filtrado (o "None"):

   *linejunk*: A function that accepts a single string argument, and
   returns true if the string is junk, or false if not. The default is
   "None". There is also a module-level function "IS_LINE_JUNK()",
   which filters out lines without visible characters, except for at
   most one hash character ("'#'") -- however the underlying
   "SequenceMatcher" class does a dynamic analysis of which lines are
   so frequent as to constitute noise, and this usually works better
   than using this function.

   *charjunk*: Una función que acepta un carácter (una cadena de
   caracteres de longitud 1) como argumento, y retorna *True* si el
   carácter es un elemento no deseado, o *False* si no lo es. El valor
   por defecto es una función a nivel del módulo
   "IS_CHARACTER_JUNK()", que filtra caracteres de espacios en blanco
   (un espacio en blanco o tabulación; es una mala idea incluir saltos
   de lineas en esto!)

   >>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
   ...              'ore\ntree\nemu\n'.splitlines(keepends=True))
   >>> print(''.join(diff), end="")
   - one
   ?  ^
   + ore
   ?  ^
   - two
   - three
   ?  -
   + tree
   + emu

difflib.restore(sequence, which)

   Retorna uno de las dos secuencias que generaron un delta.

   Dada una *sequence* producida por "Differ.compare()" o "ndiff()",
   extrae las líneas originadas por el archivo 1 o 2 (parámetro
   *which*), quitando los prefijos de la línea.

   Ejemplo:

   >>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
   ...              'ore\ntree\nemu\n'.splitlines(keepends=True))
   >>> diff = list(diff) # materialize the generated delta into a list
   >>> print(''.join(restore(diff, 1)), end="")
   one
   two
   three
   >>> print(''.join(restore(diff, 2)), end="")
   ore
   tree
   emu

difflib.unified_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\n')

   Compara *a* y *b* (listas de cadenas de caracteres); retorna un
   delta (un *generator* que genera los delta de líneas) en formato de
   diferencias unificado.

   Las diferencias unificadas son una forma compacta de mostrar sólo
   las líneas que presentan cambios y algunas líneas de contexto
   adicionales. Los cambios son mostrados en una sola línea (en lugar
   de bloques separados antes y después). El número de líneas de
   contexto se establece mediante *n*, cuyo valor por defecto es tres.

   Por defecto, las líneas de control de diferencias (aquellas con
   "---", "+++", o "@@") son creadas con un salto de línea nuevo. Esto
   es de ayuda para que las entradas creadas por
   "io.IOBase.readlines()" generen diferencias que puedan ser
   utilizadas con "io.IOBase.writelines()" ya que ambas, la entrada y
   la salida, tienen líneas nuevas al final.

   Para entradas que no tienen nuevas líneas finales, establezca el
   argumento *lineterm* como """" de forma que la salida sea uniforme
   y libre de nuevas líneas.

   The unified diff format normally has a header for filenames and
   modification times.  Any or all of these may be specified using
   strings for *fromfile*, *tofile*, *fromfiledate*, and *tofiledate*.
   The modification times are normally expressed in the ISO 8601
   format. If not specified, the strings default to blanks.

   >>> s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
   >>> s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
   >>> sys.stdout.writelines(unified_diff(s1, s2, fromfile='before.py', tofile='after.py'))
   --- before.py
   +++ after.py
   @@ -1,4 +1,4 @@
   -bacon
   -eggs
   -ham
   +python
   +eggy
   +hamster
    guido

   Vea Una interfaz de línea de comandos para difflib para un ejemplo
   mas detallado.

difflib.diff_bytes(dfunc, a, b, fromfile=b'', tofile=b'', fromfiledate=b'', tofiledate=b'', n=3, lineterm=b'\n')

   Compara *a* y *b* (listas de objetos de bytes) usando *dfunc*;
   produce una secuencia de líneas delta (también bytes) en el formato
   retornado por *dfunc*. *dfunc* debe ser invocable, comúnmente
   cualquiera de "unified_diff()" o "context_diff()".

   Permite comparar datos con codificación desconocida o
   inconsistente. Todas las entradas, excepto *n*, deben ser objetos
   de bytes, no cadenas de texto. Funciona convirtiendo sin pérdidas
   todas las entradas (excepto *n*) a cadenas de texto, e invoca
   "dfunc(a, b, fromfile, tofile, fromfiledate, tofiledate, n,
   lineterm)". La salida de *dfunc* es entonces convertida nuevamente
   a bytes, de forma que las líneas delta que son recibidas tienen la
   misma codificación desconocida/inconsistente que *a* y *b*.

   Added in version 3.5.

## Junk definition functions

difflib.IS_LINE_JUNK(line)

   Retorna "True" para líneas que deben ser ignoradas. La línea *line*
   es ignorada si *line* es un espacio vacío o contiene un solo "'#'",
   en cualquier otro caso no es ignorado. Es usado como valor por
   defecto para el parámetro *linejunk* por "ndiff()" en versiones
   anteriores.

difflib.IS_CHARACTER_JUNK(ch)

   Retorna "True" para los caracteres que deben ser ignorados. El
   carácter *ch* es ignorado si *ch* es un espacio en blanco o
   tabulación, en cualquier otro caso no es ignorado. Es utilizado
   como valor por defecto para el parámetro *charjunk* en "ndiff()".

## SequenceMatcher objects

class difflib.SequenceMatcher(isjunk=None, a='', b='', autojunk=True)

   El argumento opcional *isjunk* debe ser "None" (que es su valor por
   defecto) o una función de un solo argumento que reciba un elemento
   de la secuencia y retorne verdadero si y solo si el elemento es no
   deseado y deba ser ignorado. Pasar el argumento *isjunk* como
   "None" es equivalente a pasar "lambda x: False"; en otras palabras,
   ningún elemento es ignorado. Por ejemplo, pasar:

      lambda x: x in " \t"

   si se están comparando líneas como secuencias de caracteres, y no
   se quiere sincronizar en espacios blancos o tabulaciones.

   Los argumentos opcionales *a* y *b* son las secuencias a comparar;
   ambos tienen como valor por defecto una cadena de texto vacía. Los
   elementos de ambas secuencias deben ser *hashable*.

   El argumento opcional *autojunk* puede ser usado para deshabilitar
   la heurística automática de elementos no deseados.

   Distinto en la versión 3.2: Added the *autojunk* parameter.

   Los objetos *SequenceMatcher* reciben tres atributos: *bjunk* es el
   conjunto de elementos de *b* para los cuales *isjunk* es "True";
   *bpopular* es el set de elementos que no son basura considerados
   populares por la heurística (si no es que fue deshabilitada); *b2j*
   es un diccionario que mapea elementos de *b* a una lista de
   posiciones donde estos ocurren. Los tres atributos son reseteados
   cuando *b* es reseteado mediante "set_seqs()" o "set_seq2()".

   Added in version 3.2: Los atributos *bjunk* y *bpopular*.

   Los objetos "SequenceMatcher" tienen los siguientes métodos:

   set_seqs(a, b)

      Establece las dos secuencias a ser comparadas.

   "SequenceMatcher" calcula y almacena información detallada sobre la
   segunda secuencia, con lo cual si quieres comparar una secuencia
   contra muchas otras, usa "set_seq2()" para establecer la secuencia
   común una sola vez y llamar "set_seq1()" repetidamente, una vez por
   cada una de las otras secuencias.

   set_seq1(a)

      Establece la primer secuencia a ser comparada. La segunda
      secuencia a ser comparada no es modificada.

   set_seq2(b)

      Establece la segunda secuencia a ser comparada. La primera
      secuencia a ser comparada no es modificada.

   find_longest_match(alo=0, ahi=None, blo=0, bhi=None)

      Encuentra el bloque de coincidencia mas largo en "a[alo:ahi]" y
      "b[blo:bhi]".

      Si *isjunk* fue omitido o es "None", "find_longest_match()"
      retorna "(i, j, k)" tal que "a[i:i+k]" es igual a "b[j:j+k]",
      donde "alo <= i <= i+k <= ahi" y "blo <= j <= j+k <= bhi". Para
      todo "(i', j', k')" cumpliendo esas condiciones, las condiciones
      adicionales "k >= k'", "i <= i'", y si "i == i'", "j <= j'"
      también se cumplen. En otras palabras, de todos los bloques
      coincidentes máximos, retorna aquel que comienza antes en *a*, y
      de todos esos bloques coincidentes máximos que comienzan antes
      en *a*, retorna aquel que comienza antes en *b*.

      >>> s = SequenceMatcher(None, " abcd", "abcd abcd")
      >>> s.find_longest_match(0, 5, 0, 9)
      Match(a=0, b=4, size=5)

      Si se porporcionó *isjunk*, primero se determina el bloque
      coincidente mas largo como fue indicado anteriormente, pero con
      la restricción adicional de que no aparezca ningún elemento no
      deseado en el bloque. Entonces, ese bloque se extiende tan lejos
      como sea posible haciendo coincidir (solo) elementos no deseados
      de ambos lados. Por lo tanto, el bloque resultante nunca hará
      coincidir ningún elemento no deseado, excepto que un elemento no
      deseado idéntico pase a ser adyacente a una coincidencia
      interesante.

      Este es el mismo ejemplo que el mostrado anteriormente, pero
      considerando elementos en blanco como no deseados. Esto previene
      que "' abcd'" sea coincidente con "'abcd'" en el final de la
      segunda secuencia directamente. En cambio, sólo el "'abcd'"
      puede coincidir, y coincide con el "'abcd'" que se encuentre mas
      a la izquierda en la segunda secuencia:

      >>> s = SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")
      >>> s.find_longest_match(0, 5, 0, 9)
      Match(a=1, b=0, size=4)

      Si no coincide ningún bloque, esto retorna "(alo, blo, 0)".

      Este método retorna un *named tuple* "Match(a, b, size)".

      Distinto en la versión 3.9: Se agregaron argumentos
      predeterminados.

   get_matching_blocks()

      Retorna una lista de triplas (tuplas de tres elementos)
      describiendo subsecuencias coincidentes no superpuestas. Cada
      tripla sigue el formato "(i, j, n)", y significa que "a[i:i+n]
      == b[j:j+n]". Las triplas son monótonamente crecientes en *i* y
      *j*.

      La última tripla es un objeto ficticio (dummy), y tiene el valor
      "(len(a), len(b), 0)". Es la única tripla con "n == 0".  Si "(i,
      j, n)" y "(i', j', n')" son triplas adyacentes en la lista, y la
      segunda no es el último elemento de la lista, entonces "i+n <
      i'" o "j+n < j'"; en otras palabras, las triplas adyacentes
      describen bloques iguales no adyacentes.

         >>> s = SequenceMatcher(None, "abxcd", "abcd")
         >>> s.get_matching_blocks()
         [Match(a=0, b=0, size=2), Match(a=3, b=2, size=2), Match(a=5, b=4, size=0)]

   get_opcodes()

      Retorna una lista de quíntuplas (tuplas de cinco elementos)
      describiendo como convertir *a* en *b*. Cada tupla tiene la
      forma "(tag, i1, i2, j1, j2)". En la primer tupla se cumple que
      "i1 == j1 == 0", y las tuplas restantes tienen *i1* igual al
      *i2* de la tupla precedente, y de igual manera, *j1* igual al
      *j2* de la tupla anterior.

      Los valores de *tag* son cadenas de caracteres, con el siguiente
      significado:

      +-----------------+-----------------------------------------------+
      | Valor           | Significado                                   |
      |=================|===============================================|
      | "'replace'"     | "a[i1:i2]" debe ser reemplazado por           |
      |                 | "b[j1:j2]".                                   |
      +-----------------+-----------------------------------------------+
      | "'delete'"      | "a[i1:i2]" debe ser eliminado.  Nótese que en |
      |                 | este caso "j1 == j2".                         |
      +-----------------+-----------------------------------------------+
      | "'insert'"      | "b[j1:j2]" debe ser insertado en "a[i1:i1]".  |
      |                 | Nótese que en este caso "i1 == i2".           |
      +-----------------+-----------------------------------------------+
      | "'equal'"       | "a[i1:i2] == b[j1:j2]" (las subsecuencias son |
      |                 | iguales).                                     |
      +-----------------+-----------------------------------------------+

      Por ejemplo:

         >>> a = "qabxcd"
         >>> b = "abycdf"
         >>> s = SequenceMatcher(None, a, b)
         >>> for tag, i1, i2, j1, j2 in s.get_opcodes():
         ...     print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
         ...         tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
         delete    a[0:1] --> b[0:0]      'q' --> ''
         equal     a[1:3] --> b[0:2]     'ab' --> 'ab'
         replace   a[3:4] --> b[2:3]      'x' --> 'y'
         equal     a[4:6] --> b[3:5]     'cd' --> 'cd'
         insert    a[6:6] --> b[5:6]       '' --> 'f'

   get_grouped_opcodes(n=3)

      Retorna un *generator* de grupos de hasta *n* líneas de
      contexto.

      Empezando con los grupos retornados por "get_opcodes()", este
      método separa grupos con cambios menores y elimina los rangos
      intermedios que no tienen cambios.

      Los grupos son retornados en el mismo formato que
      "get_opcodes()".

   ratio()

      Retorna una medida de la similitud de las secuencias como un
      flotante en el rango [0, 1].

      Donde T es el número total de elementos en ambas secuencias y M
      es el número de coincidencias, esto es 2.0*M / T. Nótese que
      esto es "1.0" si las secuencias son idénticas y "0.0" si no
      tienen nada en común.

      Esto es computacionalmente costoso si "get_matching_blocks()" o
      "get_opcodes()" no fueron ejecutados, in tal caso deberías
      considerar primero "quick_ratio()" o "real_quick_ratio()" para
      obtener un límite superior.

   quick_ratio()

      Retorna un límite superior en "ratio()" relativamente rápido.

   real_quick_ratio()

      Retorna un límite superior en "ratio()" muy rápido.

The three methods that return the ratio of matching to total
characters can give different results due to differing levels of
approximation, although "quick_ratio()" and "real_quick_ratio()" are
always at least as large as "ratio()":

>>> s = SequenceMatcher(None, "abcd", "bcde")
>>> s.ratio()
0.75
>>> s.quick_ratio()
0.75
>>> s.real_quick_ratio()
1.0

## Examples

### SequenceMatcher examples

Este ejemplo compara dos cadenas de texto, considerando los espacios
en blanco como caracteres no deseados:

>>> s = SequenceMatcher(lambda x: x == " ",
...                     "private Thread currentThread;",
...                     "private volatile Thread currentThread;")

"ratio()" returns a float in [0, 1], measuring the similarity of the
sequences.  As a rule of thumb, a "ratio()" value over 0.6 means the
sequences are close matches:

>>> print(round(s.ratio(), 3))
0.866

If you're only interested in where the sequences match,
"get_matching_blocks()" is handy:

>>> for block in s.get_matching_blocks():
...     print("a[%d] and b[%d] match for %d elements" % block)
a[0] and b[0] match for 8 elements
a[8] and b[17] match for 21 elements
a[29] and b[38] match for 0 elements

Note that the last tuple returned by "get_matching_blocks()" is always
a dummy, "(len(a), len(b), 0)", and this is the only case in which the
last tuple element (number of elements matched) is "0".

If you want to know how to change the first sequence into the second,
use "get_opcodes()":

>>> for opcode in s.get_opcodes():
...     print("%6s a[%d:%d] b[%d:%d]" % opcode)
 equal a[0:8] b[0:8]
insert a[8:8] b[8:17]
 equal a[8:29] b[17:38]

Ver también:

  * La función "get_close_matches()" en este módulo que muestra lo
    simple que es el código que construye "SequenceMatcher" puede ser
    utilizada para hacer un trabajo útil.

  * Simple version control recipe for a small application built with
    "SequenceMatcher".

### Differ example

This example compares two texts. First we set up the texts, sequences
of individual single-line strings ending with newlines (such sequences
can also be obtained from the "readlines()" method of file-like
objects):

>>> text1 = '''  1. Beautiful is better than ugly.
...   2. Explicit is better than implicit.
...   3. Simple is better than complex.
...   4. Complex is better than complicated.
... '''.splitlines(keepends=True)
>>> len(text1)
4
>>> text1[0][-1]
'\n'
>>> text2 = '''  1. Beautiful is better than ugly.
...   3.   Simple is better than complex.
...   4. Complicated is better than complex.
...   5. Flat is better than nested.
... '''.splitlines(keepends=True)

Luego instanciamos el objeto *Differ*:

>>> d = Differ()

Nótese que cuando instanciamos un objeto "Differ" deberíamos pasar
funciones para filtrar lineas y caracteres no deseados. Consulte el
constructor de "Differ()" para mas detalles.

Finalmente, comparamos las dos:

>>> result = list(d.compare(text1, text2))

"result" es una lista de cadenas de caracteres, entonces vamos a
mostrarlo de una forma elegante:

>>> from pprint import pprint
>>> pprint(result)
['    1. Beautiful is better than ugly.\n',
 '-   2. Explicit is better than implicit.\n',
 '-   3. Simple is better than complex.\n',
 '+   3.   Simple is better than complex.\n',
 '?     ++\n',
 '-   4. Complex is better than complicated.\n',
 '?            ^                     ---- ^\n',
 '+   4. Complicated is better than complex.\n',
 '?           ++++ ^                      ^\n',
 '+   5. Flat is better than nested.\n']

Representado como una sola cadena de caracteres de múltiples líneas se
ve así:

>>> import sys
>>> sys.stdout.writelines(result)
    1. Beautiful is better than ugly.
-   2. Explicit is better than implicit.
-   3. Simple is better than complex.
+   3.   Simple is better than complex.
?     ++
-   4. Complex is better than complicated.
?            ^                     ---- ^
+   4. Complicated is better than complex.
?           ++++ ^                      ^
+   5. Flat is better than nested.

### Una interfaz de línea de comandos para "difflib"

This example shows how to use difflib to create a "diff"-like utility.

   """ Command-line interface to difflib.py providing diffs in four formats:

   * ndiff:    lists every line and highlights interline changes.
   * context:  highlights clusters of changes in a before/after format.
   * unified:  highlights clusters of changes in an inline format.
   * html:     generates side by side comparison with change highlights.

   """

   import sys, os, difflib, argparse
   import datetime as dt

   def file_mtime(path):
       t = dt.datetime.fromtimestamp(os.stat(path).st_mtime,
                                     dt.timezone.utc)
       return t.astimezone().isoformat()

   def main():

       parser = argparse.ArgumentParser()
       parser.add_argument('-c', action='store_true', default=False,
                           help='Produce a context format diff (default)')
       parser.add_argument('-u', action='store_true', default=False,
                           help='Produce a unified format diff')
       parser.add_argument('-m', action='store_true', default=False,
                           help='Produce HTML side by side diff '
                                '(can use -c and -l in conjunction)')
       parser.add_argument('-n', action='store_true', default=False,
                           help='Produce a ndiff format diff')
       parser.add_argument('-l', '--lines', type=int, default=3,
                           help='Set number of context lines (default 3)')
       parser.add_argument('fromfile')
       parser.add_argument('tofile')
       options = parser.parse_args()

       n = options.lines
       fromfile = options.fromfile
       tofile = options.tofile

       fromdate = file_mtime(fromfile)
       todate = file_mtime(tofile)
       with open(fromfile) as ff:
           fromlines = ff.readlines()
       with open(tofile) as tf:
           tolines = tf.readlines()

       if options.u:
           diff = difflib.unified_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=n)
       elif options.n:
           diff = difflib.ndiff(fromlines, tolines)
       elif options.m:
           diff = difflib.HtmlDiff().make_file(fromlines,tolines,fromfile,tofile,context=options.c,numlines=n)
       else:
           diff = difflib.context_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=n)

       sys.stdout.writelines(diff)

   if __name__ == '__main__':
       main()

### ndiff example

This example shows how to use "difflib.ndiff()".

   """ndiff [-q] file1 file2
       or
   ndiff (-r1 | -r2) < ndiff_output > file1_or_file2

   Print a human-friendly file difference report to stdout.  Both inter-
   and intra-line differences are noted.  In the second form, recreate file1
   (-r1) or file2 (-r2) on stdout, from an ndiff report on stdin.

   In the first form, if -q ("quiet") is not specified, the first two lines
   of output are

   -: file1
   +: file2

   Each remaining line begins with a two-letter code:

       "- "    line unique to file1
       "+ "    line unique to file2
       "  "    line common to both files
       "? "    line not present in either input file

   Lines beginning with "? " attempt to guide the eye to intraline
   differences, and were not present in either input file.  These lines can be
   confusing if the source files contain tab characters.

   The first file can be recovered by retaining only lines that begin with
   "  " or "- ", and deleting those 2-character prefixes; use ndiff with -r1.

   The second file can be recovered similarly, but by retaining only "  " and
   "+ " lines; use ndiff with -r2; or, on Unix, the second file can be
   recovered by piping the output through

       sed -n '/^[+ ] /s/^..//p'
   """

   __version__ = 1, 7, 0

   import difflib, sys

   def fail(msg):
       out = sys.stderr.write
       out(msg + "\n\n")
       out(__doc__)
       return 0

   # open a file & return the file object; gripe and return 0 if it
   # couldn't be opened
   def fopen(fname):
       try:
           return open(fname)
       except IOError as detail:
           return fail("couldn't open " + fname + ": " + str(detail))

   # open two files & spray the diff to stdout; return false iff a problem
   def fcompare(f1name, f2name):
       f1 = fopen(f1name)
       f2 = fopen(f2name)
       if not f1 or not f2:
           return 0

       a = f1.readlines(); f1.close()
       b = f2.readlines(); f2.close()
       for line in difflib.ndiff(a, b):
           print(line, end=' ')

       return 1

   # crack args (sys.argv[1:] is normal) & compare;
   # return false iff a problem

   def main(args):
       import getopt
       try:
           opts, args = getopt.getopt(args, "qr:")
       except getopt.error as detail:
           return fail(str(detail))
       noisy = 1
       qseen = rseen = 0
       for opt, val in opts:
           if opt == "-q":
               qseen = 1
               noisy = 0
           elif opt == "-r":
               rseen = 1
               whichfile = val
       if qseen and rseen:
           return fail("can't specify both -q and -r")
       if rseen:
           if args:
               return fail("no args allowed with -r option")
           if whichfile in ("1", "2"):
               restore(whichfile)
               return 1
           return fail("-r value must be 1 or 2")
       if len(args) != 2:
           return fail("need 2 filename args")
       f1name, f2name = args
       if noisy:
           print('-:', f1name)
           print('+:', f2name)
       return fcompare(f1name, f2name)

   # read ndiff output from stdin, and print file1 (which=='1') or
   # file2 (which=='2') to stdout

   def restore(which):
       restored = difflib.restore(sys.stdin.readlines(), which)
       sys.stdout.writelines(restored)

   if __name__ == '__main__':
       main(sys.argv[1:])
