---
title: '"string" --- Common string operations'
source_url: https://docs.python.org/es/3
source_path: library/string.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3930
---

# "string" --- Common string operations

**Source code:** Lib/string/__init__.py

======================================================================

Ver también:

  Cadenas de caracteres --- str

  Métodos de las cadenas de caracteres

## Constantes de cadenas

Las constantes definidas en este módulo son:

string.ascii_letters

   La concatenación de las constantes abajo descriptas
   "ascii_lowercase" y "ascii_uppercase".  Este valor es independiente
   de la configuración regional.

string.ascii_lowercase

   Las letras minúsculas "'abcdefghijklmnopqrstuvwxyz'".  Este valor
   es independiente de la configuración regional y no cambiará.

string.ascii_uppercase

   Las letras mayúsculas "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'".  Este valor
   es independiente de la configuración regional y no cambiará.

string.digits

   La cadena "'0123456789'".

string.hexdigits

   La cadena "'0123456789abcdefABCDEF'".

string.octdigits

   La cadena de caracteres "'01234567'".

string.punctuation

   Cadena de caracteres ASCII que se consideran caracteres de
   puntuación en la configuración regional "C": "!"
   #$%&'()*+,-./:;<=>?@[\]^_`{|} ~".

string.printable

   String of ASCII characters which are considered printable by
   Python. This is a combination of "digits", "ascii_letters",
   "punctuation", and "whitespace".

   Nota:

     By design, "string.printable.isprintable()" returns "False". In
     particular, "string.printable" is not printable in the POSIX
     sense (see *LC_CTYPE*).

string.whitespace

   Una cadena cuyos caracteres ASCII se consideran todos espacios en
   blanco. Esto incluye los caracteres espacio, tabulador, salto de
   línea, retorno, salto de página y tabulador vertical.

## Custom string formatting

The built-in string class provides the ability to do complex variable
substitutions and value formatting via the "format()" method described
in **PEP 3101**.  The "Formatter" class in the "string" module allows
you to create and customize your own string formatting behaviors using
the same implementation as the built-in "format()" method.

class string.Formatter

   La clase "Formatter" tiene los siguientes métodos públicos:

   format(format_string, /, *args, **kwargs)

      Método principal de la API.  Recibe una cadena de formato y
      argumentos posicionales y de palabra clave arbitrarios. Es sólo
      un envoltorio que llama a "vformat()".

      Distinto en la versión 3.7: Un argumento de cadena de formato
      ahora es solo posicional.

   vformat(format_string, args, kwargs)

      Esta función realiza es la que realmente hace el trabajo de
      formateo.  Se expone como una función independiente para los
      casos en los que desea pasar un diccionario predefinido de
      argumentos, en lugar de desempaquetar y volver a empaquetar el
      diccionario como argumentos individuales mediante la sintaxis
      "*args" y "**kwargs".  "vformat()" hace el trabajo de dividir la
      cadena de formato en datos de caracteres y campos de reemplazo.
      Llama a los diversos métodos descritos a continuación.

   Además de eso, la clase "Formatter" define varios métodos que se
   espera sean reemplazados por las subclases:

   parse(format_string)

      Itera sobre *format_string* y retorna un iterable de tuplas
      (*literal_text*, *field_name*, *format_spec*, *conversion*). Es
      usado por "vformat()" para dividir la cadena de caracteres en
      texto literal o en campos de reemplazo.

      The values in the tuple conceptually represent a span of literal
      text followed by a single replacement field.  If there is no
      literal text (which can happen if two replacement fields occur
      consecutively), then *literal_text* will be a zero-length
      string.  If there is no replacement field, then the values of
      *field_name*, *format_spec* and *conversion* will be "None". The
      value of *field_name* is unmodified and auto-numbering of non-
      numbered positional fields is done by "vformat()".

   get_field(field_name, args, kwargs)

      Given *field_name*, convert it to an object to be formatted.
      Auto-numbering of *field_name* returned from "parse()" is done
      by "vformat()" before calling this method.  Returns a tuple
      (obj, used_key). The default version takes strings of the form
      defined in **PEP 3101**, such as "0[name]" or "label.title".
      *args* and *kwargs* are as passed in to "vformat()". The return
      value *used_key* has the same meaning as the *key* parameter to
      "get_value()".

   get_value(key, args, kwargs)

      Recuperar un valor de campo determinado.  El argumento *key*
      será un entero o una cadena de caracteres.  Si es un entero,
      representa el índice del argumento posicional en *args*; si es
      una cadena, representa un argumento definido en *kwargs*.

      El parámetro *args* se establece como lista de argumentos
      posicionales en "vformat()", y el parámetro *kwargs* se
      establece como diccionario de argumentos de palabra clave.

      Para nombres de campo compuesto, estas funciones son únicamente
      llamadas para el primer componente del campo. Los componentes
      que le siguen son tratados a través de operaciones normales de
      atributo e indexación.

      Por ejemplo, la expresión de campo '0.name' haría que
      "get_value()" se llame con un argumento *key* igual a 0.  El
      atributo ''name'' se buscará después del retorno de
      "get_value()" llamando a la función incorporada "getattr()".

      Si el índice o la palabra clave hace referencia a un elemento
      que no existe, se debe generar un "IndexError" o un "KeyError".

   check_unused_args(used_args, args, kwargs)

      Implementa el chequeo de argumentos no utilizados si así se
      desea.  Los argumentos de esta función son el conjunto de todas
      las claves de argumento a las que se hizo referencia en la
      cadena de formato (enteros para argumentos posicionales y
      cadenas de caracteres para argumentos con nombre) y una
      referencia a los *args* y *kwargs* que se pasaron a *vformat*.
      El conjunto de *args* no utilizados se puede calcular a partir
      de estos parámetros. se asume que "check_unused_args()" genera
      una excepción si se produce un error en el chequeo.

   format_field(value, format_spec)

      "format_field()" simplemente llama a la función incorporada
      "format()".  El método se proporciona para que las subclases
      puedan sobrescribirlo.

   convert_field(value, conversion)

      Convierte el valor (retornado por "get_field()") dado un tipo de
      conversión (tal como la tupla retornada por el método
      "parse()"). La versión por defecto entiende los tipos de
      conversión 's' (str), 'r' (repr) y 'a' (ascii).

