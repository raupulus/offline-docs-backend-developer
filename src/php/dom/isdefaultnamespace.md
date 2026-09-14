---
title: DOMNode::isDefaultNamespace
description: Comprueba si la URI del espacio de nombres especificada es el espacio
  de nombres predeterminado
source_url: https://www.php.net/manual/es/domnode.isdefaultnamespace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/isdefaultnamespace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 14010
---

DOMNode::isDefaultNamespace

Comprueba si la URI del espacio de nombres especificada es el espacio de nombres predeterminado

## Descripción

```php
public DOMNode::isDefaultNamespace(string $namespace): bool
```php

Indica si `namespace` es el espacio de nombres especificado.

## Parámetros

`namespace`  
La URI del espacio de nombres a buscar.

## Valores devueltos

Devuelve `true` si `namespace` es el espacio de nombres predeterminado, `false` si no.
