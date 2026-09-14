---
title: Capa de objetos concretos
source_url: https://docs.python.org/es/3
source_path: c-api/concrete.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 170
---

# Capa de objetos concretos

Las funciones de este capítulo son específicas de ciertos tipos de
objetos de Python. Pasarles un objeto del tipo incorrecto no es una
buena idea; si recibe un objeto de un programa Python y no está seguro
de que tenga el tipo correcto, primero debe realizar una verificación
de tipo; por ejemplo, para verificar que un objeto es un diccionario,
utilice "PyDict_Check()". El capítulo está estructurado como el "árbol
genealógico" de los tipos de objetos Python.

Advertencia:

  Si bien las funciones descritas en este capítulo verifican
  cuidadosamente el tipo de objetos que se pasan, muchos de ellos no
  verifican si se pasa "NULL" en lugar de un objeto válido. Permitir
  que se pase "NULL" puede causar violaciones de acceso a la memoria y
  la terminación inmediata del intérprete.

## Objetos fundamentales

Esta sección describe los objetos de tipo Python y el objeto singleton
"None".

* Objetos tipo

  * Crear tipos asignados en montículo (*heap*)

* El objeto "None"

## Objetos numéricos

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

## Objetos de secuencia

Las operaciones genéricas en los objetos de secuencia se discutieron
en el capítulo anterior; Esta sección trata sobre los tipos
específicos de objetos de secuencia que son intrínsecos al lenguaje
Python.

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

## Objetos contenedor

* Objetos diccionario

  * Dictionary View Objects

  * Ordered Dictionaries

* Objetos conjunto

  * Deprecated API

## Objetos de función

* Objetos función

* Objetos de método de instancia

* Objetos método

* Objetos celda

* Objetos código

* Code Object Flags

* Extra information

## Otros objetos

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

## C API for extension modules

* Curses C API

* Internal data

* Objetos *DateTime*

* Internal data
