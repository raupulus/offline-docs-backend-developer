---
title: pspell_store_replacement
description: Registra un par de sustitución para una palabra
source_url: https://www.php.net/manual/es/function.pspell-store-replacement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-store-replacement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66520
---

pspell_store_replacement

Registra un par de sustitución para una palabra

## Descripción

```php
pspell_store_replacement(PSpell\Dictionary $dictionary, string $misspelled, string $correct): bool
```php

`pspell_store_replacement` registra un par de sustitución para una palabra de forma que esta sugerencia sea devuelta por `pspell_suggest` más tarde. Para poder utilizar esta función, se debe utilizar `pspell_new_personal` para abrir el diccionario. Para poder guardar permanentemente los pares de sustitución, se debe utilizar `pspell_config_personal` y `pspell_config_repl` para indicar el lugar de guardado de los diccionarios personales, y `pspell_save_wordlist` para registrar los cambios en el disco.

## Parámetros

`dictionary`  
Una instancia de `PSpell\Dictionary`.

`misspelled`  
La palabra mal escrita.

`correct`  
La ortografía correcta de la palabra `misspelled`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `dictionary` ahora espera una instancia de `PSpell\Dictionary` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

`pspell_store_replacement`

```
<?php
$pspell_config = pspell_config_create("en");
pspell_config_personal($pspell_config, "/var/dictionaries/custom.pws");
pspell_config_repl($pspell_config, "/var/dictionaries/custom.repl");
$pspell = pspell_new_config($pspell_config);

pspell_store_replacement($pspell, $misspelled, $correct);
pspell_save_wordlist($pspell);
?>

    
```php

## Notas

> [!NOTE]
> Esta función solo funcionará con pspell .11.2 y aspell .32.5 o versiones posteriores.
