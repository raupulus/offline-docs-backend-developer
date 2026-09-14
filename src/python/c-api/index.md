---
title: Python/C API reference manual
source_url: https://docs.python.org/es/3
source_path: c-api/index.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 350
---

# Python/C API reference manual

Este manual documenta la API utilizada por los programadores de C y C
++ que desean escribir módulos de extensión o incorporar Python. Es un
complemento de Ampliación e incrustación del intérprete de Python, que
describe los principios generales de la escritura de extensión pero no
documenta las funciones API en detalle.

* Introducción

  * Language version compatibility

  * Estándares de codificación

  * Archivos de cabecera (*Include*)

  * Macros útiles

  * Objetos, tipos y conteos de referencias

  * Excepciones

  * Integración de Python

  * Depuración de compilaciones

  * Recommended third party tools

* Estabilidad de la API en C

  * Unstable C API

  * Interfaz binaria de aplicación estable

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

  * Conversión y formato de cadenas de caracteres

  * Character classification and conversion

  * PyHash API

  * Reflexión

  * Registro de códec y funciones de soporte

  * PyTime C API

  * Soporte para Mapeo Perf

* Capa de objetos abstractos

  * Protocolo de objeto

  * Protocolo de llamada

  * Protocolo de números

  * Protocolo de secuencia

  * Protocolo de mapeo

  * Protocolo iterador

  * Protocolo búfer

* Capa de objetos concretos

  * Objetos fundamentales

  * Objetos numéricos

  * Objetos de secuencia

  * Objetos contenedor

  * Objetos de función

  * Otros objetos

  * C API for extension modules

* Interpreter initialization and finalization

  * Before Python initialization

  * Global configuration variables

  * Initializing and finalizing the interpreter

  * Cautions regarding runtime finalization

  * Process-wide parameters

* Thread states and the global interpreter lock

  * Detaching the thread state from extension code

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

  * Configuration Options

  * Runtime Python configuration API

  * PyConfig C API

  * Py_GetArgcArgv()

  * Delaying main module execution

* Gestión de la memoria

  * Visión general

  * Dominios del asignador

  * Interfaz de memoria sin procesar

  * Interfaz de memoria

  * Asignadores de objetos

  * Asignadores de memoria predeterminados

  * Personalizar asignadores de memoria

  * Configurar enlaces para detectar errores en las funciones del
    asignador de memoria de Python

  * El asignador pymalloc

  * El asignador mimalloc

  * tracemalloc C API

  * Ejemplos

* Soporte de implementación de objetos

  * Allocating objects on the heap

  * Object Life Cycle

  * Estructuras de objetos comunes

  * Type Object Structures

  * Apoyo a la recolección de basura cíclica

* Versiones de API y ABI

  * Build-time version constants

  * Run-time version

  * Bit-packing macros

* Monitoring C API

* Generating Execution Events

  * Managing the Monitoring State