## Format string syntax

The "str.format()" method and the "Formatter" class share the same
syntax for format strings (although in the case of "Formatter",
subclasses can define their own format string syntax).  The syntax is
related to that of formatted string literals and template string
literals, but it is less sophisticated and, in particular, does not
support arbitrary expressions in interpolations.

Las cadenas de caracteres de formato contienen "campos de reemplazo"
rodeados de llaves "{}". Todo lo que no está contenido entre llaves se
considera texto literal, que se copia sin cambios en la salida.  Si se
necesita incluir un carácter de llave en el texto literal, se puede
escapar duplicando: "{{" *and* "}}".

La gramática para un campo de reemplazo es la siguiente:

   replacement_field: "{" [field_name] ["!" conversion] [":" format_spec] "}"
   field_name:        arg_name ("." attribute_name | "[" element_index "]")*
   arg_name:          [identifier | digit+]
   attribute_name:    identifier
   element_index:     digit+ | index_string
   index_string:      <any source character except "]"> +
   conversion:        "r" | "s" | "a"
   format_spec:       format-spec:format_spec

En términos menos formales, el campo de reemplazo puede comenzar con
un *field_name* (nombre de campo) que especifica el objeto cuyo valor
se va a formatear e insertar en la salida en lugar del campo de
reemplazo. El nombre de campo (*field_name*) va seguido opcionalmente
de un campo *conversion* (conversión), que va precedido de un signo de
exclamación "'!'", y un *format_spec*, que va precedido de dos puntos
"':'".  Estos especifican un formato no predeterminado para el valor
de reemplazo.

Véase también la sección Format specification mini-language.

El *field_name* (nombre de campo) comienza con un *arg_name* que es un
número o una palabra clave.  Si es un número, hace referencia a un
argumento posicional y, si es una palabra clave, hace referencia a un
argumento de palabra clave. Un *arg_name* se trata como un número si
una llamada a "str.isdecimal()" sobre la cadena retorna verdadero. Si
los *arg_names* numéricos en una cadena de caracteres de formato son
una secuencia como 0, 1, 2, ..., todos pueden ser omitidos (no sólo
algunos) y los números 0, 1, 2, ... se insertarán automáticamente en
ese orden. Dado que *arg_name* no está delimitado por comillas, no es
posible especificar claves de diccionario arbitrarias (por ejemplo,
las cadenas "'10'" or "':-]'") dentro de una cadena de caracteres de
formato. El *arg_name* puede ir seguido de cualquier número de
expresiones de índice o atributo. Una expresión con forma "'.name'"
selecciona el atributo con nombre mediante "getattr()", mientras que
una expresión con forma "'[index]'" realiza una búsqueda de índice
mediante "__getitem__()".

Distinto en la versión 3.1: Los especificadores de argumentos
posicionales pueden ser omitidos en "str.format()", así "'{}
{}'.format(a, b)" es equivalente a "'{0} {1}'.format(a, b)".

Distinto en la versión 3.4: Para la clase "Formatter", los
especificadores de argumento posicional pueden ser omitidos.

Algunos ejemplos simples de cadena de formato:

   "First, thou shalt count to {0}"  # References first positional argument
   "Bring me a {}"                   # Implicitly references the first positional argument
   "From {} to {}"                   # Same as "From {0} to {1}"
   "My quest is {name}"              # References keyword argument 'name'
   "Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
   "Units destroyed: {players[0]}"   # First element of keyword argument 'players'.

