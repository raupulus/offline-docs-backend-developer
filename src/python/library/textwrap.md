---
title: '"textwrap" --- Text wrapping and filling'
source_url: https://docs.python.org/es/3
source_path: library/textwrap.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4120
---

# "textwrap" --- Text wrapping and filling

**Source code:** Lib/textwrap.py

======================================================================

The "textwrap" module provides some convenience functions, as well as
"TextWrapper", the class that does all the work. If you're just
wrapping or filling one or two text strings, the convenience functions
should be good enough; otherwise, you should use an instance of
"TextWrapper" for efficiency.

textwrap.wrap(text, width=70, *, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True, tabsize=8, max_lines=None, placeholder=' [...]')

   Envuelve el párrafo individual en *text* (una cadena) para que cada
   línea tenga como máximo *width* de caracteres de largo.  Retorna
   una lista de líneas de salida, sin las nuevas líneas finales.

   Los argumentos de palabras clave opcionales corresponden a los
   atributos de instancia de "TextWrapper", que se documentan a
   continuación.

   Ver el método "TextWrapper.wrap()" para más detalles sobre el
   comportamiento de "wrap()".

textwrap.fill(text, width=70, *, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True, tabsize=8, max_lines=None, placeholder=' [...]')

   Envuelve el único párrafo en *text*, y retorna una sola cadena que
   contiene el párrafo envuelto. "fill()" es la abreviatura de

      "\n".join(wrap(text, ...))

   En particular, "fill()" acepta exactamente los mismos argumentos de
   palabras clave que "wrap()".

textwrap.shorten(text, width, *, fix_sentence_endings=False, break_long_words=True, break_on_hyphens=True, placeholder=' [...]')

   Colapsa y trunca el *text* dado para que encaje en el *width* dado.

   Primero el espacio blanco en *text* se colapsa (todos los espacios
   blancos son reemplazados por espacios sencillos).  Si el resultado
   cabe en el *width*, se retorna. En caso contrario, se eliminan
   suficientes palabras del final para que las palabras restantes más
   el *placeholder* encajen dentro de *width*:

      >>> textwrap.shorten("Hello  world!", width=12)
      'Hello world!'
      >>> textwrap.shorten("Hello  world!", width=11)
      'Hello [...]'
      >>> textwrap.shorten("Hello world", width=10, placeholder="...")
      'Hello...'

   Los argumentos opcionales de las palabras clave corresponden a los
   atributos de la instancia de "TextWrapper", documentados a
   continuación.  Observe que el espacio en blanco se colapsa antes de
   pasar el texto a la función "TextWrapper" "fill()", por lo que
   cambiar el valor de "tabsize", "expand_tabs", "drop_whitespace", y
   "replace_whitespace" no tendrá ningún efecto.

   Added in version 3.4.

textwrap.dedent(text)

   Elimina cualquier espacio en blanco común de cada línea de *text*.

   Esto puede utilizarse para hacer que las cadenas con comillas
   triples se alineen con el borde izquierdo de la pantalla, mientras
   que se siguen presentando en el código fuente en forma indentada.

   Nótese que los tabuladores y los espacios se tratan como espacios
   en blanco, pero no son iguales: las líneas ""  hello"" y
   ""\thello"" se consideran que no tienen un espacio en blanco común.

   Las líneas que sólo contienen espacios en blanco se ignoran en la
   entrada y se normalizan a un solo carácter de nueva línea en la
   salida.

   Por ejemplo:

      def test():
          # end first line with \ to avoid the empty line!
          s = '''\
          hello
            world
          '''
          print(repr(s))          # prints '    hello\n      world\n    '
          print(repr(dedent(s)))  # prints 'hello\n  world\n'

   Distinto en la versión 3.14: The "dedent()" function now correctly
   normalizes blank lines containing only whitespace characters.
   Previously, the implementation only normalized blank lines
   containing tabs and spaces.

textwrap.indent(text, prefix, predicate=None)

   Añade *prefix* al principio de las líneas seleccionadas en *text*.

   Las líneas se separan llamando a "text.splitlines(True)".

   Por defecto, se añade *prefix* a todas las líneas que no consisten
   únicamente en espacios en blanco (incluyendo cualquier terminación
   de línea).

   Por ejemplo:

      >>> s = 'hello\n\n \nworld'
      >>> indent(s, '  ')
      '  hello\n\n \n  world'

   El argumento opcional *predicate* puede ser usado para controlar
   qué líneas están indentadas. Por ejemplo, es fácil añadir *prefix*
   incluso a las líneas vacías y de espacio en blanco:

      >>> print(indent(s, '+ ', lambda line: True))
      + hello
      +
      +
      + world

   Added in version 3.3.

"wrap()", "fill()" y "shorten()" funcionan creando una instancia
"TextWrapper" y llamando a un solo método en ella.  Esa instancia no
se reutiliza, por lo que para las aplicaciones que procesan muchas
cadenas de texto usando "wrap()" y/o "fill()", puede ser más eficiente
crear su propio objeto "TextWrapper".

El texto se envuelve preferentemente en espacios en blanco y justo
después de los guiones en palabras con guión; sólo entonces se
romperán las palabras largas si es necesario, a menos que
"TextWrapper.break_long_words" sea falso.

