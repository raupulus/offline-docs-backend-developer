---
title: '"locale" --- Internationalization services'
source_url: https://docs.python.org/es/3
source_path: library/locale.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3110
---

# "locale" --- Internationalization services

**Source code:** Lib/locale.py

======================================================================

The "locale" module opens access to the POSIX locale database and
functionality. The POSIX locale mechanism allows programmers to deal
with certain cultural issues in an application, without requiring the
programmer to know all the specifics of each country where the
software is executed.

The "locale" module is implemented on top of the "_locale" module,
which in turn uses an ANSI C locale implementation if available.

The "locale" module defines the following exception and functions:

exception locale.Error

   Cuando el *locale* pasado a "setlocale()" no es reconocido, se
   lanza una excepción.

locale.setlocale(category, locale=None)

   If *locale* is given and not "None", "setlocale()" modifies the
   locale setting for the *category*. The available categories are
   listed in the data description below. *locale* may be a string, or
   a pair, language code and encoding. An empty string specifies the
   user's default settings. If the modification of the locale fails,
   the exception "Error" is raised. If successful, the new locale
   setting is returned.

   If *locale* is a pair, it is converted to a locale name using the
   locale aliasing engine. The language code has the same format as a
   locale name, but without encoding and "@"-modifier. The language
   code and encoding can be "None".

   Si se omite *locale* o es "None", se retorna la configuración
   actual para *category*.

   Ejemplo:

      >>> import locale
      >>> loc = locale.setlocale(locale.LC_ALL)  # get current locale
      # use German locale; name and availability varies with platform
      >>> locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
      >>> locale.strcoll('f\xe4n', 'foo')  # compare a string containing an umlaut
      >>> locale.setlocale(locale.LC_ALL, '')   # use user's preferred locale
      >>> locale.setlocale(locale.LC_ALL, 'C')  # use default (C) locale
      >>> locale.setlocale(locale.LC_ALL, loc)  # restore saved locale

   "setlocale()" is not thread-safe on most systems. Applications
   typically start with a call of:

      import locale
      locale.setlocale(locale.LC_ALL, '')

   Esto establece la configuración regional de todas las categorías en
   la configuración predeterminada del usuario (normalmente
   especificada en la variable de entorno "LANG" ).  Si la
   configuración regional no se cambia a partir de entonces, el uso de
   multiprocesamiento, no debería causar problemas.

