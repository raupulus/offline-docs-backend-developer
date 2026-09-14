---
title: La biblioteca estándar de Python
source_url: https://docs.python.org/es/3
source_path: library/index.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2990
---

# La biblioteca estándar de Python

Aunque Referencia del Lenguaje Python  describe la sintaxis y
semántica precisa del lenguaje Python, este manual de referencia de la
biblioteca describe la biblioteca estándar que se distribuye con
Python. También describe algunos componentes opcionales que son
usualmente incluidos en las distribuciones de Python.

La biblioteca estándar de Python es muy amplia, y ofrece una gran
cantidad de producciones como puede verse en la larga lista de
contenidos. La biblioteca contiene módulos incorporados (escritos en
C) que brindan acceso a las funcionalidades del sistema como entrada y
salida de archivos que serían de otra forma inaccesibles para los
programadores en Python, así como módulos escritos en Python que
proveen soluciones estandarizadas para los diversos problemas que
pueden ocurrir en el día a día en la programación. Algunos de éstos
módulos están diseñados explícitamente para alentar y reforzar la
portabilidad de los programas en Python abstrayendo especificidades de
las plataformas para lograr APIs neutrales a la plataforma.

Los instaladores de Python para la plataforma Windows frecuentemente
incluyen la biblioteca estándar completa y suelen también incluir
muchos componentes adicionales. Para los sistemas operativos tipo Unix
Python suele ser provisto como una colección de paquetes, así que
puede requerirse usar las herramientas de empaquetado disponibles en
los sistemas operativos para obtener algunos o todos los componentes
opcionales.

Además de la biblioteca estándar, existe un colección creciente de
varios miles de componentes (abarcando módulos o programas
individuales, paquetes o *frameworks* completos de desarrollo de
aplicaciones), disponibles en el Python Package Index.

* Introducción

  * Notas sobre la disponibilidad

* Funciones incorporadas

* Constantes incorporadas

  * Constantes agregadas por el módulo "site"

* Tipos integrados

  * Evaluar como valor verdadero/falso

  * Operaciones booleanas --- "and", "or", "not"

  * Comparaciones

  * Tipos numéricos --- "int", "float", "complex"

  * Tipo Booleano --- "bool"

  * Tipos de iteradores

  * Tipos secuencia --- "list", "tuple", "range"

  * Text and Binary Sequence Type Methods Summary

  * Cadenas de caracteres --- "str"

  * Tipos de secuencias binarias --- "bytes", "bytearray" y
    "memoryview"

  * Conjuntos --- "set", "frozenset"

  * Tipos mapa --- "dict"

  * Tipos gestores de contexto

  * Tipos de anotaciones de type — *alias genérico*, *Union*

  * Otros tipos predefinidos

  * Atributos especiales

  * Limitación de longitud de conversión de cadena de tipo entero

* Excepciones incorporadas

  * Contexto de una excepción

  * Heredando de excepciones incorporadas

  * Clases base

  * Excepciones específicas

  * Advertencias

  * Grupos de excepciones

  * Jerarquía de excepción

* Thread Safety Guarantees

  * Thread safety levels

  * Thread safety for list objects

  * Thread safety for dict objects

  * Thread safety for set objects

  * Thread safety for bytearray objects

  * Thread safety for memoryview objects

* Servicios de procesamiento de texto

  * "string" --- Common string operations

  * "string.templatelib" --- Support for template string literals

  * "re" --- Regular expression operations

  * "difflib" --- Helpers for computing deltas

  * "textwrap" --- Text wrapping and filling

  * "unicodedata" --- Unicode Database

  * "stringprep" --- Internet String Preparation

  * "readline" --- GNU readline interface

  * "rlcompleter" --- Completion function for GNU readline

* Servicios de datos binarios

  * "struct" --- Interpret bytes as packed binary data

  * "codecs" --- Codec registry and base classes

