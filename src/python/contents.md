---
title: Contenido de la documentación de Python
source_url: https://docs.python.org/es/3
source_path: contents.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
order: 800
---

# Contenido de la documentación de Python

* Qué hay de nuevo en Python

  * What's new in Python 3.14

    * Summary -- Release highlights

    * New features

      * **PEP 649** & **PEP 749**: Deferred evaluation of annotations

      * **PEP 734**: Multiple interpreters in the standard library

      * **PEP 750**: Template string literals

      * **PEP 768**: Safe external debugger interface

      * A new type of interpreter

      * Free-threaded mode improvements

      * Improved error messages

      * **PEP 784**: Zstandard support in the standard library

      * Asyncio introspection capabilities

      * Concurrent safe warnings control

    * Other language changes

      * Built-ins

      * Command line and environment

      * PEP 758: Allow "except" and "except*" expressions without
        brackets

      * PEP 765: Control flow in "finally" blocks

      * Garbage collection

      * Default interactive shell

    * New modules

    * Improved modules

      * argparse

      * ast

      * asyncio

      * calendar

      * concurrent.futures

      * configparser

      * contextvars

      * ctypes

      * curses

      * datetime

      * decimal

      * difflib

      * dis

      * errno

      * faulthandler

      * fnmatch

      * fractions

      * functools

      * getopt

      * getpass

      * graphlib

      * heapq

      * hmac

      * http

      * imaplib

      * inspect

      * io

      * json

      * linecache

      * logging.handlers

      * math

      * mimetypes

      * multiprocessing

      * operator

      * os

      * os.path

      * pathlib

      * pdb

      * pickle

      * platform

      * pydoc

      * re

      * socket

      * ssl

      * struct

      * symtable

      * sys

      * sys.monitoring

      * sysconfig

      * tarfile

      * threading

      * tkinter

      * turtle

      * types

      * typing

      * unicodedata

      * unittest

      * urllib

      * uuid

      * webbrowser

      * zipfile

    * Optimizations

      * asyncio

      * base64

      * bdb

      * difflib

      * gc

      * io

      * pathlib

      * pdb

      * textwrap

      * uuid

      * zlib

    * Removed

      * argparse

      * ast

      * asyncio

      * email

      * importlib.abc

      * itertools

      * pathlib

      * pkgutil

      * pty

      * sqlite3

      * urllib

    * Deprecated

      * New deprecations

      * Pending removal in Python 3.15

      * Pending removal in Python 3.16

      * Pending removal in Python 3.17

      * Pending removal in Python 3.18

      * Pending removal in Python 3.19

      * Pending removal in future versions

    * CPython bytecode changes

      * Pseudo-instructions

    * C API changes

      * Python configuration C API

      * New features in the C API

      * Limited C API changes

      * Removed C APIs

      * Deprecated C APIs

        * Pending removal in Python 3.15

        * Pending removal in Python 3.16

        * Pending removal in Python 3.18

        * Pending removal in future versions

    * Build changes

      * "build-details.json"

      * Discontinuation of PGP signatures

      * Free-threaded Python is officially supported

      * Binary releases for the experimental just-in-time compiler

    * Porting to Python 3.14

      * Changes in the Python API

      * Changes in annotations (**PEP 649** and **PEP 749**)

        * Implications for annotated code

        * Implications for readers of "__annotations__"

        * Related changes

        * "from __future__ import annotations"

      * Changes in the C API

    * Notable changes in 3.14.1

    * Notable changes in 3.14.5

      * gc

  * What's New In Python 3.13

    * Summary -- Release Highlights

    * New Features

      * A better interactive interpreter

      * Improved error messages

      * Free-threaded CPython

      * An experimental just-in-time (JIT) compiler

      * Defined mutation semantics for "locals()"

      * Support for mobile platforms

    * Other Language Changes

    * New Modules

    * Improved Modules

      * argparse

      * array

      * ast

      * asyncio

      * base64

      * compileall

      * concurrent.futures

      * configparser

      * copy

      * ctypes

      * dbm

      * dis

      * doctest

      * email

      * enum

      * fractions

      * glob

      * importlib

      * io

      * ipaddress

      * itertools

      * marshal

      * math

      * mimetypes

      * mmap

      * multiprocessing

      * os

      * os.path

      * pathlib

      * pdb

      * queue

      * random

      * re

      * shutil

      * site

      * sqlite3

      * ssl

      * statistics

      * subprocess

      * sys

      * tempfile

      * time

      * tkinter

      * traceback

      * types

      * typing

      * unicodedata

      * venv

      * warnings

      * xml

      * zipimport

    * Optimizations

    * Removed Modules And APIs

      * PEP 594: Remove "dead batteries" from the standard library

      * 2to3

      * builtins

      * configparser

      * importlib.metadata

      * locale

      * opcode

      * optparse

      * pathlib

      * re

      * tkinter.tix

      * turtle

      * typing

      * unittest

      * urllib

      * webbrowser

    * New Deprecations

      * Pending removal in Python 3.14

      * Pending removal in Python 3.15

      * Pending removal in Python 3.16

      * Pending removal in Python 3.17

      * Pending removal in Python 3.18

      * Pending removal in Python 3.19

      * Pending removal in future versions

    * CPython Bytecode Changes

    * C API Changes

      * New Features

      * Changed C APIs

      * Limited C API Changes

      * Removed C APIs

      * Deprecated C APIs

        * Pending removal in Python 3.14

        * Pending removal in Python 3.15

        * Pending removal in Python 3.16

        * Pending removal in Python 3.18

        * Pending removal in future versions

    * Build Changes

    * Porting to Python 3.13

      * Changes in the Python API

      * Changes in the C API

    * Regression Test Changes

  * Novedades de Python 3.12

    * Resumen: aspectos destacados de la versión

    * Nuevas características

      * PEP 695: Sintaxis de parámetro de tipo

      * PEP 701: Formalización sintáctica de cadenas f

      * PEP 684: un GIL por intérprete

      * PEP 669: Monitoreo de bajo impacto para CPython

      * PEP 688: Hacer accesible el protocolo de búfer en Python

      * PEP 709: Integración de la comprensión

      * Mensajes de error mejorados

    * Nuevas funciones relacionadas con las sugerencias de escritura

      * PEP 692: uso de "TypedDict" para una escritura "**kwargs" más
        precisa

      * PEP 698: Decorador override para escritura estática

    * Otros cambios del lenguaje

    * Nuevos módulos

    * Módulos mejorados

      * array

      * asincio

      * calendar

      * csv

      * dis

      * fractions

      * importlib.resources

      * inspect

      * itertools

      * math

      * os

      * os.path

      * pathlib

      * platform

      * pbd

      * random

      * shutil

      * sqlite3

      * statistics

      * sys

      * tempfile

      * threading

      * tkinter

      * tokenize

      * types

      * typing

      * unicodedata

      * unittest

      * uuid

    * Optimizaciones

    * Cambios en el código de bytes de CPython

    * Demostraciones y herramientas

    * Obsoleto

      * Pending removal in Python 3.13

      * Pending removal in Python 3.14

      * Pending removal in Python 3.15

      * Pending removal in Python 3.16

      * Pending removal in Python 3.17

      * Pending removal in future versions

    * Eliminado

      * asynchat y asyncore

      * configparser

      * distutils

      * ensurepip

      * enum

      * ftplib

      * gzip

      * hashlib

      * importlib

      * imp

      * io

      * locale

      * smtpd

      * sqlite3

      * ssl

      * unittest

      * webbrowser

      * xml.etree.ElementTree

      * zipimport

      * Otros

    * Portar a Python 3.12

      * Cambios en la API de Python

    * Cambios de compilación

    * Cambios en la API de C

      * Nuevas características

      * Portar a Python 3.12

      * Obsoleto

        * Pending removal in Python 3.14

        * Pending removal in Python 3.15

        * Pending removal in Python 3.16

        * Pending removal in future versions

      * Eliminado

  * Qué hay de nuevo en Python 3.11

    * Resumen -- Aspectos destacados de la versión

    * Nuevas características

      * PEP 657: Ubicaciones de errores detallados en rastreos

      * PEP 654: Grupos de excepción y "except*"

      * PEP 678: Las excepciones se pueden enriquecer con notas

      * Mejoras en el iniciador de Windows "py.exe"

    * Nuevas funciones relacionadas con las sugerencias de tipo

      * PEP 646: Genéricos Variádicos

      * PEP 655: Marcado de elementos "TypedDict" individuales como
        requeridos o no requeridos

      * PEP 673: tipo "Self"

      * PEP 675: tipo de cadena literal arbitraria

      * PEP 681: Transformaciones de clases de datos

      * PEP 563 puede no ser el futuro

    * Otros cambios de idioma

    * Otros cambios en la implementación de CPython

    * Nuevos Módulos

    * Módulos mejorados

      * asíncio

      * contextlib

      * clases de datos

      * fecha y hora

      * enumeración

      * fcntl

      * fracciones

      * herramientas funcionales

      * gzip

      * hashlib

      * IDLE y libre de inactividad

      * inspeccionar

      * lugar

      * Inicio sesión

      * Matemáticas

      * operador

      * sistema operativo

      * rutalib

      * re

      * cerrar

      * enchufe

      * sqlite3

      * cuerda

      * sistema

      * configuración del sistema

      * archivo temporal

      * enhebrar

      * tiempo

      * tkinter

      * rastrear

      * mecanografía

      * unicodedata

      * prueba de unidad

      * venv

      * advertencias

      * archivo zip

    * Optimizaciones

    * CPython más rápido

      * Inicio más rápido

        * Importaciones congeladas / Objetos de código estático

      * Tiempo de ejecución más rápido

        * Marcos de Python más baratos y perezosos

        * Llamadas a funciones de Python en línea

        * PEP 659: Intérprete Adaptativo Especializado

      * Varios

      * Preguntas más frecuentes

        * ¿Cómo debo escribir mi código para utilizar estas
          aceleraciones?

        * ¿CPython 3.11 usará más memoria?

        * No veo ninguna aceleración en mi carga de trabajo. ¿Por qué?

        * ¿Existe un compilador JIT?

      * Sobre

    * Cambios en el código de bytes de CPython

      * Nuevos códigos de operación

      * Códigos de operación reemplazados

      * Códigos de operación cambiados/eliminados

    * Obsoleto

      * Idioma/Construidos

      * Módulos

      * Biblioteca estándar

    * Eliminación pendiente en Python 3.12

    * Remoto

    * Migración a Python 3.11

    * Construir cambios

    * Cambios en la API de C

      * Nuevas características

      * Migración a Python 3.11

      * Obsoleto

      * Eliminación pendiente en Python 3.12

      * Remoto

    * Notable changes in 3.11.4

      * tarfile

    * Notable changes in 3.11.5

      * OpenSSL

  * Qué hay de nuevo en Python 3.10

    * Resumen: aspectos destacados de la versión

    * Nuevas características

      * Administradores de contexto entre paréntesis

      * Mejores mensajes de error

        * SyntaxErrors

        * Errores de sangría

        * AttributeErrors

        * NameErrors

      * PEP 626: números de línea precisos para depuración y otras
        herramientas

      * PEP 634: Coincidencia de patrones estructurales

        * Sintaxis y operaciones

        * Enfoque declarativo

        * Patrón simple: coincidir con un literal

          * Comportamiento sin el comodín

        * Patrones con un literal y una variable

        * Patrones y clases

          * Patrones con parámetros posicionales

        * Patrones anidados

        * Patrones complejos y el comodín

        * Guardia

        * Otras características clave

      * Opción opcional "EncodingWarning" y "encoding="locale""

    * Nuevas funciones relacionadas con las sugerencias de tipos

      * PEP 604: Nuevo tipo de operador unión

      * PEP 612: Variables de especificación de parámetros

      * PEP 613: TypeAlias

      * PEP 647: protectores de tipo definidos por el usuario

    * Otros cambios de idioma

    * Nuevos módulos

    * Módulos mejorados

      * asyncio

      * argumentar

      * formación

      * asynchat, asyncore, smtpd

      * base64

      * bdb

      * bisecar

      * códecs

      * colecciones.abc

      * contextlib

      * maldiciones

      * clases de datos

        * __slots__

        * Campos solo de palabras clave

      * distutils

      * doctest

      * codificaciones

      * enum

      * entrada de archivo

      * manipulador de faltas

      * gc

      * glob

      * hashlib

      * hmac

      * IDLE e idlelib

      * importlib.metadata

      * inspeccionar

      * itertools

      * caché de línea

      * os

      * os.path

      * pathlib

      * plataforma

      * pprint

      * py_compile

      * pyclbr

      * dejar de lado

      * estadísticas

      * sitio

      * enchufe

      * ssl

      * sqlite3

      * sys

      * _hilo

      * enhebrar

      * rastrear

      * tipos

      * mecanografía

      * prueba de unidad

      * urllib.parse

      * xml

      * zipimport

    * Optimizaciones

    * Obsoleto

    * Eliminado

    * Portar a Python 3.10

      * Cambios en la sintaxis de Python

      * Cambios en la API de Python

      * Cambios en la API de C

    * Cambios en el código de bytes de CPython

    * Construir cambios

    * Cambios en la API de C

      * PEP 652: Mantenimiento del ABI estable

      * Nuevas características

      * Portar a Python 3.10

      * Obsoleto

      * Eliminado

    * Característica de seguridad notable en 3.10.7

    * Característica de seguridad notable en 3.10.8

    * Cambios notables en 3.10.12

      * archivo tar

  * Qué hay de nuevo en Python 3.9

    * Resumen: aspectos destacados de la versión

    * Debe verificar DeprecationWarning en su código

    * Nuevas características

      * Operadores de combinación y actualización de diccionarios

      * Nuevos métodos de cadena para eliminar prefijos y sufijos

      * Tipos genéricos de sugerencia en colecciones estándar

      * Nuevo analizador

    * Otros cambios de idioma

    * Nuevos módulos

      * zoneinfo

      * Graphlib

    * Módulos mejorados

      * ast

      * asyncio

      * compilar todo

      * Futuros concurrentes

      * maldiciones

      * fecha y hora

      * distutils

      * fcntl

      * ftplib

      * GC

      * hashlib

      * http

      * IDLE e idlelib

      * imaplib

      * importlib

      * inspeccionar

      * dirección IP

      * Matemáticas

      * multiprocesamiento

      * nntplib

      * os

      * Pathlib

      * pdb

      * poplib

      * pprint

      * Pydoc

      * aleatorio

      * señal

      * smtplib

      * enchufe

      * tiempo

      * sys

      * tracemalloc

      * mecanografía

      * unicodedata

      * venv

      * xml

    * Optimizaciones

    * Obsoleto

    * Remoto

    * Portar a Python 3.9

      * Cambios en la API de Python

      * Cambios en la API de C

      * Cambios en el código de bytes de CPython

    * Construir cambios

    * Cambios en la API de C

      * Nuevas características

      * Portar a Python 3.9

      * Remoto

    * Cambios notables en Python 3.9.1

      * mecanografía

      * Compatibilidad con macOS 11.0 (Big Sur) y Apple Silicon Mac

    * Cambios notables en Python 3.9.2

      * colecciones.abc

      * urllib.parse

    * Notable changes in Python 3.9.3

    * Notable changes in Python 3.9.5

      * urllib.parse

    * Notable security feature in 3.9.14

    * Notable changes in 3.9.17

      * tarfile

  * Qué hay de nuevo en Python 3.8

    * Resumen -- Aspectos destacados de la versión

    * Nuevas características

      * Expresiones de asignación

      * Parámetros solo posicionales

      * Caché del sistema de archivos paralelo para archivos de
        bytecode compilados

      * La compilación de depuración usa la misma ABI que la
        compilación de lanzamiento

      * los f-strings soportan "=" para expresiones autodocumentadas y
        depuración

      * PEP 578: Ganchos de auditoría en tiempo de ejecución de Python

      * PEP 587: Configuración de inicialización de Python

      * PEP 590: Vectorcall: un protocolo de llamada rápida para
        CPython

      * Protocolo 5 de Pickle con búferes de datos fuera de banda

    * Otros cambios en el lenguaje

    * Nuevos módulos

    * Módulos mejorados

      * ast

      * asyncio

      * builtins

      * collections

      * cProfile

      * csv

      * curses

      * ctypes

      * datetime

      * functools

      * gc

      * gettext

      * gzip

      * IDLE e idlelib

      * inspect

      * io

      * itertools

      * json.tool

      * logging

      * math

      * mmap

      * multiprocessing

      * os

      * os.path

      * pathlib

      * pickle

      * plistlib

      * pprint

      * py_compile

      * shlex

      * shutil

      * socket

      * ssl

      * statistics

      * sys

      * tarfile

      * threading

      * tokenize

      * tkinter

      * time

      * typing

      * unicodedata

      * unittest

      * venv

      * weakref

      * xml

      * xmlrpc

    * Optimizaciones

    * Cambios en la compilación y la API de C

    * Obsoleto

    * APIs y características eliminadas

    * Portando a Python 3.8

      * Cambios en el comportamiento de Python

      * Cambios en la API de Python

      * Cambios en la API de C

      * Cambios en el bytecode de CPython

      * Demos y herramientas

    * Cambios notables en Python 3.8.1

    * Notable changes in Python 3.8.2

    * Notable changes in Python 3.8.3

    * Cambios notables en Python 3.8.8

    * Notable changes in Python 3.8.9

    * Notable changes in Python 3.8.10

      * macOS 11.0 (Big Sur) and Apple Silicon Mac support

    * Notable changes in Python 3.8.10

      * urllib.parse

    * Cambios notables en Python 3.8.1

      * Cambios en la API de Python

    * Notable security feature in 3.8.14

    * Notable changes in 3.8.17

      * tarfile

  * Qué hay de nuevo en Python 3.7

    * Resumen -- Lanzamientos Destacados

    * Nuevas Características

      * PEP 563: Evaluación pospuesta de anotaciones

      * PEP 538: Coerción de configuración regional del Legado de  C

      * PEP 540: Modo de tiempo de ejecución UTF-8 forzado

      * PEP 553: Incorporada en "breakpoint()"

      * PEP 539: Nueva API C para almacenamiento local de subprocesos

      * PEP 562: Personalización del acceso a los atributos del módulo

      * PEP 564: Nuevas funciones de tiempo con resolución de
        nanosegundos

      * PEP 565: Mostrar *DeprecationWarning* en "__main__"

      * PEP 560: Soporte básico para el módulo de "typing" y tipos
        genéricos

      * PEP 552: Archivos .pyc basados en hash

      * PEP 545: Traducciones de Documentaciones de Python

      * Modo de desarrollo de Python (-X dev)

    * Otros cambios en el lenguaje

    * Nuevos módulos

      * *contextvars*

      * *dataclasses*

      * *importlib.resources*

    * Módulos mejorados

      * *argparse*

      * *asyncio*

      * *binascii*

      * *calendar*

      * *collections*

      * *compileall*

      * *concurrent.futures*

      * *contextlib*

      * *cProfile*

      * *crypt*

      * *datetime*

      * *dbm*

      * *decimal*

      * *dis*

      * *distutils*

      * *enum*

      * *functools*

      * *gc*

      * *hmac*

      * *http.client*

      * *http.server*

      * *idlelib and IDLE*

      * *importlib*

      * *io*

      * *ipaddress*

      * *itertools*

      * *locale*

      * *logging*

      * *math*

      * *mimetypes*

      * *msilib*

      * *multiprocessing*

      * *os*

      * *pathlib*

      * *pdb*

      * *py_compile*

      * *pydoc*

      * *queue*

      * *re*

      * *signal*

      * *socket*

      * *socketserver*

      * *sqlite3*

      * *ssl*

      * *string*

      * *subprocess*

      * *sys*

      * *time*

      * *tkinter*

      * *tracemalloc*

      * *types*

      * *unicodedata*

      * *unittest*

      * *unittest.mock*

      * *urllib.parse*

      * *uu*

      * *uuid*

      * *warnings*

      * xml

      * *xml.etree*

      * *xmlrpc.server*

      * *zipapp*

      * *zipfile*

    * Cambios en la API C

    * Construir cambios

    * Optimizaciones

    * Otros cambios de implementación de CPython

    * Comportamiento obsoleto de Python

    * Módulos, funciones y métodos de Python obsoletos

      * *aifc*

      * *asyncio*

      * *collections*

      * *dbm*

      * *enum*

      * *gettext*

      * *importlib*

      * *locale*

      * *macpath*

      * *threading*

      * *socket*

      * *ssl*

      * *sunau*

      * *sys*

      * *wave*

    * Funciones y tipos obsoletos de la API C

    * Eliminación de soporte de plataforma

    * Eliminaciones de API y funciones

    * Eliminaciones de módulos

    * Cambios solo en Windows

    * Portando a Python 3.7

      * Cambios en el comportamiento de Python

      * Cambios en la API Python

      * Cambios en la API de C

      * Cambios en el código de bytes de CPython

      * Cambios solo en Windows

      * Otra implementación de cambios en CPython

    * Cambios notables en Python 3.7.1

    * Cambios notables en Python 3.7.2

    * Cambios notables en Python 3.7.6

    * Cambios notables en Python 3.7.10

    * Cambios notables en Python 3.7.11

    * Cambios notables en Python 3.7.14

  * Qué hay de nuevo en Python 3.6

    * Resumen: aspectos destacados de la versión

    * Nuevas características

      * PEP 498: Literales de cadena formateados

      * PEP 526: Sintaxis para anotaciones de variables

      * PEP 515: subrayados en literales numéricos

      * PEP 525: Generadores asíncronos

      * PEP 530: Comprensiones asincrónicas

      * PEP 487: personalización más sencilla de la creación de clases

      * PEP 487: Mejoras en el protocolo descriptor

      * PEP 519: Agregar un protocolo de ruta del sistema de archivos

      * PEP 495: desambiguación de la hora local

      * PEP 529: cambie la codificación del sistema de archivos de
        Windows a UTF-8

      * PEP 528: cambie la codificación de la consola de Windows a
        UTF-8

      * PEP 520: Conservación del orden de definición de atributos de
        clase

      * PEP 468: Conservación del orden de los argumentos de las
        palabras clave

      * Nueva implementación de *dict*

      * PEP 523: Agregar una API de evaluación de marcos a CPython

      * Variable de entorno PYTHONMALLOC

      * Soporte de sondeo DTrace y SystemTap

    * Otros cambios de idioma

    * Nuevos módulos

      * misterios

    * Módulos mejorados

      * formación

      * ast

      * asyncio

      * binascii

      * cmath

      * colecciones

      * concurrent.futures

      * contextlib

      * fecha y hora

      * decimal

      * distutils

      * email

      * codificaciones

      * enumeración

      * manipulador de faltas

      * entrada de archivo

      * hashlib

      * http.client

      * idlelib y IDLE

      * importlib

      * inspeccionar

      * json

      * logging

      * math

      * multiprocesamiento

      * os

      * pathlib

      * pdb

      * pepinillo

      * pepinillos

      * pydoc

      * aleatorio

      * re

      * readline

      * rlcompleter

      * shlex

      * sitio

      * sqlite3

      * enchufe

      * servidor de sockets

      * ssl

      * Estadísticas

      * estructura

      * subproceso

      * sys

      * telnetlib

      * tiempo

      * cronométralo

      * tkinter

      * rastrear

      * tracemalloc

      * mecanografía

      * unicodedata

      * unittest.mock

      * urllib.request

      * urllib.robotparser

      * venv

      * advertencias

      * winreg

      * winsonido

      * xmlrpc.client

      * archivo zip

      * zlib

    * Optimizaciones

    * Cambios en la API de Build y C

    * Otras mejoras

    * Obsoleto

      * Nuevas palabras clave

      * Comportamiento de Python obsoleto

      * Módulos, funciones y métodos de Python obsoletos

        * asynchat

        * asyncore

        * dbm

        * distutils

        * grp

        * importlib

        * os

        * re

        * ssl

        * tkinter

        * venv

      * xml

      * Funciones y tipos obsoletos de la API de C

      * Opciones de compilación obsoletas

    * Remoto

      * Eliminaciones de API y funciones

    * Portar a Python 3.6

      * Cambios en el comportamiento del comando 'python'

      * Cambios en la API de Python

      * Cambios en la API de C

      * Cambios en el código de bytes de CPython

    * Cambios notables en Python 3.6.2

      * Nuevo objetivo de compilación "make regen-all"

      * Eliminación del objetivo de compilación "make touch"

    * Cambios notables en Python 3.6.4

    * Cambios notables en Python 3.6.5

    * Cambios notables en Python 3.6.7

    * Cambios notables en Python 3.6.10

    * Cambios notables en Python 3.6.13

    * Cambios notables en Python 3.6.14

  * Qué hay de nuevo en Python 3.5

    * Resumen -- Aspectos destacados de la versión

    * Nuevas características

      * PEP 492 - Corrutinas con sintaxis async y await

      * PEP 465 - Un operador infijo dedicado para la multiplicación
        de matrices

      * PEP 448 - Generalizaciones de desembalaje adicionales

      * PEP 461 - soporte de formateo porcentual para bytes y
        bytearray

      * PEP 484 - Indicador de tipos

      * PEP 471 - Función os.scandir() -- un iterador de directorio
        mejor y más rápido

      * PEP 475: Reintentar las llamadas al sistema que fallan con
        EINTR

      * PEP 479: Cambiar el gestor de StopIteration dentro de
        generadores

      * PEP 485: Una función para probar la igualdad aproximada

      * PEP 486: Hacer que el launcher de Python sea consciente de los
        entornos virtuales

      * PEP 488: Eliminación de archivos PYO

      * PEP 489: Inicialización del módulo de extensión multifase

    * Otros cambios en el lenguaje

    * Nuevos módulos

      * typing

      * zipapp

    * Módulos mejorados

      * argparse

      * asyncio

      * bz2

      * cgi

      * cmath

      * code

      * collections

      * collections.abc

      * compileall

      * concurrent.futures

      * configparser

      * contextlib

      * csv

      * curses

      * dbm

      * difflib

      * distutils

      * doctest

      * email

      * enum

      * faulthandler

      * functools

      * glob

      * gzip

      * heapq

      * http

      * http.client

      * idlelib e IDLE

      * imaplib

      * imghdr

      * importlib

      * inspect

      * io

      * ipaddress

      * json

      * linecache

      * locale

      * logging

      * lzma

      * math

      * multiprocessing

      * operator

      * os

      * pathlib

      * pickle

      * poplib

      * re

      * readline

      * selectors

      * shutil

      * signal

      * smtpd

      * smtplib

      * sndhdr

      * socket

      * ssl

        * Soporte de memoria BIO

        * Soporte de negociación de protocolo de capa de aplicación

        * Otros cambios

      * sqlite3

      * subprocess

      * sys

      * sysconfig

      * tarfile

      * threading

      * time

      * timeit

      * tkinter

      * traceback

      * types

      * unicodedata

      * unittest

      * unittest.mock

      * urllib

      * wsgiref

      * xmlrpc

      * xml.sax

      * zipfile

    * Otros cambios a nivel de módulo

    * Optimizaciones

    * Cambios en la compilación y la API de C

    * Obsoleto

      * Nuevas palabras clave

      * Comportamiento obsoleto de Python

      * Sistemas operativos no compatibles

      * Módulos, funciones y métodos obsoletos de Python

    * Eliminado

      * APIs y características eliminadas

    * Portando a Python 3.5

      * Cambios en el comportamiento de Python

      * Cambios en la API de Python

      * Cambios en la API de C

    * Cambios notables en Python 3.5.4

      * Nuevo objetivo de compilación "make regen-all"

      * Eliminación del objetivo de compilación "make touch"

  * Qué hay de nuevo en Python 3.4

    * Resumen -- Puntos destacados del lanzamiento

    * Nuevas Funciones

      * PEP 453: Arranque explícito de PIP en instalaciones de Python

        * Puesta en marcha de pip por defecto

        * Cambios en la documentación

      * PEP 446: Los descriptores de archivos recién creados no son
        heredables

      * Mejoras en el manejo de códecs

      * PEP 451: Un tipo ModuleSpec para el sistema de importación

      * Otros cambios de lenguaje

    * Nuevos Módulos

      * asyncio

      * ensurepip

      * enum

      * pathlib

      * selectores

      * estadísticas

      * tracemalloc

    * Módulos mejorados

      * abc

      * aifc

      * argparse

      * audioop

      * base64

      * colecciones

      * colorsys

      * contextlib

      * dbm

      * dis

      * doctest

      * email

      * archivoecmp

      * functools

      * gc

      * glob

      * hashlib

      * hmac

      * html

      * http

      * idlelib y IDLE

      * importlib

      * inspeccionar

      * dirección IP

      * logging

      * mariscal

      * mmap

      * multiprocesamiento

      * operator

      * os

      * pdb

      * pepinillo

      * plistlib

      * poplib

      * pprint

      * pty

      * pydoc

      * re

      * recurso

      * seleccionar

      * estante

      * shutil

      * smtpd

      * smtplib

      * enchufe

      * sqlite3

      * ssl

      * stat

      * struct

      * subproceso

      * sunau

      * sys

      * tarfile

      * textwrap

      * roscado

      * traceback

      * tipos

      * urllib

      * unittest

      * venv

      * onda

      * weakref

      * xml.etree

      * archivo zip

    * Cambios en la implementación de CPython

      * PEP 445: Personalización de los Asignadores de Memoria de
        CPython

      * PEP 442: Finalización segura de objetos

      * PEP 456: Algoritmo Hash seguro e intercambiable

      * PEP 436: Clínica de Argumentación

      * Otros cambios en la API de construcción y C

      * Otras mejoras

      * Optimizaciones significativas

    * Obsoleto

      * Desapariciones en la API de Python

      * Funciones obsoletas

    * Removido

      * Sistemas operativos que ya no son compatibles

      * Eliminación de la API y de las funciones

      * Limpieza del código

    * Adaptación a Python 3.4

      * Cambios en el comportamiento del comando 'python'

      * Cambios en la API de Python

      * Cambios en la API de C

    * Cambiado en 3.4.3

      * PEP 476: Habilitar la verificación de certificados por defecto
        para los clientes http stdlib

  * Qué hay de nuevo en Python 3.3

    * Resumen -- Aspectos destacados de la versión

    * PEP 405: Entornos virtuales

    * PEP 420: Paquetes para espacios de nombres implícitos

    * PEP 3118: Nueva implementación de vista de memoria y en la
      documentación del protocolo del buffer

      * Características

      * Cambios en la API

    * PEP 393: Representación flexible de cadenas de caracteres

      * Funcionalidad

      * Rendimiento y uso de recursos

    * PEP 397: Lanzador de python para windows

    * PEP 3151: Reelaborando de la jerarquía de excepciones de IO y OS

    * PEP 380: Sintaxis para delegar en un subgenerador

    * PEP 409: Suprimir el contexto de excepción

    * PEP 414: Literales *Unicode* explícitos

    * PEP 3155: Nombres calificados para clases y funciones

    * PEP 412: Diccionario de intercambio de claves

    * PEP 362: Objeto de firma de función

    * PEP 421: Agregar sys.implementation

      * SimpleNamespace

    * Usar importlib como implementación de Import

      * Nuevas APIs

      * Cambios visibles

    * Otros cambios de idioma

    * Un bloqueo de importación más detallado

    * Funciones y tipos incorporados

    * Nuevos módulos

      * faulthandler

      * ipaddress

      * lzma

    * Módulos mejorados

      * abc

      * array

      * base64

      * binascii

      * bz2

      * códecs

      * colecciones

      * contextlib

      * crypt

      * curses

      * datetime

      * decimal

        * Características

        * Cambios en la API

      * email

        * Marco de políticas

        * Política provisional con nueva API de encabezado

        * Otros cambios en la API

      * ftplib

      * functools

      * gc

      * hmac

      * http

      * html

      * imaplib

      * inspect

      * io

      * itertools

      * logging

      * math

      * mmap

      * multiprocesamiento

      * nntplib

      * os

      * pdb

      * pickle

      * pydoc

      * re

      * sched

      * select

      * shlex

      * shutil

      * signal

      * smtpd

      * smtplib

      * socket

      * socketserver

      * sqlite3

      * ssl

      * stat

      * struct

      * subprocess

      * sys

      * tarfile

      * tempfile

      * textwrap

      * threading

      * time

      * types

      * unittest

      * urllib

      * webbrowser

      * xml.etree.ElementTree

      * zlib

    * Optimizaciones

    * Construcción y cambios en la API de C

    * Obsoleto

      * Sistemas operativos no compatibles

      * Módulos , funciones y métodos obsoletos en Python

      * Funciones y tipos obsoletos en la API de C

      * Características obsoletas

    * Migración a Python 3.3

      * Portando código Python

      * Portando código C

      * Construyendo extensiones C

      * Cambios en el conmutador de línea de comandos

  * Qué hay de nuevo en Python 3.2

    * PEP 384: Definición de un ABI estable

    * PEP 389: Módulo de análisis sintáctico (*Parser*) de línea de
      comandos Argparse

    * PEP 391: Configuración basada en diccionario para Logging

    * PEP 3148: El módulo "concurrent.futures"

    * PEP 3147: Directorios del repositorio de PYC

    * PEP 3149: Archivos .so con etiquetado de versión para ABI

    * PEP 3333: Interfaz de puerta de enlace del servidor web Python
      v1.0.1

    * Otros cambios de lenguaje

    * Módulos nuevos, mejorados y obsoletos

      * email

      * elementtree

      * functools

      * itertools

      * collections

      * threading

      * datetime and time

      * math

      * abc

      * io

      * reprlib

      * logging

      * csv

      * contextlib

      * decimal and fractions

      * ftp

      * popen

      * select

      * gzip y zipfile

      * tarfile

      * hashlib

      * ast

      * os

      * shutil

      * sqlite3

      * html

      * socket

      * ssl

      * nntp

      * certificados

      * imaplib

      * http.client

      * unittest

      * random

      * poplib

      * asyncore

      * tempfile

      * inspect

      * pydoc

      * dis

      * dbm

      * ctypes

      * site

      * sysconfig

      * pdb

      * configparser

      * urllib.parse

      * mailbox

      * turtledemo

    * Multi-threading

    * Optimizations

    * Unicode

    * Codecs

    * Documentación

    * IDLE

    * Repositorio de código

    * Cambios en la API de construcción y C

    * Portar a Python 3.2

  * Qué hay de nuevo en Python 3.1

    * PEP 372: Diccionarios ordenados

    * PEP 378: Especificador de formato para el separador de miles

    * Otros cambios del lenguaje

    * Módulos nuevos, mejorados y obsoletos

    * Optimizaciones

    * IDLE

    * Cambios en la compilación y la API de C

    * Portando a Python 3.1

  * Qué hay de nuevo en Python 3.0

    * Escollos comunes

      * *Print* es una función

      * Vistas e iteradores en lugar de listas

      * Comparaciones de ordenamiento

      * Enteros

      * Texto vs. datos en lugar de unicode vs. 8 bits

    * Descripción general de los cambios de sintaxis

      * Nueva sintaxis

      * Sintaxis modificada

      * Sintaxis eliminada

    * Cambios ya presentes en Python 2.6

    * Cambios de biblioteca

    * **PEP 3101**: Un nuevo enfoque al formateo de cadena de
      caracteres

    * Cambios a excepciones

    * Otros cambios diversos

      * Operadores y métodos especiales

      * Incorporados

    * Construcción y cambios a la API de C

    * Rendimiento

    * Migración a Python 3.0

  * Qué hay de nuevo en Python 2.7

    * El futuro de Python 2.x

    * Cambios en el manejo de las advertencias de desuso

    * Características de Python 3.1

    * PEP 372: Adición de un diccionario ordenado a las colecciones

    * PEP 378: Especificador de formato para separador de miles

    * PEP 389: El módulo argparse para el análisis de líneas de
      comando

    * PEP 391: Configuración basada en diccionarios para el registro

    * PEP 3106: Vistas de diccionario

    * PEP 3137: El objeto memoryview

    * Otros cambios de lenguaje

      * Cambios en el intérprete

      * Optimizaciones

    * Módulos nuevos y mejorados

      * Nuevo módulo: importlib

      * Nuevo módulo: sysconfig

      * ttk: Widgets temáticos para Tk

      * Módulo actualizado: unittest

      * Módulo actualizado: ElementTree 1.3

    * Cambios en la API de construcción y C

      * Cápsulas

      * Cambios específicos en los puertos: Windows

      * Cambios específicos en los puertos: Mac OS X

      * Cambios específicos en los puertos: FreeBSD

    * Otros cambios y correcciones

    * Adaptación a Python 2.7

    * Nuevas funciones añadidas a las versiones de mantenimiento de
      Python 2.7

      * Dos nuevas variables de entorno para el modo de depuración

      * PEP 434: Excepción de mejora de IDLE para todas las ramas

      * PEP 466: Mejoras en la seguridad de la red para Python 2.7

      * PEP 477: Backport ensurepip (PEP 453) a Python 2.7

        * Puesta en marcha de pip por defecto

        * Cambios en la documentación

      * PEP 476: Habilitar la verificación de certificados por defecto
        para los clientes http stdlib

      * PEP 493: Herramientas de migración de verificación HTTPS para
        Python 2.7

      * Nuevo objetivo de construcción "make regen-all"

      * Eliminación del objetivo de construcción "make touch"

    * Agradecimientos

  * Qué hay de nuevo en Python 2.6

    * Python 3.0

    * Cambios en el proceso de desarrollo

      * Nuevo seguidor de incidentes: Roundup

      * Nuevo formato de documentación: texto reestructurado con
        Sphinx

    * PEP 343: La sentencia *'with'*

      * Escribiendo gestores de contexto

      * El módulo contextlib

    * PEP 366: Importaciones relativas explícitas desde un módulo
      principal

    * PEP 370: Directorio de "site-packages" por usuario

    * PEP 371: El paquete "multiprocessing"

    * PEP 3101: Formateo avanzado de cadena de caracteres

    * PEP 3105: "print" como función

    * PEP 3110: Cambios en el manejo de excepciones

    * PEP 3112: Literales de bytes

    * PEP 3116: Nueva biblioteca de E/S

    * PEP 3118: Protocolo revisado de la memoria intermedia

    * PEP 3119: Clases base abstractas

    * PEP 3127: Soporte y sintaxis de literales enteros

    * PEP 3129: Decoradores de clase

    * PEP 3141: Una jerarquía de tipos para los números

      * El módulo "fractions"

    * Otros cambios lingüísticos

      * Optimizaciones

      * Cambios de intérprete

    * Módulos nuevos y mejorados

      * El módulo "ast"

      * The "future_builtins" module

      * El módulo "json": Notación de objetos de JavaScript

      * El módulo "plistlib": Un analizador de listas de propiedades

      * mejoras en ctypes

      * Mejora de la compatibilidad con SSL

    * Cancelaciones y eliminaciones

    * Cambios en la API de construcción y C

      * Cambios específicos en los puertos: Windows

      * Cambios específicos en los puertos: Mac OS X

      * Cambios específicos en los puertos: IRIX

    * Adaptación a Python 2.6

    * Agradecimientos

  * Qué hay de nuevo en Python 2.5

    * PEP 308: Expresiones condicionales

    * PEP 309: Aplicación parcial de funciones

    * PEP 314: Metadatos para paquetes de software Python v1.1

    * PEP 328: Importaciones absolutas y relativas

    * PEP 338: Ejecutando Módulos como Scripts

    * PEP 341: Try/except/finally unificados

    * PEP 342: Nuevas funciones del generador

    * PEP 343: La declaración "con

      * Redacción de Gestores de Contexto

      * El módulo contextlib

    * PEP 352: Las excepciones como clases de nuevo estilo

    * PEP 353: Uso de ssize_t como tipo de índice

    * PEP 357: El método '__index__'

    * Otros cambios lingüísticos

      * Cambios en el intérprete interactivo

      * Optimizaciones

    * Módulos nuevos, mejorados y eliminados

      * El paquete ctypes

      * El paquete ElementTree

      * El paquete hashlib

      * El paquete sqlite3

      * El paquete wsgiref

    * Cambios en la API de construcción y C

      * Cambios específicos en los puertos

    * Adaptación a Python 2.5

    * Agradecimientos

  * Qué hay de nuevo en Python 2.4

    * PEP 218: Objetos conjunto integrados

    * PEP 237: Unificando enteros largos y enteros

    * PEP 289: Expresiones generadoras

    * PEP 292: Sustituciones simples de cadenas de caracteres

    * PEP 318: Decoradores para funciones y métodos

    * PEP 322: Iteración inversa

    * PEP 324: Nuevo módulo de subproceso

    * PEP 327: Tipo de dato decimal

      * ¿Por qué se necesita Decimal?

      * The "Decimal" type

      * The "Context" type

    * PEP 328: Importaciones multilínea

    * PEP 331: Conversiones locales-independientes números
      flotantes/cadenas de texto

    * Otros cambios en el lenguaje

      * Optimizaciones

    * Módulos nuevos, mejorados y obsoletos

      * cookielib

      * doctest

    * Cambios en la API de Build y C

      * Cambios específicos del puerto

    * Portar a Python 2.4

    * Agradecimientos

  * Qué hay de nuevo en Python 2.3

    * PEP 218: Un tipo de datos de conjunto estándar

    * PEP 255: Generadores simples

    * PEP 263: Codificación del código fuente

    * PEP 273: Importar módulos desde archivos ZIP

    * PEP 277: Soporte de nombres de archivo Unicode para Windows NT

    * PEP 278: Soporte universal de nuevas líneas

    * PEP 279: enumerate()

    * PEP 282: El paquete de registro

    * PEP 285: Un tipo booleano

    * PEP 293: Llamadas de retorno para el manejo de errores del códec

    * PEP 301: Índice de paquetes y metadatos para Distutils

    * PEP 302: Nuevos ganchos de importación

    * PEP 305: Archivos separados por comas

    * PEP 307: Mejoras en Pickle

    * Rebanadas ampliadas

    * Otros cambios en el lenguaje

      * Cambios en las cadenas de texto

      * Optimizaciones

    * Módulos nuevos, mejorados y obsoletos

      * Tipo de fecha / hora

      * El módulo optparse

    * Pymalloc: un asignador de objetos especializado

    * Cambios en la API de Build y C

      * Cambios específicos del puerto

    * Otros cambios y correcciones

    * Portar a Python 2.3

    * Agradecimientos

  * Qué hay de nuevo en Python 2.2

    * Introducción

    * PEPs 252 y 253: Cambios de tipo y clase

      * Clases antiguas y nuevas

      * Descriptores

      * Herencia múltiple: la regla del diamante

      * Acceso a atributos

      * Enlaces relacionados

    * PEP 234: Iteradores

    * PEP 255: Generadores simples

    * PEP 237: Unificación de enteros largos y enteros

    * PEP 238: Cambio del operador de división

    * Cambios en Unicode

    * PEP 227: Ámbitos anidados

    * Módulos nuevos y mejorados

    * Cambios y correcciones en el intérprete

    * Otros cambios y correcciones

    * Agradecimientos

  * Qué hay de nuevo en Python 2.1

    * Introducción

    * PEP 227: Ámbitos anidados

    * PEP 236: Directivas __future__

    * PEP 207: Comparaciones Enriquecidas

    * PEP 230: Marco de advertencia

    * PEP 229: Sistema de construcción nuevo

    * PEP 205: Referencias débiles

    * PEP 232: Atributos de la función

    * PEP 235: Importación de módulos en plataformas que no distinguen
      entre mayúsculas y minúsculas

    * PEP 217: Gancho de pantalla interactivo

    * PEP 208: Nuevo modelo de coerción

    * PEP 241: Metadatos en paquetes de Python

    * Módulos nuevos y mejorados

    * Otros cambios y correcciones

    * Agradecimientos

  * Qué hay de nuevo en Python 2.0

    * Introducción

    * ¿Qué pasa con Python 1.6?

    * Nuevo proceso de desarrollo

    * Unicode

    * Comprensión de listas

    * Asignación aumentada

    * Métodos de cadena de caracteres

    * Recogida de basura de los ciclos

    * Otros cambios en el núcleo

      * Cambios menores del lenguaje

      * Cambios en las funciones incorporadas

    * Adaptación a la versión 2.0

    * Extensión/Incorporación de cambios

    * Distutils: Facilitando la instalación de módulos

    * Módulos XML

      * Soporte de SAX2

      * Soporte DOM

      * Relación con PyXML

    * Cambios en los módulos

    * Nuevos módulos

    * Mejoras en IDLE

    * Módulos eliminados y obsoletos

    * Agradecimientos

  * Registro de cambios

    * Python next

      * macOS

      * Windows

      * Tools/Demos

      * Tests

      * Security

      * Library

      * IDLE

      * Documentation

      * Core and Builtins

      * C API

      * Build

    * Python 3.14.6 final

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * C API

    * Python 3.14.5 final

      * Security

      * Core and Builtins

      * Library

      * Tests

      * macOS

    * Python 3.14.5 release candidate 1

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Build

      * Windows

      * macOS

    * Python 3.14.4 final

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * C API

    * Python 3.14.3 final

      * Windows

      * Tools/Demos

      * Tests

      * Security

      * Library

      * IDLE

      * Documentation

      * Core and Builtins

      * C API

      * Build

    * Python 3.14.2 final

      * Security

      * Library

      * Core and Builtins

      * Library

    * Python 3.14.1 final

      * Windows

      * Tools/Demos

      * Tests

      * Security

      * Library

      * IDLE

      * Documentation

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * C API

      * Build

    * Python 3.14.0 final

      * macOS

      * Windows

      * Tools/Demos

      * Security

      * Library

    * Python 3.14.0 release candidate 3

      * Windows

      * Tools/Demos

      * Security

      * Library

      * Core and Builtins

    * Python 3.14.0 release candidate 2

      * macOS

      * Windows

      * Library

      * Documentation

      * Core and Builtins

      * C API

      * Build

    * Python 3.14.0 release candidate 1

      * Tools/Demos

      * Security

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * C API

      * Build

    * Python 3.14.0 beta 4

      * Tools/Demos

      * Tests

      * Security

      * Library

      * Documentation

      * Core and Builtins

      * C API

      * Build

    * Python 3.14.0 beta 3

      * Windows

      * Tests

      * Security

      * Library

      * Documentation

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * C API

      * Build

    * Python 3.14.0 beta 2

      * Windows

      * Tools/Demos

      * Tests

      * Security

      * Library

      * Core and Builtins

      * C API

      * Build

    * Python 3.14.0 beta 1

      * Windows

      * Tools/Demos

      * Tests

      * Security

      * Library

      * IDLE

      * Documentation

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * C API

      * Build

    * Python 3.14.0 alpha 7

      * macOS

      * Windows

      * Tools/Demos

      * Tests

      * Security

      * Library

      * Documentation

      * Core and Builtins

      * Library

      * Core and Builtins

      * C API

      * Build

    * Python 3.14.0 alpha 6

      * macOS

      * Windows

      * Tools/Demos

      * Tests

      * Security

      * Library

      * Documentation

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * C API

      * Build

    * Python 3.14.0 alpha 5

      * macOS

      * Tools/Demos

      * Tests

      * Security

      * Library

      * IDLE

      * Documentation

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * C API

      * Build

    * Python 3.14.0 alpha 4

      * macOS

      * Tools/Demos

      * Tests

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * C API

      * Build

    * Python 3.14.0 alpha 3

      * Windows

      * Tools/Demos

      * Tests

      * Security

      * Library

      * Documentation

      * Core and Builtins

      * Library

      * Core and Builtins

      * C API

      * Build

    * Python 3.14.0 alpha 2

      * Windows

      * Tools/Demos

      * Tests

      * Security

      * Library

      * Documentation

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * C API

      * Build

    * Python 3.14.0 alpha 1

      * macOS

      * Windows

      * Tools/Demos

      * Tests

      * Security

      * Library

      * IDLE

      * Documentation

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * C API

      * Build

    * Python 3.13.0 beta 1

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Build

      * Windows

      * macOS

      * IDLE

      * C API

    * Python 3.13.0 alpha 6

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * C API

    * Python 3.13.0 alpha 5

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.13.0 alpha 4

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.13.0 alpha 3

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * C API

    * Python 3.13.0 alpha 2

      * Core and Builtins

      * Library

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.13.0 alpha 1

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.12.0 beta 1

      * Security

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.12.0 alpha 7

      * Core and Builtins

      * Library

      * Core and Builtins

      * Build

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * Tools/Demos

      * C API

    * Python 3.12.0 alpha 6

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * C API

    * Python 3.12.0 alpha 5

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

    * Python 3.12.0 alpha 4

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * Tools/Demos

      * C API

    * Python 3.12.0 alpha 3

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * Tools/Demos

      * C API

    * Python 3.12.0 alpha 2

      * Security

      * Core and Builtins

      * Build

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * C API

    * Python 3.12.0 alpha 1

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.11.0 beta 1

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Build

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * Tools/Demos

      * C API

    * Python 3.11.0 alpha 7

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * Tools/Demos

      * C API

    * Python 3.11.0 alpha 6

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * IDLE

      * C API

    * Python 3.11.0 alpha 5

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Build

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * C API

    * Python 3.11.0 alpha 4

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * C API

    * Python 3.11.0 alpha 3

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * C API

    * Python 3.11.0 alpha 2

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * C API

    * Python 3.11.0 alpha 1

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.10.0 beta 1

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * C API

    * Python 3.10.0 alpha 7

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * IDLE

      * C API

    * Python 3.10.0 alpha 6

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * C API

    * Python 3.10.0 alpha 5

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * C API

    * Python 3.10.0 alpha 4

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * macOS

      * Tools/Demos

      * C API

    * Python 3.10.0 alpha 3

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.10.0 alpha 2

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * C API

    * Python 3.10.0 alpha 1

      * Security

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * C API

    * Python 3.9.0 beta 1

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * Tools/Demos

      * C API

    * Python 3.9.0 alpha 6

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.9.0 alpha 5

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.9.0 alpha 4

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * IDLE

      * C API

    * Python 3.9.0 alpha 3

      * Core and Builtins

      * Library

      * Documentation

      * Build

      * IDLE

      * C API

    * Python 3.9.0 alpha 2

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * C API

    * Python 3.9.0 alpha 1

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.8.0 beta 1

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.8.0 alpha 4

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.8.0 alpha 3

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.8.0 alpha 2

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Windows

      * IDLE

    * Python 3.8.0 alpha 1

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.7.0 final

      * Library

      * C API

    * Python 3.7.0 release candidate 1

      * Core and Builtins

      * Library

      * Documentation

      * Build

      * Windows

      * IDLE

    * Python 3.7.0 beta 5

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * macOS

      * IDLE

    * Python 3.7.0 beta 4

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

    * Python 3.7.0 beta 3

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.7.0 beta 2

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

    * Python 3.7.0 beta 1

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * C API

    * Python 3.7.0 alpha 4

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Windows

      * Tools/Demos

      * C API

    * Python 3.7.0 alpha 3

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.7.0 alpha 2

      * Core and Builtins

      * Library

      * Documentation

      * Build

      * IDLE

      * C API

    * Python 3.7.0 alpha 1

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.6.6 final

    * Python 3.6.6 release candidate 1

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.6.5 final

      * Tests

      * Build

    * Python 3.6.5 release candidate 1

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.6.4 final

    * Python 3.6.4 release candidate 1

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * macOS

      * IDLE

      * Tools/Demos

      * C API

    * Python 3.6.3 final

      * Library

      * Build

    * Python 3.6.3 release candidate 1

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * IDLE

      * Tools/Demos

    * Python 3.6.2 final

    * Python 3.6.2 release candidate 2

      * Security

    * Python 3.6.2 release candidate 1

      * Security

      * Core and Builtins

      * Library

      * IDLE

      * C API

      * Build

      * Documentation

      * Tools/Demos

      * Tests

      * Windows

    * Python 3.6.1 final

      * Core and Builtins

      * Build

    * Python 3.6.1 release candidate 1

      * Core and Builtins

      * Library

      * IDLE

      * Windows

      * C API

      * Documentation

      * Tests

      * Build

    * Python 3.6.0 final

    * Python 3.6.0 release candidate 2

      * Core and Builtins

      * Tools/Demos

      * Windows

      * Build

    * Python 3.6.0 release candidate 1

      * Core and Builtins

      * Library

      * C API

      * Documentation

      * Tools/Demos

    * Python 3.6.0 beta 4

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

    * Python 3.6.0 beta 3

      * Core and Builtins

      * Library

      * Windows

      * Build

      * Tests

    * Python 3.6.0 beta 2

      * Core and Builtins

      * Library

      * Windows

      * C API

      * Build

      * Tests

    * Python 3.6.0 beta 1

      * Core and Builtins

      * Library

      * IDLE

      * C API

      * Tests

      * Build

      * Tools/Demos

      * Windows

    * Python 3.6.0 alpha 4

      * Core and Builtins

      * Library

      * IDLE

      * Tests

      * Windows

      * Build

    * Python 3.6.0 alpha 3

      * Security

      * Core and Builtins

      * Library

      * IDLE

      * C API

      * Build

      * Tools/Demos

      * Documentation

      * Tests

    * Python 3.6.0 alpha 2

      * Security

      * Core and Builtins

      * Library

      * IDLE

      * Documentation

      * Tests

      * Windows

      * Build

      * C API

      * Tools/Demos

    * Python 3.6.0 alpha 1

      * Security

      * Core and Builtins

      * Library

      * IDLE

      * Documentation

      * Tests

      * Build

      * Windows

      * Tools/Demos

      * C API

    * Python 3.5.5 final

    * Python 3.5.5 release candidate 1

      * Security

      * Core and Builtins

      * Library

    * Python 3.5.4 final

      * Library

    * Python 3.5.4 release candidate 1

      * Security

      * Core and Builtins

      * Library

      * Documentation

      * Tests

      * Build

      * Windows

      * C API

    * Python 3.5.3 final

    * Python 3.5.3 release candidate 1

      * Security

      * Core and Builtins

      * Library

      * IDLE

      * C API

      * Documentation

      * Tests

      * Tools/Demos

      * Windows

      * Build

    * Python 3.5.2 final

      * Core and Builtins

      * Tests

      * IDLE

    * Python 3.5.2 release candidate 1

      * Security

      * Core and Builtins

      * Library

      * IDLE

      * Documentation

      * Tests

      * Build

      * Windows

      * Tools/Demos

    * Python 3.5.1 final

      * Core and Builtins

      * Windows

    * Python 3.5.1 release candidate 1

      * Core and Builtins

      * Library

      * IDLE

      * Documentation

      * Tests

      * Build

      * Windows

      * Tools/Demos

    * Python 3.5.0 final

      * Build

    * Python 3.5.0 release candidate 4

      * Library

      * Build

    * Python 3.5.0 release candidate 3

      * Core and Builtins

      * Library

    * Python 3.5.0 release candidate 2

      * Core and Builtins

      * Library

    * Python 3.5.0 release candidate 1

      * Core and Builtins

      * Library

      * IDLE

      * Documentation

      * Tests

    * Python 3.5.0 beta 4

      * Core and Builtins

      * Library

      * Build

    * Python 3.5.0 beta 3

      * Core and Builtins

      * Library

      * Tests

      * Documentation

      * Build

    * Python 3.5.0 beta 2

      * Core and Builtins

      * Library

    * Python 3.5.0 beta 1

      * Core and Builtins

      * Library

      * IDLE

      * Tests

      * Documentation

      * Tools/Demos

    * Python 3.5.0 alpha 4

      * Core and Builtins

      * Library

      * Build

      * Tests

      * Tools/Demos

      * C API

    * Python 3.5.0 alpha 3

      * Core and Builtins

      * Library

      * Build

      * Tests

      * Tools/Demos

    * Python 3.5.0 alpha 2

      * Core and Builtins

      * Library

      * Build

      * C API

      * Windows

    * Python 3.5.0 alpha 1

      * Core and Builtins

      * Library

      * IDLE

      * Build

      * C API

      * Documentation

      * Tests

      * Tools/Demos

      * Windows

