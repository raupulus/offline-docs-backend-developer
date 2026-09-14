---
title: '"re" --- Regular expression operations'
source_url: https://docs.python.org/es/3
source_path: library/re.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3640
---

# "re" --- Regular expression operations

**Código fuente:** Lib/re/

======================================================================

Este módulo proporciona operaciones de coincidencia de expresiones
regulares similares a las encontradas en Perl.

Both patterns and strings to be searched can be Unicode strings
("str") as well as 8-bit strings ("bytes"). However, Unicode strings
and 8-bit strings cannot be mixed: that is, you cannot match a Unicode
string with a bytes pattern or vice-versa; similarly, when asking for
a substitution, the replacement string must be of the same type as
both the pattern and the search string.

Las expresiones regulares usan el carácter de barra inversa ("'\'")
para indicar formas especiales o para permitir el uso de caracteres
especiales sin invocar su significado especial.  Esto choca con el uso
de Python de este carácter para el mismo propósito con los literales
de cadena; por ejemplo, para hacer coincidir una barra inversa
literal, se podría escribir "'\\\\'" como patrón, porque la expresión
regular debe ser "\\", y cada barra inversa debe ser expresada como
"\\" dentro de un literal de cadena regular de Python.  También, notar
que cualquier secuencia de escape inválida mientras se use la barra
inversa de Python en los literales de cadena ahora genera un
"SyntaxWarning" y en el futuro esto se convertirá en un "SyntaxError".
Este comportamiento ocurrirá incluso si es una secuencia de escape
válida para una expresión regular.

La solución es usar la notación de cadena *raw* de Python para los
patrones de expresiones regulares; las barras inversas no se manejan
de ninguna manera especial en un literal de cadena prefijado con
"'r'".  Así que "r"\n"" es una cadena de dos caracteres que contiene
"'\'" y "'n'", mientras que ""\n"" es una cadena de un carácter que
contiene una nueva línea.  Normalmente los patrones se expresan en
código Python usando esta notación de cadena *raw*.

Es importante señalar que la mayoría de las operaciones de expresiones
regulares están disponibles como funciones y métodos a nivel de módulo
en expresiones regulares compiladas (expresiones regulares
compiladas).  Las funciones son atajos que no requieren de compilar un
objeto regex primero, aunque pasan por alto algunos parámetros de
ajuste.

Ver también:

  The third-party regex module, which has an API compatible with the
  standard library "re" module, but offers additional functionality
  and a more thorough Unicode support.

## Sintaxis de expresiones regulares

Una expresión regular (o RE, por sus siglas en inglés) especifica un
conjunto de cadenas que coinciden con ella; las funciones de este
módulo permiten comprobar si una determinada cadena coincide con una
expresión regular dada (o si una expresión regular dada coincide con
una determinada cadena, que se reduce a lo mismo).

Las expresiones regulares pueden ser concatenadas para formar nuevas
expresiones regulares; si *A* y *B* son ambas expresiones regulares,
entonces *AB* es también una expresión regular. En general, si una
cadena *p* coincide con *A* y otra cadena *q* coincide con *B*, la
cadena *porque* coincidirá con AB.  Esto se mantiene a menos que *A* o
*B* contengan operaciones de baja precedencia; condiciones límite
entre *A* y *B*; o tengan referencias de grupo numeradas.  Así, las
expresiones complejas pueden construirse fácilmente a partir de
expresiones primitivas más simples como las que se describen aquí.
Para detalles de la teoría e implementación de las expresiones
regulares, consulte el libro de Friedl [Frie09], o casi cualquier
libro de texto sobre la construcción de compiladores.

A continuación se explica brevemente el formato de las expresiones
regulares.  Para más información y una presentación más amena,
consultar la Regular expression HOWTO.

