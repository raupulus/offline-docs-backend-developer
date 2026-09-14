---
title: '"json" --- JSON encoder and decoder'
source_url: https://docs.python.org/es/3
source_path: library/json.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3070
---

# "json" --- JSON encoder and decoder

**Código fuente:** Lib/json/__init__.py

======================================================================

JSON (JavaScript Object Notation), specified by **RFC 7159** (which
obsoletes **RFC 4627**) and by ECMA-404, is a lightweight data
interchange format inspired by JavaScript object literal syntax
(although it is not a strict subset of JavaScript [1] ).

Nota:

  The term "object" in the context of JSON processing in Python can be
  ambiguous. All values in Python are objects. In JSON, an object
  refers to any data wrapped in curly braces, similar to a Python
  dictionary.

Advertencia:

  Se debe tener cuidado al analizar datos JSON de fuentes que no son
  de confianza. Una cadena JSON maliciosa puede hacer que el
  decodificador consuma considerables recursos del CPU y la memoria.
  Se recomienda limitar el tamaño de los datos que se van a analizar.

This module exposes an API familiar to users of the standard library
"marshal" and "pickle" modules.

Codificación de jerarquías básicas de objetos de Python:

   >>> import json
   >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
   '["foo", {"bar": ["baz", null, 1.0, 2]}]'
   >>> print(json.dumps("\"foo\bar"))
   "\"foo\bar"
   >>> print(json.dumps('\u1234'))
   "\u1234"
   >>> print(json.dumps('\\'))
   "\\"
   >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
   {"a": 0, "b": 0, "c": 0}
   >>> from io import StringIO
   >>> io = StringIO()
   >>> json.dump(['streaming API'], io)
   >>> io.getvalue()
   '["streaming API"]'

Codificación compacta:

   >>> import json
   >>> json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
   '[1,2,3,{"4":5,"6":7}]'

Impresión linda:

   >>> import json
   >>> print(json.dumps({'6': 7, '4': 5}, sort_keys=True, indent=4))
   {
       "4": 5,
       "6": 7
   }

Customizing JSON object encoding:

   >>> import json
   >>> def custom_json(obj):
   ...     if isinstance(obj, complex):
   ...         return {'__complex__': True, 'real': obj.real, 'imag': obj.imag}
   ...     raise TypeError(f'Cannot serialize object of {type(obj)}')
   ...
   >>> json.dumps(1 + 2j, default=custom_json)
   '{"__complex__": true, "real": 1.0, "imag": 2.0}'

Decodificación JSON:

   >>> import json
   >>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
   ['foo', {'bar': ['baz', None, 1.0, 2]}]
   >>> json.loads('"\\"foo\\bar"')
   '"foo\x08ar'
   >>> from io import StringIO
   >>> io = StringIO('["streaming API"]')
   >>> json.load(io)
   ['streaming API']

Customizing JSON object decoding:

   >>> import json
   >>> def as_complex(dct):
   ...     if '__complex__' in dct:
   ...         return complex(dct['real'], dct['imag'])
   ...     return dct
   ...
   >>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
   ...     object_hook=as_complex)
   (1+2j)
   >>> import decimal
   >>> json.loads('1.1', parse_float=decimal.Decimal)
   Decimal('1.1')

Extendiendo "JSONEncoder":

   >>> import json
   >>> class ComplexEncoder(json.JSONEncoder):
   ...     def default(self, obj):
   ...         if isinstance(obj, complex):
   ...             return [obj.real, obj.imag]
   ...         # Let the base class default method raise the TypeError
   ...         return super().default(obj)
   ...
   >>> json.dumps(2 + 1j, cls=ComplexEncoder)
   '[2.0, 1.0]'
   >>> ComplexEncoder().encode(2 + 1j)
   '[2.0, 1.0]'
   >>> list(ComplexEncoder().iterencode(2 + 1j))
   ['[2.0', ', 1.0', ']']

