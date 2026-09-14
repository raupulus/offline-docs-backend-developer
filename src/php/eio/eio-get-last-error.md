---
title: eio_get_last_error
description: Retorna un string describiendo el último error asociado con el recurso
  solicitado
source_url: https://www.php.net/manual/es/function.eio-get-last-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-get-last-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_reviewed: false
translation_revision: 4e5389401
order: 16860
---

eio_get_last_error

Retorna un string describiendo el último error asociado con el recurso solicitado

## Descripción

```php
eio_get_last_error(resource $req): string
```php

`eio_get_last_error` retorna un string describiendo el último error asociado con el argumento `req`.

## Parámetros

`req`  
El recurso solicitado.

## Valores devueltos

`eio_get_last_error` retorna un string describiendo el último error con el recurso solicitado especificado por el argumento `req`.

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.