* Tipos de datos

  * "datetime" --- Basic date and time types

  * "zoneinfo" --- IANA time zone support

  * "calendar" --- General calendar-related functions

  * "collections" --- Container datatypes

  * "collections.abc" --- Abstract Base Classes for Containers

  * "heapq" --- Heap queue algorithm

  * "bisect" --- Array bisection algorithm

  * "array" --- Efficient arrays of numeric values

  * "weakref" --- Weak references

  * "types" --- Dynamic type creation and names for built-in types

  * "copy" --- Shallow and deep copy operations

  * "pprint" --- Data pretty printer

  * "reprlib" --- Alternate "repr()" implementation

  * "enum" --- Support for enumerations

  * "graphlib" --- Functionality to operate with graph-like structures

* Módulos numéricos y matemáticos

  * "numbers" --- Numeric abstract base classes

  * "math" --- Mathematical functions

  * "cmath" --- Mathematical functions for complex numbers

  * "decimal" --- Decimal fixed-point and floating-point arithmetic

  * "fractions" --- Rational numbers

  * "random" --- Generate pseudo-random numbers

  * "statistics" --- Mathematical statistics functions

* Módulos de programación funcional

  * "itertools" --- Functions creating iterators for efficient looping

  * "functools" --- Higher-order functions and operations on callable
    objects

  * "operator" --- Standard operators as functions

* Acceso a archivos y directorios

  * "pathlib" --- Rutas de sistemas orientada a objetos

  * "os.path" --- Common pathname manipulations

  * "stat" --- Interpreting "stat()" results

  * "filecmp" --- File and Directory Comparisons

  * "tempfile" --- Generate temporary files and directories

  * "glob" --- Unix style pathname pattern expansion

  * "fnmatch" --- Unix filename pattern matching

  * "linecache" --- Random access to text lines

  * "shutil" --- High-level file operations

* Persistencia de datos

  * "pickle" --- Python object serialization

  * "copyreg" --- Register "pickle" support functions

  * "shelve" --- Python object persistence

  * "marshal" --- Internal Python object serialization

  * "dbm" --- Interfaces to Unix "databases"

  * "sqlite3" --- DB-API 2.0 interfaz para bases de datos SQLite

* Compresión de datos y archivado

  * The "compression" package

  * "compression.zstd" --- Compression compatible with the Zstandard
    format

  * "zlib" --- Compression compatible with **gzip**

  * "gzip" --- Support for **gzip** files

  * "bz2" --- Support for **bzip2** compression

  * "lzma" --- Compression using the LZMA algorithm

  * "zipfile" --- Work with ZIP archives

  * "tarfile" --- Read and write tar archive files

* Formatos de archivo

  * "csv" --- CSV File Reading and Writing

  * "configparser" --- Configuration file parser

  * "tomllib" --- Parse TOML files

  * "netrc" --- netrc file processing

  * "plistlib" --- Generate and parse Apple ".plist" files

* Servicios criptográficos

  * "hashlib" --- Secure hashes and message digests

  * "hmac" --- Keyed-Hashing for Message Authentication

  * "secrets" --- Generate secure random numbers for managing secrets

* Servicios genéricos del sistema operativo

  * "os" --- Interfaces misceláneas del sistema operativo

  * "io" --- Core tools for working with streams

  * "time" --- Time access and conversions

  * "logging" --- Logging facility for Python

  * "logging.config" --- Logging configuration

  * "logging.handlers" --- Logging handlers

  * "platform" ---  Access to underlying platform's identifying data

  * "errno" --- Standard errno system symbols

  * "ctypes" --- A foreign function library for Python

* Command-line interface libraries

  * "argparse" --- Parser for command-line options, arguments and
    subcommands

  * "optparse" --- Parser for command line options

  * "getpass" --- Portable password input

  * "fileinput" --- Iterate over lines from multiple input streams

  * "curses" --- Terminal handling for character-cell displays

  * "curses.textpad" --- Text input widget for curses programs

  * "curses.ascii" --- Utilities for ASCII characters

  * "curses.panel" --- A panel stack extension for curses

  * "cmd" --- Support for line-oriented command interpreters

* Ejecución concurrente

  * "threading" --- Thread-based parallelism

  * "multiprocessing" --- Process-based parallelism

  * "multiprocessing.shared_memory" --- Shared memory for direct
    access across processes

  * El paquete "concurrent"

  * "concurrent.futures" --- Launching parallel tasks

  * "concurrent.interpreters" --- Multiple interpreters in the same
    process

  * "subprocess" --- Subprocess management

  * "sched" --- Event scheduler

  * "queue" --- A synchronized queue class

  * "contextvars" --- Context Variables

  * "_thread" --- Low-level threading API