Las expresiones regulares pueden contener tanto caracteres especiales
como ordinarios. La mayoría de los caracteres ordinarios, como "'A'",
"'a'", o "'0'" son las expresiones regulares más sencillas;
simplemente se ajustan a sí mismas.  Se pueden concatenar caracteres
ordinarios, así que "last" coincide con la cadena "'last'".  (En el
resto de esta sección, se escribirán los RE en "este estilo especial",
normalmente sin comillas, y las cadenas que deban coincidir "'entre
comillas simples'".)

Algunos caracteres, como "'|'" o "'('", son especiales. Los caracteres
especiales representan clases de caracteres ordinarios, o afectan a la
forma en que se interpretan las expresiones regulares que los rodean.

Los operadores de repetición o cuantificadores ("*", "+", "?",
"{m,n}", etc.) no pueden ser anidados directamente. Esto evita la
ambigüedad con el sufijo modificador no codicioso "?", y con otros
modificadores en otras implementaciones. Para aplicar una segunda
repetición a una repetición interna, se pueden usar paréntesis. Por
ejemplo, la expresión "(?:a{6})*" coincide con cualquier múltiplo de
seis caracteres "'a'".

Los caracteres especiales son:

"."
   (Dot.)  In the default mode, this matches any character except a
   newline.  If the "DOTALL" flag has been specified, this matches any
   character including a newline.  "(?s:.)" matches any character
   regardless of flags.

"^"
   (Circunflejo.)  Coincide con el comienzo de la cadena, y en modo
   "MULTILINE" también coincide inmediatamente después de cada nueva
   línea.

"$"
   Coincide con el final de la cadena o justo antes de la nueva línea
   al final de la cadena, y en modo "MULTILINE" también coincide antes
   de una nueva línea.  "foo" coincide con 'foo' y 'foobar', mientras
   que la expresión regular "foo$" sólo coincide con 'foo'.  Más
   interesante aún, al buscar "foo.$" en "'foo1\nfoo2\n'" coincide con
   'foo2' normalmente, pero solo 'foo1' en "MULTILINE`"; si busca un
   solo "$" en "'foo\n'" encontrará dos coincidencias (vacías): una
   justo antes de una nueva línea, y otra al final de la cadena.

"*"
   Hace que el RE resultante coincida con 0 o más repeticiones del RE
   precedente, tantas repeticiones como sean posibles.  "ab*"
   coincidirá con 'a', 'ab' o 'a' seguido de cualquier número de 'b'.

"+"
   Hace que la RE resultante coincida con 1 o más repeticiones de la
   RE precedente. "ab+" coincidirá con 'a' seguido de cualquier número
   distinto de cero de 'b'; no coincidirá solo con 'a'.

"?"
   Hace que la RE resultante coincida con 0 o 1 repeticiones de la RE
   precedente. "ab?" coincidirá con 'a' o 'ab'.

"*?", "+?", "??"
   Los delimitadores "'*'", "'+'", y "'?'" son todos *greedy*;
   coinciden con la mayor cantidad de texto posible.  A veces este
   comportamiento no es deseado; si el RE "<.*>" se utiliza para
   coincidir con "'<a> b <c>'", coincidirá con toda la cadena, y no
   sólo con "'<a>'".  Añadiendo "?" después del delimitador hace que
   se realice la coincidencia de manera *non-greedy* o *minimal*;
   coincidirá la *mínima* cantidad de caracteres como sea posible.
   Usando el RE "<.*?>" sólo coincidirá con "'<a>'".

"*+", "++", "?+"
   Como los cuantificadores "'*'", "'+'", y "'?'" , aquellos en los
   que se agrega "'+'" también coinciden tantas veces como sea
   posible. Sin embargo, a diferencia de los verdaderos
   cuantificadores codiciosos, estos no permiten retroceder cuando la
   expresión que le sigue no coincide. Estos se conocen como
   cuantificadores *possessive*. Por ejemplo, "a*a" coincidirá con
   "'aaaa'" porque la "a*" coincidirá con los 4 "'a'"s, pero, cuando
   se encuentra la "'a'" final, la expresión retrocede de modo que al
   final la "a*" termina coincidiendo con 3 "'a'"s total, y la cuarta
   "'a'" coincide con la final "'a'". Sin embargo, cuando "a*+a" se
   usa para que coincida con "'aaaa'", el "a*+" coincidirá con los 4
   "'a'", pero cuando el "'a'" final no encuentra más caracteres para
   coincidir, la expresión no puede retroceder y, por lo tanto, no
   coincidirá. "x*+", "x++" and "x?+" son equivalentes a "(?>x*)",
   "(?>x+)" and "(?>x?)" correspondientemente.

   Added in version 3.11.

"{m}"
   Especifica que exactamente *m* copias de la RE anterior deben
   coincidir; menos coincidencias hacen que la RE entera no coincida.
   Por ejemplo, "a{6}" coincidirá exactamente con seis caracteres
   "'a'", pero no con cinco.

"{m,n}"
   Hace que el RE resultante coincida de *m* a *n* repeticiones del RE
   precedente, tratando de coincidir con el mayor número de
   repeticiones posible.  Por ejemplo, "a{3,5}" coincidirá de 3 a 5
   caracteres "'a'".  Omitiendo *m* se especifica un límite inferior
   de cero, y omitiendo *n* se especifica un límite superior infinito.
   Por ejemplo, "a{4,}b" coincidirá con "'aaaab'" o mil caracteres
   "'a'" seguidos de una "'b'", pero no "'aaab'". La coma no puede ser
   omitida o el modificador se confundiría con la forma descrita
   anteriormente.

"{m,n}?"
   Hace que el RE resultante coincida de *m* a *n* repeticiones del RE
   precedente, tratando de coincidir con el *mínimo de* repeticiones
   posible.  Esta es la versión *non-greedy* (no codiciosa) del
   delimitador anterior.  Por ejemplo, en la cadena de 6 caracteres
   "'aaaaaa'", "a{3,5}" coincidirá con 5 caracteres "'a'", mientras
   que "a{3,5}?" solo coincidirá con 3 caracteres.

"{m,n}+"
   Hace que el RE resultante coincida de *m* a *n* repeticiones del RE
   anterior, intentando hacer coincidir tantas repeticiones como sea
   posible *sin* establecer ningún punto de retroceso. Esta es la
   versión posesiva del cuantificador anterior. Por ejemplo, en la
   cadena de 6 caracteres "'aaaaaa'", "a{3,5}+aa" intenta hacer
   coincidir 5 caracteres "'a'", entonces, al requerir 2 más "'a'"s,
   necesitará más caracteres de los disponibles y, por lo tanto,
   fallará, mientras que "a{3,5}aa" coincidirá con "a{3,5}" capturando
   5, luego 4 "'a'"s por retroceso y luego los últimos 2 "'a'"s son
   emparejados por el "aa" final en el patrón. "x{m,n}+" es
   equivalente a "(?>x{m,n})".

   Added in version 3.11.

"\"
   O bien se escapan a los caracteres especiales (lo que le permite
   hacer coincidir caracteres como "'*'", "'?'", y así sucesivamente),
   o se señala una secuencia especial; las secuencias especiales se
   explican más adelante.

   Si no se utiliza una cadena *raw* para expresar el patrón, recuerde
   que Python también utiliza la barra inversa como secuencia de
   escape en los literales de la cadena; si el analizador sintáctico
   de Python no reconoce la secuencia de escape, la barra inversa y el
   carácter subsiguiente se incluyen en la cadena resultante.  Sin
   embargo, si Python quisiera reconocer la secuencia resultante, la
   barra inversa debería repetirse dos veces.  Esto es complicado y
   difícil de entender, por lo que se recomienda encarecidamente
   utilizar cadenas *raw* para todas las expresiones salvo las más
   simples.

"[]"
   Se utiliza para indicar un conjunto de caracteres.  En un conjunto:

   * Los caracteres pueden ser listados individualmente, ej. "[amk]"
     coincidirá con "'a'", "'m'", o "'k'".

   * Los rangos de caracteres se pueden indicar mediante dos
     caracteres y separándolos con un "'-'". Por ejemplo, "[a-z]"
     coincidirá con cualquier letra ASCII en minúscula, "[0-5][0-9]"
     coincidirá con todos los números de dos dígitos desde el "00"
     hasta el "59", y "[0-9A-Fa-f]" coincidirá con cualquier dígito
     hexadecimal.  Si se escapa "-" (por ejemplo, "[a\-z]") o si se
     coloca como el primer o el último carácter (por ejemplo, "[-a]" o
     "[a-]"), coincidirá con un literal "'-'".

   * Special characters except backslash lose their special meaning
     inside sets. For example, "[(+*)]" will match any of the literal
     characters "'('", "'+'", "'*'", or "')'".

   * Backslash either escapes characters which have special meaning in
     a set such as "'-'", "']'", "'^'" and "'\\'" itself or signals a
     special sequence which represents a single character such as
     "\xa0" or "\n" or a character class such as "\w" or "\S" (defined
     below). Note that "\b" represents a single "backspace" character,
     not a word boundary as outside a set, and numeric escapes such as
     "\1" are always octal escapes, not group references. Special
     sequences which do not match a single character such as "\A" and
     "\z" are not allowed.

   * Los caracteres que no están dentro de un rango pueden ser
     coincidentes con *complementing* el conjunto. Si el primer
     carácter del conjunto es "'^'", todos los caracteres que *no*
     están en el conjunto coincidirán. Por ejemplo, "[^5]" coincidirá
     con cualquier carácter excepto con "'5'", y "[^^]" coincidirá con
     cualquier carácter excepto con "'^'". "^" no tiene un significado
     especial si no es el primer carácter del conjunto.

   * Para coincidir con un "']'" literal dentro de un set, se debe
     preceder con una barra inversa, o colocarlo al principio del set.
     Por ejemplo, tanto "[()[\]{}]" como "[]()[{}]" coincidirá con los
     paréntesis, corchetes y llaves.

   * El soporte de conjuntos anidados y operaciones de conjuntos como
     en Unicode Technical Standard #18 podría ser añadido en el
     futuro. Esto cambiaría la sintaxis, así que por el momento se
     planteará un "FutureWarning" en casos ambiguos para facilitar
     este cambio. Ello incluye conjuntos que empiecen con un literal
     "'['" o que contengan secuencias de caracteres literales "'—'",
     "'&&'", "'~~'" y "'||'". Para evitar una advertencia, utilizar el
     código de escape con una barra inversa.

   Distinto en la versión 3.7: "FutureWarning" se genera si un
   conjunto de caracteres contiene construcciones que cambiarán
   semánticamente en el futuro.

"|"
   "A|B", donde *A* y *B* pueden ser RE arbitrarias, crea una
   expresión regular que coincidirá con *A* or *B*. Un número
   arbitrario de RE puede ser separado por "'|'" de esta manera. Esto
   puede también ser usado dentro de grupos (ver más adelante). Cuando
   la cadena de destino es procesada, los RE separados por "'|'" son
   probados de izquierda a derecha. Cuando un patrón coincide
   completamente, esa rama es aceptada. Esto significa que una vez que
   *A* coincida, *B* no se comprobará más, incluso si se produce una
   coincidencia general más larga. En otras palabras, el operador de
   "'|'" nunca es codicioso. Para emparejar un literal "'|'", se usa
   "\|", o se envuelve dentro de una clase de caracteres, como en
   "[|]".

"(...)"
   Coincide con cualquier expresión regular que esté dentro de los
   paréntesis, e indica el comienzo y el final de un grupo; el
   contenido de un grupo puede ser recuperado después de que se haya
   realizado una coincidencia, y puede coincidir más adelante en la
   cadena con la secuencia especial "\number", que se describe más
   adelante. Para hacer coincidir los literales "`'('" o "')'", se usa
   "\(" o "\)", o se envuelve dentro de una clase de caracteres:
   "[(]", "[)]".

"(?...)"
   Esta es una notación de extensión (un "'?'" después de un "'('" no
   tiene ningún otro significado). El primer carácter después de "'?'"
   determina el significado y la sintaxis de la construcción. Las
   extensiones normalmente no crean un nuevo grupo; "(?P<name>…)" es
   la única excepción a esta regla. A continuación se muestran las
   extensiones actualmente soportadas.

"(?aiLmsux)"
   (One or more letters from the set "'a'", "'i'", "'L'", "'m'",
   "'s'", "'u'", "'x'".) The group matches the empty string; the
   letters set the corresponding flags for the entire regular
   expression:

   * "re.A" (ASCII-only matching)

   * "re.I" (ignore case)

   * "re.L" (locale dependent)

   * "re.M" (multi-line)

   * "re.S" (dot matches all)

   * "re.U" (Unicode matching)

   * "re.X" (verbose)

   (The flags are described in Contenidos del módulo.) This is useful
   if you wish to include the flags as part of the regular expression,
   instead of passing a *flag* argument to the "re.compile()"
   function. Flags should be used first in the expression string.

   Distinto en la versión 3.11: Esta construcción solo se puede usar
   al comienzo de la expresión.

"(?:...)"
   Una versión no capturable de los paréntesis regulares. Hace
   coincidir cualquier expresión regular que esté dentro de los
   paréntesis, pero la subcadena coincidente con el grupo *no puede*
   ser recuperada después de realizar una coincidencia o referenciada
   más adelante en el patrón.

"(?aiLmsux-imsx:...)"
   (Zero or more letters from the set "'a'", "'i'", "'L'", "'m'",
   "'s'", "'u'", "'x'", optionally followed by "'-'" followed by one
   or more letters from the "'i'", "'m'", "'s'", "'x'".) The letters
   set or remove the corresponding flags for the part of the
   expression:

   * "re.A" (ASCII-only matching)

   * "re.I" (ignore case)

   * "re.L" (locale dependent)

   * "re.M" (multi-line)

   * "re.S" (dot matches all)

   * "re.U" (Unicode matching)

   * "re.X" (verbose)

   (The flags are described in Contenidos del módulo.)

   The letters "'a'", "'L'" and "'u'" are mutually exclusive when used
   as inline flags, so they can't be combined or follow "'-'".
   Instead, when one of them appears in an inline group, it overrides
   the matching mode in the enclosing group.  In Unicode patterns
   "(?a:...)" switches to ASCII-only matching, and "(?u:...)" switches
   to Unicode matching (default).  In bytes patterns "(?L:...)"
   switches to locale dependent matching, and "(?a:...)" switches to
   ASCII-only matching (default). This override is only in effect for
   the narrow inline group, and the original matching mode is restored
   outside of the group.

   Added in version 3.6.

   Distinto en la versión 3.7: Las letras "'a'", "'L'" y "'u'" también
   pueden ser usadas en un grupo.

"(?>...)"
   Intenta hacer coincidir "..." como si fuera una expresión regular
   separada, y si tiene éxito, continúa coincidiendo con el resto del
   patrón que la sigue. Si el patrón posterior no coincide, la pila
   solo se puede desenrollar a un punto *antes* del "(?>...)" Porque
   una vez que salió, la expresión, conocida como *grupo atomico
   <atomic group>*, ha desechado todos los puntos de pila dentro de sí
   misma. Por lo tanto, "(?>.*)." nunca coincidiría con nada porque
   primero el ".*" coincidiría con todos los caracteres posibles,
   luego, al no tener nada que igualar, el "." final no coincidiría.
   Dado que no hay puntos de pila guardados en el Grupo Atómico, y no
   hay ningún punto de pila antes de él, toda la expresión no
   coincidiría.

   Added in version 3.11.

"(?P<name>...)"
   Similar a los paréntesis regulares, pero la subcadena coincidente
   con el grupo es accesible a través del nombre simbólico del grupo,
   *name*. Los nombres de grupo deben ser identificadores válidos de
   Python, y en los patrones de "bytes" solo pueden contener bytes en
   el rango ASCII.  Cada nombre de grupo debe ser definido sólo una
   vez dentro de una expresión regular.  Un grupo simbólico es también
   un grupo numerado, del mismo modo que si el grupo no tuviera
   nombre.

   Los grupos con nombre pueden ser referenciados en tres contextos.
   Si el patrón es "(?P<quote>['"]).*?(?P=quote)" (es decir, hacer
   coincidir una cadena citada con comillas simples o dobles):

   +-----------------------------------------+------------------------------------+
   | Contexto de la referencia al grupo      | Formas de hacer referencia         |
   | *quote* (cita)                          |                                    |
   |=========================================|====================================|
   | en el mismo patrón en sí mismo          | * "(?P=quote)" (como se muestra)   |
   |                                         | * "\1"                             |
   +-----------------------------------------+------------------------------------+
   | cuando se procesa el objeto de la       | * "m.group('quote')"  *            |
   | coincidencia *m*                        | "m.end('quote')" (etc.)            |
   +-----------------------------------------+------------------------------------+
   | en una cadena pasada al argumento       | * "\g<quote>"  * "\g<1>"  * "\1"   |
   | *repl* de "re.sub()"                    |                                    |
   +-----------------------------------------+------------------------------------+

   Distinto en la versión 3.12: En patrones de tipo "bytes", el nombre
   del grupo *name* solo puede contener bytes en el rango ASCII
   ("b'\x00'"-"b'\x7f'").