* El tutorial de Python

  * 1. Abriendo el apetito

  * 2. Usando el intérprete de Python

    * 2.1. Invocar el intérprete

      * 2.1.1. Paso de argumentos

      * 2.1.2. Modo interactivo

    * 2.2. El intérprete y su entorno

      * 2.2.1. Codificación del código fuente

  * 3. Una introducción informal a Python

    * 3.1. Usando Python como una calculadora

      * 3.1.1. Números

      * 3.1.2. Texto

      * 3.1.3. Listas

    * 3.2. Primeros pasos hacia la programación

  * 4. Más herramientas para control de flujo

    * 4.1. La sentencia "if"

    * 4.2. La sentencia "for"

    * 4.3. La función "range()"

    * 4.4. Las sentencias "break" y "continue"

    * 4.5. Cláusulas "else" en bucles

    * 4.6. La sentencia "pass"

    * 4.7. La sentencia "match"

    * 4.8. Definir funciones

    * 4.9. Más sobre definición de funciones

      * 4.9.1. Argumentos con valores por omisión

      * 4.9.2. Palabras claves como argumentos

      * 4.9.3. Parámetros especiales

        * 4.9.3.1. Argumentos posicionales o de palabras claves

        * 4.9.3.2. Parámetros únicamente posicionales

        * 4.9.3.3. Argumentos únicamente de palabras clave

        * 4.9.3.4. Ejemplos de Funciones

        * 4.9.3.5. Resumen

      * 4.9.4. Listas de argumentos arbitrarios

      * 4.9.5. Desempaquetando una lista de argumentos

      * 4.9.6. Expresiones lambda

      * 4.9.7. Cadenas de texto de documentación

      * 4.9.8. Anotación de funciones

    * 4.10. Intermezzo: Estilo de programación

  * 5. Estructuras de datos

    * 5.1. Más sobre listas

      * 5.1.1. Usar listas como pilas

      * 5.1.2. Usar listas como colas

      * 5.1.3. Comprensión de listas

      * 5.1.4. Listas por comprensión anidadas

    * 5.2. La instrucción "del"

    * 5.3. Tuplas y secuencias

    * 5.4. Conjuntos

    * 5.5. Diccionarios

    * 5.6. Técnicas de iteración

    * 5.7. Más acerca de condiciones

    * 5.8. Comparando secuencias y otros tipos

  * 6. Módulos

    * 6.1. Más sobre los módulos

      * 6.1.1. Ejecutar módulos como scripts

      * 6.1.2. El camino de búsqueda de los módulos

      * 6.1.3. Archivos "compilados" de Python

    * 6.2. Módulos estándar

    * 6.3. La función "dir()"

    * 6.4. Paquetes

      * 6.4.1. Importar * desde un paquete

      * 6.4.2. Referencias internas en paquetes

      * 6.4.3. Paquetes en múltiples directorios

  * 7. Entrada y salida

    * 7.1. Formateo elegante de la salida

      * 7.1.1. Formatear cadenas literales

      * 7.1.2. El método format() de cadenas

      * 7.1.3. Formateo manual de cadenas

      * 7.1.4. Viejo formateo de cadenas

    * 7.2. Leyendo y escribiendo archivos

      * 7.2.1. Métodos de los objetos Archivo

      * 7.2.2. Guardar datos estructurados con "json"

  * 8. Errores y excepciones

    * 8.1. Errores de sintaxis

    * 8.2. Excepciones

    * 8.3. Gestionando excepciones

    * 8.4. Lanzando excepciones

    * 8.5. Encadenamiento de excepciones

    * 8.6. Excepciones definidas por el usuario

    * 8.7. Definiendo acciones de limpieza

    * 8.8. Acciones predefinidas de limpieza

    * 8.9. Lanzando y gestionando múltiples excepciones no
      relacionadas

    * 8.10. Enriqueciendo excepciones con notas

  * 9. Clases

    * 9.1. Unas palabras sobre nombres y objetos

    * 9.2. Ámbitos y espacios de nombres en Python

      * 9.2.1. Ejemplo de ámbitos y espacios de nombre

    * 9.3. Un primer vistazo a las clases

      * 9.3.1. Sintaxis de definición de clases

      * 9.3.2. Objetos clase

      * 9.3.3. Objetos instancia

      * 9.3.4. Objetos método

      * 9.3.5. Variables de clase y de instancia

    * 9.4. Algunas observaciones

    * 9.5. Herencia

      * 9.5.1. Herencia múltiple

    * 9.6. Variables privadas

    * 9.7. Detalles y Cuestiones Varias

    * 9.8. Iteradores

    * 9.9. Generadores

    * 9.10. Expresiones generadoras

  * 10. Brief tour of the standard library

    * 10.1. Operating system interface

    * 10.2. File wildcards

    * 10.3. Command-line arguments

    * 10.4. Error output redirection and program termination

    * 10.5. String pattern matching

    * 10.6. Matemáticas

    * 10.7. Internet access

    * 10.8. Dates and times

    * 10.9. Data compression

    * 10.10. Performance measurement

    * 10.11. Quality control

    * 10.12. Batteries included

  * 11. Brief tour of the standard library --- part II

    * 11.1. Output formatting

    * 11.2. Plantillas

    * 11.3. Working with binary data record layouts

    * 11.4. Multi-hilos

    * 11.5. Registrando

    * 11.6. Weak references

    * 11.7. Tools for working with lists

    * 11.8. Decimal floating-point arithmetic

  * 12. Entornos virtuales y paquetes

    * 12.1. Introducción

    * 12.2. Creando entornos virtuales

    * 12.3. Manejando paquetes con pip

  * 13. ¿Y ahora qué?

  * 14. Edición de entrada interactiva y sustitución de historial

    * 14.1. Autocompletado con tab e historial de edición

    * 14.2. Alternativas al intérprete interactivo

  * 15. Floating-Point Arithmetic:  Issues and Limitations

    * 15.1. Error de Representación

  * 16. Apéndice

    * 16.1. Modo interactivo

      * 16.1.1. Manejo de errores

      * 16.1.2. Programas ejecutables de Python

      * 16.1.3. El archivo de inicio interactivo

      * 16.1.4. Los módulos de customización

