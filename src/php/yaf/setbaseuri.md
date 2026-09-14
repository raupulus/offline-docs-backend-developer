---
title: Yaf_Request_Abstract::setBaseUri
description: Establecer el URI base
source_url: https://www.php.net/manual/es/yaf-request-abstract.setbaseuri.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_request_abstract/setbaseuri.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 7418592d8
order: 106340
---

Yaf_Request_Abstract::setBaseUri

Establecer el URI base

## Descripción

```php
public Yaf_Request_Abstract::setBaseUri(string $uir): bool
```php

Establece el URI base. El URI base se usa al enrutar. En la fase de enrutamiento, el URI solicitado se usa para enrutar una petición, mientras que es URI base para saltar la parte anterior(URI base) del URI solicitado. Esto es, si viene una petición con un URI solicitado como a/b/c, si se establece el URI base a "a/b", se usará solamente "/c" en la fase de enrutamiento.

> [!NOTE]
> Generalmente, no es necesario establecer esto, Yaf lo determinará automáticamente.

## Parámetros

`uir`  
El URI base

## Valores devueltos

booleano
