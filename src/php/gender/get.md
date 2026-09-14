---
title: Gender\Gender::get
description: Obtiene el género de un nombre
source_url: https://www.php.net/manual/es/gender-gender.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gender/gender/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gender
translation_status: ready
translation_reviewed: false
translation_revision: 1742a682c
order: 26040
---

Gender\Gender::get

Obtiene el género de un nombre

## Descripción

```php
public Gender\Gender::get(string $name, [int $country]): int
```php

Obtiene el género de un nombre para un país específico.

## Parámetros

`name`  
El nombre a verificar.

`country`  
El identificador del país (una constante de la clase Gender).

## Valores devueltos

Devuelve el género del nombre.
