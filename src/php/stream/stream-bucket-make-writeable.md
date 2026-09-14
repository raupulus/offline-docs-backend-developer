---
title: stream_bucket_make_writeable
description: Devuelve un objeto de compartimento desde el cuerpo para operaciones
  sobre el mismo
source_url: https://www.php.net/manual/es/function.stream-bucket-make-writeable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-bucket-make-writeable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 32caa89e8
order: 87790
---

stream_bucket_make_writeable

Devuelve un objeto de compartimento desde el cuerpo para operaciones sobre el mismo

## Descripción

```php
stream_bucket_make_writeable(resource $brigade): StreamBucket
```php

Esta función es llamada cuando hay necesidad de acceder y operar sobre el contenido comprendido en una brigada. Típicamente llamada desde php_user_filter::filter.

## Parámetros

`brigade`  
La brigada desde donde devolver un objeto bucket.

## Valores devueltos

Devuelve un objeto bucket o `null`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Esta función ahora retorna una instancia de `StreamBucket`; anteriormente, se retornaba una `stdClass`. |

## Véase también

`stream_bucket_append`, `stream_bucket_prepend`
