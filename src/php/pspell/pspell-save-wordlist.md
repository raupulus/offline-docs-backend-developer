---
title: pspell_save_wordlist
description: Guarda el diccionario personal en un archivo
source_url: https://www.php.net/manual/es/function.pspell-save-wordlist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-save-wordlist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66510
---

pspell_save_wordlist

Guarda el diccionario personal en un archivo

## Descripción

```php
pspell_save_wordlist(PSpell\Dictionary $dictionary): bool
```php

`pspell_save_wordlist` guarda el diccionario personal de la sesión actual. La localización de los ficheros debe haber sido especificada con `pspell_config_personal` y (eventualmente) `pspell_config_repl`.

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

`pspell_add_to_personal`

```
<?php
$pspell_config = pspell_config_create("en");
pspell_config_personal($pspell_config, "/tmp/dicts/newdict");
$pspell = pspell_new_config($pspell_config);

pspell_add_to_personal($pspell, "Vlad");
pspell_save_wordlist($pspell);
?>

    
```php

## Notas

> [!NOTE]
> Esta función solo funcionará con pspell .11.2 y aspell .32.5 o versiones posteriores.
