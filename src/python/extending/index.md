---
title: Ampliación e incrustación del intérprete de Python
source_url: https://docs.python.org/es/3
source_path: extending/index.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: extending
order: 1000
---

# Ampliación e incrustación del intérprete de Python

Este documento describe cómo escribir módulos en C o C++ para extender
el intérprete de Python con nuevos módulos. Esos módulos no solo
pueden definir nuevas funciones sino también nuevos tipos de objetos y
sus métodos. El documento también describe cómo incrustar el
intérprete de Python en otra aplicación, para usarlo como un lenguaje
de extensión. Finalmente, muestra cómo compilar y vincular módulos de
extensión para que puedan cargarse dinámicamente (en tiempo de
ejecución) en el intérprete, si el sistema operativo subyacente admite
esta característica.

Este documento asume conocimientos básicos sobre Python. Para una
introducción informal al lenguaje, consulte El tutorial de Python.
Referencia del Lenguaje Python da una definición más formal del
lenguaje. La biblioteca estándar de Python documenta los tipos de
objetos, funciones y módulos existentes (tanto incorporados como
escritos en Python) que le dan al lenguaje su amplio rango de
aplicaciones.

Para obtener una descripción detallada de toda la API de Python/C,
consulte el apartado separado Python/C API reference manual.

## Herramientas de terceros recomendadas

This guide only covers the basic tools for creating extensions
provided as part of this version of CPython. Some third party tools
offer both simpler and more sophisticated approaches to creating C and
C++ extensions for Python.

## Crear extensiones sin herramientas de terceros

Esta sección de la guía cubre la creación de extensiones C y C++ sin
la ayuda de herramientas de terceros. Está destinado principalmente a
los creadores de esas herramientas, en lugar de ser una forma
recomendada de crear sus propias extensiones C.

Ver también:

  **PEP 489** -- Multi-phase extension module initialization

* 1. Extendiendo Python con C o C++

  * 1.1. Un ejemplo simple

  * 1.2. Intermezzo: errores y excepciones

  * 1.3. De vuelta al ejemplo

  * 1.4. La tabla de métodos del módulo y la función de inicialización

  * 1.5. Compilación y enlazamiento

  * 1.6. Llamando funciones Python desde C

  * 1.7. Extracción de parámetros en funciones de extensión

  * 1.8. Parámetros de palabras clave para funciones de extensión

  * 1.9. Construyendo valores arbitrarios

  * 1.10. Conteo de referencias

  * 1.11. Escribiendo extensiones en C++

  * 1.12. Proporcionar una API C para un módulo de extensión

* 2. Definición de tipos de extensión: Tutorial

  * 2.1. Lo básico

  * 2.2. Agregar datos y métodos al ejemplo básico

  * 2.3. Proporcionar un control más preciso sobre los atributos de
    datos

  * 2.4. Apoyo a la recolección de basura cíclica

  * 2.5. Subclases de otros tipos

* 3. Definición de tipos de extensión: temas variados

  * 3.1. Finalización y desasignación

  * 3.2. Presentación de objetos

  * 3.3. Gestión de atributos

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

## Incrustar el tiempo de ejecución de CPython en una aplicación más grande

A veces, en lugar de crear una extensión que se ejecute dentro del
intérprete de Python como la aplicación principal, es conveniente
incorporar el tiempo de ejecución de CPython dentro de una aplicación
más grande. Esta sección cubre algunos de los detalles involucrados en
hacerlo con éxito.

* 1. Incrustando Python en otra aplicación

  * 1.1. Incrustación de muy alto nivel

  * 1.2. Más allá de la incrustación de muy alto nivel: una visión
    general

  * 1.3. Incrustación pura

  * 1.4. Extendiendo Python incrustado

  * 1.5. Incrustando Python en C++

  * 1.6. Compilar y enlazar bajo sistemas tipo Unix
