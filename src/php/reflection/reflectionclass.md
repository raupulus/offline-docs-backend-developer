---
title: La clase ReflectionClass
source_url: https://www.php.net/manual/es/class.reflectionclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: 51fc0eaf8
order: 69690
---

## Introducción

La clase `ReflectionClass` proporciona información sobre una clase.

## Sinopsis de la clase

ReflectionClass

implements

Reflector

Constantes

public

const

int

ReflectionClass::IS_IMPLICIT_ABSTRACT

public

const

int

ReflectionClass::IS_EXPLICIT_ABSTRACT

public

const

int

ReflectionClass::IS_FINAL

public

const

int

ReflectionClass::IS_READONLY

public

const

int

ReflectionClass::SKIP_INITIALIZATION_ON_SERIALIZE

public

const

int

ReflectionClass::SKIP_DESTRUCTOR

Propiedades

public

string

name

Métodos

## Propiedades

`name`  
Nombre de la clase. Solo lectura, lanza una `ReflectionException` al intentar escribir.

`ReflectionClass::SKIP_INITIALIZATION_ON_SERIALIZE` `int`  
Indica que `serialize` no debe desencadenar la inicialización de un objeto en carga perezosa.

`ReflectionClass::SKIP_DESTRUCTOR` `int`  
Indica que un destructor de objeto no debe ser llamado al reinicializarlo como objeto perezoso.

## Constantes predefinidas

## Modificadores de ReflectionClass

`ReflectionClass::IS_IMPLICIT_ABSTRACT` `int`  
Indica si la clase es [ abstracta](#language.oop5.abstract) porque contiene métodos abstractos.

`ReflectionClass::IS_EXPLICIT_ABSTRACT` `int`  
Indica si la clase es [ abstracta](#language.oop5.abstract) debido a su definición.

`ReflectionClass::IS_FINAL` `int`  
Indica si la clase es [final](#language.oop5.final).

`ReflectionClass::IS_READONLY` `int`  
Indica si la clase es [readonly](#language.oop5.basic.class.readonly).

## Historial de cambios

| Versión | Descripción                                  |
|---------|----------------------------------------------|
| 8.4.0   | Las constantes de clase ahora están tipadas. |
| 8.0.0   | ReflectionClass::export ha sido eliminada.   |