locale.localeconv()

   Retorna la base de datos de las convenciones locales como
   diccionario. Este diccionario tiene las siguientes cadenas de
   caracteres como claves:

   +------------------------+---------------------------------------+----------------------------------+
   | Categoría              | Clave                                 | Significado                      |
   |========================|=======================================|==================================|
   | "LC_NUMERIC"           | "'decimal_point'"                     | Carácter de punto decimal.       |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'agrupación'"                        | Secuencia de números que         |
   |                        |                                       | especifica qué posiciones        |
   |                        |                                       | relativas se espera el           |
   |                        |                                       | "'miles_sep'". Si la secuencia   |
   |                        |                                       | termina con "CHAR_MAX", no se    |
   |                        |                                       | realiza ninguna agrupación       |
   |                        |                                       | adicional. Si la secuencia       |
   |                        |                                       | termina con un "0", el último    |
   |                        |                                       | tamaño de grupo se usa           |
   |                        |                                       | repetidamente.                   |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'thousands_sep'"                     | Carácter utilizado entre grupos. |
   +------------------------+---------------------------------------+----------------------------------+
   | "LC_MONETARY"          | "'int_curr_symbol'"                   | Símbolo de moneda internacional. |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'currency_symbol'"                   | Símbolo de moneda local.         |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'p_cs_precedes/n_cs_precedes'"       | Si el símbolo de moneda precede  |
   |                        |                                       | al valor (para valores positivos |
   |                        |                                       | o negativos).                    |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'p_sep_by_space/n_sep_by_space'"     | Si el símbolo de moneda está     |
   |                        |                                       | separado del valor por un        |
   |                        |                                       | espacio (para valores positivos  |
   |                        |                                       | o negativos).                    |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'mon_decimal_point'"                 | Punto decimal utilizado para     |
   |                        |                                       | valores monetarios.              |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'frac_digits'"                       | Número de dígitos fraccionarios  |
   |                        |                                       | utilizados en el formateo local  |
   |                        |                                       | de valores monetarios.           |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'int_frac_digits'"                   | Número de dígitos fraccionarios  |
   |                        |                                       | utilizados en el formateo        |
   |                        |                                       | internacional de valores         |
   |                        |                                       | monetarios.                      |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'mon_thousands_sep'"                 | Separador de grupo utilizado     |
   |                        |                                       | para valores monetarios.         |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'mon_grouping'"                      | Equivalente a "'grouping'",      |
   |                        |                                       | utilizada para valores           |
   |                        |                                       | monetarios.                      |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'positive_sign'"                     | Símbolo utilizado para anotar un |
   |                        |                                       | valor monetario positivo.        |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'negative_sign'"                     | Símbolo utilizado para anotar un |
   |                        |                                       | valor monetario negativo.        |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'p_sign_posn/n_sign_posn'"           | La posición del signo (para      |
   |                        |                                       | respuestas positivas. valores    |
   |                        |                                       | negativos), ver abajo.           |
   +------------------------+---------------------------------------+----------------------------------+

   Todos los valores numéricos se pueden establecer a "CHAR_MAX" para
   indicar que no hay ningún valor especificado en esta configuración
   regional.

   Los valores posibles para "'p_sign_posn'" y "'n_sign_posn'" se dan
   a continuación.

   +----------------+-------------------------------------------+
   | Valor          | Explicación                               |
   |================|===========================================|
   | "0"            | Moneda y valor están rodeados por         |
   |                | paréntesis.                               |
   +----------------+-------------------------------------------+
   | "1"            | El signo debe preceder al valor y al      |
   |                | símbolo de moneda.                        |
   +----------------+-------------------------------------------+
   | "2"            | El signo debe seguir el valor y el        |
   |                | símbolo de moneda.                        |
   +----------------+-------------------------------------------+
   | "3"            | El signo debe preceder inmediatamente al  |
   |                | valor.                                    |
   +----------------+-------------------------------------------+
   | "4"            | El signo debe seguir inmediatamente al    |
   |                | valor.                                    |
   +----------------+-------------------------------------------+
   | "CHAR_MAX"     | No se especifica nada en esta             |
   |                | configuración regional.                   |
   +----------------+-------------------------------------------+

   The function temporarily sets the "LC_CTYPE" locale to the
   "LC_NUMERIC" locale or the "LC_MONETARY" locale if locales are
   different and numeric or monetary strings are non-ASCII. This
   temporary change affects other threads.

   Distinto en la versión 3.7: The function now temporarily sets the
   "LC_CTYPE" locale to the "LC_NUMERIC" locale in some cases.