"(?P=name)"
   Una referencia inversa a un grupo nombrado; coincide con cualquier
   texto correspondido por el grupo anterior llamado *name*.

"(?#...)"
   Un comentario; el contenido de los paréntesis es simplemente
   ignorado.

"(?=...)"
   Coincide si "…" coincide con el siguiente patrón, pero no procesa
   nada de la cadena. Esto se llama una *lookahead assertion*
   (aserción de búsqueda anticipada). Por ejemplo, "Isaac (?=Asimov)"
   coincidirá con "'Isaac '" sólo si va seguido de "'Asimov'".

"(?!...)"
   Coincide si "…" no coincide con el siguiente. Esta es una *negative
   lookahead assertion* (aserción negativa de búsqueda anticipada).
   Por ejemplo, "Isaac (?!Asimov)" coincidirá con "'Isaac '" sólo si
   *no* es seguido por "'Asimov'".

"(?<=...)"
   Coincide si la posición actual en la cadena es precedida por una
   coincidencia para "…" que termina en la posición actual.  Esto se
   llama una *positive lookbehind assertion* (aserciones positivas de
   búsqueda tardía). "(?<=abc)def" encontrará una coincidencia en
   "'abcdef'", ya que la búsqueda tardía hará una copia de seguridad
   de 3 caracteres y comprobará si el patrón contenido coincide. El
   patrón contenido sólo debe coincidir con cadenas de alguna longitud
   fija, lo que significa que "abc" o "a|b" están permitidas, pero
   "a*" y "a{3,4}" no lo están.  Hay que tener en cuenta que los
   patrones que empiezan con aserciones positivas de búsqueda tardía
   no coincidirán con el principio de la cadena que se está buscando;
   lo más probable es que se quiera usar la función "search()" en
   lugar de la función "match()":

   >>> import re
   >>> m = re.search('(?<=abc)def', 'abcdef')
   >>> m.group(0)
   'def'

   Este ejemplo busca una palabra seguida de un guión:

   >>> m = re.search(r'(?<=-)\w+', 'spam-egg')
   >>> m.group(0)
   'egg'

   Distinto en la versión 3.5: Se añadió soporte a las referencias de
   grupo de longitud fija.

"(?<!...)"
   Coincide si la posición actual en la cadena no está precedida por
   una coincidencia de "…".  Esto se llama una *negative lookbehind
   assertion* (Aserciones negativas de búsqueda tardía).  Similar a
   las aserciones positivas de búsqueda tardía, el patrón contenido
   sólo debe coincidir con cadenas de alguna longitud fija.  Los
   patrones que empiezan con aserciones negativas pueden coincidir al
   principio de la cadena que se busca.

"(?(id/name)yes-pattern|no-pattern)"
   Will try to match with "yes-pattern" if the group with given *id*
   or *name* exists, and with "no-pattern" if it doesn't. "no-pattern"
   is optional and can be omitted. For example,
   "(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)" is a poor email matching
   pattern, which matches "'<user@host.com>'" as well as
   "'user@host.com'", but does not match "'<user@host.com'" nor
   "'user@host.com>'" in their entirety ("re.search()" finds only
   "'user@host.com'" in the former).

   Distinto en la versión 3.12: El *id* del grupo solo puede contener
   dígitos ASCII. En patrones de tipo "bytes", el *name* del grupo
   solo puede contener bytes en el rango ASCII ("b'\x00'"-"b'\x7f'").

Las secuencias especiales consisten en "'\'" y un carácter de la lista
que aparece más adelante. Si el carácter ordinario no es un dígito
ASCII o una letra ASCII, entonces el RE resultante coincidirá con el
segundo carácter.  Por ejemplo, "\$" coincide con el carácter "'$'".

"\number"
   Coincide con el contenido del grupo del mismo número.  Los grupos
   se numeran empezando por el 1. Por ejemplo, "(.+) \1" coincide con
   "'el el'" o "'55 55'", pero no con "'elel'" (notar el espacio
   después del grupo).  Esta secuencia especial sólo puede ser usada
   para hacer coincidir uno de los primeros 99 grupos.  Si el primer
   dígito del *número* es 0, o el *número* tiene 3 dígitos octales, no
   se interpretará como una coincidencia de grupo, sino como el
   carácter con valor octal *número*. Dentro de los "'['" y "']'" de
   una clase de caracteres, todos los escapes numéricos son tratados
   como caracteres.

"\A"
   Coincide sólo al principio de la cadena.

"\b"
   Matches the empty string, but only at the beginning or end of a
   word. A word is defined as a sequence of word characters. Note that
   formally, "\b" is defined as the boundary between a "\w" and a "\W"
   character (or vice versa), or between "\w" and the beginning or end
   of the string. This means that "r'\bat\b'" matches "'at'", "'at.'",
   "'(at)'", and "'as at ay'" but not "'attempt'" or "'atlas'".

   The default word characters in Unicode (str) patterns are Unicode
   alphanumerics and the underscore, but this can be changed by using
   the "ASCII" flag. Word boundaries are determined by the current
   locale if the "LOCALE" flag is used.

   Nota:

     Inside a character range, "\b" represents the backspace
     character, for compatibility with Python's string literals.

"\B"
   Matches the empty string, but only when it is *not* at the
   beginning or end of a word. This means that "r'at\B'" matches
   "'athens'", "'atom'", "'attorney'", but not "'at'", "'at.'", or
   "'at!'". "\B" is the opposite of "\b", so word characters in
   Unicode (str) patterns are Unicode alphanumerics or the underscore,
   although this can be changed by using the "ASCII" flag. Word
   boundaries are determined by the current locale if the "LOCALE"
   flag is used.

   Distinto en la versión 3.14: "\B" now matches empty input string.

"\d"
   Para los patrones de Unicode (str):
      Matches any Unicode decimal digit (that is, any character in
      Unicode character category [Nd]). This includes "[0-9]", and
      also many other digit characters.

      Matches "[0-9]" if the "ASCII" flag is used.

   Para patrones de 8 bits (bytes):
      Matches any decimal digit in the ASCII character set; this is
      equivalent to "[0-9]".

"\D"
   Matches any character which is not a decimal digit. This is the
   opposite of "\d".

   Matches "[^0-9]" if the "ASCII" flag is used.

"\s"
   Para los patrones de Unicode (str):
      Matches Unicode whitespace characters (as defined by
      "str.isspace()"). This includes "[ \t\n\r\f\v]", and also many
      other characters, for example the non-breaking spaces mandated
      by typography rules in many languages.

      Matches "[ \t\n\r\f\v]" if the "ASCII" flag is used.

   Para patrones de 8 bits (bytes):
      Coincide con los caracteres considerados como espacios en blanco
      en el conjunto de caracteres ASCII, lo que equivale a "[
      \t\n\r\f\v]".

"\S"
   Matches any character which is not a whitespace character. This is
   the opposite of "\s".

   Matches "[^ \t\n\r\f\v]" if the "ASCII" flag is used.

"\w"
   Para los patrones de Unicode (str):
      Matches Unicode word characters; this includes all Unicode
      alphanumeric characters (as defined by "str.isalnum()"), as well
      as the underscore ("_").

      Matches "[a-zA-Z0-9_]" if the "ASCII" flag is used.

   Para patrones de 8 bits (bytes):
      Matches characters considered alphanumeric in the ASCII
      character set; this is equivalent to "[a-zA-Z0-9_]". If the
      "LOCALE" flag is used, matches characters considered
      alphanumeric in the current locale and the underscore.

