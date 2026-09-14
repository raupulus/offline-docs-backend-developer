---
title: OAuth::setCAPath
description: Define el camino y la información de la CA
source_url: https://www.php.net/manual/es/oauth.setcapath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/setcapath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: false
translation_revision: bdee7e8c1
order: 56830
---

OAuth::setCAPath

Define el camino y la información de la CA

## Descripción

```php
public OAuth::setCAPath([string $ca_path], [string $ca_info]): mixed
```php

Define el certificado de autoridad (CA), tanto para el camino como para la información.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`ca_path`  
El camino de la CA a definir.

`ca_info`  
La información de la CA a definir.

## Valores devueltos

Retorna `true` en caso de éxito, o `false` si `ca_path` o `ca_info` son considerados inválidos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL oauth 1.0.0 | Antes de esta versión, `null` era devuelto en lugar de `false`. |

## Véase también

OAuth::getCaPath
