---
title: pspell_clear_session
description: Restablece la sesión actual
source_url: https://www.php.net/manual/es/function.pspell-clear-session.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-clear-session.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66380
---

pspell_clear_session

Restablece la sesión actual

## Descripción

```php
pspell_clear_session(PSpell\Dictionary $dictionary): bool
```php

`pspell_clear_session` restablece la sesión actual. El diccionario personal se vacía y, por ejemplo, si se intenta guardarlo con `pspell_save_wordlist`, no ocurrirá nada.

## Parámetros

`dictionary`  
Una instancia de `PSpell\Dictionary`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `dictionary` ahora espera una instancia de `PSpell\Dictionary` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pspell_add_to_personal`

```
<?php
$pspell_config = pspell_config_create("en");
pspell_config_personal($pspell_config, "/var/dictionaries/custom.pws");
$pspell = pspell_new_config($pspell_config);

pspell_add_to_personal($pspell, "Vlad");
pspell_clear_session($pspell);
pspell_save_wordlist($pspell);  //"Vlad" no será guardado
?>

    
```php
