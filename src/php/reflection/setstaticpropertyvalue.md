---
title: ReflectionClass::setStaticPropertyValue
description: Define el valor de una propiedad estática pública
source_url: https://www.php.net/manual/es/reflectionclass.setstaticpropertyvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/setstaticpropertyvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c4aabaa0b
order: 69670
---

ReflectionClass::setStaticPropertyValue

Define el valor de una propiedad estática pública

## Descripción

```php
public ReflectionClass::setStaticPropertyValue(string $name, mixed $value): void
```php

Define el valor de una propiedad estática pública. Si la propiedad es privada o protegida, el método fallará.

ReflectionProperty::setValue permite definir el valor de las propiedades públicas, privadas y protegidas.

## Parámetros

`name`  
El nombre de la propiedad.

`value`  
El nuevo valor para la propiedad.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | El uso de ReflectionClass::setStaticPropertyValue para definir una propiedad privada o protegida ahora produce un error fatal. Anteriormente, esto lanzaba una `ReflectionException`. |

## Véase también

ReflectionClass::getStaticPropertyValue, ReflectionProperty::setValue