locale.nl_langinfo(option)

   Retorna información específica de la configuración regional como
   una cadena de caracteres.  Esta función no está disponible en todos
   los sistemas, y el conjunto de opciones posibles también puede
   variar entre plataformas.  Los posibles valores de argumento son
   números, para los cuales las constantes simbólicas están
   disponibles en el módulo de configuración regional.

   La función "nl_langinfo()" acepta una de las siguientes claves.  La
   mayoría de las descripciones están tomadas de la descripción
   correspondiente en la biblioteca C de GNU.

   locale.CODESET

      Obtiene una cadena de caracteres con el nombre de la
      codificación de caracteres utilizada en la configuración
      regional seleccionada.

   locale.D_T_FMT

      Obtiene una cadena de caracteres que se puede utilizar como
      cadena de caracteres de formato para "time.strftime()" para
      representar la fecha y la hora de una manera específica de la
      configuración regional.

   locale.D_FMT

      Obtiene una cadena de caracteres que se puede utilizar como
      cadena de formato para "time.strftime()" para representar una
      fecha de una manera específica de la configuración regional.

   locale.T_FMT

      Obtiene una cadena de caracteres que se puede utilizar como
      cadena de formato para "time.strftime()" para representar un
      tiempo de una manera específica de la configuración regional.

   locale.T_FMT_AMPM

      Obtiene una cadena de caracteres de formato para
      "time.strftime()" para representar el tiempo en el formato
      am/pm.

   locale.DAY_1
   locale.DAY_2
   locale.DAY_3
   locale.DAY_4
   locale.DAY_5
   locale.DAY_6
   locale.DAY_7

      Consigue el nombre del n-ésimo día de la semana.

      Nota:

        Esto sigue la convención estadounidense de "DAY_1" siendo
        domingo, no la convención internacional (ISO 8601) que el
        lunes es el primer día de la semana.

   locale.ABDAY_1
   locale.ABDAY_2
   locale.ABDAY_3
   locale.ABDAY_4
   locale.ABDAY_5
   locale.ABDAY_6
   locale.ABDAY_7

      Obtener el nombre abreviado del n-ésimo día de la semana.

   locale.MON_1
   locale.MON_2
   locale.MON_3
   locale.MON_4
   locale.MON_5
   locale.MON_6
   locale.MON_7
   locale.MON_8
   locale.MON_9
   locale.MON_10
   locale.MON_11
   locale.MON_12

      Obtener el nombre del n-ésimo mes.

   locale.ABMON_1
   locale.ABMON_2
   locale.ABMON_3
   locale.ABMON_4
   locale.ABMON_5
   locale.ABMON_6
   locale.ABMON_7
   locale.ABMON_8
   locale.ABMON_9
   locale.ABMON_10
   locale.ABMON_11
   locale.ABMON_12

      Obtener el nombre abreviado del enésimo mes.

   locale.RADIXCHAR

      Obtener el carácter radical (punto decimal, coma decimal, etc.).

   locale.THOUSEP

      Obtener el carácter separador de miles (grupos de tres dígitos).

   locale.YESEXPR

      Obtener una expresión regular que se pueda usar con la función
      regex para reconocer una respuesta positiva a una pregunta de sí
      / no.

   locale.NOEXPR

      Get a regular expression that can be used with the "regex(3)"
      function to recognize a negative response to a yes/no question.

      Nota:

        The regular expressions for "YESEXPR" and "NOEXPR" use syntax
        suitable for the "regex" function from the C library, which
        might differ from the syntax used in "re".

   locale.CRNCYSTR

      Obtener el símbolo de moneda, precedido por "-" si el símbolo
      debe aparecer antes del valor, "+" si el símbolo debe aparecer
      después del valor, o "." si el símbolo debe reemplazar el
      carácter raíz.

   locale.ERA

      Get a string which describes how years are counted and displayed
      for each era in a locale.

      La mayoría de las configuraciones regionales no definen este
      valor.  Un ejemplo de una localidad que sí define este valor es
      la japonesa.  En Japón, la representación tradicional de fechas
      incluye el nombre de la época correspondiente al reinado del
      entonces emperador.

      Normally it should not be necessary to use this value directly.
      Specifying the "E" modifier in their format strings causes the
      "time.strftime()" function to use this information. The format
      of the returned string is specified in *The Open Group Base
      Specifications Issue 8*, paragraph 7.3.5.2 LC_TIME C-Language
      Access.

   locale.ERA_D_T_FMT

      Obtener una cadena de caracteres de formato para
      "time.strftime()" para representar la fecha y la hora de una
      manera específica de la era.

   locale.ERA_D_FMT

      Obtener una cadena de caracteres de formato para
      "time.strftime()" para representar una fecha de una manera
      basada en una era específica.

   locale.ERA_T_FMT

      Obtener una cadena de caracteres de formato para
      "time.strftime()" para representar una hora de una manera basada
      en una era específica.

   locale.ALT_DIGITS

      Get a string consisting of up to 100 semicolon-separated symbols
      used to represent the values 0 to 99 in a locale-specific way.
      In most locales this is an empty string.

   The function temporarily sets the "LC_CTYPE" locale to the locale
   of the category that determines the requested value ("LC_TIME",
   "LC_NUMERIC", "LC_MONETARY" or "LC_MESSAGES") if locales are
   different and the resulting string is non-ASCII. This temporary
   change affects other threads.

   Distinto en la versión 3.14: The function now temporarily sets the
   "LC_CTYPE" locale in some cases.

locale.getdefaultlocale([envvars])

   Intenta determinar la configuración regional por defecto y los
   retorna como una tupla del formulario "(código de idioma,
   codificación)".

   De acuerdo con POSIX, un programa que no ha llamado a
   "setlocale(LC_ALL, '')" se ejecuta utilizando la configuración
   regional portátil "'C'" . Llamar a "setlocale(LC_ALL, ' ')" le
   permite usar la configuración regional predeterminada definida por
   la variable "LANG" . Dado que no queremos interferir con la
   configuración de configuración regional actual, emulamos el
   comportamiento de la manera descrita anteriormente.

   Para mantener la compatibilidad con otras plataformas, no sólo se
   prueba la variable "LANG" sino una lista de variables dadas como
   parámetro *envvars*.  Se utilizará la primera que se encuentre
   definida.  *envvars* por defecto a la ruta de búsqueda utilizada en
   GNU gettext; siempre debe contener el nombre de la variable "'LANG
   '".  La ruta de búsqueda GNU gettext contiene "'LC_ALL '",
   "'LC_CTYPE '", "'LANG '" y "'LANGUAGE '", en ese orden.

   The language code has the same format as a locale name, but without
   encoding and "@"-modifier. The language code and encoding may be
   "None" if their values cannot be determined. The "C" locale is
   represented as "(None, None)".

