---
title: pspell_config_mode
description: Cambia el modo de sugerencia
source_url: https://www.php.net/manual/es/function.pspell-config-mode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-config-mode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66430
---

pspell_config_mode

Cambia el modo de sugerencia

## Descripción

```php
pspell_config_mode(PSpell\Config $config, int $mode): bool
```php

`pspell_config_mode` debe ser llamada en una configuración antes de `pspell_new_config`. Esta función determina el número de sugerencias que serán devueltas por `pspell_suggest`.

## Parámetros

`config`  
Una instancia de `PSpell\Config`.

`mode`  
El argumento de modo es el modo de trabajo del verificador ortográfico. Varios modos están disponibles:

- `PSPELL_FAST` - Modo rápido (menos sugerencias)

- `PSPELL_NORMAL` - Modo normal (más sugerencias)

- `PSPELL_BAD_SPELLERS` - Modo lento (muchas más sugerencias)

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `config` ahora espera una instancia de `PSpell\Config` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pspell_config_mode`

```
<?php
$pspell_config = pspell_config_create("en");
pspell_config_mode($pspell_config, PSPELL_FAST);
$pspell = pspell_new_config($pspell_config);
pspell_check($pspell, "thecat");
?>

    
```php
