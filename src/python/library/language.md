---
title: Servicios del lenguaje Python
source_url: https://docs.python.org/es/3
source_path: library/language.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3090
---

# Servicios del lenguaje Python

Python proporciona una serie de módulos para ayudar a trabajar con el
lenguaje Python. Estos módulos admiten tokenización, análisis,
análisis sintáctico, desensamblado de código de bytes, entre otras
funciones.

Estos módulos incluyen:

* "ast" --- Abstract syntax trees

  * Abstract grammar

  * Clases nodo

    * Nodos raíz

    * Literales

    * Variables

    * Expresiones

      * Subindexado

      * Comprensiones

    * Declaraciones

      * Importaciones

    * Control de flujo

    * La coincidencia de patrones

    * Type annotations

    * Tipos de parámetro

    * Definiciones de función y clase

    * Async y await

  * "ast" helpers

  * Compiler flags

  * Command-line usage

* "symtable" --- Access to the compiler's symbol tables

  * Generando tablas de símbolos

  * Examinando la tabla de símbolos

  * Command-Line Usage

* "token" --- Constants used with Python parse trees

* "keyword" --- Testing for Python keywords

* "tokenize" --- Tokenizer for Python source

  * Convirtiendo la entrada en *tokens*

  * Uso como línea de comandos

  * Ejemplos

* "tabnanny" --- Detection of ambiguous indentation

* "pyclbr" --- Python module browser support

  * Objetos Function

  * Objetos Class

* "py_compile" --- Compile Python source files

  * Interfaz de línea de comandos

* "compileall" --- Byte-compile Python libraries

  * Uso de la línea de comandos

  * Funciones públicas

* "dis" --- Desensamblador para bytecode de Python

  * Interfaz de línea de comandos

  * Análisis de bytecode

  * Funciones de análisis

  * Instrucciones bytecode de Python

  * Colecciones opcode

* "pickletools" --- Tools for pickle developers

  * Command-line usage

    * Command-line options

  * Programmatic interface
