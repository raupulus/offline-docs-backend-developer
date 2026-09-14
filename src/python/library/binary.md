---
title: Servicios de datos binarios
source_url: https://docs.python.org/es/3
source_path: library/binary.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1840
---

# Servicios de datos binarios

Los módulos descritos en este capítulo proporcionan algunas
operaciones básicas de servicios para la manipulación de datos
binarios. Otras operaciones sobre datos binarios específicamente
relacionadas con formatos de archivo y protocolos de red están
descritas en las secciones relevantes.

Algunas bibliotecas descritas bajo Servicios de procesamiento de texto
también funcionan o bien sobre formatos binarios compatibles con ASCII
(por ejemplo "re"), o bien sobre todos los datos binarios (por ejemplo
"difflib").

Adicionalmente, véase la documentación para los tipos de datos
binarios incorporados en Python en Tipos de secuencias binarias ---
bytes, bytearray y memoryview.

* "struct" --- Interpret bytes as packed binary data

  * Funciones y excepciones

  * Cadenas de formato

    * Orden de bytes, tamaño y alineación

    * Caracteres de formato

    * Ejemplos

  * Aplicaciones

    * Formatos nativos

    * Formatos estándar

  * Clases

* "codecs" --- Codec registry and base classes

  * Clases Base de Códec

    * Manejadores de errores

    * Codificación y decodificación sin estado

    * Codificación y decodificación incrementales

      * Objetos IncrementalEncoder

      * Objetos IncrementalDecoder

    * Codificación y decodificación de flujos

      * Objetos StreamWriter

      * Objetos StreamReader

      * Objetos StreamReaderWriter

      * Objetos StreamRecoder

  * Codificaciones y Unicode

  * Codificaciones estándar

  * Codificaciones específicas de Python

    * Codificaciones de texto

    * Transformaciones Binarias

    * Standalone Codec Functions

    * Transformaciones de texto

  * "encodings" --- Encodings package

  * "encodings.idna" --- Internationalized Domain Names in
    Applications

  * "encodings.mbcs" --- Windows ANSI codepage

  * "encodings.utf_8_sig" --- UTF-8 codec with BOM signature