Using "json" from the shell to validate and pretty-print:

   $ echo '{"json":"obj"}' | python -m json
   {
       "json": "obj"
   }
   $ echo '{1.2:3.4}' | python -m json
   Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

Consulte Command-line interface para obtener documentación detallada.

Nota:

  JSON es un subconjunto de YAML 1.2. El JSON producido por la
  configuración predeterminada de este módulo (en particular, el valor
  predeterminado *separators*) también es un subconjunto de YAML 1.0 y
  1.1. Por lo tanto, este módulo también se puede utilizar como un
  serializador YAML.

Nota:

  Los codificadores y decodificadores de este módulo conservan el
  orden de entrada y salida de forma predeterminada. El orden solo se
  pierde si los contenedores subyacentes no están ordenados.

## Uso básico

json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

   Serialize *obj* as a JSON formatted stream to *fp* (a
   ".write()"-supporting *file-like object*) using this Python-to-JSON
   conversion table.

   Nota:

     A diferencia de "pickle" y "marshal", JSON no es un protocolo
     enmarcado, por lo que intentar serializar varios objetos con
     llamadas repetidas a "dump()" utilizando el mismo *fp* dará como
     resultado un archivo JSON no válido.

   Parámetros:
      * **obj** (*object*) -- The Python object to be serialized.

      * **fp** (*file-like object*) -- The file-like object *obj* will
        be serialized to. The "json" module always produces "str"
        objects, not "bytes" objects, therefore "fp.write()" must
        support "str" input.

      * **skipkeys** (*bool*) -- If "True", keys that are not of a
        basic type ("str", "int", "float", "bool", "None") will be
        skipped instead of raising a "TypeError". Default "False".

      * **ensure_ascii** (*bool*) -- If "True" (the default), the
        output is guaranteed to have all incoming non-ASCII and non-
        printable characters escaped. If "False", all characters will
        be outputted as-is, except for the characters that must be
        escaped: quotation mark, reverse solidus, and the control
        characters U+0000 through U+001F.

      * **check_circular** (*bool*) -- If "False", the circular
        reference check for container types is skipped and a circular
        reference will result in a "RecursionError" (or worse).
        Default "True".

      * **allow_nan** (*bool*) -- If "False", serialization of out-of-
        range "float" values ("nan", "inf", "-inf") will result in a
        "ValueError", in strict compliance with the JSON
        specification. If "True" (the default), their JavaScript
        equivalents ("NaN", "Infinity", "-Infinity") are used.

      * **cls** (a "JSONEncoder" subclass) -- If set, a custom JSON
        encoder with the "default()" method overridden, for
        serializing into custom datatypes. If "None" (the default),
        "JSONEncoder" is used.

      * **indent** (*int** | **str** | **None*) -- If a positive
        integer or string, JSON array elements and object members will
        be pretty-printed with that indent level. A positive integer
        indents that many spaces per level; a string (such as ""\t"")
        is used to indent each level. If zero, negative, or """" (the
        empty string), only newlines are inserted. If "None" (the
        default), no newlines are inserted.

      * **separators** (*tuple** | **None*) -- A two-tuple:
        "(item_separator, key_separator)". If "None" (the default),
        *separators* defaults to "(', ', ': ')" if *indent* is "None",
        and "(',', ': ')" otherwise. For the most compact JSON,
        specify "(',', ':')" to eliminate whitespace.

      * **default** (*callable* | None) -- A function that is called
        for objects that can't otherwise be serialized. It should
        return a JSON encodable version of the object or raise a
        "TypeError". If "None" (the default), "TypeError" is raised.

      * **sort_keys** (*bool*) -- If "True", dictionaries will be
        outputted sorted by key. Default "False".

   Distinto en la versión 3.2: Permite cadenas  de caracteres para
   *indent* además de enteros.

   Distinto en la versión 3.4: Usa "(',', ': ')" como predeterminado
   si *indent* no es "None".

   Distinto en la versión 3.6: Todos los parámetros opcionales son
   ahora palabra-clave-solamente.

json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

   Serializa *obj* en un "str" con formato JSON usando esta conversion
   table.  Los argumentos tienen el mismo significado que en "dump()".

   Nota:

     Las llaves de los pares llave/valor de JSON siempre son del tipo
     "str". Cuando un diccionario se convierte en JSON, todas las
     llaves del diccionario se convierten en cadenas. Como resultado
     de esto, si un diccionario se convierte en JSON y, a
     continuación, se convierte nuevamente en un diccionario, el
     diccionario puede que no sea igual al original. Es decir,
     "loads(dumps(x)) != x" si x tiene llaves que no son de tipo
     cadena de caracteres.

json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

   Deserialize *fp* to a Python object using the JSON-to-Python
   conversion table.

   Parámetros:
      * **fp** (*file-like object*) -- A ".read()"-supporting *text
        file* or *binary file* containing the JSON document to be
        deserialized.

      * **cls** (a "JSONDecoder" subclass) -- If set, a custom JSON
        decoder. Additional keyword arguments to "load()" will be
        passed to the constructor of *cls*. If "None" (the default),
        "JSONDecoder" is used.

      * **object_hook** (*callable* | None) -- If set, a function that
        is called with the result of any JSON object literal decoded
        (a "dict"). The return value of this function will be used
        instead of the "dict". This feature can be used to implement
        custom decoders, for example JSON-RPC class hinting. Default
        "None".

      * **object_pairs_hook** (*callable* | None) -- If set, a
        function that is called with the result of any JSON object
        literal decoded with an ordered list of pairs. The return
        value of this function will be used instead of the "dict".
        This feature can be used to implement custom decoders. If
        *object_hook* is also set, *object_pairs_hook* takes priority.
        Default "None".

      * **parse_float** (*callable* | None) -- If set, a function that
        is called with the string of every JSON float to be decoded.
        If "None" (the default), it is equivalent to "float(num_str)".
        This can be used to parse JSON floats into custom datatypes,
        for example "decimal.Decimal".

      * **parse_int** (*callable* | None) -- If set, a function that
        is called with the string of every JSON int to be decoded. If
        "None" (the default), it is equivalent to "int(num_str)". This
        can be used to parse JSON integers into custom datatypes, for
        example "float".

      * **parse_constant** (*callable* | None) -- If set, a function
        that is called with one of the following strings:
        "'-Infinity'", "'Infinity'", or "'NaN'". This can be used to
        raise an exception if invalid JSON numbers are encountered.
        Default "None".

   Muestra:
      * **JSONDecodeError** -- When the data being deserialized is not
        a valid JSON document.

      * **UnicodeDecodeError** -- When the data being deserialized
        does not contain UTF-8, UTF-16 or UTF-32 encoded data.

   Distinto en la versión 3.1:

   * Added the optional *object_pairs_hook* parameter.

   * *parse_constant* ya no es llamado en 'null', 'true', 'false'.

   Distinto en la versión 3.6:

   * Todos los parámetros opcionales son ahora palabra-clave-
     solamente.

   * *fp* ahora puede ser un *binary file*. La codificación de entrada
     debe ser UTF-8, UTF-16 o UTF-32.

   Distinto en la versión 3.11: El *parse_int* predeterminado de
   "int()" ahora limita la longitud máxima de la cadena de enteros a
   través de la integer string conversion length limitation del
   intérprete para ayudar a evitar ataques de denegación de servicio.

json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

   Identical to "load()", but instead of a file-like object,
   deserialize *s* (a "str", "bytes" or "bytearray" instance
   containing a JSON document) to a Python object using this
   conversion table.

   Distinto en la versión 3.6: *s* ahora puede ser de tipo "bytes" o
   "bytearray". La codificación de entrada debe ser UTF-8, UTF-16 o
   UTF-32.

   Distinto en la versión 3.9: El argumento de palabra llave
   *encoding* ha sido removido.

## Codificadores y Decodificadores

class json.JSONDecoder(*, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None)

   Decodificador JSON simple.

   Realiza las siguientes traducciones en la decodificación de forma
   predeterminada:

   +-----------------+---------------------+
   | JSON            | Python              |
   |=================|=====================|
   | object          | dict                |
   +-----------------+---------------------+
   | array           | list                |
   +-----------------+---------------------+
   | string          | str                 |
   +-----------------+---------------------+
   | número (int)    | int                 |
   +-----------------+---------------------+
   | número (real)   | float               |
   +-----------------+---------------------+
   | true            | True                |
   +-----------------+---------------------+
   | false           | False               |
   +-----------------+---------------------+
   | null            | None                |
   +-----------------+---------------------+

   También entiende "NaN", "Infinity" y "-Infinity" como sus
   correspondientes valores "float", que está fuera de la
   especificación JSON.

   *object_hook* is an optional function that will be called with the
   result of every JSON object decoded and its return value will be
   used in place of the given "dict".  This can be used to provide
   custom deserializations (e.g. to support JSON-RPC class hinting).

   *object_pairs_hook* is an optional function that will be called
   with the result of every JSON object decoded with an ordered list
   of pairs.  The return value of *object_pairs_hook* will be used
   instead of the "dict".  This feature can be used to implement
   custom decoders.  If *object_hook* is also defined, the
   *object_pairs_hook* takes priority.

   Distinto en la versión 3.1: Soporte agregado para
   *object_pairs_hook*.

   *parse_float* is an optional function that will be called with the
   string of every JSON float to be decoded.  By default, this is
   equivalent to "float(num_str)".  This can be used to use another
   datatype or parser for JSON floats (e.g. "decimal.Decimal").

   *parse_int* is an optional function that will be called with the
   string of every JSON int to be decoded.  By default, this is
   equivalent to "int(num_str)".  This can be used to use another
   datatype or parser for JSON integers (e.g. "float").

   *parse_constant* is an optional function that will be called with
   one of the following strings: "'-Infinity'", "'Infinity'", "'NaN'".
   This can be used to raise an exception if invalid JSON numbers are
   encountered.

   Si *strict* es falso (''True'' es el valor predeterminado), se
   permitirán caracteres de control dentro de cadenas.  Los caracteres
   de control en este contexto son aquellos con códigos de caracteres
   en el rango 0--31, incluyendo "'\t'" (tab), "'\n'", "'\r'" and
   "'\0'".

   Si los datos que se deserializan no constituyen un documento JSON
   válido, se lanzará un "JSONDecodeError".

   Distinto en la versión 3.6: Todos los parámetros son ahora palabra-
   clave-solamente.

   decode(s)

      Retorna la representación Python de *s* (una instancia "str" que
      contiene un documento JSON).

      "JSONDecodeError" se producirá si el documento JSON entregado es
      invalido.

   raw_decode(s)

      Decodifica un documento JSON de *s* (un "str" comenzando con un
      documento JSON) y retorna una tupla de 2 de la representación
      Python y el índice en *s* donde terminó el documento.

      Esto se puede usar para decodificar un documento JSON de una
      cadena de caracteres que puede tener datos extraños al final.

class json.JSONEncoder(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)

   Codificador JSON extensible para estructuras de datos de Python.

   Admite los siguientes objetos y tipos de forma predeterminada:

   +------------------------------------------+-----------------+
   | Python                                   | JSON            |
   |==========================================|=================|
   | dict                                     | object          |
   +------------------------------------------+-----------------+
   | list, tuple                              | array           |
   +------------------------------------------+-----------------+
   | str                                      | string          |
   +------------------------------------------+-----------------+
   | int, float, Enums derivadas de int o     | number          |
   | float                                    |                 |
   +------------------------------------------+-----------------+
   | True                                     | true            |
   +------------------------------------------+-----------------+
   | False                                    | false           |
   +------------------------------------------+-----------------+
   | None                                     | null            |
   +------------------------------------------+-----------------+

   Distinto en la versión 3.4: Compatibilidad añadida con las clases
   Enum derivadas de int y float.

   A fin de extender esto para reconocer otros objetos, implementar
   una subclase con un método "default()" con otro método que retorna
   un objeto serializable para ''o'' si es posible, de lo contrario
   debe llamar a la implementación de superclase (para lanzar
   "TypeError").

   If *skipkeys* is false (the default), a "TypeError" will be raised
   when trying to encode keys that are not "str", "int", "float",
   "bool" or "None".  If *skipkeys* is true, such items are simply
   skipped.

   If *ensure_ascii* is true (the default), the output is guaranteed
   to have all incoming non-ASCII and non-printable characters
   escaped. If *ensure_ascii* is false, all characters will be output
   as-is, except for the characters that must be escaped: quotation
   mark, reverse solidus, and the control characters U+0000 through
   U+001F.

   Si *check_circular* es cierto (valor predeterminado), se
   comprobarán las listas, los diccionarios y los objetos codificados
   personalizados en busca de referencias circulares durante la
   codificación para evitar una recursividad infinita (lo que
   provocaría un "RecursionError"). De lo contrario, no se realiza
   ninguna comprobación de este tipo.

   Si *allow_nan* es cierto (valor predeterminado), "NaN", "Infinity"
   y "-Infinity" se codificarán como tales.  Este comportamiento no es
   compatible con las especificaciones JSON, pero es coherente con la
   mayoría de los codificadores y decodificadores basados en
   JavaScript.  De lo contrario, codificar dichos puntos flotantes
   provocará un "ValueError".

   Si *sort_keys* es cierto (predeterminado: "False"), la salida de
   los diccionarios se ordenará por clave; esto es útil para las
   pruebas de regresión para garantizar que las serializaciones JSON
   se pueden comparar en el día a día.

   Si *indent* es un entero no negativo o una cadena, los elementos
   del arreglo JSON y los miembros del objeto se imprimirán con ese
   nivel de sangría. Un nivel de sangría de 0, negativo o """" solo
   insertará nuevas líneas. "None" (el valor predeterminado)
   selecciona la representación más compacta. El uso de una sangría de
   entero positivo agrega sangrías de muchos espacios por nivel. Si
   *indent* es una cadena (como ""\t""), esa cadena se usa para
   agregarle sangría a cada nivel.

   Distinto en la versión 3.2: Permite cadenas  de caracteres para
   *indent* además de enteros.

   Si se especifica, *separators* debe ser una tupla
   "(separador_elemento, separador_llave)". El valor predeterminado es
   "(', ', ': ')" si *indent* es "None" y "(', ', ': ')" de lo
   contrario. Para obtener la representación JSON más compacta, debe
   especificar "(', ', ': ')" para eliminar espacios en blanco.

   Distinto en la versión 3.4: Usa "(',', ': ')" como predeterminado
   si *indent* no es "None".

   Si se especifica, *default* debería ser una función que se llama
   para objetos que de otro modo no se pueden serializar. Debería
   retornar una versión codificable JSON del objeto o generar un
   "TypeError". Si no se especifica, produce "TypeError".

   Distinto en la versión 3.6: Todos los parámetros son ahora palabra-
   clave-solamente.

   default(o)

      Implemente este método en una subclase de modo que retorne un
      objeto serializable para *o*, o llame a la implementación base
      (para generar un "TypeError").

      Por ejemplo, para admitir iteradores arbitrarios, podría
      implementar "default()" de esta manera:

         def default(self, o):
            try:
                iterable = iter(o)
            except TypeError:
                pass
            else:
                return list(iterable)
            # Let the base class default method raise the TypeError
            return super().default(o)

   encode(o)

      Retorna una representación de cadena de caracteres JSON de una
      estructura de datos de Python, *o*.  Por ejemplo:

         >>> json.JSONEncoder().encode({"foo": ["bar", "baz"]})
         '{"foo": ["bar", "baz"]}'

   iterencode(o)

      Codifica el objeto dado, *o*, y produce cada representación de
      cadena como disponible.  Por ejemplo:

         for chunk in json.JSONEncoder().iterencode(bigobject):
             mysocket.write(chunk)

