---
title: pspell_config_runtogether
description: Considera dos palabras unidas como un compuesto
source_url: https://www.php.net/manual/es/function.pspell-config-runtogether.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-config-runtogether.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66460
---

pspell_config_runtogether

Considera dos palabras unidas como un compuesto

## Descripción

```php
pspell_config_runtogether(PSpell\Config $config, bool $allow): bool
```php

Esta función indica si dos palabras unidas deben ser tratadas como un compuesto válido. Así "lechat" será tratado como un compuesto válido aunque debería haber un espacio entre estas dos palabras. Modificar esta configuración solo afecta a los resultados devueltos por `pspell_check`; `pspell_suggest` siempre devolverá sugerencias.

`pspell_config_runtogether` debe ser llamada en una configuración antes de `pspell_new_config`.

## Parámetros

`config`  
Una instancia de `PSpell\Config`.

`allow`  
`true` si dos palabras unidas deben ser tratadas como un compuesto válido, `false` en caso contrario.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `config` ahora espera una instancia de `PSpell\Config` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

`pspell_config_runtogether`

```
<?php
$pspell_config = pspell_config_create("en");
pspell_config_runtogether($pspell_config, true);
$pspell = pspell_new_config($pspell_config);
pspell_check($pspell, "thecat");
?>

    
```php
