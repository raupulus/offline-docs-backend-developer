---
title: ReflectionClass::getConstants
description: Obtener constantes
source_url: https://www.php.net/manual/es/reflectionclass.getconstants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getconstants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 69090
---

ReflectionClass::getConstants

Obtener constantes

## Descripción

```php
public ReflectionClass::getConstants([int $filter]): array
```php

Obtiene todas las constantes definidas de una clase, independientemente de su visibilidad.

## Parámetros

`filter`  
El filtro opcional, para filtrar las visibilidades constantes deseadas. Se configura utiliando las [constantes de ReflectionClassConstant](#reflectionclassconstant.constants.modifiers), y por omisión tiene todas las constantes visibles.

## Valores devueltos

Un `array` de constantes. El nombre de la constante en la clave, y en el valor, el valor de la constante.

## Historial de cambios

| Versión | Descripción                      |
|---------|----------------------------------|
| 8.0.0   | Se añadió el parámetro `filter`. |

## Véase también

ReflectionClass::getConstant
