---
title: GearmanClient::data
description: Retorna los datos de aplicación (obsoleto)
source_url: https://www.php.net/manual/es/gearmanclient.data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_revision: cf0a919c1
order: 25020
---

GearmanClient::data

Retorna los datos de aplicación (obsoleto)

## Descripción

```php
public GearmanClient::data(): string
```php

Obtiene los datos de aplicación fijados anteriormente con GearmanClient::setData.

> [!NOTE]
> Este método fue reemplazado por GearmanClient::setContext en la versión 0.6.0 de la extensión Gearman.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El mismo string de datos que fue establecido con GearmanClient::setData

## Véase también

GearmanClient::setData