class textwrap.TextWrapper(**kwargs)

   El constructor "TextWrapper" acepta un número de argumentos de
   palabras clave opcionales.  Cada argumento de palabra clave
   corresponde a un atributo de la instancia, por ejemplo

      wrapper = TextWrapper(initial_indent="* ")

   es lo mismo que

      wrapper = TextWrapper()
      wrapper.initial_indent = "* "

   You can reuse the same "TextWrapper" object many times, and you can
   change any of its options through direct assignment to instance
   attributes between uses.

   Los atributos de la instancia "TextWrapper" (y los argumentos de
   las palabras clave para el constructor) son los siguientes:

   width

      (default: "70") La longitud máxima de las líneas envueltas.
      Mientras no haya palabras individuales en el texto de entrada
      más largas que "width", "TextWrapper" garantiza que ninguna
      línea de salida será más larga que los caracteres  "width".

   expand_tabs

      (default: "True") Si es verdadero, entonces todos los caracteres
      de tabulación en *text* serán expandidos a espacios usando el
      método "expandtabs()" de *text*.

   tabsize

      (default: "8") Si "expand_tabs" es verdadero, entonces todos los
      caracteres de tabulación en *text* se expandirán a cero o más
      espacios, dependiendo de la columna actual y el tamaño de
      tabulación dado.

      Added in version 3.3.

   replace_whitespace

      (default: "True") Si es verdadero, después de la expansión por
      tabulador pero antes de envolver, el método "wrap()" reemplazará
      cada carácter de espacio en blanco con un espacio sencillo.  Los
      caracteres de los espacios en blanco reemplazados son los
      siguientes: tab, nueva línea, tab vertical, *formfeed* y
      *carriage return* ("'\t\n\v\f\r'").

      Nota:

        Si "expand_tabs" es falso y "replace_whitespace" es verdadero,
        cada carácter del tabulador será reemplazado por un solo
        espacio, que *no* es lo mismo que la expansión del tabulador.

      Nota:

        Si "replace_whitespace" es falso, las nuevas líneas pueden
        aparecer en medio de una línea y causar una salida extraña.
        Por esta razón, el texto debe ser dividido en párrafos (usando
        "str.splitlines()" o similar) que se envuelven por separado.

   drop_whitespace

      (default: "True") Si es verdadero, se eliminan los espacios en
      blanco al principio y al final de cada línea (después de la
      envoltura pero antes del indentado). Sin embargo, el espacio en
      blanco al principio del párrafo no se elimina si lo sigue un
      espacio en blanco.  Si el espacio blanco que se deja caer ocupa
      una línea entera, se deja caer toda la línea.

   initial_indent

      (default: "''") Cadena que será preparada para la primera línea
      de salida envuelta.  Cuenta hacia la longitud de la primera
      línea.  La cadena vacía no está indentada.

   subsequent_indent

      (default: "''") Cadena que se preparará para todas las líneas de
      salida envueltas excepto la primera.  Cuenta hacia la longitud
      de cada línea excepto la primera.

   fix_sentence_endings

      (default: "False") If true, "TextWrapper" attempts to detect
      sentence endings and ensure that sentences are always separated
      by exactly two spaces.  This is generally desired for text in a
      monospaced font. However, the sentence detection algorithm is
      imperfect: it assumes that a sentence ending consists of a
      lowercase letter followed by one of "'.'", "'!'", or "'?'",
      possibly followed by one of "'"'" or ""'"", followed by a space.
      One problem with this algorithm is that it is unable to detect
      the difference between "Dr." in

         [...] Dr. Frankenstein's monster [...]

      y "Spot." en:

         [...] See Spot. See Spot run [...]

      "fix_sentence_endings" es falso por defecto.

      Dado que el algoritmo de detección de oraciones se basa en
      "string.lowercase" para la definición de "letra en minúscula", y
      en la convención de utilizar dos espacios después de un punto
      para separar las oraciones en la misma línea, es específico para
      los textos en inglés.

   break_long_words

      (default: "True") Si es verdadero, entonces las palabras más
      largas que "width" se romperán para asegurar que ninguna línea
      sea más larga que "width".  Si es falso, las palabras largas no
      se romperán, y algunas líneas pueden ser más largas que "width".
      (Las palabras largas se pondrán en una línea por sí mismas, para
      minimizar la cantidad en que se excede "width").

   break_on_hyphens

      (predeterminado: "True") Si es verdadero, el ajuste se producirá
      preferiblemente en espacios en blanco y justo después de los
      guiones en palabras compuestas, como es habitual en inglés. Si
      es falso, solo los espacios en blanco se considerarán lugares
      potencialmente buenos para los saltos de línea, pero debe
      establecer "break_long_words" en falso si desea palabras
      verdaderamente insecables. El comportamiento predeterminado en
      versiones anteriores era permitir siempre romper palabras con
      guiones.

   max_lines

      (default: "None") Si es "None", entonces la salida contendrá
      como máximo *max_lines*, con un *placeholder* que aparecerá al
      final de la salida.

      Added in version 3.4.

   placeholder

      (default: "' [...]'") Cadena que aparecerá al final del texto de
      salida si ha sido truncado.

      Added in version 3.4.

   "TextWrapper" también proporciona algunos métodos públicos,
   análogos a las funciones de conveniencia a nivel de módulo:

   wrap(text)

      Envuelve el párrafo individual en *text* (una cadena) para que
      cada línea tenga como máximo "width" caracteres de largo.  Todas
      las opciones de envoltura se toman de los atributos de la
      instancia "TextWrapper".  Retorna una lista de líneas de salida,
      sin las nuevas líneas finales.  Si la salida envuelta no tiene
      contenido, la lista retornada estará vacía.

   fill(text)

      Envuelve el único párrafo en *text*, y retorna una única cadena
      que contiene el párrafo envuelto.
