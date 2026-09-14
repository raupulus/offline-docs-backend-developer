---
title: Capa de objetos abstractos
source_url: https://docs.python.org/es/3
source_path: c-api/abstract.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 30
---

# Capa de objetos abstractos

Las funciones de este capítulo interactúan con los objetos de Python
independientemente de su tipo, o con amplias clases de tipos de
objetos (por ejemplo, todos los tipos numéricos o todos los tipos de
secuencia). Cuando se usan en tipos de objetos para los que no se
aplican, lanzarán una excepción de Python.

No es posible utilizar estas funciones en objetos que no se
inicializan correctamente, como un objeto de lista que ha sido creado
por "PyList_New()", pero cuyos elementos no se han establecido en
algunos valores no-"NULL" aún.

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