## Excepciones

exception json.JSONDecodeError(msg, doc, pos)

   Subclase de "ValueError" con los siguientes atributos adicionales:

   msg

      El mensaje de error sin formato.

   doc

      El documento JSON que se está analizando.

   pos

      El índice de inicio de *doc* donde se produjo un error en el
      análisis.

   lineno

      La línea correspondiente a *pos*.

   colno

      La columna correspondiente a *pos*.

   Added in version 3.5.

## Cumplimiento e interoperabilidad estándar

The JSON format is specified by **RFC 7159** and by ECMA-404. This
section details this module's level of compliance with the RFC. For
simplicity, "JSONEncoder" and "JSONDecoder" subclasses, and parameters
other than those explicitly mentioned, are not considered.

Este módulo no cumple con la RFC de forma estricta, implementando
algunas extensiones que son válidas  en JavaScript pero no son válidas
en JSON.  En particular:

* Se aceptan y se envían valores de números Infinitos y NaN;

* Se aceptan nombres repetidos dentro de un objeto y solo se utiliza
  el valor del último par nombre-valor.

Puesto que el RFC permite a los analizadores compatibles con RFC
aceptar textos de entrada que no son compatibles con RFC, el
deserializador de este módulo es técnicamente compatible con RFC bajo
la configuración predeterminada.

