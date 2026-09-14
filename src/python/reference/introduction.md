---
title: 1. Introducción
source_url: https://docs.python.org/es/3
source_path: reference/introduction.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: reference
order: 4820
---

# 1. Introducción

Este manual de referencia describe el lenguaje de programación Python.
No pretende ser un tutorial.

Aunque intento ser lo más preciso posible, he optado por utilizar el
Español (N. de T.: del original en inglés "I chose to use English")"
en lugar de especificaciones formales para todo, excepto para la
sintaxis y el análisis léxico. Esto debería hacer el documento más
comprensible para el lector medio, pero dejará espacio para
ambigüedades. En consecuencia, si vienes de Marte y tratas de re
implementar Python sólo a partir de este documento, puede que tengas
que adivinar cosas y, de hecho, probablemente acabarías implementando
un lenguaje bastante diferente. Por otro lado, si estás usando Python
y te preguntas cuáles son las reglas precisas sobre un área particular
del lenguaje, deberías poder encontrarlas aquí. Si te gustaría ver una
definición más formal del lenguaje, quizás podrías ofrecer tu tiempo
--- o inventar una máquina clonadora :-).

Es peligroso añadir muchos detalles de implementación en un documento
de referencia: la implementación puede cambiar y otras
implementaciones del lenguaje pueden funcionar de forma diferente. Por
otro lado, CPython es la implementación de Python más usada (aunque
implementaciones alternativas están ganando soporte), y es importante
mencionar sus detalles particulares especialmente donde la
implementación  impone limitaciones adicionales. Por lo tanto,
encontrarás pequeñas "notas sobre la implementación" repartidas por
todo el texto.

Cada implementación de Python viene con un número de módulos estándar
incorporados. Éstos están documentados en La biblioteca estándar de
Python. Unos pocos de estos módulos son citados cuando interactúan de
forma significativa con la definición del lenguaje.

## 1.1. Implementaciones alternativas

Aunque hay una implementación de Python que es, de lejos, la más
popular, hay otras implementaciones alternativas que pueden ser de
particular interés para diferentes audiencias.

Las implementaciones conocidas incluyen:

CPython
   Es la implementación original, y la más mantenida, de Python y está
   escrita en C. Las nuevas características del lenguaje normalmente
   aparecen primero aquí.

Jython
   Python implementado en Java. Esta implementación puede utilizarse
   como lenguaje de scripting para aplicaciones Java, o puede
   utilizarse para crear aplicaciones utilizando las bibliotecas de
   clases Java.  También se utiliza a menudo para crear pruebas para
   bibliotecas Java. Puede encontrar más información en the Jython
   website.

Python para .NET
   Esta implementación, de hecho, usa la implementación CPython, pero
   es una aplicación .NET gestionada y usa librerías .NET. Ha sido
   creada por Brian Lloyd. Para más información ir al sitio web de
   Python for .NET.

IronPython
   Una alternativa de Python para .NET.  A diferencia de Python.NET,
   esta es una implementación completa de Python que genera IL, y
   compila código Python directamente a ensamblados .NET.  Fue creado
   por Jim Hugunin, el creador original de Jython. Para más
   información, consulte el sitio web de IronPython.

PyPy
   Una implementación de Python escrita completamente en Python.
   Soporta varias características avanzadas que no se encuentran en
   otras implementaciones como compatibilidad stackless y un
   compilador Just in Time. Uno de los objetivos del proyecto es
   fomentar la experimentación con el propio lenguaje facilitando la
   modificación del intérprete (ya que está escrito en Python). Puede
   encontrar más información en la página principal del proyecto 'PyPy
   <https://www.pypy.org/>_'.

Cada una de estas implementaciones varía de una forma u otra del
lenguaje tal y como está documentado en este manual, o introduce
información específica más allá de lo cubierto por la documentación
estándar de Python. Por favor, consulte la documentación específica de
cada implementación para saber qué tienes que saber acerca de la
implementación específica que uses.

## 1.2. Notación

