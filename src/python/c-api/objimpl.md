---
title: Soporte de implementación de objetos
source_url: https://docs.python.org/es/3
source_path: c-api/objimpl.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 550
---

# Soporte de implementación de objetos

Este capítulo describe las funciones, los tipos y las macros
utilizados al definir nuevos tipos de objetos.

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
