---
title: Parle\RParser::validate
description: Valida una entrada
source_url: https://www.php.net/manual/es/parle-rparser.validate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle/rparser/validate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 0dad2268d
order: 60940
---

Parle\RParser::validate

Valida una entrada

## Descripción

```php
public Parle\RParser::validate(string $data, Parle\RLexer $lexer): bool
```php

Valida una cadena de entrada. La cadena es analizada internamente, por lo que este método es útil para la validación rápida de la entrada.

## Parámetros

`data`  
La cadena a validar.

`lexer`  
Un objeto lexer que contiene las reglas de análisis lexical preparadas para la gramática particular.

## Valores devueltos

Devuelve un `bool` que indica si la entrada cumple o no con las reglas definidas.