* Configuración y uso de Python

  * 1. Línea de comandos y entorno

    * 1.1. Línea de comando

      * 1.1.1. Opciones de interfaz

      * 1.1.2. Opciones genéricas

      * 1.1.3. Opciones diversas

      * 1.1.4. Controlling color

    * 1.2. Variables de entorno

      * 1.2.1. Variables de modo de depuración

  * 2. Uso de Python en plataformas Unix

    * 2.1. Obteniendo e instalando la última versión de Python

      * 2.1.1. En Linux

        * 2.1.1.1. Installing IDLE

      * 2.1.2. En FreeBSD y OpenBSD

    * 2.2. Construyendo Python

    * 2.3. Rutas y archivos relacionados con Python

    * 2.4. Miscelánea

    * 2.5. OpenSSL personalizado

  * 3. Configurar Python

    * 3.1. Requisitos de compilación

      * 3.1.1. Requirements for optional modules

    * 3.2. Archivos generados

      * 3.2.1. configure script

    * 3.3. Configurar opciones

      * 3.3.1. Opciones generales

      * 3.3.2. C compiler options

      * 3.3.3. Opciones del enlazador

      * 3.3.4. Options for third-party dependencies

      * 3.3.5. Opciones de WebAssembly

      * 3.3.6. Opciones de instalación

      * 3.3.7. Opciones de desempeño

      * 3.3.8. Compilación de depuración de Python

      * 3.3.9. Opciones de depuración

      * 3.3.10. Opciones del enlazador

      * 3.3.11. Opciones de bibliotecas

      * 3.3.12. Opciones de seguridad

      * 3.3.13. Opciones macOS

      * 3.3.14. iOS Options

      * 3.3.15. Opciones de compilación cruzada

    * 3.4. Sistema de compilación Python

      * 3.4.1. Archivos principales del sistema de compilación

      * 3.4.2. Pasos principales de compilación

      * 3.4.3. Objetivos principales de Makefile

        * 3.4.3.1. make

        * 3.4.3.2. make platform

        * 3.4.3.3. make profile-opt

        * 3.4.3.4. make clean

        * 3.4.3.5. make distclean

        * 3.4.3.6. make install

        * 3.4.3.7. make test

        * 3.4.3.8. make ci

        * 3.4.3.9. make buildbottest

        * 3.4.3.10. make regen-all

      * 3.4.4. Extensiones C

    * 3.5. Banderas de compilador y vinculación

      * 3.5.1. Banderas del preprocesador

      * 3.5.2. Banderas del compilador

      * 3.5.3. Banderas de vinculación

  * 4. Uso de Python en Windows

    * 4.1. Python install manager

      * 4.1.1. Installation

      * 4.1.2. Basic use

      * 4.1.3. Command help

      * 4.1.4. Listing runtimes

      * 4.1.5. Installing runtimes

      * 4.1.6. Offline installs

      * 4.1.7. Uninstalling runtimes

      * 4.1.8. Configuration

      * 4.1.9. Shebang lines

      * 4.1.10. Advanced installation

      * 4.1.11. Administrative configuration

      * 4.1.12. Installing free-threaded binaries

      * 4.1.13. Index signatures

      * 4.1.14. Troubleshooting

    * 4.2. El paquete incrustable

      * 4.2.1. Python application

      * 4.2.2. Incrustar Python

    * 4.3. El paquete de nuget.org

      * 4.3.1. Free-threaded packages

    * 4.4. Distribuciones alternativas

    * 4.5. Supported Windows versions

    * 4.6. Removing the MAX_PATH limitation

    * 4.7. Modo UTF-8

    * 4.8. Encontrar módulos

    * 4.9. Módulos adicionales

      * 4.9.1. PyWin32

      * 4.9.2. cx_Freeze

    * 4.10. Compilar Python en Windows

    * 4.11. The full installer (deprecated)

      * 4.11.1. Pasos para la instalación

      * 4.11.2. Removing the MAX_PATH limitation

      * 4.11.3. Installing without UI

      * 4.11.4. Installing without downloading

      * 4.11.5. Modificar una instalación

      * 4.11.6. Installing free-threaded binaries

    * 4.12. Python launcher for Windows (deprecated)

      * 4.12.1. Comenzar

        * 4.12.1.1. Desde la línea de comandos

        * 4.12.1.2. Entornos virtuales

        * 4.12.1.3. Desde un script

        * 4.12.1.4. Desde asociaciones de archivos

      * 4.12.2. Shebang lines

      * 4.12.3. Argumentos en líneas shebang

      * 4.12.4. Personalización

        * 4.12.4.1. Personalización con archivos INI

        * 4.12.4.2. Personalizar las versiones de Python
          predeterminadas

      * 4.12.5. Diagnóstico

      * 4.12.6. Dry run

      * 4.12.7. Instalación bajo demanda

      * 4.12.8. Códigos de retorno

  * 5. Using Python on macOS

    * 5.1. Using Python for macOS from "python.org"

      * 5.1.1. Installation steps

      * 5.1.2. Cómo ejecutar un *script* de Python

    * 5.2. Alternative Distributions

    * 5.3. Instalación de paquetes adicionales de Python

    * 5.4. GUI Programming

    * 5.5. Advanced Topics

      * 5.5.1. Installing Free-threaded Binaries

      * 5.5.2. Installing using the command line

      * 5.5.3. Distributing Python Applications

      * 5.5.4. App Store Compliance

    * 5.6. Otros recursos

  * 6. Using Python on Android

    * 6.1. Adding Python to an Android app

    * 6.2. Building a Python package for Android

  * 7. Using Python on iOS

    * 7.1. Python at runtime on iOS

      * 7.1.1. iOS version compatibility

      * 7.1.2. Platform identification

      * 7.1.3. Standard library availability

      * 7.1.4. Binary extension modules

      * 7.1.5. Compiler stub binaries

    * 7.2. Installing Python on iOS

      * 7.2.1. Tools for building iOS apps

      * 7.2.2. Adding Python to an iOS project

      * 7.2.3. Testing a Python package

    * 7.3. App Store Compliance

      * 7.3.1. Incompatible code in the standard library

      * 7.3.2. Privacy manifests

  * 8. Editores e IDEs

    * 8.1. IDLE --- Python editor and shell

    * 8.2. Other Editors and IDEs

