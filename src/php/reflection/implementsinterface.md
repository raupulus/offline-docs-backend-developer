---
title: ReflectionClass::implementsInterface
description: Verifica si una clase implementa una interfaz
source_url: https://www.php.net/manual/es/reflectionclass.implementsinterface.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/implementsinterface.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 69400
---

ReflectionClass::implementsInterface

Verifica si una clase implementa una interfaz

## Descripción

```php
public ReflectionClass::implementsInterface(ReflectionClass $interface): bool
```php

Verifica si una clase implementa una interfaz.

## Parámetros

`interface`  
El nombre de la interfaz.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

ReflectionClass::implementsInterface lanza una `ReflectionException` si `interface` no es una interfaz.

## Véase también

ReflectionClass::isInterface, ReflectionClass::isSubclassOf, `interface_exists`, [Las interfaces](#language.oop5.interfaces)