locale.getlocale(category=LC_CTYPE)

   Returns the current setting for the given locale category as a
   tuple containing the language code and encoding. *category* may be
   one of the "LC_*" values except "LC_ALL".  It defaults to
   "LC_CTYPE".

   The language code has the same format as a locale name, but without
   encoding and "@"-modifier. The language code and encoding may be
   "None" if their values cannot be determined. The "C" locale is
   represented as "(None, None)".

locale.getpreferredencoding(do_setlocale=True)

   Retorna la *locale encoding* utilizada para los datos de texto,
   según las preferencias del usuario.  Las preferencias del usuario
   se expresan de manera diferente en diferentes sistemas, y puede que
   no estén disponibles programáticamente en algunos sistemas, por lo
   que esta función solo retorna una suposición.

   En algunos sistemas, es necesario invocar "setlocale()" para
   obtener las preferencias del usuario, por lo que esta función no es
   segura para subprocesos. Si invocar *setlocale* no es necesario o
   deseado, *do_setlocale* se debe ajustar a "False".

   En Android o si Python UTF-8 Mode está habilitado, siempre retorna
   "'utf-8'", el argumento *locale encoding* y *do_setlocale* se
   ignoran.

   La pre-inicializacioń de Python configura la configuración regional
   LC_CTYPE. Véase también la *codificación del sistema de archivos y
   manejador de errores*.

   Distinto en la versión 3.7: La función ahora siempre retorna
   ""utf-8"" en Android o si Python UTF-8 Mode está habilitado.

locale.getencoding()

   Obtenga el *locale encoding* actual:

   * En Android y VxWorks, retorna ""utf-8"".

   * En Unix, retorna la codificación de la configuración regional
     "LC_CTYPE" actual. Retorna ""utf-8"" si "nl_langinfo(CODESET)"
     retorna una cadena vacía: por ejemplo, si no se admite la
     configuración regional actual de LC_CTYPE.

   * En Windows, retorna la página de códigos ANSI.

   La pre-inicializacioń de Python configura la configuración regional
   LC_CTYPE. Véase también la *codificación del sistema de archivos y
   manejador de errores*.

   Esta función es similar a "getpreferredencoding(False)" excepto que
   esta función ignora Python UTF-8 Mode.

   Added in version 3.11.

locale.normalize(localename)

   Retorna un código de configuración regional normalizado para el
   nombre configuración regional dado.  El código de configuración
   regional retornado está formateado para usarse con "setlocale()".
   Si la normalización falla, el nombre original se retorna sin
   cambios.

   Si no se conoce la codificación dada, la función por defecto
   codifica el código de configuración regional como "setlocale()".

locale.strcoll(string1, string2)

   Compara dos cadenas según la configuración actual "LC_COLLATE" .
   Como cualquier otra función de comparación, retorna un valor
   negativo o positivo, o "0", dependiendo de si *string1* compila
   antes o después de *string2* o es igual a él.

locale.strxfrm(string)

   Transforma una cadena en una que se puede utilizar en comparaciones
   de localización.  Por ejemplo, "strxfrm(s1) < strxfrm(s2)" es
   equivalente a "strcoll(s1, s2) < 0".  Esta función se puede
   utilizar cuando la misma cadena se compara repetidamente, p. ej.,
   al agrupar una secuencia de cadenas.

locale.format_string(format, val, grouping=False, monetary=False)

   Formats a number *val* according to the current "LC_NUMERIC"
   setting. The format follows the conventions of the "%" operator.
   For floating-point values, the decimal point is modified if
   appropriate.  If *grouping* is "True", also takes the grouping into
   account.

   Si *monetary* es verdadero, la conversión utiliza separador
   monetario de miles y cadenas de caracteres de agrupación.

   Procesa especificadores de formato como en "format % val", pero
   tiene en cuenta los ajustes de configuración regional actuales.

   Distinto en la versión 3.7: Se añadió el parámetro de la palabra
   clave *monetary*.