* Comunicación en redes y entre procesos

  * "asyncio" --- Asynchronous I/O

  * "socket" --- Low-level networking interface

  * "ssl" --- TLS/SSL wrapper for socket objects

  * "select" --- Waiting for I/O completion

  * "selectors" --- High-level I/O multiplexing

  * "signal" --- Set handlers for asynchronous events

  * "mmap" --- Memory-mapped file support

* Manejo de datos de internet

  * "email" --- An email and MIME handling package

  * "json" --- JSON encoder and decoder

  * "mailbox" --- Manipulate mailboxes in various formats

  * "mimetypes" --- Map filenames to MIME types

  * "base64" --- Base16, Base32, Base64, Base85 Data Encodings

  * "binascii" --- Convert between binary and ASCII

  * "quopri" --- Encode and decode MIME quoted-printable data

* Herramientas Para Procesar Formatos de Marcado Estructurado

  * "html" --- HyperText Markup Language support

  * "html.parser" --- Simple HTML and XHTML parser

  * "html.entities" --- Definitions of HTML general entities

  * Módulos de procesamiento XML

  * "xml.etree.ElementTree" --- The ElementTree XML API

  * "xml.dom" --- The Document Object Model API

  * "xml.dom.minidom" --- Minimal DOM implementation

  * "xml.dom.pulldom" --- Support for building partial DOM trees

  * "xml.sax" --- Support for SAX2 parsers

  * "xml.sax.handler" --- Base classes for SAX handlers

  * "xml.sax.saxutils" --- SAX Utilities

  * "xml.sax.xmlreader" --- Interface for XML parsers

  * "xml.parsers.expat" --- Fast XML parsing using Expat

* Protocolos y soporte de Internet

  * "webbrowser" --- Convenient web-browser controller

  * "wsgiref" --- WSGI Utilities and Reference Implementation

  * "urllib" --- URL handling modules

  * "urllib.request" --- Extensible library for opening URLs

  * "urllib.response" --- Response classes used by urllib

  * "urllib.parse" --- Parse URLs into components

  * "urllib.error" --- Exception classes raised by urllib.request

  * "urllib.robotparser" ---  Parser for robots.txt

  * "http" --- HTTP modules

  * "http.client" --- HTTP protocol client

  * "ftplib" --- FTP protocol client

  * "poplib" --- POP3 protocol client

  * "imaplib" --- IMAP4 protocol client

  * "smtplib" --- SMTP protocol client

  * "uuid" --- UUID objects according to **RFC 9562**

  * "socketserver" --- A framework for network servers

  * "http.server" --- HTTP servers

  * "http.cookies" --- HTTP state management

  * "http.cookiejar" --- Cookie handling for HTTP clients

  * "xmlrpc" --- Módulos XMLRPC para cliente y servidor

  * "xmlrpc.client" --- XML-RPC client access

  * "xmlrpc.server" --- Basic XML-RPC servers

  * "ipaddress" --- IPv4/IPv6 manipulation library

* Servicios Multimedia

  * "wave" --- Read and write WAV files

  * "colorsys" --- Conversions between color systems

* Internacionalización

  * "gettext" --- Multilingual internationalization services

  * "locale" --- Internationalization services

* Graphical user interfaces with Tk

  * "tkinter" --- Python interface to Tcl/Tk

  * "tkinter.colorchooser" --- Color choosing dialog

  * "tkinter.font" --- Tkinter font wrapper

  * Tkinter dialogs

  * "tkinter.messagebox" --- Tkinter message prompts

  * "tkinter.scrolledtext" --- Scrolled text widget

  * "tkinter.dnd" --- Drag and drop support

  * "tkinter.ttk" --- Tk themed widgets

  * IDLE --- Python editor and shell

  * "turtle" --- Turtle graphics

