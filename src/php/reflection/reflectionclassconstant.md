---
title: La classe ReflectionClassConstant
source_url: https://www.php.net/manual/es/class.reflectionclassconstant.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclassconstant.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_revision: 51fc0eaf8
order: 69870
---

## Introducción

La classe `ReflectionClassConstant` proporciona información sobre una constante de clase.

## Sinopsis de la clase

ReflectionClassConstant

implements

Reflector

Constantes

public

const

int

ReflectionClassConstant::IS_PUBLIC

public

const

int

ReflectionClassConstant::IS_PROTECTED

public

const

int

ReflectionClassConstant::IS_PRIVATE

public

const

int

ReflectionClassConstant::IS_FINAL

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
Nombre de la constante de clase. Solo lectura, genera una `ReflectionException` al intentar modificarla.

`class`  
Nombre de la clase donde se define la constante de clase. Solo lectura, genera una `ReflectionException` al intentar modificarla.

## Constantes predefinidas

## Modificadores de ReflectionClassConstant

`ReflectionClassConstant::IS_PUBLIC` `int`  
Indica las constantes [public](#language.oop5.visibility). Anterior a PHP 7.4.0, el valor era `256`.

`ReflectionClassConstant::IS_PROTECTED` `int`  
Indica las constantes [protected](#language.oop5.visibility). Anterior a PHP 7.4.0, el valor era `512`.

`ReflectionClassConstant::IS_PRIVATE` `int`  
Indica las constantes [private](#language.oop5.visibility). Anterior a PHP 7.4.0, el valor era `1024`.

`ReflectionClassConstant::IS_FINAL` `int`  
Indica las constantes [final](#language.oop5.final) Disponible a partir de PHP 8.1.0.

> [!NOTE]
> El valor de estas constantes puede cambiar entre versiones de PHP. Se recomienda siempre utilizar las constantes y no depender de los valores directamente.

## Historial de cambios

| Versión | Descripción                                        |
|---------|----------------------------------------------------|
| 8.4.0   | Las constantes de clase ahora están tipadas.       |
| 8.0.0   | ReflectionClassConstant::export ha sido eliminada. |
