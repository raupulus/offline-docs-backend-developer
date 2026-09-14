---
title: token_name
description: Obtiene el nombre simbólico de un token PHP dado
source_url: https://www.php.net/manual/es/function.token-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tokenizer/functions/token-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tokenizer
translation_status: ready
translation_revision: cbac1ecf7
order: 94360
---

token_name

Obtiene el nombre simbólico de un token PHP dado

## Descripción

```php
token_name(int $id): string
```php

`token_name` obtiene el nombre simbólico para un valor de `id` PHP.

## Parámetros

`id`  
El valor token.

## Valores devueltos

El nombre simbólico para el `id` dado.

## Ejemplos

`token_name` ejemplo

```
<?php
// 260 es el valor de token para T_EVAL token
echo token_name(260);        // -> "T_EVAL"

// una constante token mapea a su propio nombre
echo token_name(T_FUNCTION); // -> "T_FUNCTION"
?>

    
```php

## Véase también

Listado de Tokens Analizadores

PhpToken::getTokenName