### Codificaciones de caracteres

La RFC requiere que JSON se represente mediante UTF-8, UTF-16 o
UTF-32, siendo UTF-8 el valor predeterminado recomendado para la
máxima interoperabilidad.

As permitted, though not required, by the RFC, this module's
serializer sets *ensure_ascii=True* by default, thus escaping the
output so that the resulting strings only contain printable ASCII
characters.

Aparte del parámetro *ensure_ascii*, este módulo se define
estrictamente en términos de conversión entre objetos Python y
"Unicode strings", y por lo tanto no aborda directamente el problema
de las codificaciones de caracteres.

La RFC prohíbe agregar una marca de orden byte (BOM, por sus siglas en
inglés) al inicio de un texto JSON y el serializador de este módulo no
agrega una BOM a su salida. La RFC permite, pero no requiere,
deserializadores JSON para omitir una BOM inicial en su entrada.  El
deserializador de este módulo genera un "ValueError" cuando hay una
lista de materiales inicial.

La RFC no prohíbe explícitamente las cadenas JSON que contienen
secuencias de bytes que no corresponden a caracteres Unicode válidos
(por ejemplo, sustitutos UTF-16 no espaciados), pero sí tiene en
cuenta que pueden causar problemas de interoperabilidad. De forma
predeterminada, este módulo acepta y genera puntos de código (cuando
está presente en el original "str") para dichas secuencias.

