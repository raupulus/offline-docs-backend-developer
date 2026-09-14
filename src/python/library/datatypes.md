---
title: Tipos de datos
source_url: https://docs.python.org/es/3
source_path: library/datatypes.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2250
---

# Tipos de datos

Los módulos descritos en este capítulo proporcionan una variedad de
tipos de datos especializados, como fechas y horas, matrices de tipo
fijo (*fixed-type arrays*), colas de montículos (*heap queues*), colas
de doble extremo (*double-ended queues*) y enumeraciones.

Python también proporciona algunos tipos de datos integrados,
concretamente "dict", "list", "set" y "frozenset", y "tuple". La clase
"str" se utiliza para contener cadenas de caracteres Unicode, y las
clases "bytes" y "bytearray" se utilizan para contener datos binarios.

En este capítulo se documentan los siguientes módulos:

* "datetime" --- Basic date and time types

  * Aware and naive objects

  * Constantes

  * Available types

    * Common properties

    * Determining if an object is aware or naive

  * "timedelta" objects

    * Examples of usage: "timedelta"

  * "date" objects

    * Examples of usage: "date"

  * "datetime" objects

    * Examples of usage: "datetime"

  * "time" objects

    * Examples of usage: "time"

  * "tzinfo" objects

  * "timezone" objects

  * "strftime()" and "strptime()" behavior

    * "strftime()" and "strptime()" format codes

    * Technical detail

* "zoneinfo" --- IANA time zone support

  * Usando "ZoneInfo"

  * Fuentes de datos

    * Configurando los orígenes de datos

      * Configuración en tiempo de compilación

      * Configuración del entorno

      * Configuración de tiempo de ejecución

  * La clase "ZoneInfo"

    * Representaciones de cadenas

    * Serialización de Pickle

  * Funciones

  * Globales

  * Excepciones y advertencias

* "calendar" --- General calendar-related functions

  * Command-line usage

* "collections" --- Container datatypes

  * Objetos "ChainMap"

    * Ejemplos y recetas "ChainMap"

  * Objetos "Counter"

  * Objetos "deque"

    * Recetas "deque"

  * Objetos "defaultdict"

    * Ejemplos "defaultdict"

  * "namedtuple()" Funciones *Factory* para Tuplas y Campos con
    Nombres

  * Objetos "OrderedDict"

    * Ejemplos y recetas "OrderedDict"

  * Objetos "UserDict"

  * Objetos "UserList"

  * Objetos "UserString"

* "collections.abc" --- Abstract Base Classes for Containers

  * Colecciones clases base abstractas

  * Colecciones Clases base abstractas - Descripciones detalladas

  * Ejemplos y Recetas

* "heapq" --- Heap queue algorithm

  * Ejemplos Básicos

  * Other Applications

  * Notas de Aplicación de la Cola de Prioridades

  * Teoría

* "bisect" --- Array bisection algorithm

  * Notas de rendimiento

  * Búsqueda en listas ordenadas

  * Ejemplos

* "array" --- Efficient arrays of numeric values

* "weakref" --- Weak references

  * Objetos de referencias débiles

  * Ejemplo

  * Objetos finalizadores

  * Comparando finalizadores con los métodos "__del__()"

* "types" --- Dynamic type creation and names for built-in types

  * Creación dinámica de tipos

  * Tipos de Intérpretes Estándar

  * Clases y funciones de utilidad adicionales

  * Funciones de utilidad de corutina

* "copy" --- Shallow and deep copy operations

* "pprint" --- Data pretty printer

  * Functions

  * Objetos *PrettyPrinter*

  * Ejemplo

* "reprlib" --- Alternate "repr()" implementation

  * Objetos Repr

  * Subclasificando Objetos Repr

* "enum" --- Support for enumerations

  * Module contents

  * Data types

    * Nombres soportados "__dunder__"

    * Nombres "_sunder_" compatibles

  * Utilities and decorators

  * Notas

* "graphlib" --- Functionality to operate with graph-like structures

  * Excepciones
