---
title: Gender\Gender::isNick
description: Verifica si name0 es un alias de name1
source_url: https://www.php.net/manual/es/gender-gender.isnick.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gender/gender/isnick.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gender
translation_status: ready
translation_reviewed: false
translation_revision: 1742a682c
order: 26050
---

Gender\Gender::isNick

Verifica si name0 es un alias de name1

## Descripción

```php
public Gender\Gender::isNick(string $name0, string $name1, [int $country]): array
```php

Verifica si name0 es un alias de name1.

## Parámetros

`name0`  
Nombre a verificar.

`name1`  
Nombre a verificar.

`country`  
Identificador del país, identificado por la constante de la clase Gender. Si se omite, ANY_COUNTRY será utilizado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
