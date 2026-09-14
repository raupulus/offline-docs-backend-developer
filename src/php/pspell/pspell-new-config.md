---
title: pspell_new_config
description: Carga un nuevo diccionario con los parámetros especificados en una configuración
source_url: https://www.php.net/manual/es/function.pspell-new-config.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-new-config.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66480
---

pspell_new_config

Carga un nuevo diccionario con los parámetros especificados en una configuración

## Descripción

```php
pspell_new_config(PSpell\Config $config): PSpell\Dictionary
```php

`pspell_new_config` abre un nuevo diccionario con los ajustes de la configuración `config`, creada con `pspell_config_create` y modificada con las funciones `pspell_config_*`. Este método proporciona la máxima flexibilidad, y dispone de todas las funcionalidades ofrecidas por `pspell_new` y `pspell_new_personal`.

## Parámetros

`config`  
La `config` es la que es devuelta por `pspell_config_create` cuando la configuración es creada.

## Valores devueltos

Devuelve una instancia de `PSpell\Dictionary` en caso de éxito, o `false` si ocurre un error

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `config` ahora espera una instancia de `PSpell\Config` ; anteriormente, se esperaba un `resource`. |
| 8.1.0 | Ahora devuelve una instancia de `PSpell\Dictionary`; anteriormente se devolvía un `resource`. |

## Ejemplos

`pspell_new_config`

```
<?php
$pspell_config = pspell_config_create("en");
pspell_config_personal($pspell_config, "/var/dictionaries/custom.pws");
pspell_config_repl($pspell_config, "/var/dictionaries/custom.repl");
$pspell = pspell_new_config($pspell_config);
?>

    
```php
