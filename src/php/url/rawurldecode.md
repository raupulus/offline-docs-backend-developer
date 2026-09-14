---
title: rawurldecode
description: Decodificar cadenas codificadas estilo URL
source_url: https://www.php.net/manual/es/function.rawurldecode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/url/functions/rawurldecode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: url
translation_status: ready
translation_revision: 0c9c2dd66
order: 100250
---

rawurldecode

Decodificar cadenas codificadas estilo URL

## Descripción

```php
rawurldecode(string $string): string
```php

Devuelve una cadena en donde las con secuencias con signos de porcentaje (`%`) seguidos de dos dígitos hexadecimales, son reemplazados con caracteres literales.

## Parámetros

`string`  
La URL a ser decodificada.

## Valores devueltos

Devuelve la URL decodificada, como una cadena.

## Ejemplos

Ejemplo de `rawurldecode`

```
<?php

echo rawurldecode('foo%20bar%40baz'); // foo bar@baz

?>

    
```php

## Notas

> [!NOTE]
> `rawurldecode` no decodifica los símbolos más ('+') como espacios. `urldecode` lo hace.

## Véase también

`rawurlencode`, `urldecode`, `urlencode`, [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986)
