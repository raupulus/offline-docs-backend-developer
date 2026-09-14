---
title: La clase ReflectionMethod
source_url: https://www.php.net/manual/es/class.reflectionmethod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 51fc0eaf8
order: 71110
---

## Introducción

La clase `ReflectionMethod` proporciona información sobre un método.

## Sinopsis de la clase

ReflectionMethod

extends

ReflectionFunctionAbstract

Constantes

public

const

int

ReflectionMethod::IS_STATIC

public

const

int

ReflectionMethod::IS_PUBLIC

public

const

int

ReflectionMethod::IS_PROTECTED

public

const

int

ReflectionMethod::IS_PRIVATE

public

const

int

ReflectionMethod::IS_ABSTRACT

public

const

int

ReflectionMethod::IS_FINAL

Propiedades

public

string

class

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`name`  
Nombre del método

`class`  
Nombre de la clase

## Constantes predefinidas

## Modificadores de ReflectionMethod

`ReflectionMethod::IS_STATIC` `int`  
Indica que el método es estático Anterior a PHP 7.4.0, el valor era `1`.

`ReflectionMethod::IS_PUBLIC` `int`  
Indica que el método es público Anterior a PHP 7.4.0, el valor era `256`.

`ReflectionMethod::IS_PROTECTED` `int`  
Indica que el método es protegido Anterior a PHP 7.4.0, el valor era `512`.

`ReflectionMethod::IS_PRIVATE` `int`  
Indica que el método es privado Anterior a PHP 7.4.0, el valor era `1024`.

`ReflectionMethod::IS_ABSTRACT` `int`  
Indica que el método es abstracto Anterior a PHP 7.4.0, el valor era `2`.

`ReflectionMethod::IS_FINAL` `int`  
Indica que el método es final Anterior a PHP 7.4.0, el valor era `4`.

> [!NOTE]
> El valor de estas constantes puede cambiar entre versiones de PHP. Se recomienda siempre utilizar las constantes y no depender de los valores directamente.

## Historial de cambios

| Versión | Descripción                                  |
|---------|----------------------------------------------|
| 8.4.0   | Las constantes de clase ahora están tipadas. |
| 8.0.0   | ReflectionMethod::export ha sido eliminada.  |