* Referencia del Lenguaje Python

  * 1. Introducción

    * 1.1. Implementaciones alternativas

    * 1.2. Notación

      * 1.2.1. Lexical and Syntactic definitions

  * 2. Análisis léxico

    * 2.1. Estructura de línea

      * 2.1.1. Líneas lógicas

      * 2.1.2. Líneas físicas

      * 2.1.3. Comentarios

      * 2.1.4. Declaración de Codificación

      * 2.1.5. Unión explícita de líneas

      * 2.1.6. Unión implícita de líneas

      * 2.1.7. Líneas en blanco

      * 2.1.8. Sangría

      * 2.1.9. Espacios en blanco entre tokens

      * 2.1.10. End marker

    * 2.2. Otros tokens

    * 2.3. Names (identifiers and keywords)

      * 2.3.1. Palabras clave

      * 2.3.2. Palabras clave suaves

      * 2.3.3. Clases reservadas de identificadores

      * 2.3.4. Non-ASCII characters in names

    * 2.4. Literales

    * 2.5. Literales de cadenas y bytes

      * 2.5.1. Triple-quoted strings

      * 2.5.2. String prefixes

      * 2.5.3. Formal grammar

      * 2.5.4. Secuencias de escape

        * 2.5.4.1. Ignored end of line

        * 2.5.4.2. Escaped characters

        * 2.5.4.3. Octal character

        * 2.5.4.4. Hexadecimal character

        * 2.5.4.5. Named Unicode character

        * 2.5.4.6. Hexadecimal Unicode characters

        * 2.5.4.7. Unrecognized escape sequences

      * 2.5.5. Bytes literals

      * 2.5.6. Raw string literals

      * 2.5.7. f-strings

      * 2.5.8. t-strings

      * 2.5.9. Formal grammar for f-strings

    * 2.6. Literales numéricos

      * 2.6.1. Literales enteros

      * 2.6.2. Literales de punto flotante

      * 2.6.3. Literales imaginarios

    * 2.7. Operators and delimiters

  * 3. Modelo de datos

    * 3.1. Objetos, valores y tipos

    * 3.2. Jerarquía de tipos estándar

      * 3.2.1. None

      * 3.2.2. NotImplemented

      * 3.2.3. Elipsis

      * 3.2.4. "numbers.Number"

        * 3.2.4.1. "numbers.Integral"

        * 3.2.4.2. "numbers.Real" ("float")

        * 3.2.4.3. "numbers.Complex" ("complex")

      * 3.2.5. Secuencias

        * 3.2.5.1. Secuencias inmutables

        * 3.2.5.2. Secuencias mutables

      * 3.2.6. Tipos de conjuntos

      * 3.2.7. Mapeos

        * 3.2.7.1. Diccionarios

      * 3.2.8. Tipos invocables

        * 3.2.8.1. Funciones definidas por el usuario

          * 3.2.8.1.1. Atributos especiales de solo lectura

          * 3.2.8.1.2. Atributos especiales de escritura

        * 3.2.8.2. Métodos de instancia

        * 3.2.8.3. Funciones generadoras

        * 3.2.8.4. Funciones de corrutina

        * 3.2.8.5. Funciones generadoras asincrónicas

        * 3.2.8.6. Funciones incorporadas

        * 3.2.8.7. Métodos incorporados

        * 3.2.8.8. Clases

        * 3.2.8.9. Instancias de clases

      * 3.2.9. Módulos

        * 3.2.9.1. Import-related attributes on module objects

        * 3.2.9.2. Other writable attributes on module objects

        * 3.2.9.3. Module dictionaries

      * 3.2.10. Clases personalizadas

        * 3.2.10.1. Atributos especiales

        * 3.2.10.2. Métodos especiales

      * 3.2.11. Instancias de clase

        * 3.2.11.1. Atributos especiales

      * 3.2.12. Objetos E/S (también conocidos como objetos de
        archivo)

      * 3.2.13. Tipos internos

        * 3.2.13.1. Objetos de código

          * 3.2.13.1.1. Atributos especiales de solo lectura

          * 3.2.13.1.2. Métodos en objetos de código

        * 3.2.13.2. Objetos de marco

          * 3.2.13.2.1. Atributos especiales de solo lectura

          * 3.2.13.2.2. Atributos especiales de escritura

          * 3.2.13.2.3. Métodos de objeto de marco

        * 3.2.13.3. Objetos de seguimiento de pila (traceback)

        * 3.2.13.4. Objetos de segmento (Slice objects)

        * 3.2.13.5. Objetos de método estático

        * 3.2.13.6. Objetos de método de clase

    * 3.3. Nombres especiales de método

      * 3.3.1. Personalización básica

      * 3.3.2. Personalizando acceso a atributos

        * 3.3.2.1. Personalizando acceso a atributos de módulo

        * 3.3.2.2. Implementando descriptores

        * 3.3.2.3. Invocando descriptores

        * 3.3.2.4. __slots__

      * 3.3.3. Personalización de creación de clases

        * 3.3.3.1. Metaclases

        * 3.3.3.2. Resolviendo entradas de la Orden de Resolución de
          Métodos (MRU)

        * 3.3.3.3. Determinando la metaclase adecuada

        * 3.3.3.4. Preparando el espacio de nombres de la clase

        * 3.3.3.5. Ejecutando el cuerpo de la clase

        * 3.3.3.6. Creando el objeto de clase

        * 3.3.3.7. Usos para metaclases

      * 3.3.4. Personalizando revisiones de instancia y subclase

      * 3.3.5. Emulando tipos genéricos

        * 3.3.5.1. El propósito de *__class_getitem__*

        * 3.3.5.2. *__class_getitem__* frente a *__getitem__*

      * 3.3.6. Emulando objetos que se pueden llamar

      * 3.3.7. Emulando tipos de contenedores

      * 3.3.8. Emulando tipos numéricos

      * 3.3.9. Gestores de Contexto en la Declaración *with*

      * 3.3.10. Personalización de argumentos posicionales en la
        coincidencia de patrones de clase

      * 3.3.11. Emulando tipos de búfer

      * 3.3.12. Annotations

      * 3.3.13. Búsqueda de método especial

    * 3.4. Corrutinas

      * 3.4.1. Objetos esperables

      * 3.4.2. Objetos de corrutina

      * 3.4.3. Iteradores asíncronos

      * 3.4.4. Gestores de contexto asíncronos

  * 4. Modelo de ejecución

    * 4.1. Estructura de un programa

    * 4.2. Nombres y vínculos

      * 4.2.1. Vinculación de nombres

      * 4.2.2. Resolución de nombres

      * 4.2.3. Ámbitos de anotación

      * 4.2.4. Evaluación perezosa

      * 4.2.5. Integraciones y ejecución restringida

      * 4.2.6. Interacción con funcionalidades dinámicas

    * 4.3. Excepciones

    * 4.4. Runtime Components

      * 4.4.1. General Computing Model

      * 4.4.2. Python Runtime Model

  * 5. El sistema de importación

    * 5.1. "importlib"

    * 5.2. Paquetes

      * 5.2.1. Paquetes regulares

      * 5.2.2. Paquetes de espacio de nombres

    * 5.3. Buscando

      * 5.3.1. La caché del módulo

      * 5.3.2. Buscadores y cargadores

      * 5.3.3. Ganchos de importación

      * 5.3.4. La meta ruta (*path*)

    * 5.4. Cargando

      * 5.4.1. Cargadores

      * 5.4.2. Submódulos

      * 5.4.3. Module specs

      * 5.4.4. __path__ attributes on modules

      * 5.4.5. Representación (*Reprs*) de módulos

      * 5.4.6. Invalidación del código de bytes en caché

    * 5.5. El buscador basado en rutas

      * 5.5.1. Buscadores de entradas de ruta

      * 5.5.2. Buscadores de entradas de ruta

    * 5.6. Reemplazando el sistema de importación estándar

    * 5.7. Paquete Importaciones relativas

    * 5.8. Consideraciones especiales para __main__

      * 5.8.1. __main__.__spec__

    * 5.9. Referencias

  * 6. Expresiones

    * 6.1. Conversiones aritméticas

    * 6.2. Átomos

      * 6.2.1. Built-in constants

      * 6.2.2. Identificadores (Nombres)

        * 6.2.2.1. Alteración de nombre privado

      * 6.2.3. Literales

        * 6.2.3.1. Literals and object identity

        * 6.2.3.2. String literal concatenation

      * 6.2.4. Formas entre paréntesis

      * 6.2.5. Despliegues para listas, conjuntos y diccionarios

      * 6.2.6. Despliegues de lista

      * 6.2.7. Despliegues de conjuntos

      * 6.2.8. Despliegues de diccionario

      * 6.2.9. Expresiones de generador

      * 6.2.10. Expresiones *yield*

        * 6.2.10.1. Métodos generador-iterador

        * 6.2.10.2. Ejemplos

        * 6.2.10.3. Funciones generadoras asincrónicas

        * 6.2.10.4. Métodos asincrónicos de generador-iterador

    * 6.3. Primarios

      * 6.3.1. Referencias de atributos

      * 6.3.2. Subscriptions and slicings

        * 6.3.2.1. Segmentos

        * 6.3.2.2. Comma-separated subscripts

        * 6.3.2.3. "Starred" subscriptions

        * 6.3.2.4. Formal subscription grammar

      * 6.3.3. Invocaciones

    * 6.4. Expresión await

    * 6.5. El operador de potencia

    * 6.6. Aritmética unaria y operaciones bit a bit

    * 6.7. Operaciones aritméticas binarias

    * 6.8. Operaciones de desplazamiento

    * 6.9. Operaciones bit a bit binarias

    * 6.10. Comparaciones

      * 6.10.1. Comparaciones de valor

      * 6.10.2. Operaciones de prueba de membresía

      * 6.10.3. Comparaciones de identidad

    * 6.11. Operaciones booleanas

    * 6.12. Expresiones de asignación

    * 6.13. Expresiones condicionales

    * 6.14. Lambdas

    * 6.15. Listas de expresiones

    * 6.16. Orden de evaluación

    * 6.17. Prioridad de operador

  * 7. Declaraciones simples

    * 7.1. Declaraciones de tipo expresión

    * 7.2. Declaraciones de asignación

      * 7.2.1. Declaraciones de asignación aumentada

      * 7.2.2. Declaraciones de asignación anotadas

    * 7.3. La declaración "assert"

    * 7.4. La declaración "pass"

    * 7.5. La declaración "del"

    * 7.6. La declaración "return"

    * 7.7. La declaración "yield"

    * 7.8. La declaración "raise"

    * 7.9. La declaración "break"

    * 7.10. La declaración "continue"

    * 7.11. La declaración "import"

      * 7.11.1. Declaraciones Futuras

    * 7.12. La declaración "global"

    * 7.13. La declaración "nonlocal"

    * 7.14. The "type" statement

  * 8. Sentencias compuestas

    * 8.1. La sentencia "if"

    * 8.2. La sentencia "while"

    * 8.3. La sentencia "for"

    * 8.4. La sentencia "try"

      * 8.4.1. Cláusula "except"

      * 8.4.2. Cláusula "except*"

      * 8.4.3. La sentencia "else"

      * 8.4.4. Cláusula "finally"

    * 8.5. La sentencia "with"

    * 8.6. La sentencia "match"

      * 8.6.1. Resumen

      * 8.6.2. Protecciones

      * 8.6.3. Bloques de Casos Irrefutables

      * 8.6.4. Patrones

        * 8.6.4.1. Patrones OR

        * 8.6.4.2. patrones AS

        * 8.6.4.3. Patrones literales

        * 8.6.4.4. Patrones de captura

        * 8.6.4.5. Patrones comodín

        * 8.6.4.6. Patrones de valor

        * 8.6.4.7. Patrones de grupo

        * 8.6.4.8. Patrones de secuencia

        * 8.6.4.9. Patrones de mapeo

        * 8.6.4.10. Patrones de clase

    * 8.7. Definiciones de funciones

    * 8.8. Definiciones de clase

    * 8.9. Corrutinas

      * 8.9.1. Definición de la función corrutina

      * 8.9.2. La sentencia "async for"

      * 8.9.3. La sentencia "async with"

    * 8.10. Listas de tipo parámetro

      * 8.10.1. Funciones genéricas

      * 8.10.2. Clases genéricas

      * 8.10.3. Alias de tipo genérico

    * 8.11. Annotations

  * 9. Componentes de nivel superior

    * 9.1. Programas completos de Python

    * 9.2. Entrada de archivo

    * 9.3. Entrada interactiva

    * 9.4. Entrada de expresión

  * 10. Especificación completa de la gramática

