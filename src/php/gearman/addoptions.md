---
title: GearmanClient::addOptions
description: Añade opciones al cliente
source_url: https://www.php.net/manual/es/gearmanclient.addoptions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/addoptions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 24880
---

GearmanClient::addOptions

Añade opciones al cliente

## Descripción

```php
public GearmanClient::addOptions(int $option): bool
```php

Añade una o varias opciones a las ya existentes.

## Parámetros

`option`  
Las opciones a añadir. Una de las constantes siguientes o la combinación de constantes utilizando el operador de manipulación de bits (“\|”): `GEARMAN_CLIENT_GENERATE_UNIQUE`, `GEARMAN_CLIENT_NON_BLOCKING`, `GEARMAN_CLIENT_UNBUFFERED_RESULT` o `GEARMAN_CLIENT_FREE_TASKS`.

## Valores devueltos

Devuelve siempre `true`.
