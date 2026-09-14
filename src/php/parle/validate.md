---
title: Parle\Parser::validate
description: Valida una entrada
source_url: https://www.php.net/manual/es/parle-parser.validate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle/parser/validate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: eb9855d8a
order: 60660
---

Parle\Parser::validate

Valida una entrada

## Descripción

```php
public Parle\Parser::validate(string $data, Parle\Lexer $lexer): bool
```php

Valida una string de entrada. La string es analizada internamente, por lo que este método es útil para la validación rápida de la entrada.

## Parámetros

`data`  
La string a validar.

`lexer`  
Un objeto lexer que contiene las reglas de análisis léxico preparadas para la gramática particular.

## Valores devueltos

Devuelve un `bool` que indica si la entrada cumple o no con las reglas definidas.
