---
title: DOMNode::isSupported
description: Comprueba si una característica está soportada para la versión especificada
source_url: https://www.php.net/manual/es/domnode.issupported.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/issupported.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 14040
---

DOMNode::isSupported

Comprueba si una característica está soportada para la versión especificada

## Descripción

```php
public DOMNode::isSupported(string $feature, string $version): bool
```php

Comprueba si la característica solicitada dada por `feature` está soportada para la versión especificada dada por `version`.

## Parámetros

`feature`  
La característica a comprobar. Véase el ejemplo de DOMImplementation::hasFeature para una lista de características.

`version`  
El número de versión de `feature` a comprobar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

DOMImplementation::hasFeature