* Herramientas de desarrollo

  * "typing" --- Support for type hints

  * "pydoc" --- Documentation generator and online help system

  * Modo de desarrollo de Python

  * "doctest" --- Test interactive Python examples

  * "unittest" --- Unit testing framework

  * "unittest.mock" --- mock object library

  * "unittest.mock" --- getting started

  * "test" --- Regression tests package for Python

  * "test.support" --- Utilities for the Python test suite

  * "test.support.socket_helper" --- Utilities for socket tests

  * "test.support.script_helper" --- Utilities for the Python
    execution tests

  * "test.support.bytecode_helper" --- Support tools for testing
    correct bytecode generation

  * "test.support.threading_helper" --- Utilities for threading tests

  * "test.support.os_helper" --- Utilities for os tests

  * "test.support.import_helper" --- Utilities for import tests

  * "test.support.warnings_helper" --- Utilities for warnings tests

* Depuración y perfilado

  * Tabla de auditoría de eventos

  * "bdb" --- Debugger framework

  * "faulthandler" --- Dump the Python traceback

  * "pdb" --- The Python Debugger

  * Los perfiladores de Python

  * "timeit" --- Measure execution time of small code snippets

  * "trace" --- Trace or track Python statement execution

  * "tracemalloc" --- Trace memory allocations

* Empaquetado y distribución de software

  * "ensurepip" --- Bootstrapping the "pip" installer

  * "venv" --- Creation of virtual environments

  * "zipapp" --- Manage executable Python zip archives

* Servicios en tiempo de ejecución de Python

  * "sys" --- System-specific parameters and functions

  * "sys.monitoring" --- Execution event monitoring

  * "sysconfig" --- Provide access to Python's configuration
    information

  * "builtins" --- Built-in objects

  * "__main__" --- Top-level code environment

  * "warnings" --- Warning control

  * "dataclasses" --- Data Classes

  * "contextlib" --- Utilidades para declaraciones de contexto "with"

  * "abc" --- Abstract Base Classes

  * "atexit" --- Exit handlers

  * "traceback" --- Print or retrieve a stack traceback

  * "__future__" --- Future statement definitions

  * "gc" --- Garbage Collector interface

  * "inspect" --- Inspect live objects

  * "annotationlib" --- Functionality for introspecting annotations

  * "site" --- Site-specific configuration hook

* Intérpretes de Python personalizados

  * "code" --- Interpreter base classes

  * "codeop" --- Compile Python code

* Importando módulos

  * "zipimport" --- Import modules from Zip archives

  * "pkgutil" --- Package extension utility

  * "modulefinder" --- Find modules used by a script

  * "runpy" --- Localización y ejecución de módulos Python

  * "importlib" --- La implementación de "import"

  * "importlib.resources" -- Package resource reading, opening and
    access

  * "importlib.resources.abc" -- Abstract base classes for resources

  * "importlib.metadata" -- Acceso a los metadatos de los paquetes

  * La inicialización de la ruta de búsqueda de módulo de "sys.path"

* Servicios del lenguaje Python

  * "ast" --- Abstract syntax trees

  * "symtable" --- Access to the compiler's symbol tables

  * "token" --- Constants used with Python parse trees

  * "keyword" --- Testing for Python keywords

  * "tokenize" --- Tokenizer for Python source

  * "tabnanny" --- Detection of ambiguous indentation

  * "pyclbr" --- Python module browser support

  * "py_compile" --- Compile Python source files

  * "compileall" --- Byte-compile Python libraries

  * "dis" --- Desensamblador para bytecode de Python

  * "pickletools" --- Tools for pickle developers

* Servicios Específicos para MS Windows

  * "msvcrt" --- Useful routines from the MS VC++ runtime

  * "winreg" --- Windows registry access

  * "winsound" --- Sound-playing interface for Windows

* Unix-specific services

  * "shlex" --- Simple lexical analysis

  * "posix" --- The most common POSIX system calls

  * "pwd" --- The password database

  * "grp" --- The group database

  * "termios" --- POSIX style tty control

  * "tty" --- Terminal control functions

  * "pty" --- Pseudo-terminal utilities

  * "fcntl" --- The "fcntl" and "ioctl" system calls

  * "resource" --- Resource usage information

  * "syslog" --- Unix syslog library routines

* Modules command-line interface (CLI)

* Módulos reemplazados

  * "getopt" --- C-style parser for command line options

* Removed Modules

* Consideraciones de seguridad
