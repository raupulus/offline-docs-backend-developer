---
title: CommonMark\Parse
description: Análisis sintáctico
source_url: https://www.php.net/manual/es/function.commonmark-parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cmark/functions/commonmark.parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cmark
translation_status: ready
translation_reviewed: false
translation_revision: 876a6a393
order: 7430
---

CommonMark\Parse

Análisis sintáctico

## Descripción

```php
CommonMark\Parse(string $content, [int $options]): CommonMark\Node
```php

Deberá analizar `content`

## Parámetros

`content`  
reducción de la carga string

`options`  
Una máscara de:

`CommonMark\Parser\Normal` (`int`)  

`CommonMark\Parser\Normalize` (`int`)  

`CommonMark\Parser\ValidateUTF8` (`int`)  

`CommonMark\Parser\Smart` (`int`)  

## Valores devueltos

Devolverá la raíz de CommonMark\Node