"\W"
   Matches any character which is not a word character. This is the
   opposite of "\w". By default, matches non-underscore ("_")
   characters for which "str.isalnum()" returns "False".

   Matches "[^a-zA-Z0-9_]" if the "ASCII" flag is used.

   If the "LOCALE" flag is used, matches characters which are neither
   alphanumeric in the current locale nor the underscore.

"\z"
   Coincide sólo el final de la cadena.

   Added in version 3.14.

"\Z"
   The same as "\z".  For compatibility with old Python versions.

La mayoría de las secuencias de escape soportadas por los literales de
cadena de Python también son aceptadas por el analizador de
expresiones regulares:

   \a      \b      \f      \n
   \N      \r      \t      \u
   \U      \v      \x      \\

(Notar que "\b" se usa para representar los límites de las palabras, y
significa "retroceso" (*backspace*) sólo dentro de las clases de
caracteres.)

"'\u'", "'\U'", and "'\N'" escape sequences are only recognized in
Unicode (str) patterns. In bytes patterns they are errors. Unknown
escapes of ASCII letters are reserved for future use and treated as
errors.

Los escapes octales se incluyen en una forma limitada.  Si el primer
dígito es un 0, o si hay tres dígitos octales, se considera un escape
octal. De lo contrario, es una referencia de grupo.  En cuanto a los
literales de cadena, los escapes octales siempre tienen como máximo
tres dígitos de longitud.

Distinto en la versión 3.3: Se han añadido las secuencias de escape
"'\u'" y "'\U'".

Distinto en la versión 3.6: Los escapes desconocidos que consisten en
"'\'" y una letra ASCII ahora son errores.

Distinto en la versión 3.8: Se añadió la secuencia de escape
"'\N{*name*}'". Como en los literales de cadena, se expande al
carácter Unicode nombrado (p. ej. "'\N{EM DASH}'").

## Contenidos del módulo

El módulo define varias funciones, constantes y una excepción. Algunas
de las funciones son versiones simplificadas de los métodos completos
de las expresiones regulares compiladas.  La mayoría de las
aplicaciones no triviales utilizan siempre la forma compilada.

### Indicadores

Distinto en la versión 3.6: Ahora las constantes de indicadores son
instancias de "RegexFlag", que es una subclase de "enum.IntFlag".

class re.RegexFlag

   Una clase "enum.IntFlag" contiene las opciones regex que se
   enumeran a continuación.

   Added in version 3.11: - added to "__all__"

re.A
re.ASCII

   Make "\w", "\W", "\b", "\B", "\d", "\D", "\s" and "\S" perform
   ASCII-only matching instead of full Unicode matching.  This is only
   meaningful for Unicode (str) patterns, and is ignored for bytes
   patterns.

   Corresponds to the inline flag "(?a)".

   Nota:

     The "U" flag still exists for backward compatibility, but is
     redundant in Python 3 since matches are Unicode by default for
     "str" patterns, and Unicode matching isn't allowed for bytes
     patterns. "UNICODE" and the inline flag "(?u)" are similarly
     redundant.

re.DEBUG

   Display debug information about compiled expression.

   No corresponding inline flag.

re.I
re.IGNORECASE

   Perform case-insensitive matching; expressions like "[A-Z]" will
   also  match lowercase letters. Full Unicode matching (such as "Ü"
   matching "ü") also works unless the "ASCII" flag is used to disable
   non-ASCII matches. The current locale does not change the effect of
   this flag unless the "LOCALE" flag is also used.

   Corresponds to the inline flag "(?i)".

   Note that when the Unicode patterns "[a-z]" or "[A-Z]" are used in
   combination with the "IGNORECASE" flag, they will match the 52
   ASCII letters and 4 additional non-ASCII letters: 'İ' (U+0130,
   Latin capital letter I with dot above), 'ı' (U+0131, Latin small
   letter dotless i), 'ſ' (U+017F, Latin small letter long s) and 'K'
   (U+212A, Kelvin sign). If the "ASCII" flag is used, only letters
   'a' to 'z' and 'A' to 'Z' are matched.

re.L
re.LOCALE

   Make "\w", "\W", "\b", "\B" and case-insensitive matching dependent
   on the current locale. This flag can be used only with bytes
   patterns.

   Corresponds to the inline flag "(?L)".

   Advertencia:

     This flag is discouraged; consider Unicode matching instead. The
     locale mechanism is very unreliable as it only handles one
     "culture" at a time and only works with 8-bit locales. Unicode
     matching is enabled by default for Unicode (str) patterns and it
     is able to handle different locales and languages.

   Distinto en la versión 3.6: "LOCALE" can be used only with bytes
   patterns and is not compatible with "ASCII".

   Distinto en la versión 3.7: Compiled regular expression objects
   with the "LOCALE" flag no longer depend on the locale at compile
   time. Only the locale at matching time affects the result of
   matching.

re.M
re.MULTILINE

   When specified, the pattern character "'^'" matches at the
   beginning of the string and at the beginning of each line
   (immediately following each newline); and the pattern character
   "'$'" matches at the end of the string and at the end of each line
   (immediately preceding each newline).  By default, "'^'" matches
   only at the beginning of the string, and "'$'" only at the end of
   the string and immediately before the newline (if any) at the end
   of the string.

   Corresponds to the inline flag "(?m)".

re.NOFLAG

   Indica que no se aplica ninguna bandera, el valor es "0". Esta
   bandera puede ser utilizada como valor predeterminado para un
   argumento de palabra clave de función o como un valor que será
   condicionalmente combinado con otras banderas usando el operador
   binario OR. Ejemplo de uso como valor predeterminado:

      def myfunc(text, flag=re.NOFLAG):
          return re.match(text, flag)

   Added in version 3.11.

re.S
re.DOTALL

   Make the "'.'" special character match any character at all,
   including a newline; without this flag, "'.'" will match anything
   *except* a newline.

   Corresponds to the inline flag "(?s)".

re.U
re.UNICODE

   In Python 3, Unicode characters are matched by default for "str"
   patterns. This flag is therefore redundant with **no effect** and
   is only kept for backward compatibility.

   See "ASCII" to restrict matching to ASCII characters instead.

re.X
re.VERBOSE

   Esta bandera permite escribir expresiones regulares que se ven
   mejor y son más legibles, facilitando la separación visual de las
   secciones lógicas del patrón y la adición de comentarios. Los
   espacios en blanco dentro del patrón se ignoran, excepto cuando
   están en una clase de caracteres, o cuando están precedidos por una
   barra inversa sin escapar, o dentro de tokens como "*?", "(?:" o
   "(?P<...>". Por ejemplo, "(? :" y "* ?" no están permitidos. Cuando
   una línea contiene un "#" que no está en una clase de caracteres y
   no está precedida por una barra inversa sin escapar, todos los
   caracteres desde el "#" más a la izquierda hasta el final de la
   línea son ignorados.

   Esto significa que los dos siguientes objetos expresión regular que
   coinciden con un número decimal son funcionalmente iguales:

      a = re.compile(r"""\d +  # the integral part
                         \.    # the decimal point
                         \d *  # some fractional digits""", re.X)
      b = re.compile(r"\d+\.\d*")

   Corresponde al indicador en línea "(?x)".

### Funciones

re.compile(pattern, flags=0)

   Compila un patrón de expresión regular en un objeto de expresión
   regular, que puede ser usado para las coincidencias usando
   "match()", "search()" y otros métodos, descritos más adelante.

   The expression's behaviour can be modified by specifying a *flags*
   value. Values can be any of the flags variables, combined using
   bitwise OR (the "|" operator).

   La secuencia

      prog = re.compile(pattern)
      result = prog.match(string)

   es equivalente a

      result = re.match(pattern, string)

   pero usando "re.compile()" y guardando el objeto resultante de la
   expresión regular para su reutilización es más eficiente cuando la
   expresión será usada varias veces en un solo programa.

   Nota:

     Las versiones compiladas de los patrones más recientes pasaron a
     "re.compile()" y las funciones de coincidencia a nivel de módulo
     están en caché, así que los programas que usan sólo unas pocas
     expresiones regulares a la vez no tienen que preocuparse de
     compilar expresiones regulares.

re.search(pattern, string, flags=0)

   Explora la cadena de caracteres *string* en busca de la primera
   ubicación donde el patrón *pattern* de la expresión regular produce
   una coincidencia, y retorna un "Match" correspondiente. Retorna
   "None" si ninguna posición en la cadena coincide con el patrón;
   nota que esto es diferente a encontrar una coincidencia de longitud
   cero en algún punto de la cadena.

   The expression's behaviour can be modified by specifying a *flags*
   value. Values can be any of the flags variables, combined using
   bitwise OR (the "|" operator).

re.match(pattern, string, flags=0)

   Si cero o más caracteres al principio de la cadena *string*
   coinciden con el patrón *pattern* de la expresión regular, retorna
   un "Match" correspondiente. Retorna "None" si la cadena no coincide
   con el patrón; notar que esto es diferente de una coincidencia de
   longitud cero.

   Notar que incluso en el modo "MULTILINE", "re.match()" sólo
   coincidirá al principio de la cadena y no al principio de cada
   línea.

   Si se quiere localizar una coincidencia en cualquier lugar de la
   *string* ("cadena"), se utiliza "search()" en su lugar (ver también
   search() vs. match()).

   The expression's behaviour can be modified by specifying a *flags*
   value. Values can be any of the flags variables, combined using
   bitwise OR (the "|" operator).

