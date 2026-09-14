---
title: Persistencia de datos
source_url: https://docs.python.org/es/3
source_path: library/persistence.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3430
---

# Persistencia de datos

Los módulos descritos en este capítulo soportan el almacenamiento de
datos de Python de forma persistente en el disco. Los módulos "pickle"
y "marshal" pueden convertir muchos tipos de datos de Python en un
flujo de bytes y luego recrear los objetos a partir de los bytes. Los
diversos módulos relacionados con DBM admiten una familia de formatos
de archivo basados en hash que almacenan un mapeo de cadenas a otras
cadenas.

La lista de módulos descritos en este capítulo es:

* "pickle" --- Python object serialization

  * Relación con otros módulos de Python

    * Comparación con "marshal"

    * Comparación con "json"

  * Formato de flujo de datos

  * Interfaz del módulo

  * ¿Qué se puede serializar (pickled) y deserializar (unpickled) con
    *pickle*?

  * *Pickling* de Instancias de clases

    * Persistencia de objetos externos

    * Tablas de despacho

    * Manejo de objetos con estado

  * Reducción personalizada para tipos, funciones y otros objetos

  * Búferes fuera de banda

    * API de proveedor

    * API de consumidor

    * Ejemplo

  * Restricción de globals

  * Performance

  * Ejemplos

  * Command-line interface

* "copyreg" --- Register "pickle" support functions

  * Ejemplo

* "shelve" --- Python object persistence

  * Restricciones

  * Ejemplo

* "marshal" --- Internal Python object serialization

* "dbm" --- Interfaces to Unix "databases"

  * "dbm.sqlite3" --- SQLite backend for dbm

  * "dbm.gnu" --- GNU database manager

  * "dbm.ndbm" --- New Database Manager

  * "dbm.dumb" --- Portable DBM implementation

* "sqlite3" --- DB-API 2.0 interfaz para bases de datos SQLite

  * Tutorial

  * Referencia

    * Funciones del módulo

    * Constantes del módulo

    * Objetos de conexión

    * Objetos cursor

    * Objetos fila (*Row*)

    * Objetos fila (*Row*)

    * Objetos PrepareProtocol

    * Excepciones

    * SQLite y tipos de Python

    * Adaptadores y convertidores predeterminados (en desuso)

    * Interfaz de línea de comandos

  * Guías prácticas

    * Cómo usar marcadores de posición para vincular valores en
      consultas SQL

    * Cómo adaptar tipos de Python personalizados a valores de SQLite

      * Cómo escribir objetos adaptables

      * Como registrar un adaptador invocable

    * Como convertir valores SQLite a tipos de Python personalizados

    * Ejemplos para adaptadores y convertidores

    * Cómo utilizar los métodos de acceso directo de conexión

    * Como usar la conexión con un administrador de contexto

    * Como trabajar con URIs SQLite

    * Cómo crear y utilizar fábricas de filas

    * Cómo manejar codificaciones de texto que no sean UTF-8

  * Explicación

    * Control transaccional

      * Control de transacciones mediante el atributo "autocommit"

      * Control de transacciones mediante el atributo
        "isolation_level"
