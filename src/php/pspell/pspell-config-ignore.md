---
title: pspell_config_ignore
description: Ignora las palabras de menos de N caracteres
source_url: https://www.php.net/manual/es/function.pspell-config-ignore.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-config-ignore.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66420
---

pspell_config_ignore

Ignora las palabras de menos de N caracteres

## Descripción

```php
pspell_config_ignore(PSpell\Config $config, int $min_length): bool
```php

`pspell_config_ignore` debe ser utilizada con una configuración antes de llamar a `pspell_new_config`. Esta función permite al verificador ignorar las palabras cortas.

## Parámetros

`config`  
Una instancia de `PSpell\Config`.

`min_length`  
Las palabras de menos de `min_length` caracteres serán ignoradas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `config` ahora espera una instancia de `PSpell\Config` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

`pspell_config_ignore`

```
<?php
$pspell_config = pspell_config_create("en");
pspell_config_ignore($pspell_config, 5);
$pspell = pspell_new_config($pspell_config);
pspell_check($pspell, "abcd");  // Esta palabra no provocará un error
?>

    
```php
