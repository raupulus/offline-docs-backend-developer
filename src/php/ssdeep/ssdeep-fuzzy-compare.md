---
title: ssdeep_fuzzy_compare
description: Calcula el puntaje de coincidencia entre 2 firmas de hash difuso
source_url: https://www.php.net/manual/es/function.ssdeep-fuzzy-compare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssdeep/functions/ssdeep-fuzzy-compare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssdeep
translation_status: ready
translation_revision: 2885123b1
order: 86360
---

ssdeep_fuzzy_compare

Calcula el puntaje de coincidencia entre 2 firmas de hash difuso

## Descripción

```php
ssdeep_fuzzy_compare(string $signature1, string $signature2): int
```php

Calcula el puntaje de coincidencia entre la `signature1` y la `signature2` utilizando el [ contexto desencadenado por fragmentos de hashing](http://dfrws.org/2006/proceedings/12-Kornblum.pdf), y devuelve el puntaje de coincidencia.

## Parámetros

`signature1`  
La cadena que representa la primera firma de hash difuso.

`signature2`  
La cadena que representa la segunda firma de hash difuso.

## Valores devueltos

Devuelve un entero entre 0 y 100 en caso de éxito, o `false` si ocurre un error.
