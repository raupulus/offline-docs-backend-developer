---
title: pspell_check
description: Verifica un término
source_url: https://www.php.net/manual/es/function.pspell-check.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-check.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66370
---

pspell_check

Verifica un término

## Descripción

```php
pspell_check(PSpell\Dictionary $dictionary, string $word): bool
```php

`pspell_check` verifica la ortografía de un término.

## Parámetros

`dictionary`  
Una instancia de `PSpell\Dictionary`.

`word`  
El término a verificar.

## Valores devueltos

Devuelve `true` si la ortografía es correcta, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `dictionary` ahora espera una instancia de `PSpell\Dictionary` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pspell_check`

```
<?php
$pspell = pspell_new ("fr");

if (pspell_check($pspell, "testt")) {
    echo 'La ortografía es correcta';
} else {
    echo 'Disculpe, ortografía incorrecta';
}
?>

    
```php
