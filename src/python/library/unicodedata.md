---
title: '"unicodedata" --- Unicode Database'
source_url: https://docs.python.org/es/3
source_path: library/unicodedata.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4350
---

# "unicodedata" --- Unicode Database

======================================================================

This module provides access to the Unicode Character Database (UCD)
which defines character properties for all Unicode characters. The
data contained in this database is compiled from the UCD version
16.0.0.

El módulo utiliza los mismos nombres y símbolos definidos por el Anexo
#44 del estándar Unicode de la "Base de datos de caracteres Unicode".
Define las siguientes funciones:

Ver también:

  The CÓMO (HOWTO) Unicode for more information about Unicode and how
  to use this module.

unicodedata.lookup(name)

   Look up character by name.  If a character with the given name is
   found, return the corresponding character.  If not found,
   "KeyError" is raised. For example:

      >>> unicodedata.lookup('LEFT CURLY BRACKET')
      '{'

   The characters returned by this function are the same as those
   produced by "\N" escape sequence in string literals. For example:

      >>> unicodedata.lookup('MIDDLE DOT') == '\N{MIDDLE DOT}'
      True

   Distinto en la versión 3.3: Se ha agregado soporte para alias de
   nombre [1] y secuencias con nombre [2].

unicodedata.name(chr, default=None, /)

   Returns the name assigned to the character *chr* as a string. If no
   name is defined, *default* is returned, or, if not given,
   "ValueError" is raised. For example:

      >>> unicodedata.name('½')
      'VULGAR FRACTION ONE HALF'
      >>> unicodedata.name('\uFFFF', 'fallback')
      'fallback'

unicodedata.decimal(chr, default=None, /)

   Returns the decimal value assigned to the character *chr* as
   integer. If no such value is defined, *default* is returned, or, if
   not given, "ValueError" is raised. For example:

      >>> unicodedata.decimal('\N{ARABIC-INDIC DIGIT NINE}')
      9
      >>> unicodedata.decimal('\N{SUPERSCRIPT NINE}', -1)
      -1

unicodedata.digit(chr, default=None, /)

   Returns the digit value assigned to the character *chr* as integer.
   If no such value is defined, *default* is returned, or, if not
   given, "ValueError" is raised:

      >>> unicodedata.digit('\N{SUPERSCRIPT NINE}')
      9

unicodedata.numeric(chr, default=None, /)

   Returns the numeric value assigned to the character *chr* as float.
   If no such value is defined, *default* is returned, or, if not
   given, "ValueError" is raised:

      >>> unicodedata.numeric('½')
      0.5

unicodedata.category(chr)

   Returns the general category assigned to the character *chr* as
   string. General category names consist of two letters. See the
   General Category Values section of the Unicode Character Database
   documentation for a list of category codes. For example:

      >>> unicodedata.category('A')  # 'L'etter, 'u'ppercase
      'Lu'

unicodedata.bidirectional(chr)

   Returns the bidirectional class assigned to the character *chr* as
   string. If no such value is defined, an empty string is returned.
   See the Bidirectional Class Values section of the Unicode Character
   Database documentation for a list of bidirectional codes. For
   example:

      >>> unicodedata.bidirectional('\N{ARABIC-INDIC DIGIT SEVEN}') # 'A'rabic, 'N'umber
      'AN'

unicodedata.combining(chr)

   Returns the canonical combining class assigned to the character
   *chr* as integer. Returns "0" if no combining class is defined. See
   the Canonical Combining Class Values section of the Unicode
   Character Database for more information.

unicodedata.east_asian_width(chr)

   Returns the east asian width assigned to the character *chr* as
   string. For a list of widths and or more information, see the
   Unicode Standard Annex #11.

unicodedata.mirrored(chr)

   Returns the mirrored property assigned to the character *chr* as
   integer. Returns "1" if the character has been identified as a
   "mirrored" character in bidirectional text, "0" otherwise. For
   example:

      >>> unicodedata.mirrored('>')
      1

unicodedata.decomposition(chr)

   Returns the character decomposition mapping assigned to the
   character *chr* as string. An empty string is returned in case no
   such mapping is defined. For example:

      >>> unicodedata.decomposition('Ã')
      '0041 0303'

unicodedata.normalize(form, unistr)

   Retorna la forma normalizada *form* para la cadena Unicode
   *unistr*. Los valores válidos para *form* son 'NFC', 'NFKC', 'NFD'
   y 'NFKD'.

   El estándar Unicode define varias formas de normalización de una
   cadena Unicode, basándose en la definición de equivalencia canónica
   y equivalencia de compatibilidad. En Unicode, varios caracteres se
   pueden expresar de diversas formas. Por ejemplo, el carácter U+00C7
   (LETRA C LATINA MAYÚSCULA CON CEDILLA) también se puede expresar
   con la secuencia U+0043 (LETRA C LATINA MAYÚSCULA) U+0327 (CEDILLA
   COMBINABLE).

   Para cada carácter, hay dos formas normalizadas: la forma normal C
   y la forma normal D. La forma normal D (NFD) también se conoce como
   descomposición canónica y traduce cada carácter a su forma
   descompuesta. La forma normal C (NFC) primero aplica una
   descomposición canónica y luego vuelve a componer los caracteres
   combinados previamente.

   In addition to these two forms, there are two additional normal
   forms based on compatibility equivalence. In Unicode, certain
   characters are supported which normally would be unified with other
   characters. For example, U+2160 (ROMAN NUMERAL ONE) is really the
   same thing as U+0049 (LATIN CAPITAL LETTER I). However, it is
   supported in Unicode for compatibility with existing character sets
   (for example, gb2312).

   The normal form KD (NFKD) will apply the compatibility
   decomposition, that is, replace all compatibility characters with
   their equivalents. The normal form KC (NFKC) first applies the
   compatibility decomposition, followed by the canonical composition.

   Incluso si dos cadenas Unicode están normalizadas y parecen iguales
   para un lector humano, si una tiene caracteres combinados y la otra
   no, es posible que no se comparen como iguales.

unicodedata.is_normalized(form, unistr)

   Retorna si la cadena Unicode *unistr* está en la forma normalizada
   *form*. Los valores válidos para *form* son 'NFC', 'NFKC', 'NFD' y
   'NFKD'.

   Added in version 3.8.

Además, el módulo expone las siguientes constantes:

unicodedata.unidata_version

   La versión de la base de datos Unicode usada en este módulo.

unicodedata.ucd_3_2_0

   Este es un objeto que tiene los mismos métodos que el módulo
   completo, pero usa la versión 3.2 de la base de datos Unicode en su
   lugar. Es útil para aplicaciones que requieren esta versión
   específica de la base de datos Unicode (como IDNA).

-[ Notas al pie ]-

[1] https://www.unicode.org/Public/16.0.0/ucd/NameAliases.txt

[2] https://www.unicode.org/Public/16.0.0/ucd/NamedSequences.txt
