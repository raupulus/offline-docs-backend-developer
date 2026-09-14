---
title: Herramientas de desarrollo
source_url: https://docs.python.org/es/3
source_path: library/development.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2300
---

# Herramientas de desarrollo

Los módulos descritos en este capítulo le ayudan a escribir software.
Por ejemplo, el módulo "pydoc" toma un módulo y genera documentación
basada en el contenido del módulo.  Los módulos "doctest" y "unittest"
contienen frameworks para escribir pruebas unitarias que ejecutan y
validan automáticamente el código, verificando que se produce la
salida esperada.

La lista de módulos descritos en este capítulo es:

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

  * Línea de tiempo de obsolescencia de características principales

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

  * Order of precedence of "side_effect", "return_value" and *wraps*

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

  * Ejecución de pruebas utilizando la interfaz de línea de comandos

* "test.support" --- Utilities for the Python test suite

* "test.support.socket_helper" --- Utilities for socket tests

* "test.support.script_helper" --- Utilities for the Python execution
  tests

* "test.support.bytecode_helper" --- Support tools for testing correct
  bytecode generation

* "test.support.threading_helper" --- Utilities for threading tests

* "test.support.os_helper" --- Utilities for os tests

* "test.support.import_helper" --- Utilities for import tests

* "test.support.warnings_helper" --- Utilities for warnings tests
