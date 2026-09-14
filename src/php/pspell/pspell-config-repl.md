---
title: pspell_config_repl
description: Selecciona el archivo que contiene los pares de reemplazo
source_url: https://www.php.net/manual/es/function.pspell-config-repl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-config-repl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66450
---

pspell_config_repl

Selecciona el archivo que contiene los pares de reemplazo

## Descripción

```php
pspell_config_repl(PSpell\Config $config, string $filename): bool
```php

Selecciona el archivo que contiene los pares de reemplazo.

Los pares de reemplazo mejoran la calidad del verificador. Cuando una palabra está mal escrita y no se encuentra ninguna sugerencia válida en el diccionario, `pspell_store_replacement` se utilizará para registrar un par de reemplazo y `pspell_save_wordlist` para guardar el diccionario con los pares de reemplazo.

`pspell_config_repl` debe ser utilizado con una configuración antes de llamar a `pspell_new_config`.

## Parámetros

`config`  
Una instancia de `PSpell\Config`.

`filename`  
El archivo debe ser accesible en escritura para el usuario que invoca PHP (ej. nobody).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `config` ahora espera una instancia de `PSpell\Config` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

`pspell_config_repl`

```
<?php
$pspell_config = pspell_config_create("en");
pspell_config_personal($pspell_config, "/var/dictionaries/custom.pws");
pspell_config_repl($pspell_config, "/var/dictionaries/custom.repl");
$pspell = pspell_new_config($pspell_config);
pspell_check($pspell, "thecat");
?>

    
```php

## Notas

> [!NOTE]
> Esta función solo funcionará con pspell .11.2 y aspell .32.5 o versiones posteriores.