* La biblioteca estándar de Python

  * Introducción

    * Notas sobre la disponibilidad

      * Plataformas WebAssembly

      * Mobile platforms

  * Funciones incorporadas

  * Constantes incorporadas

    * Constantes agregadas por el módulo "site"

  * Tipos integrados

    * Evaluar como valor verdadero/falso

    * Operaciones booleanas --- "and", "or", "not"

    * Comparaciones

    * Tipos numéricos --- "int", "float", "complex"

      * Operaciones de bits en números enteros

      * Métodos adicionales de los enteros

      * Métodos adicionales de float

      * Additional Methods on Complex

      * Calculo del *hash* de tipos numéricos

    * Tipo Booleano --- "bool"

    * Tipos de iteradores

      * Tipos generador

    * Tipos secuencia --- "list", "tuple", "range"

      * Operaciones comunes de las secuencias

      * Tipos de secuencia inmutables

      * Tipos de secuencia mutables

      * Listas

      * Tuplas

      * Rangos

    * Text and Binary Sequence Type Methods Summary

    * Cadenas de caracteres --- "str"

      * Métodos de las cadenas de caracteres

      * Formatted String Literals (f-strings)

        * Debug specifier

        * Conversion specifier

        * Format specifier

      * Template String Literals (t-strings)

      * Formateo de cadenas al estilo "*printf*"

    * Tipos de secuencias binarias --- "bytes", "bytearray" y
      "memoryview"

      * Objetos de tipo Bytes

      * Objetos de tipo *Bytearray*

      * Operaciones de *bytes* y *bytearray*

      * Usando el formateo tipo "printf" con bytes

      * Vistas de memoria

    * Conjuntos --- "set", "frozenset"

    * Tipos mapa --- "dict"

      * Objetos tipos vista de diccionario

    * Tipos gestores de contexto

    * Tipos de anotaciones de type — *alias genérico*, *Union*

      * Tipo Alias Genérico

        * Clases genéricas estándar

        * Atributos especiales de los objetos "GenericAlias"

      * Tipo de conversión

    * Otros tipos predefinidos

      * Módulos

      * Clases e instancias de clase

      * Funciones

      * Métodos

      * Objetos código

      * Objetos Tipo

      * El objeto nulo (*Null*)

      * El objeto puntos suspensivos (*Ellipsis*)

      * El objeto *NotImplemented*

      * Objetos internos

    * Atributos especiales

    * Limitación de longitud de conversión de cadena de tipo entero

      * APIs afectadas

      * Configuración del límite

      * Configuración recomendada

  * Excepciones incorporadas

    * Contexto de una excepción

    * Heredando de excepciones incorporadas

    * Clases base

    * Excepciones específicas

      * Excepciones del sistema operativo

    * Advertencias

    * Grupos de excepciones

    * Jerarquía de excepción

  * Thread Safety Guarantees

    * Thread safety levels

      * Incompatible

      * Compatible

      * Safe on distinct objects

      * Safe on shared objects

      * Atomic

    * Thread safety for list objects

    * Thread safety for dict objects

    * Thread safety for set objects

    * Thread safety for bytearray objects

    * Thread safety for memoryview objects

  * Servicios de procesamiento de texto

    * "string" --- Common string operations

      * Constantes de cadenas

      * Custom string formatting

      * Format string syntax

        * Format specification mini-language

        * Ejemplos de formateo

      * Template strings ($-strings)

      * Funciones de ayuda

    * "string.templatelib" --- Support for template string literals

      * Template strings

      * Types

      * Helper functions

    * "re" --- Regular expression operations

      * Sintaxis de expresiones regulares

      * Contenidos del módulo

        * Indicadores

        * Funciones

        * Excepciones

      * Objetos expresión regular

      * Objetos de coincidencia

      * Ejemplos de expresiones regulares

        * Buscando un par

        * Simular scanf()

        * search() vs. match()

        * Haciendo una guía telefónica

        * Mungear texto

        * Encontrar todos los adverbios

        * Encontrar todos los adverbios y sus posiciones

        * Notación de cadena *raw*

        * Escribir un Tokenizador

    * "difflib" --- Helpers for computing deltas

      * Junk heuristic

      * The "difflib" algorithm

      * Diff generation

      * Junk definition functions

      * SequenceMatcher objects

      * Examples

        * SequenceMatcher examples

        * Differ example

        * Una interfaz de línea de comandos para "difflib"

        * ndiff example

    * "textwrap" --- Text wrapping and filling

    * "unicodedata" --- Unicode Database

    * "stringprep" --- Internet String Preparation

    * "readline" --- GNU readline interface

      * Archivo de inicio

      * Búfer de línea

      * Archivo de historial

      * Lista del historial

      * Ganchos (*hooks*) de inicialización

      * Terminación

      * Ejemplo

    * "rlcompleter" --- Completion function for GNU readline

  * Servicios de datos binarios

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

  * Tipos de datos

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

    * "graphlib" --- Functionality to operate with graph-like
      structures

      * Excepciones

  * Módulos numéricos y matemáticos

    * "numbers" --- Numeric abstract base classes

      * La torre numérica

      * Notes for type implementers

        * Agregar más *ABCs* numéricos

        * Implementar operaciones aritméticas

    * "math" --- Mathematical functions

      * Number-theoretic functions

      * Floating point arithmetic

      * Floating point manipulation functions

      * Power, exponential and logarithmic functions

      * Summation and product functions

      * Conversión angular

      * Funciones trigonométricas

      * Funciones hiperbólicas

      * Funciones especiales

      * Constantes

    * "cmath" --- Mathematical functions for complex numbers

      * Conversión a y desde coordenadas polares

      * Funciones logarítmicas y de potencias

      * Funciones trigonométricas

      * Funciones hiperbólicas

      * Funciones de clasificación

      * Constantes

    * "decimal" --- Decimal fixed-point and floating-point arithmetic

      * Quick-start tutorial

      * Objetos Decimal

        * Operandos lógicos

      * Objetos context

      * Constantes

      * Modos de redondeo

      * Señales

      * Floating-point notes

        * Mitigación del error de redondeo usando mayor precisión

        * Valores especiales

      * Trabajando con hilos

      * Casos prácticos

      * Preguntas frecuentes sobre decimal

    * "fractions" --- Rational numbers

    * "random" --- Generate pseudo-random numbers

      * Funciones de contabilidad

      * Funciones para los bytes

      * Funciones para enteros

      * Funciones para secuencias

      * Discrete distributions

      * Distribuciones para los nombres reales

      * Generador alternativo

      * Notas sobre la Reproducibilidad

      * Ejemplos

      * Recetas

      * Command-line usage

      * Command-line example

    * "statistics" --- Mathematical statistics functions

      * Promedios y medidas de tendencia central

      * Medidas de dispersión

      * Estadísticas para relaciones entre dos entradas

      * Detalles de las funciones

      * Excepciones

      * Objetos "NormalDist"

      * Examples and Recipes

        * Problemas de probabilidad clásicos

        * Entradas de Monte Carlo para simulaciones

        * Aproximación de la distribución binomial

        * Clasificador bayesiano ingenuo

  * Módulos de programación funcional

    * "itertools" --- Functions creating iterators for efficient
      looping

      * Itertool Functions

      * Fórmulas con itertools

    * "functools" --- Higher-order functions and operations on
      callable objects

      * "partial" Objetos

    * "operator" --- Standard operators as functions

      * Asignación de operadores a funciones

      * Operadores *In-place*

  * Acceso a archivos y directorios

    * "pathlib" --- Rutas de sistemas orientada a objetos

      * Uso básico

      * Excepciones

      * Rutas puras

        * Propiedades generales

        * Operadores

        * Acceso a partes individuales

        * Métodos y propiedades

      * Rutas concretas

        * Análisis y generación de URI

        * Ampliando y resolviendo caminos

        * Consulta de tipo de archivo y estado

        * Lectura y escritura de archivos

        * Directorios de lectura

        * Creando archivos y directorios

        * Copying, moving and deleting

        * Permisos y propiedad

      * Lenguaje de patrones

      * Comparación con el módulo "glob"

      * Comparación con los módulos "os" y "os.path"

        * Herramientas correspondientes

      * Protocols

    * "os.path" --- Common pathname manipulations

    * "stat" --- Interpreting "stat()" results

    * "filecmp" --- File and Directory Comparisons

      * La clase "dircmp"

    * "tempfile" --- Generate temporary files and directories

      * Ejemplos

      * Funciones y variables deprecadas

    * "glob" --- Unix style pathname pattern expansion

      * Examples

    * "fnmatch" --- Unix filename pattern matching

    * "linecache" --- Random access to text lines

    * "shutil" --- High-level file operations

      * Operaciones de directorios y archivos

        * Operaciones de copia eficientes dependientes de la
          plataforma

        * ejemplo de *copytree*

        * ejemplo de rmtree

      * Operaciones de archivado

        * Ejemplo de archivado

        * Ejemplo de archivado con *base_dir*

      * Consulta el tamaño de la terminal de salida

  * Persistencia de datos

    * "pickle" --- Python object serialization

      * Relación con otros módulos de Python

        * Comparación con "marshal"

        * Comparación con "json"

      * Formato de flujo de datos

      * Interfaz del módulo

      * ¿Qué se puede serializar (pickled) y deserializar (unpickled)
        con *pickle*?

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

        * Cómo adaptar tipos de Python personalizados a valores de
          SQLite

          * Cómo escribir objetos adaptables

          * Como registrar un adaptador invocable

        * Como convertir valores SQLite a tipos de Python
          personalizados

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

  * Compresión de datos y archivado

    * The "compression" package

    * "compression.zstd" --- Compression compatible with the Zstandard
      format

      * Exceptions

      * Reading and writing compressed files

      * Compressing and decompressing data in memory

      * Zstandard dictionaries

      * Advanced parameter control

      * Miscellaneous

      * Examples

    * "zlib" --- Compression compatible with **gzip**

    * "gzip" --- Support for **gzip** files

      * Ejemplos de uso

      * Command-line interface

        * Command-line options

    * "bz2" --- Support for **bzip2** compression

      * (De)compresión de archivos

      * (De)compresión incremental

      * (Des)comprimir en un solo paso

      * Ejemplos de uso

    * "lzma" --- Compression using the LZMA algorithm

      * Leyendo y escribiendo ficheros comprimidos

      * Comprimiendo y descomprimiendo datos en memoria

      * Misceláneas

      * Especificando cadenas de filtro personalizadas

      * Constants

      * Ejemplos

    * "zipfile" --- Work with ZIP archives

      * ZipFile objects

      * Path objects

      * PyZipFile objects

      * ZipInfo objects

      * Command-line interface

        * Opciones de línea de comando

      * Problemas de descompresión

        * Del archivo mismo

        * File system limitations

        * Limitaciones de recursos

        * Interrupción

        * Comportamientos predeterminados de extracción

    * "tarfile" --- Read and write tar archive files

      * Objetos *TarFile*

      * Objetos TarInfo

      * Extraction filters

        * Default named filters

        * Filter errors

        * Hints for further verification

        * Supporting older Python versions

        * Stateful extraction filter example

      * Interfaz de línea de comandos

        * Opciones de línea de comandos

      * Ejemplos

        * Reading examples

        * Writing examples

      * Formatos tar con soporte

      * Problemas unicode

  * Formatos de archivo

    * "csv" --- CSV File Reading and Writing

      * Contenidos del módulo

      * Dialectos y parámetros de formato

      * Objetos *Reader*

      * Objetos *Writer*

      * Ejemplos

    * "configparser" --- Configuration file parser

      * Inicio Rápido

      * Tipos de Datos Soportados

      * Valores de contingencia

      * Estructura soportada para el archivo ini

      * Unnamed Sections

      * Interpolación de valores

      * Acceso por protocolo de mapeo

      * Personalizando el comportamiento del parser

      * Ejemplos de la API heredada

      * Objetos ConfigParser

      * Objetos RawConfigParser

      * Excepciones

    * "tomllib" --- Parse TOML files

      * Ejemplos

      * Tabla de conversión

    * "netrc" --- netrc file processing

      * Objetos netrc

    * "plistlib" --- Generate and parse Apple ".plist" files

      * Ejemplos

  * Servicios criptográficos

    * "hashlib" --- Secure hashes and message digests

      * Algoritmos de hash

      * Usage

      * Constructors

      * Attributes

      * Hash Objects

      * Resúmenes SHAKE de largo variable

      * Cifrado de archivos

      * Derivación de clave

      * BLAKE2

        * Creando objetos hash

        * Constantes

        * Ejemplos

          * Cifrado simple

          * Usar diferentes tamaños de resumen

          * Cifrado de clave

          * Cifrado aleatorio

          * Personalización

          * Modo de árbol

        * Créditos

    * "hmac" --- Keyed-Hashing for Message Authentication

    * "secrets" --- Generate secure random numbers for managing
      secrets

      * Números aleatorios

      * Generando tokens

        * ¿Cuántos bytes deben tener los tokens?

      * Otras funciones

      * Recetas y mejores prácticas

  * Servicios genéricos del sistema operativo

    * "os" --- Interfaces misceláneas del sistema operativo

      * Nombres de archivos, argumentos de la línea de comandos y
        variables de entorno

      * Modo Python UTF-8

      * Parámetros de proceso

      * Creación de objetos de tipo archivo

      * Operaciones de descriptores de archivos

        * Consultando las dimensiones de una terminal

        * Herencia de los descriptores de archivos

      * Archivos y directorios

        * Descriptores de archivos del temporizador

        * Atributos extendidos de Linux

      * Gestión de proceso

      * Interfaz al planificador

      * Información miscelánea del sistema

      * Números al azar

    * "io" --- Core tools for working with streams

      * Resumen

        * E/S Texto

        * E/S Binaria

        * E/S sin formato

      * Codificación de texto

        * EncodingWarning opcional

      * Interfaz de módulo de alto nivel

      * Jerarquía de clases

        * Clases base E/S

        * Archivo sin formato E/S

        * *Streams* almacenados (búfer)

        * E/S Texto

      * Static Typing

      * Rendimiento

        * E/S Binaria

        * E/S Texto

        * Multihilo

        * Reentrada

    * "time" --- Time access and conversions

      * Las Funciones

      * Constantes de ID de reloj

      * Constantes de zona horaria

    * "logging" --- Logging facility for Python

      * Objetos logger

      * Niveles de logging

      * Gestor de objetos

      * Objetos formateadores

      * Filtro de Objetos

      * Objetos LogRecord

      * Atributos LogRecord

      * Objetos LoggerAdapter

      * Seguridad del hilo

      * Funciones a nivel de módulo

      * Atributos a nivel de módulo

      * Integración con el módulo de advertencias

    * "logging.config" --- Logging configuration

      * Funciones de configuración

      * Consideraciones de seguridad

      * Esquema del diccionario de configuración

        * Detalles del esquema del diccionario

        * Configuración incremental

        * Conexiones de objeto

        * Objetos definidos por el usuario

        * Handler configuration order

        * Acceso a objetos externos

        * Acceso a objetos internos

        * Resolución de importación e importadores personalizados

        * Configuring QueueHandler and QueueListener

      * Formato de archivo de configuración

    * "logging.handlers" --- Logging handlers

      * StreamHandler

      * FileHandler

      * NullHandler

      * WatchedFileHandler

      * BaseRotatingHandler

      * RotatingFileHandler

      * TimedRotatingFileHandler

      * SocketHandler

      * DatagramHandler

      * Gestor *SysLog* (*SysLogHandler*)

      * Gestor de eventos *NTELog* (NTEventLogHandler)

      * SMTPHandler

      * MemoryHandler

      * HTTPHandler

      * QueueHandler

      * QueueListener

    * "platform" ---  Access to underlying platform's identifying data

      * Cross platform

      * Java platform

      * Windows platform

      * macOS platform

      * iOS platform

      * Unix platforms

      * Linux platforms

      * Android platform

      * Command-line usage

    * "errno" --- Standard errno system symbols

    * "ctypes" --- A foreign function library for Python

      * tutorial de ctypes

        * Carga de bibliotecas de enlaces dinámicos

        * Acceder a las funciones de los dll cargados

        * Funciones de llamada

        * Tipos de datos fundamentales

        * Funciones de llamada, continuación

        * Calling variadic functions

        * Funciones de llamada con sus propios tipos de datos
          personalizados

        * Especificar los tipos de argumentos requeridos (prototipos
          de funciones)

        * Tipos de retorno

        * Pasar los punteros (o: pasar los parámetros por referencia)

        * Estructuras y uniones

        * Structure/union layout, alignment and byte order

        * Campos de bits en estructuras y uniones

        * Arreglos

        * Punteros

        * Thread safety without the GIL

        * Conversiones de tipos

        * Tipos incompletos

        * Funciones de retrollamadas (*callback*)

        * Acceder a los valores exportados de los dlls

        * Sorpresas

        * Tipos de datos de tamaño variable

      * referencia ctypes

        * Encontrar bibliotecas compartidas

        * Listing loaded shared libraries

        * Cargando bibliotecas compartidas

        * Funciones foráneas

        * Prototipos de funciones

        * Funciones de utilidad

        * Tipos de datos

        * Tipos de datos fundamentales

        * Tipos de datos estructurados

        * Arreglos y punteros

        * Exceptions

  * Command-line interface libraries

    * "argparse" --- Parser for command-line options, arguments and
      subcommands

      * Objetos *ArgumentParser*

        * *prog*

        * uso

        * *description*

        * *epilog*

        * *parents*

        * *formatter_class*

        * *prefix_chars*

        * *fromfile_prefix_chars*

        * *argument_default*

        * *allow_abbrev*

        * *conflict_handler*

        * *add_help*

        * exit_on_error

        * suggest_on_error

        * color

      * El método *add_argument()*

        * *name or flags*

        * *action*

        * *nargs*

        * *const*

        * *default*

        * *type*

        * *choices*

        * *required*

        * *help*

        * *metavar*

        * *dest*

        * deprecated

        * Las clases *Action*

      * El método *parse_args()*

        * Sintaxis del valor de la opción

        * Argumentos no válidos

        * Argumentos conteniendo "-"

        * Abreviaturas de los argumentos (coincidencia de prefijos)

        * Más allá de "sys.argv"

        * El objeto *Namespace*

      * Otras utilidades

        * Subcommands

        * Objetos *FileType*

        * Grupos de argumentos

        * Exclusión mutua

        * Valores por defecto del analizador

        * Mostrando la ayuda

        * Análisis parcial

        * Personalizando el análisis de archivos

        * Métodos de salida

        * Análisis entremezclado

        * Registering custom types or actions

      * Excepciones

        * Tutorial de *argparse*

          * Conceptos

          * Las bases

          * Introducción a los argumentos posicionales

          * Introducción a los argumentos opcionales

            * Opciones cortas

          * Combinar argumentos opcionales y posicionales

          * Un poco mas avanzado

            * Especificando argumentos ambiguos

            * Opciones conflictivas

          * Cómo traducir la salida de argparse

          * Custom type converters

          * Conclusión

        * Migrating "optparse" code to "argparse"

    * "optparse" --- Parser for command line options

      * Choosing an argument parsing library

      * Introduction

      * Contexto

        * Terminología

        * ¿Qué finalidad tienen las opciones?

        * ¿Qué finalidad tienen los argumentos posicionales?

      * Tutorial

        * Comprendiendo las acciones de opción

        * La acción store

        * Manejo de opciones booleanas (flags)

        * Otras acciones

        * Valores por defecto

        * Generando ayuda

          * Agrupando opciones

        * Imprimir una cadena de caracteres con la versión del
          programa

        * How "optparse" handles errors

        * Reuniendo todas las piezas

      * Guía de referencia

        * Creando el analizador sintáctico (parser)

        * Completando el analizador con opciones

        * Definiendo las opciones

        * Atributos de opción

        * Acciones de opción estándares

        * Tipos de opción estándares

        * Analizando los argumentos

        * Consultar y manipular el analizador de opciones

        * Conflictos entre opciones

        * Limpieza

        * Otros métodos

      * Retrollamadas de opción

        * Definición de una opción con retrollamada

        * Cómo son invocadas las retrollamadas

        * Lanzando errores en una retrollamada

        * Ejemplo de retrollamada 1: una retrollamada trivial

        * Ejemplo de retrollamada 2: comprobar el orden de las
          opciones

        * Ejemplo de retrollamada 3: comprobar el orden de las
          opciones (generalizado)

        * Ejemplo de retrollamada 4: comprobar una condición
          arbitraria

        * Ejemplo de retrollamada 5: argumentos fijos

        * Ejemplo de retrollamada 6: argumentos variables

      * Extending "optparse"

        * Agregando nuevos tipos

        * Agregando nuevas acciones

      * Excepciones

    * "getpass" --- Portable password input

    * "fileinput" --- Iterate over lines from multiple input streams

    * "curses" --- Terminal handling for character-cell displays

      * Funciones

      * Window objects

      * Constantes

    * "curses.textpad" --- Text input widget for curses programs

      * Objeto de caja de texto

    * "curses.ascii" --- Utilities for ASCII characters

    * "curses.panel" --- A panel stack extension for curses

      * Funciones

      * Panel objects

    * "cmd" --- Support for line-oriented command interpreters

      * Objetos Cmd

      * Ejemplo Cmd

  * Ejecución concurrente

    * "threading" --- Thread-based parallelism

      * Introduction

      * GIL and performance considerations

      * Reference

        * Thread-local data

        * Thread objects

        * Lock objects

        * RLock objects

        * Condition objects

        * Semaphore objects

        * "Semaphore" example

        * Event objects

        * Timer objects

        * Barrier objects

      * Uso de *locks*, condiciones y semáforos en la declaración
        "with"

    * "multiprocessing" --- Process-based parallelism

      * Introducción

        * La clase "Process"

        * Contextos y métodos de inicio

        * Intercambiando objetos entre procesos

        * Sincronización entre procesos

        * Compartiendo estado entre procesos

        * Usando una piscina de trabajadores (*pool of workers*)

      * Referencia

        * Global start method

        * "Process" y excepciones

        * Tuberías (*Pipes*) y Colas (*Queues*)

        * Miscelánea

        * Objetos de conexión *Connection Objects*

        * Primitivas de sincronización (*Synchronization primitives*)

        * Objetos compartidos "ctypes"

          * The "multiprocessing.sharedctypes" module

        * Administradores (*Managers*)

          * Administradores customizables (*Customized managers*)

          * Utilizando un administrador remoto

        * Objetos Proxy (*Proxy Objects*)

          * Limpieza (*Cleanup*)

        * Piscinas de procesos (*Process Pools*)

        * Oyentes y clientes (*Listeners and Clients*)

          * Formatos de dirección (*Address formats*)

        * Llaves de autentificación

        * *Logging*

        * The "multiprocessing.dummy" module

      * Pautas de programación

        * Todos los métodos de inicio

        * Los métodos de inicio *spawn* y *forkserver*

      * Ejemplos

    * "multiprocessing.shared_memory" --- Shared memory for direct
      access across processes

    * El paquete "concurrent"

    * "concurrent.futures" --- Launching parallel tasks

      * Objetos ejecutores

      * ThreadPoolExecutor

        * Ejemplo de ThreadPoolExecutor

      * InterpreterPoolExecutor

      * ProcessPoolExecutor

        * Ejemplo de *ProcessPoolExecutor*

      * Objetos futuro

      * Funciones del módulo

      * Clases de Excepciones

    * "concurrent.interpreters" --- Multiple interpreters in the same
      process

      * Key details

      * Introduction

        * Multiple Interpreters and Isolation

        * Running in an Interpreter

        * Concurrency and Parallelism

        * Communication Between Interpreters

        * "Sharing" Objects

      * Reference

        * Interpreter objects

        * Exceptions

        * Communicating Between Interpreters

      * Basic usage

    * "subprocess" --- Subprocess management

      * Using the "subprocess" Module

        * Argumentos frecuentemente empleados

        * El constructor de Popen

        * Excepciones

      * Consideraciones sobre seguridad

      * Objetos Popen

      * Elementos auxiliares de Popen en Windows

        * Constantes de Windows

      * Antigua API de alto nivel

      * Replacing Older Functions with the "subprocess" Module

        * Cómo reemplazar la sustitución de órdenes de **/bin/sh**

        * Cómo remplazar los flujos de la shell

        * Cómo reemplazar "os.system()"

        * Cómo reemplazar la familia "os.spawn"

        * Replacing "os.popen()"

      * Funciones de llamada a la shell de retrocompatibilidad

      * Notas

        * Timeout Behavior

        * Cómo convertir una secuencia de argumentos a una cadena en
          Windows

        * Disable use of "posix_spawn()"

    * "sched" --- Event scheduler

      * Objetos de "Scheduler"

    * "queue" --- A synchronized queue class

      * Objetos de la cola

        * Waiting for task completion

        * Terminating queues

      * Objetos de cola simple

    * "contextvars" --- Context Variables

      * variables de contexto

      * Gestión de contexto manual

      * Soporte asyncio

    * "_thread" --- Low-level threading API

  * Comunicación en redes y entre procesos

    * "asyncio" --- Asynchronous I/O

      * Runners

        * Ejecutando un programa asyncio

        * Gestor de contexto del runner

        * Manejando interrupciones de teclado

      * Coroutines and tasks

        * Corrutinas

        * Esperables

        * Creating tasks

        * Task cancellation

        * Task groups

          * Terminating a task group

        * Durmiendo

        * Running tasks concurrently

        * Eager task factory

        * Shielding from cancellation

        * Tiempo agotado

        * Waiting primitives

        * Running in threads

        * Scheduling from other threads

        * Introspección

        * Task object

      * Streams

        * StreamReader

        * StreamWriter

        * Ejemplos

          * Cliente eco TCP usando *streams*

          * Servidor eco TCP usando *streams*

          * Obtener encabezados HTTP

          * Registrar un socket abierto para esperar datos usando
            *streams*

      * Primitivas de sincronización

        * Lock

        * Event

        * Condition

        * Semaphore

        * BoundedSemaphore

        * Barrera

      * Sub-procesos

        * Creando sub-procesos

        * Constantes

        * Interactuando con Subprocesos

          * Subprocesos y Hilos

          * Ejemplos

      * Colas

        * Cola

        * Cola de prioridad

        * Cola UEPA (o *LIFO* en inglés)

        * Excepciones

        * Ejemplos

      * Excepciones

      * Call graph introspection

        * Low level utility functions

      * Command-line introspection tools

        * Command-line options

      * Event loop

        * Event loop methods

          * Iniciar y para el bucle

          * Programación de llamadas de retorno

          * Planificando llamadas retardadas

          * Creating futures and tasks

          * Abriendo conexiones de red

          * Creando servidores de red

          * Transfiriendo archivos

          * TLS upgrade

          * Viendo descriptores de archivos

          * Trabajar con objetos sockets directamente

          * DNS

          * Trabajando con tuberías

          * Señales Unix

          * Ejecutando código en un hilos o grupos de procesos

          * Error handling API

          * Habilitando el modo depuración

          * Running subprocesses

        * Callback handles

        * Server objects

        * Event loop implementations

        * Examples

          * Hola Mundo con call_soon()

          * Muestra la fecha actual con call_later()

          * Mirar un descriptor de archivo para leer eventos

          * Establece los gestores de señal para SIGINT y SIGTERM

      * Futures

        * Funciones Future

        * Objeto Future

      * Transportes y protocolos

        * Transportes

          * Jerarquía de transportes

          * Transporte base

          * Transportes de solo lectura

          * Transportes de solo escritura

          * Transportes de datagramas

          * Transportes de subprocesos

        * Protocolos

          * Protocolos base

          * Protocolo base

          * Protocolos de *streaming*

          * Protocolos de *streaming* mediante búfer

          * Protocolos de datagramas

          * Protocolos de subprocesos

        * Ejemplos

          * Servidor de eco TCP

          * Cliente de eco TCP

          * Servidor de eco UDP

          * Cliente de eco UDP

          * Conectando sockets existentes

          * *loop.subprocess_exec()* y *SubprocessProtocol*

      * Políticas

        * Obteniendo y configurando la política

        * Objetos de política

        * Personalizar Políticas

      * Soporte de plataforma

        * Todas las plataformas

        * Windows

          * Soporte de sub-procesos en Windows

        * macOS

      * Extensión

        * Escribir un bucle de eventos personalizado

        * Constructores privados Future y Task

        * Soporte de por vida de tareas

      * Índice de API de alto nivel

        * Tareas

        * Colas

        * Subprocesos

        * Flujos

        * Sincronización

        * Excepciones

      * Índice de API de bajo nivel

        * Obtención del bucle de eventos

        * Métodos del bucle de eventos

        * Transportes

        * Protocolos

        * Políticas de bucle de eventos

      * Desarrollando con asyncio

        * Modo depuración

        * Concurrencia y multihilo

        * Ejecutando código bloqueante

        * Logueando

        * Detectar corrutinas no esperadas

        * Detectar excepciones nunca recuperadas

        * Asynchronous generators best practices

          * Close asynchronous generators explicitly

          * Create asynchronous generators only when the event loop is
            running

          * Avoid concurrent iteration and closure of the same
            generator

      * asyncio and free-threaded Python

        * Thread safety considerations

        * Using asyncio with threads

        * Producer/consumer across threads

    * "socket" --- Low-level networking interface

      * Familias Socket

      * Contenido del módulo

        * Excepciones

        * Constantes

        * Funciones

          * Creación de sockets

          * Otras funciones

      * Objetos Socket

      * Notas sobre los tiempos de espera del socket

        * Tiempos de espera y el método "connect"

        * Tiempos de espera y el método "accept"

      * Ejemplo

    * "ssl" --- TLS/SSL wrapper for socket objects

      * Functions, constants, and exceptions

        * Creación de sockets

        * Creación de contexto

        * Excepciones

        * Generación aleatoria

        * Gestión de certificados

        * Constantes

      * SSL sockets

      * SSL contexts

      * Certificados

        * Cadenas de certificados

        * Certificados CA

        * Clave y certificado combinados

        * Certificados auto-firmados

      * Ejemplos

        * Pruebas de compatibilidad con SSL

        * Operación del lado del cliente

        * Operación del lado del servidor

      * Notas sobre los sockets no bloqueantes

      * Memory BIO support

      * Sesión SSL

      * Consideraciones de seguridad

        * Los mejores valores por defecto

        * Ajustes manuales

          * Verificación de certificados

          * Versiones del protocolo

          * Selección de cifrado

        * Multiprocesamiento

      * TLS 1.3

    * "select" --- Waiting for I/O completion

      * "/dev/poll" polling objects

      * Edge and level trigger polling (epoll) objects

      * Polling objects

      * Kqueue objects

      * Kevent objects

    * "selectors" --- High-level I/O multiplexing

      * Introducción

      * Clases

      * Ejemplos

    * "signal" --- Set handlers for asynchronous events

      * Reglas generales

        * Ejecución de los gestores de señales de Python

        * Señales e hilos

      * Contenidos del módulo

      * Ejemplos

      * Nota sobre SIGPIPE

      * Nota sobre Manejadores de Señales y Excepciones

    * "mmap" --- Memory-mapped file support

      * Constantes MADV_*

      * Constantes MAP_*

  * Manejo de datos de internet

    * "email" --- An email and MIME handling package

      * "email.message": Representing an email message

      * "email.parser": Parsing email messages

        * API *FeedParser*

        * API *Parser*

        * Notas adicionales

      * "email.generator": Generating MIME documents

      * "email.policy": Policy Objects

      * "email.errors": Exception and Defect classes

      * "email.headerregistry": Custom Header Objects

      * "email.contentmanager": Managing MIME Content

        * Instancias gestoras de contenido

      * "email": Ejemplos

      * "email.message.Message": Representar un mensaje de correo
        electrónico usando la API "compat32"

      * "email.mime": Creating email and MIME objects from scratch

      * "email.header": Internationalized headers

      * "email.charset": Representing character sets

      * "email.encoders": Encoders

      * "email.utils": Miscellaneous utilities

      * "email.iterators": Iterators

    * "json" --- JSON encoder and decoder

      * Uso básico

      * Codificadores y Decodificadores

      * Excepciones

      * Cumplimiento e interoperabilidad estándar

        * Codificaciones de caracteres

        * Valores de número infinito y NaN

        * Nombres repetidos dentro de un objeto

        * Valores de nivel superior No-Objeto , No-Arreglo

        * Limitaciones de la implementación

      * Command-line interface

        * Command-line options

    * "mailbox" --- Manipulate mailboxes in various formats

      * "Mailbox" objects

        * "Maildir" objects

        * "mbox" objects

        * "MH" objects

        * "Babyl" objects

        * "MMDF" objects

      * "Message" objects

        * "MaildirMessage" objects

        * "mboxMessage" objects

        * "MHMessage" objects

        * "BabylMessage" objects

        * "MMDFMessage" objects

      * Excepciones

      * Ejemplos

    * "mimetypes" --- Map filenames to MIME types

      * MimeTypes objects

      * Command-line usage

      * Command-line example

    * "base64" --- Base16, Base32, Base64, Base85 Data Encodings

      * RFC 4648 Encodings

      * Base85 Encodings

      * Legacy Interface

      * Consideraciones de Seguridad

    * "binascii" --- Convert between binary and ASCII

    * "quopri" --- Encode and decode MIME quoted-printable data

  * Herramientas Para Procesar Formatos de Marcado Estructurado

    * "html" --- HyperText Markup Language support

    * "html.parser" --- Simple HTML and XHTML parser

      * Aplicación ejemplo de un analizador sintáctico (*parser*) de
        HTML

      * Métodos "HTMLParser"

      * Ejemplos

    * "html.entities" --- Definitions of HTML general entities

    * Módulos de procesamiento XML

      * XML security

    * "xml.etree.ElementTree" --- The ElementTree XML API

      * Tutorial

        * Árbol y elementos XML

        * Procesando XML

        * API de consulta para un procesamiento no bloqueante

        * Encontrando elementos interesantes

        * Modificando un archivo XML

        * Construyendo documentos XML

        * Procesando XML con espacio de nombres

      * Soporte de XPath

        * Ejemplo

        * Sintaxis XPath soportada

      * Referencia

        * Funciones

      * Soporte de XInclude

        * Ejemplo

      * Referencia

        * Funciones

        * Objetos Element

        * Objetos ElementTree

        * Objetos QName

        * Objetos TreeBuilder

        * Objetos XMLParser

        * Objetos XMLPullParser

        * Excepciones

    * "xml.dom" --- The Document Object Model API

      * Contenido del módulo

      * Objetos en el DOM

        * Objetos *DOMImplementation*

        * Objetos nodo

        * Objetos *NodeList*

        * Objetos *DocumentType*

        * Objetos documento

        * Objetos elemento

        * Objetos atributo

        * Objetos *NamedNodeMap*

        * Objetos comentario

        * Objetos Texto y *CDATASection*

        * Objetos *ProcessingInstruction*

        * Excepciones

      * Conformidad

        * Mapeo de tipos

        * Métodos de acceso (*accessor*)

    * "xml.dom.minidom" --- Minimal DOM implementation

      * Objetos del DOM

      * Ejemplo de DOM

      * minidom y el estándar DOM

    * "xml.dom.pulldom" --- Support for building partial DOM trees

      * Objetos DOMEventStream

    * "xml.sax" --- Support for SAX2 parsers

      * Objetos SAXException

    * "xml.sax.handler" --- Base classes for SAX handlers

      * Objetos ContentHandler

      * Objetos DTDHandler

      * Objetos EntityResolver

      * Objetos ErrorHandler

      * Objetos DTDHandler

    * "xml.sax.saxutils" --- SAX Utilities

    * "xml.sax.xmlreader" --- Interface for XML parsers

      * Objetos XMLReader

      * Objetos IncrementalParser

      * Objetos localizadores

      * Objetos InputSource

      * La Interfaz "Attributes"

      * La Interfaz "AttributesNS"

    * "xml.parsers.expat" --- Fast XML parsing using Expat

      * Objetos XMLParser

      * Excepciones de ExpatError

      * Ejemplo

      * Descripciones del modelo de contenido

      * Constantes de error de expansión

  * Protocolos y soporte de Internet

    * "webbrowser" --- Convenient web-browser controller

      * Command-line interface

      * Browser controller objects

    * "wsgiref" --- WSGI Utilities and Reference Implementation

      * "wsgiref.util" -- WSGI environment utilities

      * "wsgiref.headers" -- WSGI response header tools

      * "wsgiref.simple_server" -- a simple WSGI HTTP server

      * "wsgiref.validate" --- WSGI conformance checker

      * "wsgiref.handlers" -- server/gateway base classes

      * "wsgiref.types" -- WSGI types for static type checking

      * Ejemplos

    * "urllib" --- URL handling modules

    * "urllib.request" --- Extensible library for opening URLs

      * Objetos Request

      * Objetos OpenerDirector

      * Objetos BaseHandler

      * Objetos HTTPRedirectHandler

      * Objetos HTTPCookieProcessor

      * Objetos ProxyHandler

      * Objetos HTTPPasswordMgr

      * Objetos HTTPPasswordMgrWithPriorAuth

      * Objetos AbstractBasicAuthHandler

      * Objetos HTTPBasicAuthHandler

      * Objetos ProxyBasicAuthHandler

      * Objetos AbstractDigestAuthHandler

      * Objetos HTTPDigestAuthHandler

      * Objetos ProxyDigestAuthHandler

      * Objetos HTTPHandler

      * Objetos HTTPSHandler

      * Objetos FileHandler

      * Objetos DataHandler

      * Objetos FTPHandler

      * Objetos CacheFTPHandler

      * Objetos UnknownHandler

      * Objetos HTTPErrorProcessor

      * Ejemplos

      * Interfaz heredada

      * "urllib.request" Restrictions

    * "urllib.response" --- Response classes used by urllib

    * "urllib.parse" --- Parse URLs into components

      * Análisis de URL

      * Análisis de seguridad de URL

      * Análisis de bytes codificados ASCII

      * Resultados del análisis estructurado

      * Cita de URL

    * "urllib.error" --- Exception classes raised by urllib.request

    * "urllib.robotparser" ---  Parser for robots.txt

    * "http" --- HTTP modules

      * Códigos de estado HTTP

      * Categoría de estado HTTP

      * Métodos HTTP

    * "http.client" --- HTTP protocol client

      * Objetos de "HTTPConnection"

      * Objetos de "HTTPResponse"

      * Ejemplos

      * Objetos de "HTTPMessage"

    * "ftplib" --- FTP protocol client

      * Reference

        * FTP objects

        * FTP_TLS objects

        * Module variables

    * "poplib" --- POP3 protocol client

      * Objetos POP3

      * Ejemplo POP3

    * "imaplib" --- IMAP4 protocol client

      * Objetos de IMAP4

      * Ejemplo IMAP4

    * "smtplib" --- SMTP protocol client

      * Objetos SMTP

      * Ejemplo SMTP

    * "uuid" --- UUID objects according to **RFC 9562**

      * Uso de la línea de comandos

      * Ejemplo

      * Ejemplo de línea de comandos

    * "socketserver" --- A framework for network servers

      * Notas de creación del servidor

      * Objetos de servidor

      * Solicitar objetos de controlador

      * Ejemplos

        * "socketserver.TCPServer" Ejemplo

        * "socketserver.UDPServer" Ejemplo

        * Mixins asincrónicos

    * "http.server" --- HTTP servers

      * Command-line interface

      * Security considerations

    * "http.cookies" --- HTTP state management

      * Objetos de cookie

      * Objetos Morsel

      * Ejemplo

    * "http.cookiejar" --- Cookie handling for HTTP clients

      * CookieJar and FileCookieJar objects

      * Subclases FileCookieJar y co-operación con navegadores web

      * CookiePolicy objects

      * DefaultCookiePolicy objects

      * Cookie objects

      * Ejemplos

    * "xmlrpc" --- Módulos XMLRPC para cliente y servidor

    * "xmlrpc.client" --- XML-RPC client access

      * Objetos *ServerProxy*

      * Objetos *DateTime*

      * Objetos binarios

      * Objetos Faults

      * Objetos ProtocolError

      * Objetos MultiCall

      * Funciones de Conveniencia

      * Ejemplo de uso de cliente

      * Ejemplo de uso de cliente y servidor

    * "xmlrpc.server" --- Basic XML-RPC servers

      * SimpleXMLRPCServer objects

        * SimpleXMLRPCServer example

      * CGIXMLRPCRequestHandler

      * Documentando el servidor XMLRPC

      * DocXMLRPCServer objects

      * DocCGIXMLRPCRequestHandler

    * "ipaddress" --- IPv4/IPv6 manipulation library

      * Funciones de fábrica de conveniencia

      * Direcciones IP

        * Objetos de dirección

        * Conversión a cadenas y enteros

        * Operadores

          * Operadores de comparación

          * Operadores aritméticos

      * Definiciones de red IP

        * Prefijo, máscara de red y máscara de host

        * Objetos de red

        * Operadores

          * Operadores lógicos

          * Iteración

          * Redes como contenedores de direcciones

      * Objetos de interfaz

        * Operadores

          * Operadores lógicos

      * Otras funciones de nivel de módulo

      * Excepciones personalizadas

  * Servicios Multimedia

    * "wave" --- Read and write WAV files

      * Los objetos *Wave_read*

      * Los objetos *Wave_write*

    * "colorsys" --- Conversions between color systems

  * Internacionalización

    * "gettext" --- Multilingual internationalization services

      * GNU API **gettext**

      * API basada en clases

        * La clase "NullTranslations"

        * La clase "GNUTranslations"

        * Soporte de catálogo de mensajes de Solaris

        * El constructor del catálogo

      * Internacionalizando sus programas y módulos

        * Agregar configuración regional a su módulo

        * Agregar configuración regional a su aplicación

        * Cambiar idiomas sobre la marcha

        * Traducciones diferidas

      * Agradecimientos

    * "locale" --- Internationalization services

      * Segundo plano, detalles, indicaciones, consejos y advertencias

      * Locale names

      * Para escritores de extensión y programas que incrustan Python

      * Acceso a los catálogos de mensajes

  * Graphical user interfaces with Tk

    * "tkinter" --- Python interface to Tcl/Tk

      * Arquitectura

      * Tkinter modules

      * Tkinter life preserver

        * A Hello World program

        * Important Tk concepts

        * Understanding how Tkinter wraps Tcl/Tk

        * ¿Cómo lo hago?, ¿Cómo funciona?

        * Navigating the Tcl/Tk reference manual

      * Modelo de subprocesamiento

      * Handy reference

        * Setting options

        * Geometry management

        * Coupling widget variables

        * The window manager

        * Tk option data types

        * Bindings and events

        * The index parameter

        * Imágenes

      * Reference

        * Base and mixin classes

        * Toplevel widgets

        * Widget classes

        * Variable classes

        * Image classes

        * Other classes

        * Module-level functions

        * File handlers

        * Constants

    * "tkinter.colorchooser" --- Color choosing dialog

    * "tkinter.font" --- Tkinter font wrapper

    * Tkinter dialogs

      * "tkinter.simpledialog" --- Standard Tkinter input dialogs

      * "tkinter.filedialog" --- File selection dialogs

        * Native load/save dialogs

      * "tkinter.commondialog" --- Dialog window templates

      * "tkinter.dialog" --- Classic Tk dialog boxes

    * "tkinter.messagebox" --- Tkinter message prompts

    * "tkinter.scrolledtext" --- Scrolled text widget

    * "tkinter.dnd" --- Drag and drop support

    * "tkinter.ttk" --- Tk themed widgets

      * Uso de Ttk

      * Ttk widgets

      * Widget

        * Standard options

        * Scrollable widget options

        * Label options

        * Compatibility options

        * Widget states

        * ttk.Widget

      * Combobox

        * Opciones

        * Eventos virtuales

        * ttk.Combobox

      * Spinbox

        * Opciones

        * Eventos virtuales

        * ttk.Spinbox

      * Notebook

        * Opciones

        * Tab options

        * Tab identifiers

        * Eventos virtuales

        * ttk.Notebook

      * Progressbar

        * Opciones

        * ttk.Progressbar

      * Separator

        * Opciones

      * Sizegrip

        * Notas específicas por plataforma

        * Errores detectados

      * Treeview

        * Opciones

        * Item options

        * Tag options

        * Column identifiers

        * Eventos virtuales

        * ttk.Treeview

      * Ttk styling

        * Diseños

      * Additional widgets

    * IDLE --- Python editor and shell

      * Menús

        * Menú de archivo (Shell y Editor)

        * Menú editar (Shell y Editor)

        * Menú de formato (solo ventana del Editor)

        * Menú ejecutar (solo ventana Editor)

        * Menú de shell (solo ventana de shell)

        * Menú de depuración (solo ventana de shell)

        * Menú de opciones (Shell y editor)

        * Menú de ventana (shell y editor)

        * Menú de ayuda (shell y editor)

        * Menús contextuales

      * Edición y navegación

        * Ventana del editor

        * Atajos de teclado

        * Indentación automática

        * Buscar y reemplazar

        * Terminaciones

        * Sugerencias de llamada

        * Format block

        * Contexto del código

        * Ventana de Shell

        * Colores del texto

      * Inicio y ejecución de código

        * Command-line usage

        * Error de inicio

        * Ejecutando código del usuario

        * Salida del usuario en consola

        * Desarrollando aplicaciones tkinter

        * Ejecutando sin un subproceso

      * Ayuda y preferencias

        * Recursos de ayuda

        * Preferencias de configuración

        * IDLE en macOS

        * Extensiones

      * idlelib --- implementation of IDLE application

    * "turtle" --- Turtle graphics

      * Introducción

      * Empezar

      * Tutorial

        * Iniciando un entorno para tortugas

        * Dibujo básico

          * Control del lápiz

          * La posición de la tortuga

        * Creando patrones algorítmicos

      * Cómo...

        * Empiece lo antes posible

        * Automatically begin and end filling

        * Utilice el espacio de nombres del módulo "turtle"

        * Utilice gráficos de tortugas en un guión

        * Utilice gráficos de tortuga orientados a objetos

      * Referencia gráficos de tortugas

        * Métodos Turtle

        * Métodos de TurtleScreen/Screen

      * Métodos de *RawTurtle/Turtle* Y sus correspondientes funciones

        * Movimiento de Turtle

        * Mostrar el estado de la tortuga

        * Configuración de las medidas

        * Control del lápiz

          * Estado de dibujo

          * Control del color

          * Relleno

          * Más controles de dibujo

        * Estado de la Tortuga

          * Visibilidad

          * Apariencia

        * Usando eventos

        * Métodos especiales de *Turtle*

        * Formas compuestas

      * Métodos de *TurtleScreen/Screen* y sus correspondientes
        funciones

        * Control de ventana

        * Control de animación

        * Usando eventos de pantalla

        * Métodos de entrada

        * Configuración y métodos especiales

        * Métodos específicos de *Screen*, no heredados de
          *TurtleScreen*

      * Clases públicas

      * Explicación

      * Ayuda y configuración

        * Cómo usar la ayuda

        * Traducción de cadenas de documentos a diferentes idiomas

        * Cómo configurar Screen and Turtles

      * "turtledemo" --- Demo scripts

      * Cambios desde Python 2.6

      * Cambios desde Python 3.0

  * Herramientas de desarrollo

    * "typing" --- Support for type hints

      * Especificación del sistema de tipos de Python

      * Alias de tipo

      * NewType

      * Anotaciones en objetos invocables

      * Genéricos

      * Anotaciones en tuplas

      * El tipo de objetos de clase

      * Anotación de generadores y corrutinas

      * Tipos genéricos definidos por el usuario

      * El tipo "Any"

      * Subtipado nominal vs estructural

      * Contenido del módulo

        * Primitivos especiales de tipado

          * Tipos especiales

          * Formas especiales

          * Creación de tipos genéricos y alias de tipos

          * Otras directivas especiales

        * Protocolos

        * ABCs and Protocols for working with I/O

        * Funciones y decoradores

        * Ayudas de introspección

        * Constantes

        * Alias obsoletos

          * Alias de tipos integrados

          * Alias de tipos en "collections"

          * Alias ​​a otros tipos concretos

          * Alias de ABCs de contenedores en "collections.abc"

          * Alias para ABCs asíncronos en "collections.abc"

          * Alias a otros ABCs en "collections.abc"

          * Alias de ABCs "contextlib"

      * Línea de tiempo de obsolescencia de características
        principales

    * "pydoc" --- Documentation generator and online help system

    * Modo de desarrollo de Python

      * Efectos del modo de desarrollo de Python

      * Ejemplo de ResourceWarning

      * Ejemplo de error de descriptor de archivo incorrecto

    * "doctest" --- Test interactive Python examples

      * Uso simple: verificar ejemplos en docstrings

      * Uso Simple: Verificar ejemplos en un Archivo de Texto

      * Command-line Usage

      * Cómo funciona

        * ¿Qué docstrings son examinados?

        * ¿Cómo se reconocen los ejemplos de docstring?

        * ¿Cuál es el contexto de ejecución?

        * ¿Y las excepciones?

        * Banderas de Opción

        * Directivas

        * Advertencias

      * API básica

      * API de unittest

      * API avanzada

        * Objetos DocTest

        * Objetos *Example*

        * Objetos *DocTestFinder*

        * Objetos *DocTestParser*

        * TestResults objects

        * Objetos *DocTestRunner*

        * Objetos *OutputChecker*

      * Depuración

      * Plataforma improvisada

    * "unittest" --- Unit testing framework

      * Ejemplo sencillo

      * Interfaz de línea de comandos

        * Opciones de la línea de órdenes

      * Descubrimiento de pruebas

      * Organización del código de pruebas

      * Reutilización de código de prueba anterior

      * Omitir tests y fallos esperados

      * Distinguiendo iteraciones de tests empleando subtests

      * Clases y funciones

        * Casos de test

        * Agrupando tests

        * Cargando y ejecutando tests

          * load_tests protocolo

      * Instalaciones para clases y módulos

        * setUpClass y tearDownClass

        * setUpModule y tearDownModule

      * Manejo de señales

    * "unittest.mock" --- mock object library

      * Guía rápida

      * La clase Mock

        * Llamar a los objetos simulados

        * Eliminar atributos

        * Los nombres de los objetos simulados y el atributo *name*

        * Adjuntar objetos simulados como atributos

      * Parcheadores

        * patch

        * patch.object

        * patch.dict

        * patch.multiple

        * métodos start y stop de patch

        * parchear objetos incorporados (builtins)

        * TEST_PREFIX

        * Anidando decoradores patch

        * Dónde parchear

        * Parcheando descriptores y objetos proxy

      * MagicMock y el soporte de métodos mágicos

        * Simular métodos mágicos

        * Magic Mock

      * Ayudantes

        * sentinel

        * DEFAULT

        * call

        * create_autospec

        * ANY

        * FILTER_DIR

        * mock_open

        * Autoespecificación

        * Sellar objetos simulados

      * Order of precedence of "side_effect", "return_value" and
        *wraps*

    * "unittest.mock" --- getting started

      * Usando mock

        * Mock patching methods

        * Mock for method calls on an object

        * Mocking classes

        * Nombrando tus mocks

        * Tracking all calls

        * Setting return values and attributes

        * Generar excepciones con mocks

        * Funciones de efectos secundarios e iterables

        * Iteradores asincrónicos de Mocking

        * El gestor de contexto asincrónico de Mocking

        * Creating a mock from an existing object

        * Uso de side_effect para devolver el contenido por archivo

      * Patch decorators

      * Further examples

        * Mocking de llamadas encadenadas

        * Mocking parcial

        * Mocking a generator method

        * Aplicar el mismo parche a cada método de prueba

        * Mocking unbound methods

        * Comprobación de varias llamadas con mock

        * Copiando con argumentos mutables

        * Nesting patches

        * Mocking a un diccionario usando MagickMock

        * Mock de subclases y sus atributos

        * Importaciones de Mocking con patch.dict

        * Seguimiento del orden de las llamadas y de las aserciones de
          llamadas menos detalladas

        * Coincidencia de argumentos más compleja

    * "test" --- Regression tests package for Python

      * Writing Unit Tests for the "test" package

      * Ejecución de pruebas utilizando la interfaz de línea de
        comandos

    * "test.support" --- Utilities for the Python test suite

    * "test.support.socket_helper" --- Utilities for socket tests

    * "test.support.script_helper" --- Utilities for the Python
      execution tests

    * "test.support.bytecode_helper" --- Support tools for testing
      correct bytecode generation

    * "test.support.threading_helper" --- Utilities for threading
      tests

    * "test.support.os_helper" --- Utilities for os tests

    * "test.support.import_helper" --- Utilities for import tests

    * "test.support.warnings_helper" --- Utilities for warnings tests

  * Depuración y perfilado

    * Tabla de auditoría de eventos

    * "bdb" --- Debugger framework

    * "faulthandler" --- Dump the Python traceback

      * Volcar el rastreo

      * Dumping the C stack

        * C Stack Compatibility

      * Estado del gestor de fallos

      * Volcar los rastreos después de un tiempo de espera

      * Volcar el rastreo en una señal del usuario

      * Problema con descriptores de archivo

      * Ejemplo

    * "pdb" --- The Python Debugger

      * Command-line interface

      * Debugger commands

    * Los perfiladores de Python

      * Introducción a los perfiladores

      * Manual instantáneo de usuario

      * "profile" and "cProfile" Module Reference

      * La clase "Stats"

      * ¿Qué es el perfil determinista?

      * Limitaciones

      * Calibración

      * Usando un temporizador personalizado

    * "timeit" --- Measure execution time of small code snippets

      * Ejemplos básicos

      * Interfaz de Python

      * Interfaz de línea de comandos

      * Ejemplos

    * "trace" --- Trace or track Python statement execution

      * Uso de la línea de comandos

        * Opciones principales

        * Modificadores

        * Filtros

      * Interfaz programática

    * "tracemalloc" --- Trace memory allocations

      * Ejemplos

        * Mostrar los 10 principales

        * Calcula las diferencias

        * Consigue el seguimiento del bloque de memoria

        * "Los 10 más bonitos"

          * Graba los tamaños actual y máximo de todos los bloques de
            memoria rastreados

      * API

        * Funciones

        * Filtro de dominio

        * Filtro

        * Cuadro

        * Captura instantánea

        * Estadística

        * StatisticDiff

        * Rastro

        * Seguimiento

  * Empaquetado y distribución de software

    * "ensurepip" --- Bootstrapping the "pip" installer

      * Command-line interface

      * API del módulo

    * "venv" --- Creation of virtual environments

      * Creación de entornos virtuales

      * Cómo funcionan los venvs

      * API

      * Un ejemplo de la extensión de "EnvBuilder"

    * "zipapp" --- Manage executable Python zip archives

      * Ejemplo básico

      * Interfaz de línea de comando

      * API de Python

      * Ejemplos

      * Especificar el intérprete

      * Creando aplicaciones independientes con zipapp

        * Advertencias

      * El formato de archivado Zip de aplicaciones Python

  * Servicios en tiempo de ejecución de Python

    * "sys" --- System-specific parameters and functions

    * "sys.monitoring" --- Execution event monitoring

      * Identificadores de herramientas

        * Registro y uso de herramientas

      * Eventos

        * Eventos locales

        * Deprecated event

        * Eventos auxiliares

        * Otros eventos

        * El evento STOP_ITERATION

      * Activar y desactivar eventos

        * Configuración de eventos globalmente

        * Eventos por objeto de código

        * Deshabilitando eventos

      * Registrando funciones de retrollamada

        * Argumentos de la función de retrollamada

    * "sysconfig" --- Provide access to Python's configuration
      information

      * Variables de configuración

      * Rutas de instalación

      * User scheme

        * "posix_user"

        * "nt_user"

        * "osx_framework_user"

      * Home scheme

        * "posix_home"

      * Prefix scheme

        * "posix_prefix"

        * "nt"

      * Installation path functions

      * Otras funciones

      * Command-line usage

    * "builtins" --- Built-in objects

    * "__main__" --- Top-level code environment

      * "__name__ == '__main__'"

        * ¿Qué es el "entorno de código de máximo nivel"?

        * Uso idiomático

        * Consideraciones de empaquetado

      * "__main__.py" en paquetes de Python

        * Uso idiomático

      * "import __main__"

    * "warnings" --- Warning control

      * Categorías de advertencia

      * El filtro de advertencias

        * Repeated Warning Suppression Criteria

        * Descripción de los filtros de advertencia

        * Filtro de advertencia predeterminado

        * Anulando el filtro por defecto

      * Eliminación temporal de las advertencias

      * Advertencias de prueba

      * Actualización del código para las nuevas versiones de las
        dependencias

      * Funciones disponibles

      * Gestores de contexto disponibles

      * Concurrent safety of Context Managers

    * "dataclasses" --- Data Classes

      * Contenidos del módulo

      * Procesamiento posterior a la inicialización

      * Variables de clase

      * Variable de solo inicialización

      * Instancias congeladas

      * Herencia

      * Re-ordering of keyword-only parameters in "__init__()"

      * Funciones fábrica por defecto

      * Valores por defecto mutables

      * Campos tipo descriptor

    * "contextlib" --- Utilidades para declaraciones de contexto
      "with"

      * Utilidades

      * Ejemplos y recetas

        * Apoyando un número variable de gestores de contexto

        * Capturando excepciones de los métodos "__enter__"

        * Limpieza en una implementación "__enter__"

        * Reemplazar cualquier uso de "try-finally" y marcar variables

        * Usar un gestor de contexto como decorador de funciones

      * Gestores de contexto de uso único, reutilizables y reentrantes

        * Gestores contextuales reentrantes

        * Gestores contextuales reutilizables

    * "abc" --- Abstract Base Classes

    * "atexit" --- Exit handlers

      * "atexit" Example

    * "traceback" --- Print or retrieve a stack traceback

      * Module-Level Functions

      * "TracebackException" Objects

      * "StackSummary" Objects

      * "FrameSummary" Objects

      * Examples of Using the Module-Level Functions

      * Examples of Using "TracebackException"

    * "__future__" --- Future statement definitions

      * Module Contents

    * "gc" --- Garbage Collector interface

    * "inspect" --- Inspect live objects

      * Tipos y miembros

      * Recuperar el código fuente

      * Introspección de los invocables con el objeto Signature

      * Clases y funciones

      * La pila del interprete

      * Obteniendo atributos estáticamente

      * Current State of Generators, Coroutines, and Asynchronous
        Generators

      * Objetos de código Bit Flags

      * Buffer flags

      * Command-line interface

    * "annotationlib" --- Functionality for introspecting annotations

      * Annotation semantics

      * Classes

      * Functions

      * Recipes

        * Using annotations in a metaclass

        * Creating a custom callable annotate function

      * Limitations of the "STRING" format

      * Limitations of the "FORWARDREF" format

      * Security implications of introspecting annotations

    * "site" --- Site-specific configuration hook

      * "sitecustomize"

      * "usercustomize"

      * Configuración de *Readline*

      * Contenido del módulo

      * Command-line interface

  * Intérpretes de Python personalizados

    * "code" --- Interpreter base classes

      * Objetos de intérprete interactivo

      * Objetos de consola interactiva

    * "codeop" --- Compile Python code

  * Importando módulos

    * "zipimport" --- Import modules from Zip archives

      * Objetos zipimporter

      * Ejemplos

    * "pkgutil" --- Package extension utility

    * "modulefinder" --- Find modules used by a script

      * Ejemplo de uso de "ModuleFinder"

    * "runpy" --- Localización y ejecución de módulos Python

    * "importlib" --- La implementación de "import"

      * Introducción

      * Funciones

      * "importlib.abc" -- Abstract base classes related to import

      * "importlib.machinery" -- Importers and path hooks

      * "importlib.util" -- Utility code for importers

      * Ejemplos

        * Importar programáticamente

        * Comprobando si se puede importar un módulo

        * Importar un archivo fuente directamente

        * Implementar importaciones diferidas

        * Configurar un importador

        * Aproximando "importlib.import_module()"

    * "importlib.resources" -- Package resource reading, opening and
      access

      * Functional API

    * "importlib.resources.abc" -- Abstract base classes for resources

    * "importlib.metadata" -- Acceso a los metadatos de los paquetes

      * Descripción general

      * API funcional

        * Puntos de entrada

        * Metadatos de distribución

        * Versiones de distribución

        * Archivos de distribución

        * Requerimientos de la distribución

        * Mapeo de paquetes de importación a distribución

      * Distribuciones

      * Distribution Discovery

      * Implementing Custom Providers

        * Example

    * La inicialización de la ruta de búsqueda de módulo de "sys.path"

      * Virtual Environments

      * Archivos _pth

      * Python embebido

  * Servicios del lenguaje Python

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

  * Servicios Específicos para MS Windows

    * "msvcrt" --- Useful routines from the MS VC++ runtime

      * Operaciones con archivos

      * Consola E/S

      * Otras funciones

    * "winreg" --- Windows registry access

      * Funciones

      * Constantes

        * HKEY_* Constantes

        * Access Rights

          * Específico de 64 bits

        * Tipos de valor

      * Objetos de control del registro

    * "winsound" --- Sound-playing interface for Windows

  * Unix-specific services

    * "shlex" --- Simple lexical analysis

      * objetos "shlex"

      * Reglas de análisis

      * Compatibilidad mejorada con intérprete de comandos

    * "posix" --- The most common POSIX system calls

      * Soporte de archivos grandes

      * Contenido notable del módulo

    * "pwd" --- The password database

    * "grp" --- The group database

    * "termios" --- POSIX style tty control

      * Ejemplo

    * "tty" --- Terminal control functions

    * "pty" --- Pseudo-terminal utilities

      * Ejemplo

    * "fcntl" --- The "fcntl" and "ioctl" system calls

    * "resource" --- Resource usage information

      * Límites de recursos

      * Utilización de recursos

    * "syslog" --- Unix syslog library routines

      * Ejemplos

        * Ejemplo sencillo

  * Modules command-line interface (CLI)

  * Módulos reemplazados

    * "getopt" --- C-style parser for command line options

  * Removed Modules

  * Consideraciones de seguridad

