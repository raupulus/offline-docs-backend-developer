---
title: ReflectionReference::fromArrayElement
description: Crear un ReflectionReference desde un elemento de un array
source_url: https://www.php.net/manual/es/reflectionreference.fromarrayelement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionreference/fromarrayelement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: e50e79746
order: 71850
---

ReflectionReference::fromArrayElement

Crear un ReflectionReference desde un elemento de un array

## Descripción

```php
public static ReflectionReference::fromArrayElement(array $array, int $key): ReflectionReference
```php

Crear un `ReflectionReference` desde un elemento de un array.

## Parámetros

`array`  
El array que contiene la referencia potencial.

`key`  
La clave; sea un integer o un string.

## Valores devueltos

Devuelve una instancia de `ReflectionReference` si `$array[$key]` es una referencia, o null en caso contrario.

## Errores/Excepciones

Si `array` no es un array, o `key` no es un integer o string, se lanza una `TypeError`. Si `$array[$key]` no existe, se lanza una `ReflectionException`.
