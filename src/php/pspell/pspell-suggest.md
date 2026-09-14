---
title: pspell_suggest
description: Sugiere la ortografía de una palabra
source_url: https://www.php.net/manual/es/function.pspell-suggest.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-suggest.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66530
---

pspell_suggest

Sugiere la ortografía de una palabra

## Descripción

```php
pspell_suggest(PSpell\Dictionary $dictionary, string $word): array
```php

`pspell_suggest` devuelve un array de sugerencias para la palabra `word`.

## Parámetros

`dictionary`  
Una instancia de `PSpell\Dictionary`.

`word`  
La palabra probada.

## Valores devueltos

Devuelve un array de sugerencias para la palabra `word`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `dictionary` ahora espera una instancia de `PSpell\Dictionary` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pspell_suggest`

```
<?php
$pspell = pspell_new("en");

if (!pspell_check($pspell, "testt")) {
    $suggestions = pspell_suggest($pspell, "testt");

    foreach ($suggestions as $suggestion) {
        echo "Ortografías sugeridas: $suggestion<br />";
    }
}
?>

    
```php
