---
title: deflate_add
description: Comprime datos de manera incremental
source_url: https://www.php.net/manual/es/function.deflate-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/deflate_add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: true
translation_revision: e8ac70bf5
order: 108710
---

deflate_add

Comprime datos de manera incremental

## Descripción

```php
deflate_add(DeflateContext $context, string $data, [int $flush_mode]): string
```php

Comprime de manera incremental los datos en el contexto especificado.

## Parámetros

`context`  
Un contexto creado con `deflate_init`.

`data`  
Un fragmento de datos a comprimir.

`flush_mode`  
Una de las `ZLIB_BLOCK`, `ZLIB_NO_FLUSH`, `ZLIB_PARTIAL_FLUSH`, `ZLIB_SYNC_FLUSH` (por defecto), `ZLIB_FULL_FLUSH`, `ZLIB_FINISH`. Normalmente, querrá establecer `ZLIB_NO_FLUSH` para maximizar la compresión, y `ZLIB_FINISH` para terminar con el último fragmento de datos. Consulte el [manual de zlib](http://www.zlib.net/manual.html) para una descripción detallada de estas constantes.

## Valores devueltos

Devuelve un fragmento de datos comprimidos, o `false` si ocurre un error.

## Errores/Excepciones

Si se proporciona un argumento inválido, se genera un error de nivel `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `context` ahora espera una instancia de `DeflateContext`; anteriormente se esperaba un `recurso`. |

## Véase también

deflate_init