### Valores de número infinito y NaN

El RFC no permite la representación de los valores de número infinito
o NaN. A pesar de eso, de forma predeterminada, este módulo acepta y
genera "Infinity", "-Infinity" y "NaN" como si fueran valores
literales de número JSON válidos:

   >>> # Neither of these calls raises an exception, but the results are not valid JSON
   >>> json.dumps(float('-inf'))
   '-Infinity'
   >>> json.dumps(float('nan'))
   'NaN'
   >>> # Same when deserializing
   >>> json.loads('-Infinity')
   -inf
   >>> json.loads('NaN')
   nan

En el serializador, el parámetro *allow_nan* se puede utilizar para
modificar este comportamiento.  En el deserializador, se puede
utilizar el parámetro *parse_constant* para modificar este
comportamiento.

### Nombres repetidos dentro de un objeto

La RFC especifica que los nombres dentro de un objeto JSON deben ser
únicos, pero no exige cómo se deben controlar los nombres repetidos en
los objetos JSON.  De forma predeterminada, este módulo no genera una
excepción; en su lugar, ignora todo excepto el último par nombre-valor
para un nombre dado:

   >>> weird_json = '{"x": 1, "x": 2, "x": 3}'
   >>> json.loads(weird_json)
   {'x': 3}

El parámetro *object_pairs_hook* se puede utilizar para alterar este
comportamiento.

