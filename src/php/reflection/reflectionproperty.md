---
title: La clase ReflectionProperty
source_url: https://www.php.net/manual/es/class.reflectionproperty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: 51fc0eaf8
order: 71830
---

## Introducción

La clase `ReflectionProperty` proporciona información sobre las propiedades de las clases.

## Sinopsis de la clase

ReflectionProperty

implements

Reflector

Constantes

public

const

int

ReflectionProperty::IS_STATIC

public

const

int

ReflectionProperty::IS_READONLY

public

const

int

ReflectionProperty::IS_PUBLIC

public

const

int

ReflectionProperty::IS_PROTECTED

public

const

int

ReflectionProperty::IS_PRIVATE

public

const

int

ReflectionProperty::IS_ABSTRACT

public

const

int

ReflectionProperty::IS_PROTECTED_SET

public

const

int

ReflectionProperty::IS_PRIVATE_SET

public

const

int

ReflectionProperty::IS_VIRTUAL

public

const

int

ReflectionProperty::IS_FINAL

Propiedades

public

string

name

public

string

class

Métodos

## Propiedades

`name`  
Nombre de la propiedad. Solo lectura, lanza una `ReflectionException` al intentar escribir.

`class`  
Nombre de la clase donde se definió la propiedad. Solo lectura, lanza una `ReflectionException` al intentar escribir.

## Constantes predefinidas

## Modificadores de ReflectionProperty

`ReflectionProperty::IS_STATIC` `int`  
Indica que la propiedad es [static](#language.oop5.static). Anterior a PHP 7.4.0, el valor era `1`.

`ReflectionProperty::IS_READONLY` `int`  
Indica que la propiedad es [readonly](#language.oop5.properties.readonly-properties). Disponible a partir de PHP 8.1.0.

`ReflectionProperty::IS_PUBLIC` `int`  
Indica que la propiedad es [pública](#language.oop5.visibility). Anterior a PHP 7.4.0, el valor era `256`.

`ReflectionProperty::IS_PROTECTED` `int`  
Indica que la propiedad es [protegida](#language.oop5.visibility). Anterior a PHP 7.4.0, el valor era `512`.

`ReflectionProperty::IS_PRIVATE` `int`  
Indica que la propiedad es [privada](#language.oop5.visibility). Anterior a PHP 7.4.0, el valor era `1024`.

`ReflectionProperty::IS_ABSTRACT` `int`  
Indica que la propiedad es [abstracta](#language.oop5.abstract). Disponible a partir de PHP 8.4.0.

`ReflectionProperty::IS_PROTECTED_SET` `int`  
Disponible a partir de PHP 8.4.0.

`ReflectionProperty::IS_PRIVATE_SET` `int`  
Disponible a partir de PHP 8.4.0.

`ReflectionProperty::IS_VIRTUAL` `int`  
Disponible a partir de PHP 8.4.0.

`ReflectionProperty::IS_FINAL` `int`  
Indica que la propiedad es [final](#language.oop5.final). Disponible a partir de PHP 8.4.0.

> [!NOTE]
> El valor de estas constantes puede cambiar entre versiones de PHP. Se recomienda siempre utilizar las constantes y no depender de los valores directamente.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Las constantes de clase ahora están tipadas. |
| 8.4.0 | Se añadieron `ReflectionProperty::IS_VIRTUAL`, `ReflectionProperty::IS_PRIVATE_SET`, `ReflectionProperty::IS_PROTECTED_SET`, `ReflectionProperty::IS_ABSTRACT`, y `ReflectionProperty::IS_FINAL`. |
| 8.0.0 | ReflectionProperty::export ha sido eliminada. |
