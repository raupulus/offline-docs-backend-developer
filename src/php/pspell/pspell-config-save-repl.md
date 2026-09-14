---
title: pspell_config_save_repl
description: Determina si se deben guardar los pares de reemplazo con el diccionario
source_url: https://www.php.net/manual/es/function.pspell-config-save-repl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-config-save-repl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66470
---

pspell_config_save_repl

Determina si se deben guardar los pares de reemplazo con el diccionario

## Descripción

```php
pspell_config_save_repl(PSpell\Config $config, bool $save): bool
```php

`pspell_config_save_repl` determina si `pspell_save_wordlist` debe guardar los pares de reemplazo con el diccionario. Generalmente, no es necesario utilizar esta función ya que, si `pspell_config_repl` se utiliza, los pares de reemplazo serán guardados de todas formas por `pspell_save_wordlist`, y, si no es así, no lo serán.

`pspell_config_save_repl` debe ser llamada en una configuración antes de llamar a `pspell_new_config`.

## Parámetros

`config`  
Una instancia de `PSpell\Config`.

`save`  
`true` si los pares de reemplazo deben ser guardados, `false` en caso contrario.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `config` ahora espera una instancia de `PSpell\Config` ; anteriormente, se esperaba un `resource`. |

## Notas

> [!NOTE]
> Esta función solo funcionará con pspell .11.2 y aspell .32.5 o versiones posteriores.
