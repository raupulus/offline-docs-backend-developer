---
title: pspell_config_data_dir
description: Directorio que contiene los archivos de datos lingüísticos
source_url: https://www.php.net/manual/es/function.pspell-config-data-dir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-config-data-dir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66400
---

pspell_config_data_dir

Directorio que contiene los archivos de datos lingüísticos

## Descripción

```php
pspell_config_data_dir(PSpell\Config $config, string $directory): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `config` ahora espera una instancia de `PSpell\Config` ; anteriormente, se esperaba un `resource`. |