### Valores de nivel superior No-Objeto , No-Arreglo

La versión anterior de JSON especificada por el obsoleto **RFC 4627**
requería que el valor de nivel superior de un texto JSON fuera un
objeto JSON o un arreglo (Python "dict" o "list"), y no podía ser un
valor JSON nulo, booleano, numérico o de cadena.  **RFC 7159** eliminó
esa restricción, y este módulo no ha implementado ni ha implementado
nunca esa restricción en su serializador o en su deserializador.

Independientemente, para lograr la máxima interoperabilidad, es
posible que usted desee adherirse voluntariamente a la restricción.

### Limitaciones de la implementación

Algunas implementaciones del deserializador JSON pueden establecer
límites en:

* el tamaño de los textos JSON aceptados

* el nivel máximo de anidamiento de objetos y arreglos JSON

* el rango y precisión de los números JSON

* el contenido y la longitud máxima de las cadenas de caracteres JSON

Este módulo no impone tales límites más allá de los propios tipos de
datos de Python relevantes o del propio intérprete de Python.

Al serializar en JSON, tenga en cuenta las limitaciones en las
aplicaciones que pueden consumir su JSON.  En particular, es común que
los números JSON se deserialicen en números de doble precisión IEEE
754 y, por lo tanto, estén sujetos al rango y las limitaciones de
precisión de esa representación.  Esto es especialmente relevante
cuando se serializan valores de Python "int" de magnitud
extremadamente grande, o cuando se serializan instancias de tipos
numéricos "exóticos" como "decimal. Decimal".