El campo *conversion* causa una coerción de tipo antes del formateo.
Normalmente, el formateo es hecho el método "__format__()" del valor
mismo. Sin embargo, en algunos es deseable forzar el tipo a ser
formateado como una cadena de caracteres, sobrescribiendo su propia
definición de formateo. Cuando se convierte el valor a una cadena de
caracteres antes de llamar al método "__format__()", la lógica normal
de formateo es evitada.

Tres banderas de conversión son admitidas actualmente: "'!s'", que
llama a "str()" con el valor; "'!r'", que llama a "repr()"; y "'!a'"
que llama a "ascii()".

Algunos ejemplos:

   "Harold's a clever {0!s}"        # Calls str() on the argument first
   "Bring out the holy {name!r}"    # Calls repr() on the argument first
   "More {!a}"                      # Calls ascii() on the argument first

El campo *format_spec* contiene la especificación de cómo presentar el
valor, incluyendo detalles como ancho del campo, alineación, relleno,
precisión decimal, etc. Cada tipo de valor puede definir su propio
"mini lenguaje de formateo" o interpretación de *format_spec*.

La mayoría de los tipos integrados admiten un formateo común de mini-
idioma descrito en la siguiente sección.

Un campo *format_spec* también puede incluir campos de reemplazo
anidados dentro de él. Estos campos de reemplazo anidados pueden
contener un nombre de campo, una bandera de conversión y una
especificación de formato, pero no se permite anidamiento más
profundo.  Los campos de reemplazo dentro de *format_spec* se
sustituyen antes de que la cadena *format_spec* se interprete. Esto
permite especificar dinámicamente el formato de un valor.

Para más ejemplos, véase la sección Ejemplos de formateo.

### Format specification mini-language

"Format specifications" are used within replacement fields contained
within a format string to define how individual values are presented
(see Format string syntax, f-strings, and t-strings). They can also be
passed directly to the built-in "format()" function.  Each formattable
type may define how the format specification is to be interpreted.

La mayoría de los tipos integrados implementan las siguientes opciones
para especificaciones de formato, aunque algunas de las opciones de
formateo sólo son posibles con los tipos numéricos.

Una convención general es que una especificación de formato vacía
produce el mismo resultado que llamar a la función "str()" con el
valor. Una especificación no vacía típicamente modifica el resultado.

La forma general de un *especificador estándar de formato* es:

   format_spec:             [options][width_and_precision][type]
   options:                 [[fill]align][sign]["z"]["#"]["0"]
   fill:                    <any character>
   align:                   "<" | ">" | "=" | "^"
   sign:                    "+" | "-" | " "
   width_and_precision:     [width_with_grouping][precision_with_grouping]
   width_with_grouping:     [width][grouping]
   precision_with_grouping: "." [precision][grouping] | "." grouping
   width:                   digit+
   precision:               digit+
   grouping:                "," | "_"
   type:                    "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g"
                            | "G" | "n" | "o" | "s" | "x" | "X" | "%"

Si se especifica un valor *align* válido, puede ir precedido por un
carácter *fill*, que puede ser cualquier carácter y cuyo valor
predeterminado es un espacio si se omite. No es posible utilizar una
llave literal (""{"" or ""}"") como el carácter *fill* en un formato
literal de cadena o cuando se utiliza el método "str.format()".  Sin
embargo, es posible insertar una llave con un campo de reemplazo
anidado.  Esta limitación no afecta a la función "format()".

El significado de las distintas opciones de alineación es el
siguiente:

