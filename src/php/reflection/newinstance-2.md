---
title: ReflectionClass::newInstance
description: Crear una nueva instancia de la clase utilizando los argumentos proporcionados
source_url: https://www.php.net/manual/es/reflectionclass.newinstance.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/newinstance.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69600
---

ReflectionClass::newInstance

Crear una nueva instancia de la clase utilizando los argumentos proporcionados

## Descripción

```php
public ReflectionClass::newInstance(mixed ...$args): object
```php

Crear una nueva instancia de la clase utilizando los argumentos proporcionados a su constructor.

## Parámetros

`args`  
Acepta un número variable de argumentos que son pasados al constructor, como en la función `call_user_func`.

## Valores devueltos

## Errores/Excepciones

Una `ReflectionException` si el constructor no es público.

Una `ReflectionException` si la clase no tiene constructor y el parámetro `args` contiene al menos un argumento.

## Véase también

ReflectionClass::newInstanceArgs, ReflectionClass::newInstanceWithoutConstructor
