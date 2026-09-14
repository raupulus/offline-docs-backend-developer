---
title: mb_lcfirst
description: Convierte la primera letra de un string a minúscula
source_url: https://www.php.net/manual/es/function.mb-lcfirst.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-lcfirst.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 154d93899
order: 45270
---

mb_lcfirst

Convierte la primera letra de un string a minúscula

## Descripción

```php
mb_lcfirst(string $string, [string $encoding]): string
```php

Realiza una operación `lcfirst` segura para multi-octetos, y devuelve un string con la primera letra de `string` en minúscula.

## Parámetros

`string`  
El string de entrada.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve el string resultante.

## Véase también

mb_ucfirst

lcfirst