* Ampliación e incrustación del intérprete de Python

  * Herramientas de terceros recomendadas

  * Crear extensiones sin herramientas de terceros

    * 1. Extendiendo Python con C o C++

      * 1.1. Un ejemplo simple

      * 1.2. Intermezzo: errores y excepciones

      * 1.3. De vuelta al ejemplo

      * 1.4. La tabla de métodos del módulo y la función de
        inicialización

      * 1.5. Compilación y enlazamiento

      * 1.6. Llamando funciones Python desde C

      * 1.7. Extracción de parámetros en funciones de extensión

      * 1.8. Parámetros de palabras clave para funciones de extensión

      * 1.9. Construyendo valores arbitrarios

      * 1.10. Conteo de referencias

        * 1.10.1. Conteo de referencias en Python

        * 1.10.2. Reglas de propiedad

        * 1.10.3. Hielo delgado

        * 1.10.4. Punteros NULL

      * 1.11. Escribiendo extensiones en C++

      * 1.12. Proporcionar una API C para un módulo de extensión

    * 2. Definición de tipos de extensión: Tutorial

      * 2.1. Lo básico

      * 2.2. Agregar datos y métodos al ejemplo básico

      * 2.3. Proporcionar un control más preciso sobre los atributos
        de datos

      * 2.4. Apoyo a la recolección de basura cíclica

      * 2.5. Subclases de otros tipos

    * 3. Definición de tipos de extensión: temas variados

      * 3.1. Finalización y desasignación

      * 3.2. Presentación de objetos

      * 3.3. Gestión de atributos

        * 3.3.1. Gestión de atributos genéricos

        * 3.3.2. Gestión de atributos específicos de tipo

      * 3.4. Comparación de Objetos

      * 3.5. Soporte de protocolo abstracto

      * 3.6. Soporte de referencia débil

      * 3.7. Más Sugerencias

    * 4. Construyendo extensiones C y C++

      * 4.1. Building C and C++ Extensions with setuptools

    * 5. Creación de extensiones C y C++ en Windows

      * 5.1. Un enfoque de libro de cocina

      * 5.2. Diferencias entre Unix y Windows

      * 5.3. Usar DLL en la práctica

  * Incrustar el tiempo de ejecución de CPython en una aplicación más
    grande

    * 1. Incrustando Python en otra aplicación

      * 1.1. Incrustación de muy alto nivel

      * 1.2. Más allá de la incrustación de muy alto nivel: una visión
        general

      * 1.3. Incrustación pura

      * 1.4. Extendiendo Python incrustado

      * 1.5. Incrustando Python en C++

      * 1.6. Compilar y enlazar bajo sistemas tipo Unix

