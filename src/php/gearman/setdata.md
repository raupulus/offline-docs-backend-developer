---
title: GearmanClient::setData
description: Establece los datos de aplicación (obsoleto)
source_url: https://www.php.net/manual/es/gearmanclient.setdata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/setdata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_revision: 330a38c4d
order: 25240
---

GearmanClient::setData

Establece los datos de aplicación (obsoleto)

## Descripción

```php
public GearmanClient::setData(string $data): bool
```php

Establece datos arbitrarios para la aplicación que pueden ser leídos posteriormente con GearmanClient::data.

> [!NOTE]
> Este método ha sido reemplazado por GearmanClient::setContext en la versión 0.6.0 de la extensión Gearman.

## Parámetros

`data`  

## Valores devueltos

Siempre retorna `true`.

## Véase también

GearmanClient::data
