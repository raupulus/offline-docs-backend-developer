---
title: stream_bucket_prepend
description: Añadir inicialmente un bucket a una brigada
source_url: https://www.php.net/manual/es/function.stream-bucket-prepend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-bucket-prepend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: 32caa89e8
order: 87810
---

stream_bucket_prepend

Añadir inicialmente un bucket a una brigada

## Descripción

```php
stream_bucket_prepend(resource $brigade, StreamBucket $bucket): void
```php

Esta función puede ser llamada para añadir un bucket a una brigada de buckets. Es típicamente llamada desde el método php_user_filter::filter.

## Parámetros

`brigade`  
`brigade` es un recurso que apunta a una `bucket brigade` que contiene uno o varios objetos `bucket`.

`bucket`  
Un objeto bucket.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `bucket` ahora espera una instancia de `StreamBucket`; anteriormente, se esperaba una `stdClass`. |

## Ejemplos

Ejemplo con `stream_bucket_prepend`

```
<?php

class foo extends php_user_filter {
  protected $calls = 0;
  public function filter($in, $out, &$consumed, $closing) {
    while ($bucket = stream_bucket_make_writeable($in)) {
      $consumed += $bucket->datalen;
      if ($this->calls++ == 2) {
        // Este bucket aparecerá antes que cualquier otro bucket.
        stream_bucket_prepend($in, $bucket);
      }
    }
    return PSFS_FEED_ME;
  }
}
stream_filter_register('test', 'foo');
print  file_get_contents('php://filter/read=test/resource=foo');
?>

    
```php
