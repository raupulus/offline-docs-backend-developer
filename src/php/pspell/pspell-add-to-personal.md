---
title: pspell_add_to_personal
description: Añade la palabra al diccionario personal
source_url: https://www.php.net/manual/es/function.pspell-add-to-personal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-add-to-personal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66350
---

pspell_add_to_personal

Añade la palabra al diccionario personal

## Descripción

```php
pspell_add_to_personal(PSpell\Dictionary $dictionary, string $word): bool
```php

`pspell_add_to_personal` añade una palabra al diccionario personal. Si se utiliza `pspell_new_config` con `pspell_config_personal` para abrir el diccionario, el diccionario personal podrá ser guardado posteriormente con `pspell_save_wordlist`.

## Parámetros

`dictionary`  
Una instancia de `PSpell\Dictionary`.

`word`  
La palabra añadida.

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
pspell_config_personal($pspell_config, "/var/dictionaries/custom.pws");
$pspell = pspell_new_config($pspell_config);

pspell_add_to_personal($pspell, "Vlad");
pspell_save_wordlist($pspell);
?>

    
```php

## Notas

> [!NOTE]
> Esta función solo funcionará si se dispone de pspell .11.2 y aspell .32.5 o versiones posteriores.