locale.currency(val, symbol=True, grouping=False, international=False)

   Formatea un número *val* según la configuración actual
   "LC_MONETARY" .

   The returned string includes the currency symbol if *symbol* is
   true, which is the default. If *grouping* is "True" (which is not
   the default), grouping is done with the value. If *international*
   is "True" (which is not the default), the international currency
   symbol is used.

   Nota:

     This function will not work with the 'C' locale, so you have to
     set a locale via "setlocale()" first.

locale.str(float)

   Formats a floating-point number using the same format as the built-
   in function "str(float)", but takes the decimal point into account.

locale.delocalize(string)

   Convierte una cadena de caracteres en una cadena de números
   normalizada, siguiendo la configuración "LC_NUMERIC".

   Added in version 3.5.

locale.localize(string, grouping=False, monetary=False)

   Convierte una cadena de números normalizada en una cadena de
   caracteres formateada siguiendo la configuración "LC_NUMERIC".

   Added in version 3.10.

locale.atof(string, func=float)

   Convierte una cadena en un número, siguiendo la configuración de
   "LC_NUMERIC", llamando a *func* según el resultado de llamar a
   "delocalize()" en *string*.

locale.atoi(string)

   Convierte una cadena de caracteres a un entero, siguiendo las
   convenciones "LC_NUMERIC" .

locale.LC_CTYPE

   Locale category for the character type functions.  Most
   importantly, this category defines the text encoding, i.e. how
   bytes are interpreted as Unicode codepoints.  See **PEP 538** and
   **PEP 540** for how this variable might be automatically coerced to
   "C.UTF-8" to avoid issues created by invalid settings in containers
   or incompatible settings passed over remote SSH connections.

   Python doesn't internally use locale-dependent character
   transformation functions from "ctype.h". Instead, "pyctype.h"
   provides locale-independent equivalents like "Py_TOLOWER".

locale.LC_COLLATE

   Locale category for sorting strings.  The functions "strcoll()" and
   "strxfrm()" of the "locale" module are affected.

locale.LC_TIME

   Categoría de configuración regional para el formateo de hora.  La
   función "time.strftime()" sigue estas convenciones.

locale.LC_MONETARY

   Categoría de configuración regional para el formateo de valores
   monetarios.  Las opciones disponibles están disponibles en la
   función "localeconv()" .

locale.LC_MESSAGES

   Categoría de configuración regional para visualización de mensajes.
   Python actualmente no admite mensajes de configuración regional
   específicos de la aplicación.  Los mensajes mostrados por el
   sistema operativo, como los retornados por "os.strerror()" podrían
   verse afectados por esta categoría.

   This value may not be available on operating systems not conforming
   to the POSIX standard, most notably Windows.

locale.LC_NUMERIC

   Locale category for formatting numbers.  The functions
   "format_string()", "atoi()", "atof()" and "str()" of the "locale"
   module are affected by that category.  All other numeric formatting
   operations are not affected.

locale.LC_ALL

   Combinación de todos los ajustes de configuración regional.  Si se
   utiliza este indicador cuando se cambia la localización, se intenta
   establecer la localización para todas las categorías. Si eso falla
   para cualquier categoría, ninguna categoría se cambia en absoluto.
   Cuando la configuración regional se recupera usando este indicador,
   se retorna una cadena de caracteres que indica la configuración
   para todas las categorías. Esta cadena de caracteres se puede usar
   más tarde para restaurar la configuración.

locale.CHAR_MAX

   Esta es una constante simbólica utilizada para diferentes valores
   retornados por "localeconv()".

## Segundo plano, detalles, indicaciones, consejos y advertencias

El estándar C define la configuración regional como una propiedad de
todo el programa que puede ser relativamente costosa de cambiar.
Además de eso, alguna implementación se rompe de tal manera que los
cambios de configuración local frecuentes pueden causar volcados de
núcleo.  Esto hace que la configuración regional sea algo dolorosa de
usar correctamente.

Inicialmente, cuando se inicia un programa, la configuración regional
es la configuración regional "C", no importa cuál sea la configuración
regional preferida por el usuario.  Hay una excepción: la categoría
"LC_CTYPE" se cambia al inicio para establecer la codificación de la
configuración regional actual en la codificación de configuración
regional preferida del usuario. El programa debe decir explícitamente
que quiere la configuración regional preferida del usuario para otras
categorías llamando a "setlocale(LC_ALL, '')".