re.fullmatch(pattern, string, flags=0)

   Si toda la cadena *string* coincide con el patrón *pattern* de la
   expresión regular, retorna un "Match" correspondiente. Retorna
   "None" si la cadena no coincide con el patrón; notar que esto es
   diferente de una coincidencia de longitud cero.

   The expression's behaviour can be modified by specifying a *flags*
   value. Values can be any of the flags variables, combined using
   bitwise OR (the "|" operator).

   Added in version 3.4.

re.split(pattern, string, maxsplit=0, flags=0)

   Divide la *string* ("cadena") por el número de ocurrencias del
   *pattern* ("patrón").  Si se utilizan paréntesis de captura en
   *pattern*, entonces el texto de todos los grupos en el patrón
   también se retornan como parte de la lista resultante. Si
   *maxsplit* (máxima divisibilidad) es distinta de cero, como mucho
   se producen *maxsplit* divisiones, y el resto de la cadena se
   retorna como elemento final de la lista.

      >>> re.split(r'\W+', 'Words, words, words.')
      ['Words', 'words', 'words', '']
      >>> re.split(r'(\W+)', 'Words, words, words.')
      ['Words', ', ', 'words', ', ', 'words', '.', '']
      >>> re.split(r'\W+', 'Words, words, words.', maxsplit=1)
      ['Words', 'words, words.']
      >>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
      ['0', '3', '9']

   Si hay grupos de captura en el separador y coincide al principio de
   la cadena, el resultado comenzará con una cadena vacía.  Lo mismo
   ocurre con el final de la cadena:

      >>> re.split(r'(\W+)', '...words, words...')
      ['', '...', 'words', ', ', 'words', '...', '']

   De esa manera, los componentes de los separadores se encuentran
   siempre en los mismos índices relativos dentro de la lista de
   resultados.

   Adjacent empty matches are not possible, but an empty match can
   occur immediately after a non-empty match.

      >>> re.split(r'\b', 'Words, words, words.')
      ['', 'Words', ', ', 'words', ', ', 'words', '.']
      >>> re.split(r'\W*', '...words...')
      ['', '', 'w', 'o', 'r', 'd', 's', '', '']
      >>> re.split(r'(\W*)', '...words...')
      ['', '...', '', '', 'w', '', 'o', '', 'r', '', 'd', '', 's', '...', '', '', '']

   The expression's behaviour can be modified by specifying a *flags*
   value. Values can be any of the flags variables, combined using
   bitwise OR (the "|" operator).

   Distinto en la versión 3.1: Se añadió el argumento de los
   indicadores opcionales.

   Distinto en la versión 3.7: Se añadió el soporte de la división en
   un patrón que podría coincidir con una cadena vacía.

   Obsoleto desde la versión 3.13: Passing *maxsplit* and *flags* as
   positional arguments is deprecated. In future Python versions they
   will be keyword-only parameters.

re.findall(pattern, string, flags=0)

   Retorna todas las coincidencias no superpuestas de *pattern* en
   *string*, como una lista de strings o tuplas. El *string* se
   escanea de izquierda a derecha y las coincidencias se retornan en
   el orden en que se encuentran. Las coincidencias vacías se incluyen
   en el resultado.

   El resultado depende del número de grupos detectados en el patrón.
   Si no hay grupos, retorna una lista de strings que coincidan con el
   patrón completo. Si existe exactamente un grupo, retorna una lista
   de strings que coincidan con ese grupo. Si hay varios grupos
   presentes, retorna una lista de tuplas de strings que coinciden con
   los grupos. Los grupos que no son detectados no afectan la forma
   del resultado.

   >>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
   ['foot', 'fell', 'fastest']
   >>> re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
   [('width', '20'), ('height', '10')]

   The expression's behaviour can be modified by specifying a *flags*
   value. Values can be any of the flags variables, combined using
   bitwise OR (the "|" operator).

   Distinto en la versión 3.7: Las coincidencias no vacías ahora
   pueden empezar justo después de una coincidencia vacía anterior.

re.finditer(pattern, string, flags=0)

   Retorna un *iterador* que produce objetos "Match" sobre todas las
   coincidencias no superpuestas para el patrón de RE *pattern* en la
   *string*. La *string* es examinada de izquierda a derecha, y las
   coincidencias son retornadas en el orden en que se encuentran. Las
   coincidencias vacías se incluyen en el resultado.

   The expression's behaviour can be modified by specifying a *flags*
   value. Values can be any of the flags variables, combined using
   bitwise OR (the "|" operator).

   Distinto en la versión 3.7: Las coincidencias no vacías ahora
   pueden empezar justo después de una coincidencia vacía anterior.

re.sub(pattern, repl, string, count=0, flags=0)

   Retorna la cadena obtenida reemplazando las ocurrencias no
   superpuestas del *pattern* ("patrón") en la *string* ("cadena") por
   el reemplazo de *repl*.  Si el patrón no se encuentra, se retorna
   *string* sin cambios.  *repl* puede ser una cadena o una función;
   si es una cadena, cualquier barra inversa escapada en ella es
   procesada.  Es decir, "\n" se convierte en un carácter de una sola
   línea nueva, "\r" se convierte en un retorno de carro, y así
   sucesivamente.  Los escapes desconocidos de las letras ASCII se
   reservan para un uso futuro y se tratan como errores.  Otros
   escapes desconocidos como "\&" no se utilizan. Las referencias
   inversas, como "\6", se reemplazan por la subcadena que corresponde
   al grupo 6 del patrón. Por ejemplo:

      >>> re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
      ...        r'static PyObject*\npy_\1(void)\n{',
      ...        'def myfunc():')
      'static PyObject*\npy_myfunc(void)\n{'

   Si *repl* es una función, se llama para cada ocurrencia no
   superpuesta de *pattern*.  La función toma un solo argumento
   "Match", y retorna la cadena de sustitución.  Por ejemplo:

      >>> def dashrepl(matchobj):
      ...     if matchobj.group(0) == '-': return ' '
      ...     else: return '-'
      ...
      >>> re.sub('-{1,2}', dashrepl, 'pro----gram-files')
      'pro--gram files'
      >>> re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
      'Baked Beans & Spam'

   El patrón puede ser una cadena o un "Pattern".

   The optional argument *count* is the maximum number of pattern
   occurrences to be replaced; *count* must be a non-negative integer.
   If omitted or zero, all occurrences will be replaced.

   Adjacent empty matches are not possible, but an empty match can
   occur immediately after a non-empty match. As a result, "sub('x*',
   '-', 'abxd')" returns "'-a-b--d-'" instead of "'-a-b-d-'".

   En los argumentos *repl* de tipo cadena, además de los escapes de
   caracteres y las referencias inversas descritas anteriormente,
   "\g<name>" usará la subcadena coincidente con el grupo llamado
   "name", como se define en la sintaxis "(?P<name>...)". "\g<number>"
   utiliza el número de grupo correspondiente; "\g<2>" es por lo tanto
   equivalente a "\2", pero no es ambiguo en un reemplazo como sucede
   con "\g<2>0".  "\20" se interpretaría como una referencia al grupo
   20, no como una referencia al grupo 2 seguido del carácter literal
   "'0'".  La referencia inversa "\g<0>" sustituye en toda la
   subcadena coincidente con la RE.

   The expression's behaviour can be modified by specifying a *flags*
   value. Values can be any of the flags variables, combined using
   bitwise OR (the "|" operator).

   Distinto en la versión 3.1: Se añadió el argumento de los
   indicadores opcionales.

   Distinto en la versión 3.5: Los grupos no coincidentes son
   reemplazados por una cadena vacía.

   Distinto en la versión 3.6: Los escapes desconocidos en el
   *pattern* que consisten en "'\'" y una letra ASCII ahora son
   errores.

   Distinto en la versión 3.7: Unknown escapes in *repl* consisting of
   "'\'" and an ASCII letter now are errors. An empty match can occur
   immediately after a non-empty match.

   Distinto en la versión 3.12: El *id* del grupo solo puede contener
   dígitos ASCII. En las cadenas de reemplazo "bytes", el nombre del
   grupo *name* solo puede contener bytes en el rango ASCII
   ("b'\x00'"-"b'\x7f'").

   Obsoleto desde la versión 3.13: Passing *count* and *flags* as
   positional arguments is deprecated. In future Python versions they
   will be keyword-only parameters.

re.subn(pattern, repl, string, count=0, flags=0)

   Realiza la misma operación que "sub()", pero retorna una tupla
   "(new_string, number_of_subs_made)".

   The expression's behaviour can be modified by specifying a *flags*
   value. Values can be any of the flags variables, combined using
   bitwise OR (the "|" operator).

