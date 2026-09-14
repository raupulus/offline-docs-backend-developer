---
title: '"tokenize" --- Tokenizer for Python source'
source_url: https://docs.python.org/es/3
source_path: library/tokenize.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4260
---

# "tokenize" --- Tokenizer for Python source

**Código fuente:** Lib/tokenize.py

======================================================================

The "tokenize" module provides a lexical scanner for Python source
code, implemented in Python.  The scanner in this module returns
comments as tokens as well, making it useful for implementing "pretty-
printers", including colorizers for on-screen displays.

Para simplificar el manejo de flujos de tokens, todos los tokens
operator y delimiter y "Ellipsis" se retorna usando el tipo genérico
"OP". El tipo exacto se puede determinar usando la propiedad
"exact_type" en la *named tuple* retornada por "tokenize.tokenize()".

Advertencia:

  Ten en cuenta que las funciones en este módulo están diseñadas
  únicamente para analizar código Python sintácticamente válido
  (código que no genera errores al ser analizado usando
  "ast.parse()"). El comportamiento de las funciones en este módulo es
  **indefinido** cuando se proporciona código Python no válido y puede
  cambiar en cualquier momento.

## Convirtiendo la entrada en *tokens*

El punto de entrada principal es un *generador*:

tokenize.tokenize(readline)

   El generador "tokenize()" requiere un argumento, *readline*, que
   debe ser un objeto invocable que provee la misma interfaz que el
   método "io.IOBase.readline()" de los objetos archivos. Cada llamada
   a la función debe retornar una línea de entrada como bytes.

   El generador produce una tupla con los siguientes 5 miembros: El
   tipo de token, la cadena del token, una tupla "(srow, scol)" de
   enteros especificando la fila y columna donde el token empieza en
   el código, una "(erow, ecol)" de enteros especificando la fila y
   columna donde el token acaba en el código, y la línea en la que se
   encontró el token. La línea pasada (el último elemento de la tupla)
   es la línea *física*. La tupla se retorna como una *named tuple*
   con los campos: "type string start end line".

   La *named tuple* retorna tiene una propiedad adicional llamada
   "exact_type" que contiene el tipo de operador exacto para tokens
   "OP". Para todos los otros tipos de token, "exact_type" es el valor
   del campo "type" de la tupla con su respectivo nombre.

   Distinto en la versión 3.1: Añadido soporte para tuplas con nombre.

   Distinto en la versión 3.3: Añadido soporte para "exact_type".

   "tokenize()" determina la codificación del fichero buscando una
   marca BOM UTF-8 o una *cookie* de codificación, de acuerdo con
   **PEP 263**.

tokenize.generate_tokens(readline)

   Convertir a tokens una fuente leyendo cadenas unicode en lugar de
   bytes.

   Como "tokenize()", el argumento *readline* es un invocable que
   retorna una sola línea de entrada. Sin embargo, "generate_tokens()"
   espera que *readline* retorne un objeto *str* en lugar de *bytes*.

   El resultado es un iterador que produce tuplas con nombre,
   exactamente como "tokenize()". No produce un token "ENCODING".

All constants from the "token" module are also exported from
"tokenize".

Otra función se encarga de invertir el proceso de conversión. Esto es
útil para crear herramientas que convierten a tokens un script,
modificar el flujo de token, y escribir el script modificado.

tokenize.untokenize(iterable)

   Convierte los *tokens* de vuelta en código fuente Python. El
   *iterable* debe retornar secuencias con al menos dos elementos, el
   tipo de *token* y la cadena del *token*. Cualquier otro elemento de
   la secuencia es ignorado.

   The result is guaranteed to tokenize back to match the input so
   that the conversion is lossless and round-trips are assured.  The
   guarantee applies only to the token type and token string as the
   spacing between tokens (column positions) may change.

   Retorna bytes, codificados usando el token "ENCODING", que es el
   primer elemento de la secuencia retornada por "tokenize()". Si no
   hay un token de codificación en la entrada, retorna una cadena.

"tokenize()" necesita detectar la codificación de los ficheros fuente
que convierte a tokens. La función que utiliza para hacer esto está
disponible como:

tokenize.detect_encoding(readline)

   La función "detect_encoding()" se usa para detectar la codificación
   que debería usarse al leer un fichero fuente Python. Requiere un
   argumento, *readline*, del mismo modo que el generador
   "tokenize()".

   Llamará a *readline* un máximo de dos veces, retornando la
   codificación usada, como cadena, y una lista del resto de líneas
   leídas, no descodificadas de *bytes*.

   Detecta la codificación a partir de la presencia de una marca BOM
   UTF-8 o una *cookie* de codificación, como se especifica en **PEP
   263**. Si ambas están presentes pero en desacuerdo, se lanzará un
   "SyntaxError". Resaltar que si se encuentra la marca BOM, se
   retornará "'utf-8-sig'" como codificación.

   Si no se especifica una codificación, por defecto se retornará
   "'utf-8'".

   Usa "open()" para abrir ficheros fuente Python: Ésta utiliza
   "detect_encoding()" para detectar la codificación del fichero.

