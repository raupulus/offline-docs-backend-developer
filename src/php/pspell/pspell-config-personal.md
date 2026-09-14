---
title: pspell_config_personal
description: Selecciona el fichero que contiene el diccionario personal
source_url: https://www.php.net/manual/es/function.pspell-config-personal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-config-personal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66440
---

pspell_config_personal

Selecciona el fichero que contiene el diccionario personal

## Descripción

```php
pspell_config_personal(PSpell\Config $config, string $filename): bool
```php

Selecciona el fichero que contiene el diccionario personal. El diccionario personal será cargado y utilizado además del diccionario estándar, una vez que se haya llamado a `pspell_new_config`. El fichero es también donde `pspell_save_wordlist` guardará el diccionario personal.

`pspell_config_personal` debe ser llamada en una configuración antes de llamar a `pspell_new_config`.

## Parámetros

`config`  
Una instancia de `PSpell\Config`.

`filename`  
El diccionario personal. Si el fichero no existe, será creado. El fichero debe ser accesible en escritura para el usuario que invoca PHP (ej. nobody).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `config` ahora espera una instancia de `PSpell\Config` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

`pspell_config_personal`

```
<?php
$pspell_config = pspell_config_create("en");
pspell_config_personal($pspell_config, "/var/dictionaries/custom.pws");
$pspell = pspell_new_config($pspell_config);
pspell_check($pspell, "thecat");
?>

    
```php

## Notas

> [!NOTE]
> Esta función solo funcionará con pspell .11.2 y aspell .32.5 o versiones posteriores.