re.escape(pattern)

   Caracteres de escape especiales en *pattern* (" patrón"). Esto es
   útil si quieres hacer coincidir una cadena literal arbitraria que
   puede tener metacaracteres de expresión regular en ella.  Por
   ejemplo:

      >>> print(re.escape('https://www.python.org'))
      https://www\.python\.org

      >>> legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
      >>> print('[%s]+' % re.escape(legal_chars))
      [abcdefghijklmnopqrstuvwxyz0123456789!\#\$%\&'\*\+\-\.\^_`\|\~:]+

      >>> operators = ['+', '-', '*', '/', '**']
      >>> print('|'.join(map(re.escape, sorted(operators, reverse=True))))
      /|\-|\+|\*\*|\*

   Esta función no debe usarse para la cadena de reemplazo en "sub()"
   y "subn()", sólo deben escaparse las barras inversas.  Por ejemplo:

      >>> digits_re = r'\d+'
      >>> sample = '/usr/sbin/sendmail - 0 errors, 12 warnings'
      >>> print(re.sub(digits_re, digits_re.replace('\\', r'\\'), sample))
      /usr/sbin/sendmail - \d+ errors, \d+ warnings

   Distinto en la versión 3.3: El carácter de "'_'" ya no se escapa.

   Distinto en la versión 3.7: Sólo se escapan los caracteres que
   pueden tener un significado especial en una expresión regular. Como
   resultado, "'!'", "'"'", "'%'", ""'"", "','", "'/'", "':'", "';'",
   "'<'", "'='", "'>'", "'@'" y ""`"" ya no se escapan.

re.purge()

   Despeja la caché de expresión regular.

### Excepciones

exception re.PatternError(msg, pattern=None, pos=None)

   Exception raised when a string passed to one of the functions here
   is not a valid regular expression (for example, it might contain
   unmatched parentheses) or when some other error occurs during
   compilation or matching.  It is never an error if a string contains
   no match for a pattern.  The "PatternError" instance has the
   following additional attributes:

   msg

      El mensaje de error sin formato.

   pattern

      El patrón de expresión regular.

   pos

      El índice en *pattern* ("patrón") donde la compilación falló
      (puede ser "None").

   lineno

      La línea correspondiente a *pos* (puede ser "None").

   colno

      La columna correspondiente a *pos* (puede ser "None").

   Distinto en la versión 3.5: Se añadieron atributos adicionales.

   Distinto en la versión 3.13: "PatternError" was originally named
   "error"; the latter is kept as an alias for backward compatibility.

## Objetos expresión regular

class re.Pattern

   Objeto de expresión regular compilada devuelto por "re.compile()".

   Patterns are generic over the type of string they handle ("str" or
   "bytes").

   Distinto en la versión 3.9: "re.Pattern" soporta "[]" para indicar
   un patrón Unicode (str) o de bytes. Ver Tipo Alias Genérico.

Pattern.search(string[, pos[, endpos]])

   Escanea a través de la cadena *string* buscando la primera
   ubicación donde esta expresión regular produce una coincidencia, y
   retorna un "Match" correspondiente.  Retorna "None" si ninguna
   posición en la cadena coincide con el patrón; notar que esto es
   diferente a encontrar una coincidencia de longitud cero en algún
   punto de la cadena.

   El segundo parámetro opcional *pos* proporciona un índice en la
   cadena donde la búsqueda debe comenzar; por defecto es "0".  Esto
   no es completamente equivalente a dividir la cadena; el patrón de
   carácter "'^'" coincide en el inicio real de la cadena y en las
   posiciones justo después de una nueva línea, pero no necesariamente
   en el índice donde la búsqueda va a comenzar.

   El parámetro opcional *endpos* limita hasta dónde se buscará la
   cadena; será como si la cadena fuera de *endpos* caracteres de
   largo, por lo que sólo se buscará una coincidencia entre los
   caracteres de *pos* a "endpos - 1".  Si *endpos* es menor que
   *pos*, no se encontrará ninguna coincidencia; de lo contrario, si
   *rx* es un objeto de expresión regular compilado,
   "rx.search(string, 0, 50)" es equivalente a "rx.search(string[:50],
   0)".

      >>> pattern = re.compile("d")
      >>> pattern.search("dog")     # Match at index 0
      <re.Match object; span=(0, 1), match='d'>
      >>> pattern.search("dog", 1)  # No match; search doesn't include the "d"

Pattern.match(string[, pos[, endpos]])

   Si cero o más caracteres en el comienzo *beginning* de la cadena
   *string* coinciden con esta expresión regular, retorna un "Match"
   correspondiente. Retorna "None" si la cadena no coincide con el
   patrón; notar que esto es diferente de una coincidencia de longitud
   cero.

   Los parámetros opcionales *pos* y *endpos* tienen el mismo
   significado que para el método "search()".

      >>> pattern = re.compile("o")
      >>> pattern.match("dog")      # No match as "o" is not at the start of "dog".
      >>> pattern.match("dog", 1)   # Match as "o" is the 2nd character of "dog".
      <re.Match object; span=(1, 2), match='o'>

   Si se quiere encontrar una coincidencia en cualquier lugar de
   *string*, utilizar "search()" en su lugar (ver también search() vs.
   match()).

Pattern.fullmatch(string[, pos[, endpos]])

   Si toda la cadena *string* coincide con esta expresión regular,
   retorna un "Match" correspondiente.  Retorna "None" si la cadena no
   coincide con el patrón; notar que esto es diferente de una
   coincidencia de longitud cero.

   Los parámetros opcionales *pos* y *endpos* tienen el mismo
   significado que para el método "search()".

      >>> pattern = re.compile("o[gh]")
      >>> pattern.fullmatch("dog")      # No match as "o" is not at the start of "dog".
      >>> pattern.fullmatch("ogre")     # No match as not the full string matches.
      >>> pattern.fullmatch("doggie", 1, 3)   # Matches within given limits.
      <re.Match object; span=(1, 3), match='og'>

   Added in version 3.4.

Pattern.split(string, maxsplit=0)

   Idéntico a la función "split()", usando el patrón compilado.

Pattern.findall(string[, pos[, endpos]])

   Similar a la función "findall()", usando el patrón compilado, pero
   también acepta parámetros opcionales *pos* y *endpos* que limitan
   la región de búsqueda como para "search()".

Pattern.finditer(string[, pos[, endpos]])

   Similar a la función "finditer()", usando el patrón compilado, pero
   también acepta parámetros opcionales *pos* y *endpos* que limitan
   la región de búsqueda como para "search()".

Pattern.sub(repl, string, count=0)

   Idéntico a la función "sub()", usando el patrón compilado.

Pattern.subn(repl, string, count=0)

   Idéntico a la función "subn()", usando el patrón compilado.

Pattern.flags

   The regex matching flags.  This is a combination of the flags given
   to "compile()", any "(?...)" inline flags in the pattern, and
   implicit flags such as "UNICODE" if the pattern is a Unicode
   string.

Pattern.groups

   El número de grupos de captura en el patrón.

Pattern.groupindex

   Un diccionario que mapea cualquier nombre de grupo simbólico
   definido por "(?P<id>)" para agrupar números.  El diccionario está
   vacío si no se utilizaron grupos simbólicos en el patrón.

Pattern.pattern

   La cadena de patrones a partir de la cual el objeto de patrón fue
   compilado.

Distinto en la versión 3.7: Se añadió el soporte de "copy.copy()" y
"copy.deepcopy()".  Los objetos expresión regular compilados se
consideran atómicos.

## Objetos de coincidencia

Los objetos de coincidencia siempre tienen un valor booleano de "True"
("Verdadero"). Ya que "match()" y "search()" retornan "None" cuando no
hay coincidencia. Se puede probar si hubo una coincidencia con una
simple declaración "if":

   match = re.search(pattern, string)
   if match:
       process(match)

class re.Match

   Objeto Match devuelto por llamadas exitosas a "match" y "search".

   Matches are generic over the type of string which was matched
   ("str" or "bytes").

   Distinto en la versión 3.9: "re.Match" soporta "[]" para indicar
   una coincidencia Unicode (str) o de bytes. Ver Tipo Alias Genérico.

Match.expand(template)

   Return the string obtained by doing backslash substitution on the
   template string *template*, as done by the "sub()" method. Escapes
   such as "\n" are converted to the appropriate characters, and
   numeric backreferences ("\1", "\2") and named backreferences
   ("\g<1>", "\g<name>") are replaced by the contents of the
   corresponding group. The backreference "\g<0>" will be replaced by
   the entire match.

   Distinto en la versión 3.5: Los grupos no coincidentes son
   reemplazados por una cadena vacía.

Match.group([group1, ...])

   Returns one or more subgroups of the match.  If there is a single
   argument, the result is a single string; if there are multiple
   arguments, the result is a tuple with one item per argument.
   Without arguments, *group1* defaults to zero (the whole match is
   returned). If a *groupN* argument is zero, the corresponding return
   value is the entire matching string; if it is a positive integer,
   it is the string matching the corresponding parenthesized group.
   If a group number is negative or larger than the number of groups
   defined in the pattern, an "IndexError" exception is raised. If a
   group is contained in a part of the pattern that did not match, the
   corresponding result is "None". If a group is contained in a part
   of the pattern that matched multiple times, the last match is
   returned.

      >>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
      >>> m.group(0)       # The entire match
      'Isaac Newton'
      >>> m.group(1)       # The first parenthesized subgroup.
      'Isaac'
      >>> m.group(2)       # The second parenthesized subgroup.
      'Newton'
      >>> m.group(1, 2)    # Multiple arguments give us a tuple.
      ('Isaac', 'Newton')

   Si la expresión regular usa la sintaxis "(?P<name>...)", los
   argumentos *groupN* también pueden ser cadenas que identifican a
   los grupos por su nombre de grupo.  Si un argumento de cadena no se
   usa como nombre de grupo en el patrón, se produce una excepción
   "IndexError".

   Un ejemplo moderadamente complicado:

      >>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
      >>> m.group('first_name')
      'Malcolm'
      >>> m.group('last_name')
      'Reynolds'

   Los grupos nombrados también pueden ser referidos por su índice:

      >>> m.group(1)
      'Malcolm'
      >>> m.group(2)
      'Reynolds'

   Si un grupo coincide varias veces, sólo se puede acceder a la
   última coincidencia:

      >>> m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
      >>> m.group(1)                        # Returns only the last match.
      'c3'

Match.__getitem__(g)

   Esto es idéntico a "m.group(g)".  Esto permite un acceso más fácil
   a un grupo individual de una coincidencia:

      >>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
      >>> m[0]       # The entire match
      'Isaac Newton'
      >>> m[1]       # The first parenthesized subgroup.
      'Isaac'
      >>> m[2]       # The second parenthesized subgroup.
      'Newton'

   Los grupos con nombre también son compatibles:

      >>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Isaac Newton")
      >>> m['first_name']
      'Isaac'
      >>> m['last_name']
      'Newton'

   Added in version 3.6.

Match.groups(default=None)

   Retorna una tupla que contenga todos los subgrupos de la
   coincidencia, desde 1 hasta tantos grupos como haya en el patrón.
   El argumento *default* ("por defecto") se utiliza para los grupos
   que no participaron en la coincidencia; por defecto es "None".

   Por ejemplo:

      >>> m = re.match(r"(\d+)\.(\d+)", "24.1632")
      >>> m.groups()
      ('24', '1632')

   Si hacemos que el decimal y todo lo que sigue sea opcional, no
   todos los grupos podrían participar en la coincidencia.  Estos
   grupos serán por defecto "None" a menos que se utilice el argumento
   *default*:

      >>> m = re.match(r"(\d+)\.?(\d+)?", "24")
      >>> m.groups()      # Second group defaults to None.
      ('24', None)
      >>> m.groups('0')   # Now, the second group defaults to '0'.
      ('24', '0')

Match.groupdict(default=None)

   Retorna un diccionario que contiene todos los subgrupos *nombrados*
   de la coincidencia, tecleado por el nombre del subgrupo.  El
   argumento *por defecto* se usa para los grupos que no participaron
   en la coincidencia; por defecto es "None".  Por ejemplo:

      >>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
      >>> m.groupdict()
      {'first_name': 'Malcolm', 'last_name': 'Reynolds'}

Match.start([group])
Match.end([group])

   Retorna los índices del comienzo y el final de la subcadena
   coincidiendo con el *group*; el *group* por defecto es cero (es
   decir, toda la subcadena coincidente). Retorna "-1" si *grupo*
   existe pero no ha contribuido a la coincidencia.  Para un objeto
   coincidente *m*, y un grupo *g* que sí contribuyó a la
   coincidencia, la subcadena coincidente con el grupo *g*
   (equivalente a "m.group(g)") es

      m.string[m.start(g):m.end(g)]

   Notar que "m.start(group)" será igual a "m.end(group)" si *group*
   coincidió con una cadena nula.  Por ejemplo, después de "m =
   re.search('b(c?)', 'cba')", "m.start(0)" es 1, "m.end(0)" es 2,
   "m.start(1)" y "m.end(1)" son ambos 2, y "m.start(2)" produce una
   excepción "IndexError".

   Un ejemplo que eliminará *remove_this* ("quita esto") de las
   direcciones de correo electrónico:

      >>> email = "tony@tiremove_thisger.net"
      >>> m = re.search("remove_this", email)
      >>> email[:m.start()] + email[m.end():]
      'tony@tiger.net'

Match.span([group])

   Para una coincidencia *m*, retorna la tupla-2 "(m.inicio(grupo),
   m.fin(grupo))". Notar que si *group* no contribuyó a la
   coincidencia, esto es "(-1, -1)". *group* por se convierte a cero
   para toda la coincidencia.

Match.pos

   El valor de *pos* que fue pasado al método "search()" o "match()"
   de un objeto regex.  Este es el índice de la cadena en la que el
   motor RE comenzó a buscar una coincidencia.

Match.endpos

   El valor de *endpos* que se pasó al método "search()" o "match()"
   de un objeto regex.  Este es el índice de la cadena más allá de la
   cual el motor RE no irá.

Match.lastindex

   El índice entero del último grupo de captura coincidente, o``None``
   si no hay ningún grupo coincidente. Por ejemplo, las expresiones
   "(a)b", "((a)(b))" y "((ab))" tendrán "lastindex == 1" si se
   aplican a la cadena "'ab'", mientras que la expresión "(a)(b)"
   tendrá "lastindex == 2", si se aplica a la misma cadena.

Match.lastgroup

   El nombre del último grupo capturador coincidente, o``None`` si el
   grupo no tenía nombre, o si no había ningún grupo coincidente.

Match.re

   El objeto de expresión regular cuyo método "match()" o "search()"
   produce esta instancia de coincidencia.

Match.string

   La cadena pasada a "match()" o "search()".

Distinto en la versión 3.7: Se añadió el soporte de "copy.copy()" y
"copy.deepcopy()".  Los objetos de coincidencia se consideran
atómicos.

## Ejemplos de expresiones regulares

### Buscando un par

En este ejemplo, se utilizará la siguiente función de ayuda para
mostrar los objetos de coincidencia con un poco más de elegancia:

   def displaymatch(match):
       if match is None:
           return None
       return '<Match: %r, groups=%r>' % (match.group(), match.groups())

Supongamos que se está escribiendo un programa de póquer en el que la
mano de un jugador se representa como una cadena de 5 caracteres en la
que cada carácter representa una carta, "a" para el as, "k" para el
rey, "q" para la reina, "j" para la jota, "t" para el 10, y del " 2"
al "9" representando la carta con ese valor.

Para ver si una cadena dada es una mano válida, se podría hacer lo
siguiente:

   >>> valid = re.compile(r"^[a2-9tjqk]{5}$")
   >>> displaymatch(valid.match("akt5q"))  # Valid.
   "<Match: 'akt5q', groups=()>"
   >>> displaymatch(valid.match("akt5e"))  # Invalid.
   >>> displaymatch(valid.match("akt"))    # Invalid.
   >>> displaymatch(valid.match("727ak"))  # Valid.
   "<Match: '727ak', groups=()>"

Esa última mano, ""727ak"", contenía un par, o dos de las mismas
cartas de valor. Para igualar esto con una expresión regular, se
podrían usar referencias inversas como tales:

   >>> pair = re.compile(r".*(.).*\1")
   >>> displaymatch(pair.match("717ak"))     # Pair of 7s.
   "<Match: '717', groups=('7',)>"
   >>> displaymatch(pair.match("718ak"))     # No pairs.
   >>> displaymatch(pair.match("354aa"))     # Pair of aces.
   "<Match: '354aa', groups=('a',)>"

Para averiguar en qué carta consiste el par, se podría utilizar el
método "group()" del objeto de coincidencia de la siguiente manera:

   >>> pair = re.compile(r".*(.).*\1")
   >>> pair.match("717ak").group(1)
   '7'

   # Error because re.match() returns None, which doesn't have a group() method:
   >>> pair.match("718ak").group(1)
   Traceback (most recent call last):
     File "<pyshell#23>", line 1, in <module>
       re.match(r".*(.).*\1", "718ak").group(1)
   AttributeError: 'NoneType' object has no attribute 'group'

   >>> pair.match("354aa").group(1)
   'a'

### Simular scanf()

Actualmente, Python no tiene un equivalente a "scanf()". Las
expresiones regulares son generalmente más poderosas, aunque también
más detalladas, que las cadenas de formato de "scanf()". La tabla
siguiente ofrece algunas correspondencias más o menos equivalentes
entre los tokens de formato de "scanf()" y expresiones regulares.

+----------------------------------+-----------------------------------------------+
| Token "scanf()"                  | Expresión regular                             |
|==================================|===============================================|
## | "%c"                             | "."                                           |

## | "%5c"                            | ".{5}"                                        |

## | "%d"                             | "[-+]?\d+"                                    |

## | "%e", "%E", "%f", "%g"           | "[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?"     |

## | "%i"                             | "[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)"         |

## | "%o"                             | "[-+]?[0-7]+"                                 |

## | "%s"                             | "\S+"                                         |

## | "%u"                             | "\d+"                                         |

## | "%x", "%X"                       | "[-+]?(0[xX])?[\dA-Fa-f]+"                    |

Para extraer el nombre de archivo y los números de una cadena como

   /usr/sbin/sendmail - 0 errors, 4 warnings

utilizaría un formato "scanf()" como

   %s - %d errors, %d warnings

La expresión regular equivalente sería

   (\S+) - (\d+) errors, (\d+) warnings

### search() vs. match()

Python ofrece diferentes operaciones primitivas basadas en expresiones
regulares:

* "re.match()" verifica una coincidencia solo al principio de la
  cadena

* "re.search()" busca una coincidencia en cualquier parte de la cadena
  (esto es lo que Perl hace por defecto)

* "re.fullmatch()" verifica si la cadena completa es una coincidencia

Por ejemplo:

   >>> re.match("c", "abcdef")    # No match
   >>> re.search("c", "abcdef")   # Match
   <re.Match object; span=(2, 3), match='c'>
   >>> re.fullmatch("p.*n", "python") # Match
   <re.Match object; span=(0, 6), match='python'>
   >>> re.fullmatch("r.*n", "python") # No match

Las expresiones regulares que comienzan con "'^'" pueden ser usadas
con "search()" para restringir la coincidencia al principio de la
cadena:

   >>> re.match("c", "abcdef")    # No match
   >>> re.search("^c", "abcdef")  # No match
   >>> re.search("^a", "abcdef")  # Match
   <re.Match object; span=(0, 1), match='a'>

Notar, sin embargo, que en el modo "MULTILINE" "match()" sólo coincide
al principio de la cadena, mientras que usando "search()" con una
expresión regular que comienza con "'^'" coincidirá al principio de
cada línea.

   >>> re.match("X", "A\nB\nX", re.MULTILINE)  # No match
   >>> re.search("^X", "A\nB\nX", re.MULTILINE)  # Match
   <re.Match object; span=(4, 5), match='X'>

### Haciendo una guía telefónica

"split()" divide una cadena en una lista delimitada por el patrón
recibido.  El método es muy útil para convertir datos textuales en
estructuras de datos que pueden ser fácilmente leídas y modificadas
por Python, como se demuestra en el siguiente ejemplo en el que se
crea una guía telefónica.

Primero, aquí está la información.  Normalmente puede venir de un
archivo, aquí se usa la sintaxis de cadena de triple comilla

   >>> text = """Ross McFluff: 834.345.1254 155 Elm Street
   ...
   ... Ronald Heathmore: 892.345.3428 436 Finley Avenue
   ... Frank Burger: 925.541.7625 662 South Dogwood Way
   ...
   ...
   ... Heather Albrecht: 548.326.4584 919 Park Place"""

Las entradas (*entries*) están separadas por una o más líneas nuevas.
Ahora se convierte la cadena en una lista en la que cada línea no
vacía tiene su propia entrada:

   >>> entries = re.split("\n+", text)
   >>> entries
   ['Ross McFluff: 834.345.1254 155 Elm Street',
   'Ronald Heathmore: 892.345.3428 436 Finley Avenue',
   'Frank Burger: 925.541.7625 662 South Dogwood Way',
   'Heather Albrecht: 548.326.4584 919 Park Place']

Finalmente, se divide cada entrada en una lista con nombre, apellido,
número de teléfono y dirección.  Se utiliza el parámetro "maxsplit"
(división máxima) de "split()" porque la dirección tiene espacios
dentro del patrón de división:

   >>> [re.split(":? ", entry, maxsplit=3) for entry in entries]
   [['Ross', 'McFluff', '834.345.1254', '155 Elm Street'],
   ['Ronald', 'Heathmore', '892.345.3428', '436 Finley Avenue'],
   ['Frank', 'Burger', '925.541.7625', '662 South Dogwood Way'],
   ['Heather', 'Albrecht', '548.326.4584', '919 Park Place']]

El patrón ":?" coincide con los dos puntos después del apellido, de
manera que no aparezca en la lista de resultados.  Con "maxsplit" de
"4", se podría separar el número de casa del nombre de la calle:

   >>> [re.split(":? ", entry, maxsplit=4) for entry in entries]
   [['Ross', 'McFluff', '834.345.1254', '155', 'Elm Street'],
   ['Ronald', 'Heathmore', '892.345.3428', '436', 'Finley Avenue'],
   ['Frank', 'Burger', '925.541.7625', '662', 'South Dogwood Way'],
   ['Heather', 'Albrecht', '548.326.4584', '919', 'Park Place']]

### Mungear texto

"sub()" reemplaza cada ocurrencia de un patrón con una cadena o el
resultado de una función.  Este ejemplo demuestra el uso de "sub()"
con una función para "mungear" (*munge*) el texto, o aleatorizar el
orden de todos los caracteres en cada palabra de una frase excepto el
primer y último carácter:

   >>> def repl(m):
   ...     inner_word = list(m.group(2))
   ...     random.shuffle(inner_word)
   ...     return m.group(1) + "".join(inner_word) + m.group(3)
   ...
   >>> text = "Professor Abdolmalek, please report your absences promptly."
   >>> re.sub(r"(\w)(\w+)(\w)", repl, text)
   'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'
   >>> re.sub(r"(\w)(\w+)(\w)", repl, text)
   'Pofsroser Aodlambelk, plasee reoprt yuor asnebces potlmrpy.'

### Encontrar todos los adverbios

"findall()" coincide con *todas* las ocurrencias de un patrón, no sólo
con la primera, como lo hace "search()".  Por ejemplo, si un escritor
quisiera encontrar todos los adverbios en algún texto, podría usar
"findall()" de la siguiente manera:

   >>> text = "He was carefully disguised but captured quickly by police."
   >>> re.findall(r"\w+ly\b", text)
   ['carefully', 'quickly']

### Encontrar todos los adverbios y sus posiciones

Si se desea obtener más información sobre todas las coincidencias de
un patrón en lugar del texto coincidente, "finditer()" es útil ya que
proporciona "Match" objetos en lugar de cadenas. Continuando con el
ejemplo anterior, si un escritor quisiera encontrar todos los
adverbios *y sus posiciones* en algún texto, usaría "finditer()" de la
siguiente manera:

   >>> text = "He was carefully disguised but captured quickly by police."
   >>> for m in re.finditer(r"\w+ly\b", text):
   ...     print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
   07-16: carefully
   40-47: quickly

### Notación de cadena *raw*

La notación de cadena *raw* ("r "text"") permite escribir expresiones
regulares razonables.  Sin ella, para "escapar" cada barra inversa
("'\'") en una expresión regular tendría que ser precedida por otra.
Por ejemplo, las dos siguientes líneas de código son funcionalmente
idénticas:

   >>> re.match(r"\W(.)\1\W", " ff ")
   <re.Match object; span=(0, 4), match=' ff '>
   >>> re.match("\\W(.)\\1\\W", " ff ")
   <re.Match object; span=(0, 4), match=' ff '>

Cuando uno quiere igualar una barra inversa literal, debe escaparse en
la expresión regular.  Con la notación de cadena *raw*, esto significa
"r"\\"".  Sin la notación de cadena, uno debe usar ""\\\\"", haciendo
que las siguientes líneas de código sean funcionalmente idénticas:

   >>> re.match(r"\\", r"\\")
   <re.Match object; span=(0, 1), match='\\'>
   >>> re.match("\\\\", r"\\")
   <re.Match object; span=(0, 1), match='\\'>

### Escribir un Tokenizador

Un tokenizador o analizador léxico analiza una cadena para categorizar
grupos de caracteres.  Este es un primer paso útil para escribir un
compilador o intérprete.

Las categorías de texto se especifican con expresiones regulares.  La
técnica consiste en combinarlas en una única expresión regular maestra
y en hacer un bucle sobre las sucesivas coincidencias:

   from typing import NamedTuple
   import re

   class Token(NamedTuple):
       type: str
       value: int | float | str
       line: int
       column: int

   def tokenize(code):
       keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
       token_specification = [
           ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
           ('ASSIGN',   r':='),           # Assignment operator
           ('END',      r';'),            # Statement terminator
           ('ID',       r'[A-Za-z]+'),    # Identifiers
           ('OP',       r'[+\-*/]'),      # Arithmetic operators
           ('NEWLINE',  r'\n'),           # Line endings
           ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
           ('MISMATCH', r'.'),            # Any other character
       ]
       tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
       line_num = 1
       line_start = 0
       for mo in re.finditer(tok_regex, code):
           kind = mo.lastgroup
           value = mo.group()
           column = mo.start() - line_start
           if kind == 'NUMBER':
               value = float(value) if '.' in value else int(value)
           elif kind == 'ID' and value in keywords:
               kind = value
           elif kind == 'NEWLINE':
               line_start = mo.end()
               line_num += 1
               continue
           elif kind == 'SKIP':
               continue
           elif kind == 'MISMATCH':
               raise RuntimeError(f'{value!r} unexpected on line {line_num}')
           yield Token(kind, value, line_num, column)

   statements = '''
       IF quantity THEN
           total := total + price * quantity;
           tax := price * 0.05;
       ENDIF;
   '''

   for token in tokenize(statements):
       print(token)

El tokenizador produce el siguiente resultado:

   Token(type='IF', value='IF', line=2, column=4)
   Token(type='ID', value='quantity', line=2, column=7)
   Token(type='THEN', value='THEN', line=2, column=16)
   Token(type='ID', value='total', line=3, column=8)
   Token(type='ASSIGN', value=':=', line=3, column=14)
   Token(type='ID', value='total', line=3, column=17)
   Token(type='OP', value='+', line=3, column=23)
   Token(type='ID', value='price', line=3, column=25)
   Token(type='OP', value='*', line=3, column=31)
   Token(type='ID', value='quantity', line=3, column=33)
   Token(type='END', value=';', line=3, column=41)
   Token(type='ID', value='tax', line=4, column=8)
   Token(type='ASSIGN', value=':=', line=4, column=12)
   Token(type='ID', value='price', line=4, column=15)
   Token(type='OP', value='*', line=4, column=21)
   Token(type='NUMBER', value=0.05, line=4, column=23)
   Token(type='END', value=';', line=4, column=27)
   Token(type='ENDIF', value='ENDIF', line=5, column=4)
   Token(type='END', value=';', line=5, column=9)

[Frie09] Friedl, Jeffrey. *Mastering Regular Expressions*. 3a ed.,
         O'Reilly Media, 2009. La tercera edición del libro ya no
         abarca a Python en absoluto, pero la primera edición cubría
         la escritura de buenos patrones de expresiones regulares con
         gran detalle.
