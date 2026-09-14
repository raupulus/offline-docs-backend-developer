---
title: pspell_config_dict_dir
description: Ubicación del archivo global de palabras
source_url: https://www.php.net/manual/es/function.pspell-config-dict-dir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-config-dict-dir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66410
---

pspell_config_dict_dir

Ubicación del archivo global de palabras

## Descripción

```php
pspell_config_dict_dir(PSpell\Config $config, string $directory): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `config` ahora espera una instancia de `PSpell\Config` ; anteriormente, se esperaba un `resource`. |
