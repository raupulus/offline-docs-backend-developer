---
title: La clase ReflectionAttribute
source_url: https://www.php.net/manual/es/class.reflectionattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_revision: 51fc0eaf8
order: 69040
---

## Introducción

La clase `ReflectionAttribute` proporciona información sobre un [Atributo](#language.attributes).

## Sinopsis de la clase

ReflectionAttribute

implements

Reflector

Constantes

public

const

int

ReflectionAttribute::IS_INSTANCEOF

Propiedades

public

string

name

Métodos

## Propiedades

`name`  
El nombre del atributo.

## Constantes predefinidas

## Banderas ReflectionAttribute

`ReflectionAttribute::IS_INSTANCEOF` `int`  
Devuelve los atributos con una verificación `instanceof`.

> [!NOTE]
> Los valores de estas constantes pueden cambiar entre versiones de PHP. Se recomienda utilizar siempre las constantes y no confiar en los valores directamente.

## Historial de cambios

| Versión | Descripción                                        |
|---------|----------------------------------------------------|
| 8.4.0   | Todas las constantes de clase ahora están tipadas. |
| 8.4.0   | Se añadió ReflectionAttribute::\$name.             |