* Python/C API reference manual

  * Introducción

    * Language version compatibility

    * Estándares de codificación

    * Archivos de cabecera (*Include*)

    * Macros útiles

      * Docstring macros

      * General utility macros

        * Numeric utilities

        * Assertion utilities

        * Type size utilities

        * Macro definition utilities

      * Declaration utilities

      * Outdated macros

    * Objetos, tipos y conteos de referencias

      * Conteo de Referencias

        * Detalles del conteo de referencia

      * Tipos

    * Excepciones

    * Integración de Python

    * Depuración de compilaciones

    * Recommended third party tools

  * Estabilidad de la API en C

    * Unstable C API

    * Interfaz binaria de aplicación estable

      * Limited C API

      * Stable ABI

      * Alcance y rendimiento de la API limitada

      * Advertencias de la API limitada

    * Consideraciones de la plataforma

    * Contenido de la API limitada

  * La capa de muy alto nivel

    * Available start symbols

    * Stack Effects

  * Conteo de referencias

  * Manejo de excepciones

    * Impresión y limpieza

    * Lanzando excepciones

    * Emitir advertencias

    * Consultando el indicador de error

    * Manejo de señal

    * Clases de excepción

    * Objetos excepción

    * Objetos unicode de excepción

    * Control de recursión

    * Exception and warning types

      * Exception types

      * OSError aliases

      * Warning types

    * Tracebacks

  * Defining extension modules

    * Multiple module instances

    * Initialization function

    * Multi-phase initialization

    * Legacy single-phase initialization

  * Utilidades

    * Utilidades del sistema operativo

    * Funciones del Sistema

    * Control de procesos

    * Importando módulos

    * Soporte de empaquetado (*marshalling*) de datos

    * Analizando argumentos y construyendo valores

      * Analizando argumentos

        * Cadena de caracteres y búferes

        * Números

        * Otros objetos

        * Funciones API

      * Construyendo valores

    * Conversión y formato de cadenas de caracteres

    * Character classification and conversion

    * PyHash API

    * Reflexión

    * Registro de códec y funciones de soporte

      * API de búsqueda de códec

      * API de registro para controladores de errores de codificación
        Unicode

      * Codec utility variables

    * PyTime C API

      * Types

      * Clock Functions

      * Raw Clock Functions

      * Conversion functions

    * Soporte para Mapeo Perf

  * Capa de objetos abstractos

    * Protocolo de objeto

    * Protocolo de llamada

      * El protocolo *tp_call*

      * El protocolo vectorcall

        * Control de recursión

        * API de soporte para vectorcall

      * API para invocar objetos

      * API de soporte de llamadas

    * Protocolo de números

    * Protocolo de secuencia

    * Protocolo de mapeo

    * Protocolo iterador

    * Protocolo búfer

      * Estructura de búfer

      * Tipos de solicitud búfer

        * campos independientes de solicitud

        * formato de sólo lectura

        * formas, *strides*, *suboffsets*

        * solicitudes de contigüidad

        * solicitudes compuestas

      * Arreglos complejos

        * Estilo NumPy: forma y *strides*

        * Estilo PIL: forma, *strides* y *suboffsets*

      * Funciones relacionadas a búfer

  * Capa de objetos concretos

    * Objetos fundamentales

      * Objetos tipo

        * Crear tipos asignados en montículo (*heap*)

      * El objeto "None"

    * Objetos numéricos

      * Objetos enteros

        * Export API

        * PyLongWriter API

        * Deprecated API

      * Objetos booleanos

      * Floating-Point Objects

        * Funciones de empaquetado y desempaquetado

          * Funciones de Empaquetado

          * Funciones de Desempaquetado

      * Objetos de números complejos

        * Números complejos como estructuras C

        * Números complejos como objetos de Python

    * Objetos de secuencia

      * Objetos bytes

      * Objetos de arreglos de bytes (*bytearrays*)

        * Macros de verificación de tipos

        * Funciones API directas

        * Macros

      * Objetos y códecs unicode

        * Objetos unicode

          * Tipo unicode

          * Propiedades de caracteres Unicode

          * Creando y accediendo a cadenas de caracteres Unicode

          * Codificación regional

          * Codificación del sistema de archivos

          * soporte wchar_t

        * Códecs incorporados

          * Códecs genéricos

          * Códecs UTF-8

          * Códecs UTF-32

          * Códecs UTF-16

          * Códecs UTF-7

          * Códecs Unicode escapado

          * Códecs para Unicode escapado en bruto

          * Códecs Latin-1

          * Códecs ASCII

          * Códecs de mapa de caracteres

          * Códecs MBCS para Windows

        * Métodos y funciones de ranura (*Slot*)

        * PyUnicodeWriter

        * Deprecated API

      * Objetos tupla

      * Objetos de secuencia de estructura

      * Objetos lista

    * Objetos contenedor

      * Objetos diccionario

        * Dictionary View Objects

        * Ordered Dictionaries

      * Objetos conjunto

        * Deprecated API

    * Objetos de función

      * Objetos función

      * Objetos de método de instancia

      * Objetos método

      * Objetos celda

      * Objetos código

      * Code Object Flags

      * Extra information

    * Otros objetos

      * File objects

        * Soft-deprecated API

      * Objetos módulo

      * Module definitions

        * Module slots

      * Creating extension modules dynamically

      * Funciones de soporte

        * Module lookup (single-phase initialization)

      * Objetos iteradores

        * Range Objects

        * Builtin Iterator Types

        * Other Iterator Objects

      * Objetos descriptores

        * Built-in descriptors

      * Objetos rebanada (*slice*)

        * Objeto elipsis

      * Objetos de vista de memoria (*MemoryView*)

      * Pickle buffer objects

      * Objetos de referencia débil

      * Cápsulas

      * Frame objects

        * Frame locals proxies

        * Legacy local variable APIs

        * Internal frames

      * Objetos generadores

        * Asynchronous Generator Objects

        * Deprecated API

      * Objetos corrutina

      * Objetos de variables de contexto

      * Objetos para indicaciones de tipado

    * C API for extension modules

      * Curses C API

      * Internal data

      * Objetos *DateTime*

      * Internal data

  * Interpreter initialization and finalization

    * Before Python initialization

    * Global configuration variables

    * Initializing and finalizing the interpreter

    * Cautions regarding runtime finalization

    * Process-wide parameters

  * Thread states and the global interpreter lock

    * Detaching the thread state from extension code

      * APIs

    * Non-Python created threads

    * Legacy API

    * Cautions about fork()

    * High-level APIs

    * GIL-state APIs

    * Low-level APIs

  * Asynchronous notifications

  * Operating system thread APIs

  * Synchronization primitives

    * Python critical section API

    * Legacy locking APIs

  * Thread-local storage support

    * Thread-specific storage API

    * Dynamic allocation

    * Methods

    * Legacy APIs

  * Multiple interpreters in a Python process

    * A per-interpreter GIL

    * Bugs and caveats

    * High-level APIs

    * Low-level APIs

    * Advanced debugger support

  * Profiling and tracing

  * Reference tracing

  * Configuración de inicialización de Python

    * PyInitConfig C API

      * Ejemplo

      * Create Config

      * Error Handling

      * Get Options

      * Set Options

      * Module

      * Initialize Python

    * Configuration Options

    * Runtime Python configuration API

    * PyConfig C API

      * Ejemplo

      * PyWideStringList

      * PyStatus

      * PyPreConfig

      * Preinicialización de Python con PyPreConfig

      * PyConfig

      * Inicialización con PyConfig

      * Configuración aislada

      * Configuración de Python

      * Configuración de la ruta de Python

    * Py_GetArgcArgv()

    * Delaying main module execution

  * Gestión de la memoria

    * Visión general

    * Dominios del asignador

    * Interfaz de memoria sin procesar

    * Interfaz de memoria

      * Deprecated aliases

    * Asignadores de objetos

    * Asignadores de memoria predeterminados

    * Personalizar asignadores de memoria

    * Configurar enlaces para detectar errores en las funciones del
      asignador de memoria de Python

    * El asignador pymalloc

      * Personalizar asignador de arena de pymalloc

    * El asignador mimalloc

    * tracemalloc C API

    * Ejemplos

  * Soporte de implementación de objetos

    * Allocating objects on the heap

      * Soft-deprecated aliases

    * Object Life Cycle

      * Life Events

      * Cyclic Isolate Destruction

      * Functions

    * Estructuras de objetos comunes

      * Tipos objeto base y macros

      * Implementando funciones y métodos

      * Acceder a atributos de tipos de extensión

        * Member flags

        * Member types

        * Defining Getters and Setters

    * Type Object Structures

      * Referencia rápida

        * "ranuras *tp*" (*tp slots*)

        * sub-ranuras (*sub-slots*)

        * ranura de *typedefs*

      * Definición de "PyTypeObject"

      * Ranuras (*Slots*) "PyObject"

      * Ranuras "PyVarObject"

      * Ranuras "PyTypeObject"

      * Tipos estáticos

      * Tipos Heap

      * Estructuras de objetos de números

      * Estructuras de objetos mapeo

      * Estructuras de objetos secuencia

      * Estructuras de objetos búfer

      * Estructuras de objetos asíncronos

      * Tipo Ranura *typedefs*

      * Ejemplos

    * Apoyo a la recolección de basura cíclica

      * Controlar el estado del recolector de basura

      * Consultar el estado del recolector de basura

  * Versiones de API y ABI

    * Build-time version constants

    * Run-time version

    * Bit-packing macros

  * Monitoring C API

  * Generating Execution Events

    * Managing the Monitoring State

