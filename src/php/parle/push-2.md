---
title: Parle\Parser::push
description: Añade una regla de gramática
source_url: https://www.php.net/manual/es/parle-parser.push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle/parser/push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: a2ca02540
order: 60570
---

Parle\Parser::push

Añade una regla de gramática

## Descripción

```php
public Parle\Parser::push(string $name, string $rule): int
```php

Añade una regla de gramática. El identificador de producción devuelto puede ser utilizado más tarde en el proceso de análisis para identificar la regla correspondiente.

## Parámetros

`name`  
El nombre de la regla.

`rule`  
La regla a añadir. La sintaxis es compatible con Bison.

## Valores devueltos

Devuelve un `int` que representa el índice de la regla.
