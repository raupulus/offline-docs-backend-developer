---
title: EvStat::stat
description: Inicializa la llamada a stat
source_url: https://www.php.net/manual/es/evstat.stat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evstat/stat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18580
---

EvStat::stat

Inicializa la llamada a stat

## Descripción

```php
public EvStat::stat(): bool
```php

Inicializa la llamada a stat (actualización de la caché interna). El comando llamará a stat (usando `lstat`) en la ruta de acceso especificada `path` en el observador y establecerá los valores encontrados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si `path` existe. De lo contrario, `false`.

## Véase también

EvStat::attr

EvStat::prev