* Installing Python modules

  * Palabras clave

  * Uso básico

  * ¿Cómo...

    * ... instalo paquetes solamente para el usuario actual?

    * ... instalo paquetes científicos de Python?

    * ... trabajo con múltiples versiones de Python instaladas en
      paralelo?

  * Problemas de instalación comunes

    * Instalando en el Python del sistema bajo Linux

    * Pip no está instalado

    * Instalando extensiones binarias

* Comos (*HOWTOs*) de Python

* Preguntas más frecuentes de Python

  * Preguntas frecuentes generales sobre Python

    * Información general

    * Python en el mundo real

  * Preguntas frecuentes de programación

    * General questions

    * Core language

    * Números y cadenas

    * Rendimiento

    * Sequences (tuples/lists)

    * Objetos

    * Módulos

  * Preguntas frecuentes sobre diseño e historia

    * ¿Por qué Python usa indentación para agrupar declaraciones?

    * ¿Por qué obtengo resultados extraños con operaciones aritméticas
      simples?

    * ¿Por qué los cálculos de punto flotante son tan inexactos?

    * ¿Por qué las cadenas de caracteres de Python son inmutables?

    * ¿Por qué debe usarse 'self' explícitamente en las definiciones y
      llamadas de métodos?

    * ¿Por qué no puedo usar una tarea en una expresión?

    * ¿Por qué Python usa métodos para alguna funcionalidad (por
      ejemplo, list.index()) pero funciones para otra (por ejemplo,
      len(list))?

    * ¿Por qué join() es un método de cadena de caracteres en lugar de
      un método de lista o tupla?

    * ¿Qué tan rápido van las excepciones?

    * ¿Por qué no hay un *switch* o una declaración *case* en Python?

    * ¿No puede emular hilos en el intérprete en lugar de confiar en
      una implementación de hilos específica del sistema operativo?

    * ¿Por qué las expresiones lambda no pueden contener sentencias?

    * ¿Se puede compilar Python en código máquina, C o algún otro
      lenguaje?

    * ¿Cómo gestiona Python la memoria?

    * ¿Por qué CPython no utiliza un esquema de recolección de basura
      más tradicional?

    * ¿Por qué no se libera toda la memoria cuando sale CPython?

    * ¿Por qué hay tipos de datos separados de tuplas y listas?

    * ¿Cómo se implementan las listas en Python?

    * ¿Cómo se implementan los diccionarios en CPython?

    * ¿Por qué las claves del diccionario deben ser inmutables?

    * ¿Por qué list.sort() no retorna la lista ordenada?

    * ¿Cómo se especifica y aplica una especificación de interfaz en
      Python?

    * ¿Por qué no hay goto?

    * ¿Por qué las cadenas de caracteres sin formato (r-strings) no
      pueden terminar con una barra diagonal inversa?

    * ¿Por qué Python no tiene una declaración "with" para las
      asignaciones de atributos?

    * ¿Por qué los generadores no admiten la declaración with?

    * ¿Por qué se requieren dos puntos para las declaraciones
      if/while/def/class?

    * ¿Por qué Python permite comas al final de las listas y tuplas?

  * Preguntas frecuentes sobre bibliotecas y extensiones

    * Cuestiones generales sobre bibliotecas

    * Tareas comunes

    * Hilos

    * Entrada y salida

    * Programación de Redes/Internet

    * Bases de datos

    * Matemáticas y numérica

  * Extendiendo/Embebiendo FAQ

    * ¿Puedo crear mis propias funciones en C?

    * ¿Puedo crear mis propias funciones en C++?

    * Escribir en C es difícil; ¿no hay otra alternativa?

    * ¿Cómo puedo ejecutar declaraciones arbitrarias de Python desde
      C?

    * ¿Cómo puedo evaluar una expresión arbitraria de Python desde C?

    * ¿Cómo extraigo valores C de un objeto Python?

    * ¿Cómo utilizo Py_BuildValue() para crear una tupla de un tamaño
      arbitrario?

    * ¿Cómo puedo llamar un método de un objeto desde C?

    * ¿Cómo obtengo la salida de PyErr_Print() (o cualquier cosa que
      se imprime a stdout/stderr)?

    * ¿Cómo accedo al módulo escrito en Python desde C?

    * ¿Cómo hago una interface a objetos C++ desde Python?

    * He agregado un módulo usando el archivo de configuración y el
      *make* falla. ¿Porque?

    * ¿Cómo puedo depurar una extensión?

    * Quiero compilar un módulo Python en mi sistema Linux, pero me
      faltan algunos archivos . ¿Por qué?

    * ¿Cómo digo "entrada incompleta" desde "entrada inválida"?

    * ¿Cómo encuentro símbolos g++ __builtin_new o __pure_virtual?

    * ¿Puedo crear una clase objeto con algunos métodos implementado
      en C y otros en Python (por ejemplo a través de la herencia)?

  * Preguntas frecuentes sobre Python en Windows

    * ¿Cómo ejecutar un programa Python en Windows?

    * ¿Cómo hacer que los scripts de Python sean ejecutables?

    * ¿Por qué Python tarda en comenzar?

    * ¿Cómo hacer un ejecutable a partir de un script de Python?

    * ¿Es un archivo "*.pyd" lo mismo que una DLL?

    * ¿Cómo puedo integrar Python en una aplicación de Windows?

    * ¿Cómo puedo evitar que mi editor inserte pestañas en mi archivo
      fuente de Python?

    * ¿Cómo verifico una pulsación de tecla sin bloquearla?

    * ¿Cómo resuelvo el error de api-ms-win-crt-runtime-l1-1-0.dll no
      encontrado?

  * Preguntas frecuentes sobre la Interfaz Gráfica de Usuario (*GUI*)

    * Preguntas generales de la GUI

    * ¿Qué conjuntos de herramientas de GUI existen para Python?

    * Preguntas de Tkinter

  * "¿Por qué está Python instalado en mi ordenador?" FAQ

    * ¿Qué es Python?

    * ¿Por qué Python está instalado en mi máquina?

    * ¿Puedo eliminar Python?

* Desusos

  * Pending removal in Python 3.15

  * Pending removal in Python 3.16

  * Pending removal in Python 3.17

  * Pending removal in Python 3.18

  * Pending removal in Python 3.19

  * Pending removal in future versions

  * C API deprecations

    * Pending removal in Python 3.15

    * Pending removal in Python 3.18

    * Pending removal in future versions

* Glosario

* About this documentation

  * Contributors to the Python documentation

* Lidiar con errores

  * Documentación de errores

  * Utilizar el issue tracker de Python

  * Para empezar a contribuir en Python

* Derechos de autor

* Historia y Licencia

  * Historia del software

  * Términos y condiciones para acceder o usar Python

    * PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2

    * ACUERDO DE LICENCIA DE BEOPEN.COM PARA PYTHON 2.0

    * ACUERDO DE LICENCIA CNRI PARA PYTHON 1.6.1

    * ACUERDO DE LICENCIA CWI PARA PYTHON 0.9.0 HASTA 1.2

    * ZERO-CLAUSE BSD LICENSE FOR CODE IN THE PYTHON DOCUMENTATION

  * Licencias y reconocimientos para software incorporado

    * Mersenne Twister

    * Sockets

    * Servicios de socket asincrónicos

    * Gestión de cookies

    * Seguimiento de ejecución

    * funciones UUencode y UUdecode

    * Llamadas a procedimientos remotos XML

    * test_epoll

    * Seleccionar kqueue

    * SipHash24

    * strtod y dtoa

    * OpenSSL

    * expat

    * libffi

    * zlib

    * cfuhash

    * libmpdec

    * Conjunto de pruebas W3C C14N

    * mimalloc

    * asyncio

    * Global Unbounded Sequences (GUS)

    * Zstandard bindings

    * Unicode Character Database