## Command-line interface

**Código fuente:** Lib/json/tool.py

======================================================================

The "json" module can be invoked as a script via "python -m json" to
validate and pretty-print JSON objects. The "json.tool" submodule
implements this interface.

Si no se especifican los argumentos opcionales "infile" y "outfile",
se utilizarán "sys.stdin" y "sys.stdout" respectivamente:

   $ echo '{"json": "obj"}' | python -m json
   {
       "json": "obj"
   }
   $ echo '{1.2:3.4}' | python -m json
   Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

Distinto en la versión 3.5: La salida está ahora en el mismo orden que
la entrada. Utilice la opción "--sort-keys" para ordenar la salida de
los diccionarios alfabéticamente por llave.

Distinto en la versión 3.14: The "json" module may now be directly
executed as "python -m json". For backwards compatibility, invoking
the CLI as "python -m json.tool" remains supported.

### Command-line options

infile

   El archivo JSON que se va a validar o imprimir con impresión linda:

      $ python -m json mp_films.json
      [
          {
              "title": "And Now for Something Completely Different",
              "year": 1971
          },
          {
              "title": "Monty Python and the Holy Grail",
              "year": 1975
          }
      ]

   Si no se especifica *infile*, lee "sys.stdin".

outfile

   Escribe la salida de *infile* en el *outfile* dado. De lo
   contrario, lo escribe en "sys.stdout".

--sort-keys

   Ordena la salida de los diccionarios alfabéticamente por llave.

   Added in version 3.5.

--no-ensure-ascii

   Deshabilita el escape de caracteres que no sean ascii, véase
   "json.dumps()" para más información.

   Added in version 3.9.

--json-lines

   Analiza cada línea de entrada como objeto JSON independiente.

   Added in version 3.8.

--indent, --tab, --no-indent, --compact

   Opciones mutuamente exclusivas para control de espacios en blanco.

   Added in version 3.9.

-h, --help

   Muestra el mensaje de ayuda.

-[ Notas de pie de página ]-

[1] Como se indica en la errata para RFC 7159, JSON permite caracteres
    literales U+2028 (SEPARADOR DE LINEA) y U+2029 (SEPARADOR DE
    PÁRRAFO) en cadenas, mientras que JavaScript (a partir de
    ECMAScript Edición 5.1) no lo hace.