Generalmente es una mala idea llamar "setlocale()" en alguna rutina de
biblioteca, ya que como efecto secundario afecta a todo el programa.
Guardar y restaurar es casi igual de malo: es caro y afecta a otros
hilos que se ejecutan antes de que los ajustes se hayan restaurado.

Si, al codificar un módulo para uso general, se necesita una versión
configuración regional independiente de una operación que se ve
afectada por la localización (como ciertos formatos utilizados con
"time.strftime()"), tendrá que encontrar una manera de hacerlo sin
usar la rutina de biblioteca estándar.  Aún mejor es convencerse a sí
mismo de que el uso de la configuración regional está bien.  Sólo como
último recurso debe documentar que su módulo no es compatible con la
configuración regional no-   "C".

The only way to perform numeric operations according to the locale is
to use the special functions defined by this module: "atof()",
"atoi()", "format_string()", "str()".

No hay manera de realizar conversiones de casos y clasificaciones de
caracteres de acuerdo a la configuración regional.  Para cadenas de
texto (Unicode) estas se hacen de acuerdo con el valor de carácter
solamente, mientras que para cadenas de bytes, las conversiones y
clasificaciones se hacen de acuerdo con el valor ASCII del byte, y
bytes cuyo bit alto se establece (es decir, bytes no ASCII) nunca se
convierten o se consideran parte de una clase de caracteres como letra
o espacio en blanco.

## Locale names

The format of the locale name is platform dependent, and the set of
supported locales can depend on the system configuration.

On Posix platforms, it usually has the format [1]:

     language ["_" territory] ["." charset] ["@" modifier]

where *language* is a two- or three-letter language code from ISO 639,
*territory* is a two-letter country or region code from ISO 3166,
*charset* is a locale encoding, and *modifier* is a script name, a
language subtag, a sort order identifier, or other locale modifier
(for example, "latin", "valencia", "stroke" and "euro").

On Windows, several formats are supported. [2] [3] A subset of IETF
BCP 47 tags:

     language ["-" script] ["-" territory] ["." charset]
     language ["-" script] "-" territory "-" modifier

where *language* and *territory* have the same meaning as in Posix,
*script* is a four-letter script code from ISO 15924, and *modifier*
is a language subtag, a sort order identifier or custom modifier (for
example, "valencia", "stroke" or "x-python"). Both hyphen ("'-'") and
underscore ("'_'") separators are supported. Only UTF-8 encoding is
allowed for BCP 47 tags.

Windows also supports locale names in the format:

     language ["_" territory] ["." charset]

where *language* and *territory* are full names, such as "English" and
"United States", and *charset* is either a code page number (for
example, "1252") or UTF-8. Only the underscore separator is supported
in this format.

The "C" locale is supported on all platforms.

[1] IEEE Std 1003.1-2024; 8.2 Internationalization Variables

[2] UCRT Locale names, Languages, and Country/Region strings

[3] Locale Names

## Para escritores de extensión y programas que incrustan Python

Los módulos de extensión nunca deben llamar a "setlocale()", excepto
para averiguar cuál es la configuración regional actual.  Pero dado
que el valor de retorno sólo se puede utilizar portablemente para
restaurarlo, eso no es muy útil (excepto quizás para averiguar si la
localización es o no es "C").

When Python code uses the "locale" module to change the locale, this
also affects the embedding application.  If the embedding application
doesn't want this to happen, it should remove the "_locale" extension
module (which does all the work) from the table of built-in modules in
the "config.c" file, and make sure that the "_locale" module is not
accessible as a shared library.

## Acceso a los catálogos de mensajes

locale.gettext(msg)

locale.dgettext(domain, msg)

locale.dcgettext(domain, msg, category)

locale.textdomain(domain)

locale.bindtextdomain(domain, dir)

locale.bind_textdomain_codeset(domain, codeset)

The locale module exposes the C library's gettext interface on systems
that provide this interface.  It consists of the functions
"gettext()", "dgettext()", "dcgettext()", "textdomain()",
"bindtextdomain()", and "bind_textdomain_codeset()".  These are
similar to the same functions in the "gettext" module, but use the C
library's binary format for message catalogs, and the C library's
search algorithms for locating message catalogs.

Python applications should normally find no need to invoke these
functions, and should use "gettext" instead.  A known exception to
this rule are applications that link with additional C libraries which
internally invoke C functions "gettext" or "dcgettext".  For these
applications, it may be necessary to bind the text domain, so that the
libraries can properly locate their message catalogs.
