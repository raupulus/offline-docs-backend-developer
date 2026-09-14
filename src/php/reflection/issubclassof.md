---
title: ReflectionClass::isSubclassOf
description: Verifica si la clase es una subclase
source_url: https://www.php.net/manual/es/reflectionclass.issubclassof.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/issubclassof.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_revision: 84f256090
order: 69550
---

ReflectionClass::isSubclassOf

Verifica si la clase es una subclase

## Descripción

```php
public ReflectionClass::isSubclassOf(ReflectionClass $class): bool
```php

Verifica si la clase es una subclase de la clase especificada o implementa una interfaz especificada.

## Parámetros

`class`  
Puede ser el nombre de la clase como `string` o un objeto `ReflectionClass` de la clase a verificar.

## Valores devueltos

Retorna `true` si la clase es una subclase de la clase o interfaz especificada, o `false` en caso contrario.

## Véase también

ReflectionClass::isInterface, ReflectionClass::implementsInterface, `is_subclass_of`, `get_parent_class`