tokenize.open(filename)

   Abrir un fichero en modo sólo lectura usando la codificación
   detectada por "detect_encoding()".

   Added in version 3.2.

exception tokenize.TokenError

   Lanzada cuando una expresión o docstring que puede separarse en más
   líneas no está completa en el fichero, por ejemplo:

      """Beginning of
      docstring

   o:

      [1,
       2,
       3

## Uso como línea de comandos

Added in version 3.3.

The "tokenize" module can be executed as a script from the command
line. It is as simple as:

   python -m tokenize [-e] [filename.py]

Se aceptan las siguientes opciones:

-h, --help

   muestra el mensaje de ayuda y sale

-e, --exact

   muestra los nombres de token usando el tipo exacto

Si se especifica "filename.py", se convierte su contenido a tokens por
la salida estándar. En otro caso, se convierte la entrada estándar.

## Ejemplos

Ejemplo de un script que transforma literales float en objetos
Decimal:

   from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
   from io import BytesIO

   def decistmt(s):
       """Substitute Decimals for floats in a string of statements.

       >>> from decimal import Decimal
       >>> s = 'print(+21.3e-5*-.1234/81.7)'
       >>> decistmt(s)
       "print (+Decimal ('21.3e-5')*-Decimal ('.1234')/Decimal ('81.7'))"

       The format of the exponent is inherited from the platform C library.
       Known cases are "e-007" (Windows) and "e-07" (not Windows).  Since
       we're only showing 12 digits, and the 13th isn't close to 5, the
       rest of the output should be platform-independent.

       >>> exec(s)  #doctest: +ELLIPSIS
       -3.21716034272e-0...7

       Output from calculations with Decimal should be identical across all
       platforms.

       >>> exec(decistmt(s))
       -3.217160342717258261933904529E-7
       """
       result = []
       g = tokenize(BytesIO(s.encode('utf-8')).readline)  # tokenize the string
       for toknum, tokval, _, _, _ in g:
           if toknum == NUMBER and '.' in tokval:  # replace NUMBER tokens
               result.extend([
                   (NAME, 'Decimal'),
                   (OP, '('),
                   (STRING, repr(tokval)),
                   (OP, ')')
               ])
           else:
               result.append((toknum, tokval))
       return untokenize(result).decode('utf-8')

Ejemplo de conversión desde la línea de comandos. El *script*:

   def say_hello():
       print("Hello, World!")

   say_hello()

se convertirá en la salida siguiente, donde la primera columna es el
rango de coordenadas línea/columna donde se encuentra el token, la
segunda columna es el nombre del token, y la última columna es el
valor del token, si lo hay

   $ python -m tokenize hello.py
   0,0-0,0:            ENCODING       'utf-8'
   1,0-1,3:            NAME           'def'
   1,4-1,13:           NAME           'say_hello'
   1,13-1,14:          OP             '('
   1,14-1,15:          OP             ')'
   1,15-1,16:          OP             ':'
   1,16-1,17:          NEWLINE        '\n'
   2,0-2,4:            INDENT         '    '
   2,4-2,9:            NAME           'print'
   2,9-2,10:           OP             '('
   2,10-2,25:          STRING         '"Hello, World!"'
   2,25-2,26:          OP             ')'
   2,26-2,27:          NEWLINE        '\n'
   3,0-3,1:            NL             '\n'
   4,0-4,0:            DEDENT         ''
   4,0-4,9:            NAME           'say_hello'
   4,9-4,10:           OP             '('
   4,10-4,11:          OP             ')'
   4,11-4,12:          NEWLINE        '\n'
   5,0-5,0:            ENDMARKER      ''

Los nombres de tipos de token exactos se pueden mostrar con la opción
"-e":

   $ python -m tokenize -e hello.py
   0,0-0,0:            ENCODING       'utf-8'
   1,0-1,3:            NAME           'def'
   1,4-1,13:           NAME           'say_hello'
   1,13-1,14:          LPAR           '('
   1,14-1,15:          RPAR           ')'
   1,15-1,16:          COLON          ':'
   1,16-1,17:          NEWLINE        '\n'
   2,0-2,4:            INDENT         '    '
   2,4-2,9:            NAME           'print'
   2,9-2,10:           LPAR           '('
   2,10-2,25:          STRING         '"Hello, World!"'
   2,25-2,26:          RPAR           ')'
   2,26-2,27:          NEWLINE        '\n'
   3,0-3,1:            NL             '\n'
   4,0-4,0:            DEDENT         ''
   4,0-4,9:            NAME           'say_hello'
   4,9-4,10:           LPAR           '('
   4,10-4,11:          RPAR           ')'
   4,11-4,12:          NEWLINE        '\n'
   5,0-5,0:            ENDMARKER      ''

Ejemplo de tokenización de un fichero programáticamente, leyendo
cadenas unicode en lugar de *bytes* con "generate_tokens()":

   import tokenize

   with tokenize.open('hello.py') as f:
       tokens = tokenize.generate_tokens(f.readline)
       for token in tokens:
           print(token)

O leyendo *bytes* directamente con "tokenize()":

   import tokenize

   with open('hello.py', 'rb') as f:
       tokens = tokenize.tokenize(f.readline)
       for token in tokens:
           print(token)
