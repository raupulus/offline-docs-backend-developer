---
title: DOMXPath::__construct
description: Crea un nuevo objeto DOMXPath
source_url: https://www.php.net/manual/es/domxpath.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domxpath/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 21e1338e9
order: 14290
---

DOMXPath::\_\_construct

Crea un nuevo objeto

DOMXPath

## Descripción

```php
public DOMXPath::__construct(DOMDocument $document, [bool $registerNodeNS])
```php

Crea un nuevo objeto `DOMXPath`.

## Parámetros

`document`  
El objeto `DOMDocument` asociado con el objeto `DOMXPath`.

`registerNodeNS`  
Indica si se deben registrar automáticamente los prefijos de espacio de nombres en vigor del nodo de contexto en el objeto `DOMXPath`. Esto puede ser utilizado para evitar tener que llamar manualmente a DOMXPath::registerNamespace para cada espacio de nombres en vigor. En caso de conflicto de prefijos de espacio de nombres, solo se registra el prefijo de espacio de nombres descendiente más cercano.
