---
title: '"tomllib" --- Parse TOML files'
source_url: https://docs.python.org/es/3
source_path: library/tomllib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4270
---

# "tomllib" --- Parse TOML files

Added in version 3.11.

**Código fuente:** Lib/tomllib

======================================================================

This module provides an interface for parsing TOML 1.0.0 (Tom's
Obvious Minimal Language, https://toml.io). This module does not
support writing TOML.

Advertencia:

  Be cautious when parsing data from untrusted sources. A malicious
  TOML string may cause the decoder to consume considerable CPU and
  memory resources. Limiting the size of data to be parsed is
  recommended.

Ver también:

  The Tomli-W package is a TOML writer that can be used in conjunction
  with this module, providing a write API familiar to users of the
  standard library "marshal" and "pickle" modules.

Ver también:

  The TOML Kit package is a style-preserving TOML library with both
  read and write capability. It is a recommended replacement for this
  module for editing already existing TOML files.

Este módulo define las siguientes funciones:

tomllib.load(fp, /, *, parse_float=float)

   Lee un archivo TOML. El primer argumento debe ser un objeto de
   archivo legible y binario. Retorna un "dict". Convierte los tipos
   TOML a Python utilizando esta tabla de conversión.

   *parse_float* se llamará con la cadena de cada TOML flotante que se
   decodificará.  Por defecto, esto es equivalente a "float(num_str)".
   Esto se puede utilizar para usar otro tipo de datos o analizador
   para flotantes TOML (por ejemplo, "decimal.Decimal"). La llamada no
   debe devolver un "dict" o un "list", de lo contrario se lanza un
   "ValueError".

   Un "TOMLDecodeError" se levantará en un documento TOML inválido.

tomllib.loads(s, /, *, parse_float=float)

   Carga TOML de un objeto "str". Retorna un "dict". Convierte los
   tipos TOML a Python utilizando esta tabla de conversión. El
   argumento *parse_float* tiene el mismo significado que en "load()".

   Un "TOMLDecodeError" se levantará en un documento TOML inválido.

Las siguientes excepciones están disponibles:

exception tomllib.TOMLDecodeError(msg, doc, pos)

   Subclass of "ValueError" with the following additional attributes:

   msg

      The unformatted error message.

   doc

      The TOML document being parsed.

   pos

      The index of *doc* where parsing failed.

   lineno

      The line corresponding to *pos*.

   colno

      The column corresponding to *pos*.

   Distinto en la versión 3.14: Added the *msg*, *doc* and *pos*
   parameters. Added the "msg", "doc", "pos", "lineno" and "colno"
   attributes.

   Obsoleto desde la versión 3.14: Passing free-form positional
   arguments is deprecated.

## Ejemplos

Analiza un TOML file:

   import tomllib

   with open("pyproject.toml", "rb") as f:
       data = tomllib.load(f)

Analiza un TOML string:

   import tomllib

   toml_str = """
   python-version = "3.11.0"
   python-implementation = "CPython"
   """

   data = tomllib.loads(toml_str)

## Tabla de conversión

+--------------------+----------------------------------------------------------------------------------------+
| TOML               | Python                                                                                 |
|====================|========================================================================================|
## | TOML document      | dict                                                                                   |

## | cadena             | str                                                                                    |

## | integer            | int                                                                                    |

## | flotante           | flotante (configurable con *parse_float*)                                              |

## | boolean            | bool                                                                                   |

| offset date-time   | datetime.datetime (atributo "tzinfo" establecido en una instancia de                   |
## |                    | "datetime.timezone")                                                                   |

## | local date-time    | datetime.datetime (atributo "tzinfo" establecido en "None")                            |

## | local date         | datetime.date                                                                          |

## | local time         | datetime.time                                                                          |

## | array              | list                                                                                   |

## | tabla              | dict                                                                                   |

## | inline table       | dict                                                                                   |

## | array of tables    | list of dicts                                                                          |
