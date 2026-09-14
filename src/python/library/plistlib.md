---
title: '"plistlib" --- Generate and parse Apple ".plist" files'
source_url: https://docs.python.org/es/3
source_path: library/plistlib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3490
---

# "plistlib" --- Generate and parse Apple ".plist" files

**Código fuente:** Lib/plistlib.py

======================================================================

Este módulo proporciona una interfaz para leer y escribir los archivos
de "lista de propiedades" utilizados por Apple, principalmente en
macOS e iOS. Este módulo admite archivos plist binarios y XML.

El formato de lista de propiedades (".plist") es una serialización
simple que soporta tipos de objetos básicos, como diccionarios,
listas, números y cadenas. Generalmente el objeto de nivel superior es
un diccionario.

Para escribir y analizar un archivo plist usa las funciones "dump()" y
"load()".

To work with plist data in bytes or string objects, use "dumps()" and
"loads()".

Los valores pueden ser cadenas, enteros, flotantes, booleanos, tuplas,
listas, diccionarios (pero solo con claves de cadena), "bytes",
"bytearray" u objetos "datetime.datetime".

Distinto en la versión 3.4: Nueva API, API antigua obsoleta. Añadido
soporte para plists en formato binario.

Distinto en la versión 3.8: Añadido soporte para lectura y escritura
de tokens "UID" en plists binarios como lo usan NSKeyedArchiver y
NSKeyedUnarchiver.

Distinto en la versión 3.9: API antigua eliminada.

Ver también:

  PList manual page
     Documentación de Apple del formato de archivo.

Este módulo define las siguientes funciones:

plistlib.load(fp, *, fmt=None, dict_type=dict, aware_datetime=False)

   Lee un archivo plist. *fp* debe ser un objeto de archivo binario y
   legible. Retorna el objeto raíz desempaquetado (el cual
   generalmente es un diccionario).

   El *fmt* es el formato del archivo y los siguientes valores son
   válidos:

   * "None": Autodetecta el formato de archivo

   * "FMT_XML": Formato de archivo XML

   * "FMT_BINARY": Formato binario plist

   EL *dict_type* es el tipo usado por los diccionarios que son leídos
   del archivo plist.

   When *aware_datetime* is true, fields with type "datetime.datetime"
   will be created as aware object, with "tzinfo" as "datetime.UTC".

   Los datos XML para el formato "FMT_XML" son analizados usando el
   analizador Expat desde "xml.parsers.expat" -- consulte su
   documentación para conocer las posibles excepciones en XML mal
   formado. Elementos desconocidos serán simplemente ignorados por el
   analizador plist.

   The parser raises "InvalidFileException" when the file cannot be
   parsed.

   Added in version 3.4.

   Distinto en la versión 3.13: The keyword-only parameter
   *aware_datetime* has been added.

plistlib.loads(data, *, fmt=None, dict_type=dict, aware_datetime=False)

   Load a plist from a bytes or string object. See "load()" for an
   explanation of the keyword arguments.

   Added in version 3.4.

   Distinto en la versión 3.13: *data* can be a string when *fmt*
   equals "FMT_XML".

plistlib.dump(value, fp, *, fmt=FMT_XML, sort_keys=True, skipkeys=False, aware_datetime=False)

   Write *value* to a plist file. *fp* should be a writable, binary
   file object.

   El argumento *fmt* especifica el formato del archivo plist y puede
   ser uno de los siguientes valores:

   * "FMT_XML": Archivo plist con formato XML

   * "FMT_BINARY": Archivo plist con formato binario

   Cuando *sort_keys* es verdadero (el valor por defecto) las claves
   para los diccionarios serán escritas al plist ordenadamente, si no
   serán escritas en el orden de iteración del diccionario.

   Cuando *skipkeys* es falso (el valor por defecto) la función lanza
   "TypeError" cuando una clave del diccionario no es una cadena de
   caracteres, si no tales claves serán omitidas.

   When *aware_datetime* is true and any field with type
   "datetime.datetime" is set as an aware object, it will convert to
   UTC timezone before writing it.

   Una excepción "TypeError" será levantada si el objeto es un tipo no
   admitido o el contenedor que contiene tipos no admitidos.

   Una excepción "OverflowError" será levantada para valores enteros
   que no pueden ser representados en archivos plist (binarios).

   Added in version 3.4.

   Distinto en la versión 3.13: The keyword-only parameter
   *aware_datetime* has been added.

plistlib.dumps(value, *, fmt=FMT_XML, sort_keys=True, skipkeys=False, aware_datetime=False)

   Retorna *value* como un objeto de bytes con formato plist. Consulte
   la documentación de "dump()" para una explicación de los argumentos
   de palabra clave de esta función.

   Added in version 3.4.

Las siguientes clases están disponibles:

class plistlib.UID(data)

   Envuelve un "int". Este es usado leyendo o escribiendo datos
   codificados NSKeyedArchiver, los cuales contienen UID (ver manual
   PList).

   data

      Int value of the UID.  It must be in the range "0 <= data <
      2**64".

   Added in version 3.8.

Las siguientes constantes están disponibles:

plistlib.FMT_XML

   El formato XML para archivos plist.

   Added in version 3.4.

plistlib.FMT_BINARY

   El formato binario para archivos plist

   Added in version 3.4.

The module defines the following exceptions:

exception plistlib.InvalidFileException

   Raised when a file cannot be parsed.

   Added in version 3.4.

## Ejemplos

Generar un plist:

   import datetime as dt
   import plistlib

   pl = dict(
       aString = "Doodah",
       aList = ["A", "B", 12, 32.1, [1, 2, 3]],
       aFloat = 0.1,
       anInt = 728,
       aDict = dict(
           anotherString = "<hello & hi there!>",
           aThirdString = "M\xe4ssig, Ma\xdf",
           aTrueValue = True,
           aFalseValue = False,
       ),
       someData = b"<binary gunk>",
       someMoreData = b"<lots of binary gunk>" * 10,
       aDate = dt.datetime.now()
   )
   print(plistlib.dumps(pl).decode())

Analizar un plist:

   import plistlib

   plist = b"""<plist version="1.0">
   <dict>
       <key>foo</key>
       <string>bar</string>
   </dict>
   </plist>"""
   pl = plistlib.loads(plist)
   print(pl["foo"])
