---
title: El atributo Attribute
source_url: https://www.php.net/manual/es/class.attribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/attributes/attribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 5e36b489f
order: 2900
---

## Introducción

Los atributos ofrecen la capacidad de añadir información de metadatos estructurados y legibles por máquina en las declaraciones del código: Clases, métodos, funciones, argumentos, propiedades y constantes de clase pueden ser el objetivo de un atributo. Los metadatos definidos por los atributos pueden entonces ser inspeccionados en tiempo de ejecución usando las [APIs de Reflexión](#book.reflection). Los atributos podrían por lo tanto ser considerados como un lenguaje de configuración integrado directamente en el código.

## Sinopsis de la clase

\#\[\Attribute\]

final

Attribute

Constantes

const

int

Attribute::TARGET_CLASS

const

int

Attribute::TARGET_FUNCTION

const

int

Attribute::TARGET_METHOD

const

int

Attribute::TARGET_PROPERTY

const

int

Attribute::TARGET_CLASS_CONSTANT

const

int

Attribute::TARGET_PARAMETER

const

int

Attribute::TARGET_CONSTANT

const

int

Attribute::TARGET_ALL

const

int

Attribute::IS_REPEATABLE

Propiedades

public

int

flags

Métodos

## Constantes predefinidas

`Attribute::TARGET_CLASS`  

`Attribute::TARGET_FUNCTION`  

`Attribute::TARGET_METHOD`  

`Attribute::TARGET_PROPERTY`  

`Attribute::TARGET_CLASS_CONSTANT`  

`Attribute::TARGET_PARAMETER`  

`Attribute::TARGET_CONSTANT`  

`Attribute::TARGET_ALL`  

`Attribute::IS_REPEATABLE`  

## Propiedades

`flags`  

## Historial de cambios

| Versión | Descripción                                 |
|---------|---------------------------------------------|
| 8.5.0   | Se ha añadido `Attribute::TARGET_CONSTANT`. |

## Véase también

[Visión general de los atributos](#language.attributes)