+-----------+------------------------------------------------------------+
| Opción    | Significado                                                |
|===========|============================================================|
| "'<'"     | Fuerza el campo a ser alineado a la izquierda dentro del   |
|           | espacio disponible (éste es el comportamiento por defecto  |
## |           | para la mayoría de los objetos).                           |

| "'>'"     | Fuerza el campo a ser alineado a la derecha dentro del     |
|           | espacio disponible (éste es el comportamiento por defecto  |
## |           | para números).                                             |

| "'='"     | Forces the padding to be placed after the sign (if any)    |
|           | but before the digits.  This is used for printing fields   |
|           | in the form '+000000120'. This alignment option is only    |
|           | valid for numeric types, excluding "complex". It becomes   |
|           | the default for numbers when '0' immediately precedes the  |
## |           | field width.                                               |

| "'^'"     | Fuerza el centrado del campo dentro del espacio            |
## |           | disponible.                                                |

Notar que, a menos que se defina un ancho de campo mínimo, el ancho
del campo siempre tendrá el mismo tamaño que los datos para
rellenarlo, de modo que la opción de alineación no tiene ningún
significado en este caso.

La opción *sign* (signo) sólo es válida para los tipos numéricos y
puede ser una de las siguientes:

+-----------+------------------------------------------------------------+
| Opción    | Significado                                                |
|===========|============================================================|
| "'+'"     | Indicates that a sign should be used for both positive as  |
## |           | well as negative numbers.                                  |

| "'-'"     | Indicates that a sign should be used only for negative     |
## |           | numbers (this is the default behavior).                    |

| espacio   | Indicates that a leading space should be used on positive  |
## |           | numbers, and a minus sign on negative numbers.             |

La opción "'z'" convierte los valores de coma flotante de cero
negativos en cero positivos después de redondear al formato de
precisión. Esta opción solo es válida para los tipos de presentación
de coma flotante.

Distinto en la versión 3.11: Se agregó la opción "'z'" (véase también
**PEP 682**).

La opción "'#'" hace que la "forma alternativa" se utilice para la
conversión.  La forma alternativa se define de forma diferente para
diferentes tipos.  Esta opción solo es válida para los tipos entero,
flotante y complejo. Para los enteros, cuando se utiliza la salida
binaria, octal o hexadecimal, esta opción agrega el respectivo prefijo
"'0b'", "'0o'" o "'0x'" al valor de salida. Para los flotantes y
complejos, la forma alternativa hace que el resultado de la conversión
siempre contenga un carácter de punto decimal, incluso si no hay
dígitos que lo sigan. Normalmente, un carácter de punto decimal
aparece en el resultado de estas conversiones sólo si un dígito lo
sigue. Además, para las conversiones "'g'" y "'G'", los ceros finales
no se eliminan del resultado.

The *width* is a decimal integer defining the minimum total field
width, including any prefixes, separators, and other formatting
characters. If not specified, then the field width will be determined
by the content.

When no explicit alignment is given, preceding the *width* field by a
zero ("'0'") character enables sign-aware zero-padding for numeric
types, excluding "complex".  This is equivalent to a *fill* character
of "'0'" with an *alignment* type of "'='".

Distinto en la versión 3.10: Anteponer el campo *width* por "'0'" ya
no afecta el alineamiento por defecto para cadenas de caracteres.

La *precisión* es un entero decimal que indica cuántos dígitos deben
mostrarse después del punto decimal para los tipos de presentación
"'f'" y "'F'", o antes y después del punto decimal para los tipos de
presentación "'g'" o "'G'". Para los tipos de presentación de cadena,
el campo indica el tamaño máximo del campo; en otras palabras, cuántos
caracteres se utilizarán del contenido del campo. La *precisión* no
está permitida para los tipos de presentación de enteros.

The *grouping* option after *width* and *precision* fields specifies a
digit group separator for the integral and fractional parts of a
number respectively. It can be one of the following:

+-----------+------------------------------------------------------------+
| Opción    | Significado                                                |
|===========|============================================================|
| "','"     | Inserts a comma every 3 digits for integer presentation    |
|           | type "'d'" and floating-point presentation types,          |
|           | excluding "'n'". For other presentation types, this option |
## |           | is not supported.                                          |

| "'_'"     | Inserts an underscore every 3 digits for integer           |
|           | presentation type "'d'" and floating-point presentation    |
|           | types, excluding "'n'". For integer presentation types     |
|           | "'b'", "'o'", "'x'", and "'X'", underscores are inserted   |
|           | every 4 digits. For other presentation types, this option  |
## |           | is not supported.                                          |

For a locale-aware separator, use the "'n'" float presentation type or
integer presentation type instead.

Distinto en la versión 3.1: Se agregó la opción "','" (véase también
**PEP 378**).

Distinto en la versión 3.6: Se agregó la opción "'_'" (véase también
**PEP 515**).

Distinto en la versión 3.14: Support the *grouping* option for the
fractional part.

Finalmente, *type* (el tipo) determina como presentar los datos.

Los tipos de presentación cadena disponibles son:

   +-----------+------------------------------------------------------------+
   | Tipo      | Significado                                                |
   |===========|============================================================|
   | "'s'"     | Formato de cadena de caracteres. Éste es el tipo por       |
   |           | defecto y puede ser omitido.                               |
   +-----------+------------------------------------------------------------+
   | None      | Lo mismo que "'s'".                                        |
   +-----------+------------------------------------------------------------+

Los tipos disponibles para la presentación de enteros son:

   +-----------+------------------------------------------------------------+
   | Tipo      | Significado                                                |
   |===========|============================================================|
   | "'b'"     | Formato binario. retorna el número en base 2.              |
   +-----------+------------------------------------------------------------+
   | "'c'"     | Carácter. Convierte el entero en el carácter unicode       |
   |           | correspondiente antes de imprimirlo.                       |
   +-----------+------------------------------------------------------------+
   | "'d'"     | Decimal entero. retorna el número en base 10.              |
   +-----------+------------------------------------------------------------+
   | "'o'"     | Formato octal. retorna el número en base 8.                |
   +-----------+------------------------------------------------------------+
   | "'x'"     | Formato hexadecimal. retorna el número en base 16,         |
   |           | utilizando letras minúsculas para los dígitos superiores a |
   |           | 9.                                                         |
   +-----------+------------------------------------------------------------+
   | "'X'"     | Formato hexadecimal. retorna el número en base 16,         |
   |           | utilizando letras mayúsculas para los dígitos superiores a |
   |           | 9. En caso de que "'#'" se especifique, el prefijo "'0x'"  |
   |           | convertirá en "'0X'" también.                              |
   +-----------+------------------------------------------------------------+
   | "'n'"     | Number. This is the same as "'d'", except that it uses the |
   |           | current locale setting to insert the appropriate digit     |
   |           | group separators. Note that the default locale is not the  |
   |           | system locale. Depending on your use case, you may wish to |
   |           | set "LC_NUMERIC" with "locale.setlocale()" before using    |
   |           | "'n'".                                                     |
   +-----------+------------------------------------------------------------+
   | None      | Lo mismo que "'d'".                                        |
   +-----------+------------------------------------------------------------+

In addition to the above presentation types, integers can be formatted
with the floating-point presentation types listed below (except "'n'"
and "None"). When doing so, "float()" is used to convert the integer
to a floating-point number before formatting.

Los tipos de presentación disponibles para valores  "float" y
"Decimal" son:

   +-----------+------------------------------------------------------------+
   | Tipo      | Significado                                                |
   |===========|============================================================|
   | "'e'"     | Scientific notation. For a given precision "p", formats    |
   |           | the number in scientific notation with the letter 'e'      |
   |           | separating the coefficient from the exponent. The          |
   |           | coefficient has one digit before and "p" digits after the  |
   |           | decimal point, for a total of "p + 1" significant digits.  |
   |           | With no precision given, uses a precision of "6" digits    |
   |           | after the decimal point for "float", and shows all         |
   |           | coefficient digits for "Decimal".  If "p=0", the decimal   |
   |           | point is omitted unless the "#" option is used.  For       |
   |           | "float", the exponent always contains at least two digits, |
   |           | and is zero if the value is zero.                          |
   +-----------+------------------------------------------------------------+
   | "'E'"     | Notación científica. Igual que "'e'" excepto que utiliza   |
   |           | una 'E' mayúscula como carácter separador.                 |
   +-----------+------------------------------------------------------------+
   | "'f'"     | Fixed-point notation. For a given precision "p", formats   |
   |           | the number as a decimal number with exactly "p" digits     |
   |           | following the decimal point. With no precision given, uses |
   |           | a precision of "6" digits after the decimal point for      |
   |           | "float", and uses a precision large enough to show all     |
   |           | coefficient digits for "Decimal".  If "p=0", the decimal   |
   |           | point is omitted unless the "#" option is used.            |
   +-----------+------------------------------------------------------------+
   | "'F'"     | Notación de punto fijo. Igual que "'f'", pero convierte    |
   |           | (nulos) "nan" a "NAN" e "inf" a "INF".                     |
   +-----------+------------------------------------------------------------+
   | "'g'"     | Formato general. Para una precisión dada "p >= 1",         |
   |           | redondea el número a "p" dígitos significativos y luego    |
   |           | formatea el resultado como formato de punto fijo o en      |
   |           | notación científica, dependiendo de su magnitud. Una       |
   |           | precisión de "0" es tratada como equivalente a una         |
   |           | precisión de "1".  Las reglas precisas son las siguientes: |
   |           | supongamos que el resultado formateado con el tipo de      |
   |           | presentación "'e'" y la precisión "p-1" tiene exponente    |
   |           | "exp".  Entonces, si "m <= exp < p", donde "m" es -4 para  |
   |           | *floats* y -6 para "Decimals", el número se formatea con   |
   |           | el tipo de presentación "'f'" y la precisión "p-1-exp".    |
   |           | De lo contrario, el número se formatea con el tipo de      |
   |           | presentación "'e'" y precisión "p-1". En ambos casos, los  |
   |           | ceros finales insignificantes se eliminan del significado, |
   |           | y el punto decimal también se elimina si no hay dígitos    |
   |           | restantes que lo sigan, a menos que se utilice la opción   |
   |           | "'#'".  Si no se da una precisión, usa una precisión de    |
   |           | "6" dígitos significativos para "float". Para "Decimal" el |
   |           | coeficiente del resultado se construye usando los dígitos  |
   |           | del coeficiente del valor; se usa notación científica para |
   |           | valores menores a "1e-6" en valor absoluto y valores donde |
   |           | el valor posicional del dígito menos significativo es      |
   |           | mayor a 1, de otra forma se usa notación de punto fijo.    |
   |           | Infinito positivo y negativo, cero positivo y negativo, y  |
   |           | nulos (*nans*) son respectivamente formateados como "inf", |
   |           | "-inf", "0", "-0" y "nan", independientemente de la        |
   |           | precisión.                                                 |
   +-----------+------------------------------------------------------------+
   | "'G'"     | Formato general. Igual que "'g'" excepto que cambia a      |
   |           | "'E'" si el número se vuelve muy grande. Las               |
   |           | representaciones de infinito y NaN también se convierten a |
   |           | mayúsculas.                                                |
   +-----------+------------------------------------------------------------+
   | "'n'"     | Number. This is the same as "'g'", except that it uses the |
   |           | current locale setting to insert the appropriate digit     |
   |           | group separators for the integral part of a number. Note   |
   |           | that the default locale is not the system locale.          |
   |           | Depending on your use case, you may wish to set            |
   |           | "LC_NUMERIC" with "locale.setlocale()" before using "'n'". |
   +-----------+------------------------------------------------------------+
   | "'%'"     | Porcentaje. Multiplica el número por 100 y lo muestra en   |
   |           | formato fijo ("'f'") seguido del signo porcentaje.         |
   +-----------+------------------------------------------------------------+
   | None      | For "float" this is like the "'g'" type, except that when  |
   |           | fixed- point notation is used to format the result, it     |
   |           | always includes at least one digit past the decimal point, |
   |           | and switches to the scientific notation when "exp >= p -   |
   |           | 1".  When the precision is not specified, the latter will  |
   |           | be as large as needed to represent the given value         |
   |           | faithfully.  Para "Decimal", esto es lo mismo que "'g'" o  |
   |           | "'G'" dependiendo del valor de "context.capitals" para el  |
   |           | contexto decimal actual.  El efecto general es el de       |
   |           | igualar la salida de "str()" al ser alterada  por los      |
   |           | otros modificadores de formato.                            |
   +-----------+------------------------------------------------------------+

The result should be correctly rounded to a given precision "p" of
digits after the decimal point.  The rounding mode for "float" matches
that of the "round()" builtin.  For "Decimal", the rounding mode of
the current context will be used.

The available presentation types for "complex" are the same as those
for "float" ("'%'" is not allowed).  Both the real and imaginary
components of a complex number are formatted as floating-point
numbers, according to the specified presentation type.  They are
separated by the mandatory sign of the imaginary part, the latter
being terminated by a "j" suffix.  If the presentation type is
missing, the result will match the output of "str()" (complex numbers
with a non-zero real part are also surrounded by parentheses),
possibly altered by other format modifiers.

### Ejemplos de formateo

Esta sección contiene ejemplos de la sintaxis "str.format()" y
comparaciones con el antiguo método de formateo usando "%".

En la mayoría de los casos, la sintaxis es similar al antiguo formato
"%", con la adición de "{}" y con ":" utilizado en lugar de "%". Por
ejemplo, "'%03.2f'" puede ser traducido como "'{:03.2f}'".

La nueva sintaxis de formato también soporta opciones diferentes y
nuevas que se muestran en los ejemplos siguientes.

Accediendo argumentos por posición:

   >>> '{0}, {1}, {2}'.format('a', 'b', 'c')
   'a, b, c'
   >>> '{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only
   'a, b, c'
   >>> '{2}, {1}, {0}'.format('a', 'b', 'c')
   'c, b, a'
   >>> '{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
   'c, b, a'
   >>> '{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
   'abracadabra'

Accediendo argumentos por nombre:

   >>> 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
   'Coordinates: 37.24N, -115.81W'
   >>> coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
   >>> 'Coordinates: {latitude}, {longitude}'.format(**coord)
   'Coordinates: 37.24N, -115.81W'

Accediendo los atributos de los argumentos:

   >>> c = 3-5j
   >>> ('The complex number {0} is formed from the real part {0.real} '
   ...  'and the imaginary part {0.imag}.').format(c)
   'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'
   >>> class Point:
   ...     def __init__(self, x, y):
   ...         self.x, self.y = x, y
   ...     def __str__(self):
   ...         return 'Point({self.x}, {self.y})'.format(self=self)
   ...
   >>> str(Point(4, 2))
   'Point(4, 2)'

Accediendo ítems de los argumentos:

   >>> coord = (3, 5)
   >>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
   'X: 3;  Y: 5'

Reemplazar "%s" y "%r":

   >>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
   "repr() shows quotes: 'test1'; str() doesn't: test2"

Alinear el texto y especificar el ancho:

   >>> '{:<30}'.format('left aligned')
   'left aligned                  '
   >>> '{:>30}'.format('right aligned')
   '                 right aligned'
   >>> '{:^30}'.format('centered')
   '           centered           '
   >>> '{:*^30}'.format('centered')  # use '*' as a fill char
   '***********centered***********'

Reemplazar "%+f", "%-f", y "% f" y especificar el signo:

   >>> '{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
   '+3.140000; -3.140000'
   >>> '{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
   ' 3.140000; -3.140000'
   >>> '{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
   '3.140000; -3.140000'

Reemplazando "%x" y "%o" y convirtiendo el valor a diferentes bases:

   >>> # format also supports binary numbers
   >>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
   'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
   >>> # with 0x, 0o, or 0b as prefix:
   >>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
   'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

Using the comma or the underscore as a digit group separator:

   >>> '{:,}'.format(1234567890)
   '1,234,567,890'
   >>> '{:_}'.format(1234567890)
   '1_234_567_890'
   >>> '{:_b}'.format(1234567890)
   '100_1001_1001_0110_0000_0010_1101_0010'
   >>> '{:_x}'.format(1234567890)
   '4996_02d2'
   >>> '{:_}'.format(123456789.123456789)
   '123_456_789.12345679'
   >>> '{:.,}'.format(123456789.123456789)
   '123456789.123,456,79'
   >>> '{:,._}'.format(123456789.123456789)
   '123,456,789.123_456_79'

Expresar un porcentaje:

   >>> points = 19
   >>> total = 22
   >>> 'Correct answers: {:.2%}'.format(points/total)
   'Correct answers: 86.36%'

Uso del formateo específico de tipo:

   >>> import datetime as dt
   >>> d = dt.datetime(2010, 7, 4, 12, 15, 58)
   >>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
   '2010-07-04 12:15:58'

Anidando argumentos y ejemplos más complejos:

   >>> for align, text in zip('<^>', ['left', 'center', 'right']):
   ...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
   ...
   'left<<<<<<<<<<<<'
   '^^^^^center^^^^^'
   '>>>>>>>>>>>right'
   >>>
   >>> octets = [192, 168, 0, 1]
   >>> '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
   'C0A80001'
   >>> int(_, 16)
   3232235521
   >>>
   >>> width = 5
   >>> for num in range(5,12):
   ...     for base in 'dXob':
   ...         print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
   ...     print()
   ...
       5     5     5   101
       6     6     6   110
       7     7     7   111
       8     8    10  1000
       9     9    11  1001
      10     A    12  1010
      11     B    13  1011

## Template strings ($-strings)

Nota:

  The feature described here was introduced in Python 2.4; a simple
  templating method based upon regular expressions. It predates
  "str.format()", formatted string literals, and template string
  literals.It is unrelated to template string literals (t-strings),
  which were introduced in Python 3.14. These evaluate to
  "string.templatelib.Template" objects, found in the
  "string.templatelib" module.

Las cadenas de plantilla proporcionan sustituciones de cadenas de
caracteres más sencillas como se describe en **PEP 292**.  Un caso de
uso principal para las cadenas de plantilla es la internacionalización
(i18n) ya que en ese contexto, la sintaxis y la funcionalidad más
sencillas hacen la traducción más fácil que otras instalaciones de
formato de cadena de caracteres integradas en Python.  Como ejemplo de
una biblioteca creada sobre cadenas de plantilla para i18n, véase el
paquete flufl.i18n.

Las cadenas de caracteres de plantilla admiten sustituciones basadas
en "$" de acuerdo a las siguientes reglas:

* "$$" es un escape. Es reemplazado con un único "$".

* "$identifier" (identificador) nombra un comodín de sustitución que
  coincide con una clave de asignación de ""identifier""
  (identificador).  De forma predeterminada, ""identifier"" está
  restringido a cualquier cadena alfanumérica ASCII (insensible a
  mayúsculas/minúsculas e incluyendo los guiones bajos) que comience
  con un guión bajo o una letra ASCII.  El primer carácter no
  identificador después del carácter "$" termina esta especificación
  de comodín.

* "${identifier}" es equivalente a "$identifier". Es requerido cuando
  caracteres identificadores válidos siguen al comodín pero no son
  parte de él, por ejemplo ""${noun}ification"".

Cualquier otra aparición de "$" en la cadena de caracteres resultará
en una excepción "ValueError".

The "string" module provides a "Template" class that implements these
rules.  The methods of "Template" are:

class string.Template(template)

   El constructor sólo lleva un argumento, la cadena plantilla.

   substitute(mapping={}, /, **kwds)

      Realiza la sustitución de plantilla y retorna una nueva cadena
      de caracteres. *mapping* (mapeo) es un objeto tipo diccionario
      con claves (*keys*) que coinciden con los *placeholders*
      (comodines) de la plantilla. Como alternativa, es posible pasar
      argumentos de palabra clave cuyas palabras clave son los
      *placeholders* (comodines). Cuando *mapping* y *kwds* son dados
      y hay elementos duplicados, los *placeholders* (comodines) de
      *kwds* tienen prioridad.

   safe_substitute(mapping={}, /, **kwds)

      Igual que "substitute()", excepto que si faltan comodines de
      *mapping* y *kwds*, en lugar de generar una excepción
      "KeyError", el comodín original aparecerá en la cadena de
      caracteres resultante intacta.  Además, a diferencia de
      "substitute()", cualquier otra aparición de "$" simplemente
      retornará "$" en lugar de generar "ValueError".

      Mientras que otras excepciones aún pueden ocurrir, este método
      es llamado "seguro" (*safe*) porque siempre intenta retornar una
      cadena de caracteres que pueda ser usada en lugar de levantar
      una excepción. Desde otro punto de vista, el método
      "safe_substitute()" es en realidad para nada seguro, dado que
      ignorará plantillas defectuosas con delimitadores colgados,
      llaves sin cerrar, o comodines que no son identificadores
      válidos en Python.

   is_valid()

      Returns "False" if the template has invalid placeholders that
      will cause "substitute()" to raise "ValueError".

      Added in version 3.11.

   get_identifiers()

      Retorna una lista de los identificadores válidos en la
      plantilla, en el orden en que aparecen por primera vez,
      ignorando cualquier identificador no válido.

      Added in version 3.11.

   Las instancias de "Template" también proporcionan un atributo de
   datos públicos:

   template

      Éste es el objeto que se le pasa como argumento *template* al
      constructor. En general, no debería ser modificado, pero el
      acceso de sólo lectura (*read-only*) no es impuesto.

Aquí un ejemplo de cómo usar una plantilla (*Template*):

   >>> from string import Template
   >>> s = Template('$who likes $what')
   >>> s.substitute(who='tim', what='kung pao')
   'tim likes kung pao'
   >>> d = dict(who='tim')
   >>> Template('Give $who $100').substitute(d)
   Traceback (most recent call last):
   ...
   ValueError: Invalid placeholder in string: line 1, col 11
   >>> Template('$who likes $what').substitute(d)
   Traceback (most recent call last):
   ...
   KeyError: 'what'
   >>> Template('$who likes $what').safe_substitute(d)
   'tim likes $what'

Uso avanzado: es posible derivar subclases de "Template" para
personalizar la sintaxis de *placeholder*, caracteres de delimitación,
o bien la expresión regular entera usada para procesar cadenas de
plantillas. Para ello, es posible sobrescribir los siguientes
atributos de clase:

* *delimiter*: es la cadena de caracteres literal que describe al
  delimitador que introduce un comodín.  El valor predeterminado es
  "$".  Notar que esto *no debe* ser una expresión regular, ya que la
  implementación llamará a "re.escape()" en esta cadena de caracteres
  según sea necesario.  Tener en cuenta además, que se no puede
  cambiar el delimitador después haber creado la clase (es decir, se
  debe establecer un delimitador diferente en el espacio de nombres de
  la subclase).

* *idpattern* -- Esta es la expresión regular que describe el patrón
  para comodines fuera de las llaves.  El valor predeterminado es la
  expresión regular "(?a:[_a-z][_a-z0-9]*)".  Si se proporciona este
  argumento y *braceidpattern* es "None" este patrón también se
  aplicará a los comodines entre llaves.

  Nota:

    Dado que el valor predeterminado de *flags* es "re.IGNORECASE", el
    patrón "[a-z]" puede coincidir con algunos caracteres que no son
    ASCII. Por ello se utiliza aquí la bandera local "a".

  Distinto en la versión 3.7: *braceidpattern* puede ser usado para
  definir patrones separados, usados dentro y fuera de los corchetes.

* *braceidpattern* -- Es como *idpattern* pero describe el patrón para
  comodines entre llaves.  El valor por defecto es "None", lo que
  significa volver a *idpattern* (es decir, el mismo patrón se utiliza
  tanto dentro como fuera de las llaves). Si se proporciona, esto le
  permite definir diferentes patrones para comodines dentro y fuera de
  las llaves.

  Added in version 3.7.

* *flags* -- Banderas de expresión regular que se aplicarán al
  compilar la expresión regular utilizada para reconocer
  sustituciones.  El valor por defecto es "re.IGNORECASE".  Téngase en
  cuenta que "re.VERBOSE" siempre se agregará a las banderas, por lo
  que *idpattern* (s) personalizado(s) debe(n) seguir las convenciones
  de expresiones regulares detalladas.

  Added in version 3.2.

Alternatively, you can provide the entire regular expression pattern
by overriding the class attribute *pattern*.  If you do this, the
value must be a regular expression pattern string, or a compiled
regular expression object, with four named capturing groups.  The
capturing groups correspond to the rules given above, along with the
invalid placeholder rule:

* *escaped* -- Este grupo coincide con la secuencia de escape en el
  patrón predeterminado, por ejemplo, "$$".

* *named* -- Este grupo coincide con el nombre comodín fuera de las
  llaves. No debe incluir el delimitador del grupo de captura.

* *braced* -- Este grupo coincide con el nombre del comodín adjunto;
  no debe incluir ni el delimitador ni las llaves en el grupo de
  captura.

* *invalid* -- Este grupo se empareja con cualquier otro patrón de
  delimitación (usualmente un único carácter) y debe ser lo último en
  aparecer en la expresión regular.

Los métodos de esta clase generarán "ValueError" si el patrón coincide
con la plantilla sin que coincida uno de estos grupos nombrados.

## Funciones de ayuda

string.capwords(s, sep=None)

   Separa el argumento en dos palabras utilizando el método
   "str.split()", convierte a mayúsculas vía "str.capitalize()" y une
   las palabras en mayúscula con el método "str.join()". Si el segundo
   argumento opcional *sep* está ausente o es "None", los espacios en
   blanco se reemplazarán con un único espacio y los espacios en
   blanco iniciales y finales se eliminarán; caso contrario, *sep* se
   usa para separar y unir las palabras.
