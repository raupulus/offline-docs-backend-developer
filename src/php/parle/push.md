---
title: Parle\Lexer::push
description: Añade una regla de análisis
source_url: https://www.php.net/manual/es/parle-lexer.push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle/lexer/push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 60470
---

Parle\Lexer::push

Añade una regla de análisis

## Descripción

```php
public Parle\Lexer::push(string $regex, int $id, [int $userId]): void
```php

Añade un patrón para el reconocimiento de los lexemas.

## Parámetros

`regex`  
Expresión regular utilizada para el reconocimiento de los lexemas.

`id`  
El identificador del token. Si la instancia del analizador léxico está destinada a ser utilizada sola, puede ser un número arbitrario. Si la instancia del analizador léxico debe ser pasada al analizador, debe ser un identificador devuelto por Parle\Parser::tokenid.

## Valores devueltos

No se retorna ningún valor.
