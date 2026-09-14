---
title: Servicios en tiempo de ejecución de Python
source_url: https://docs.python.org/es/3
source_path: library/python.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3600
---

# Servicios en tiempo de ejecución de Python

Los módulos descritos en este capítulo proporcionan una amplia gama de
servicios relacionados con el intérprete de Python y su interacción
con su entorno.  Esta es una descripción general:

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

* "sysconfig" --- Provide access to Python's configuration information

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

* "contextlib" --- Utilidades para declaraciones de contexto "with"

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

Ver también:

  * Consulte el módulo "concurrent.interpreters", que de manera
    similar expone funcionalidades centrales del entorno de ejecución.