The descriptions of lexical analysis and syntax use a grammar notation
that is a mixture of EBNF and PEG. For example:

   name:   letter (letter | digit | "_")*
   letter: "a"..."z" | "A"..."Z"
   digit:  "0"..."9"

In this example, the first line says that a "name" is a "letter"
followed by a sequence of zero or more "letter"s, "digit"s, and
underscores. A "letter" in turn is any of the single characters "'a'"
through "'z'" and "A" through "Z"; a "digit" is a single character
from "0" to "9".

Each rule begins with a name (which identifies the rule that's being
defined) followed by a colon, ":". The definition to the right of the
colon uses the following syntax elements:

* "name": A name refers to another rule. Where possible, it is a link
  to the rule's definition.

  * "TOKEN": An uppercase name refers to a *token*. For the purposes
    of grammar definitions, tokens are the same as rules.

* ""text"", "'text'": Text in single or double quotes must match
  literally (without the quotes). The type of quote is chosen
  according to the meaning of "text":

  * "'if'": A name in single quotes denotes a keyword.

  * ""case"": A name in double quotes denotes a soft-keyword.

  * "'@'": A non-letter symbol in single quotes denotes an "OP" token,
    that is, a delimiter or operator.

* "e1 e2": Items separated only by whitespace denote a sequence. Here,
  "e1" must be followed by "e2".

* "e1 | e2": A vertical bar is used to separate alternatives. It
  denotes PEG's "ordered choice": if "e1" matches, "e2" is not
  considered. In traditional PEG grammars, this is written as a slash,
  "/", rather than a vertical bar. See **PEP 617** for more background
  and details.

* "e*": A star means zero or more repetitions of the preceding item.

* "e+": Likewise, a plus means one or more repetitions.

* "[e]": A phrase enclosed in square brackets means zero or one
  occurrences. In other words, the enclosed phrase is optional.

* "e?": A question mark has exactly the same meaning as square
  brackets: the preceding item is optional.

* "(e)": Parentheses are used for grouping.

The following notation is only used in lexical definitions.

* ""a"..."z"": Two literal characters separated by three dots mean a
  choice of any single character in the given (inclusive) range of
  ASCII characters.

* "<...>": A phrase between angular brackets gives an informal
  description of the matched symbol (for example, "<any ASCII
  character except "\">"), or an abbreviation that is defined in
  nearby text (for example, "<Lu>").

Some definitions also use *lookaheads*, which indicate that an element
must (or must not) match at a given position, but without consuming
any input:

* "&e": a positive lookahead (that is, "e" is required to match)

* "!e": a negative lookahead (that is, "e" is required *not* to match)

The unary operators ("*", "+", "?") bind as tightly as possible; the
vertical bar ("|") binds most loosely.

White space is only meaningful to separate tokens.

Rules are normally contained on a single line, but rules that are too
long may be wrapped:

   literal: stringliteral | bytesliteral
            | integer | floatnumber | imagnumber

Alternatively, rules may be formatted with the first line ending at
the colon, and each alternative beginning with a vertical bar on a new
line. For example:

   literal:
      | stringliteral
      | bytesliteral
      | integer
      | floatnumber
      | imagnumber

This does *not* mean that there is an empty first alternative.

### 1.2.1. Lexical and Syntactic definitions

There is some difference between *lexical* and *syntactic* analysis:
the *lexical analyzer* operates on the individual characters of the
input source, while the *parser* (syntactic analyzer) operates on the
stream of *tokens* generated by the lexical analysis. However, in some
cases the exact boundary between the two phases is a CPython
implementation detail.

The practical difference between the two is that in *lexical*
definitions, all whitespace is significant. The lexical analyzer
discards all whitespace that is not converted to tokens like
"token.INDENT" or "NEWLINE". *Syntactic* definitions then use these
tokens, rather than source characters.

This documentation uses the same BNF grammar for both styles of
definitions. All uses of BNF in the next chapter (Análisis léxico) are
lexical definitions; uses in subsequent chapters are syntactic
definitions.
