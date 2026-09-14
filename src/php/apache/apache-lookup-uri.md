---
title: apache_lookup_uri
description: Realiza una petición parcial para el URI especificado y devuelve toda
  la información relacionada con el mismo
source_url: https://www.php.net/manual/es/function.apache-lookup-uri.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apache/functions/apache-lookup-uri.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apache
translation_status: ready
translation_reviewed: true
translation_revision: a331ac8a8
order: 4770
---

apache_lookup_uri

Realiza una petición parcial para el URI especificado y devuelve toda la información relacionada con el mismo

## Descripción

```php
apache_lookup_uri(string $filename): object
```php

Esta función realiza una petición parcial para el URI especificado. Esta petición permite simplemente obtener toda la información importante sobre el recurso concernido.

Esta función es soportada cuando PHP está instalado como módulo de Apache.

## Parámetros

`filename`  
El nombre del fichero (URI) que será solicitado.

## Valores devueltos

Un `object` con la información relativa al URI. Las propiedades de este `object` son las siguientes :

status, the_request, status_line, method, content_type, handler, uri, filename, path_info, args, boundary, no_cache, no_local_copy, allowed, send_bodyct, bytes_sent, byterange, clength, unparsed_uri, mtime, request_time

Devuelve `false` en caso de fallo.

## Ejemplos

Ejemplo con `apache_lookup_uri`

```
<?php
$info = apache_lookup_uri('index.php?var=value');
print_r($info);

if (file_exists($info->filename)) {
    echo '¡El fichero existe!';
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    stdClass Object
    (
        [status] => 200
        [the_request] => GET /dir/file.php HTTP/1.1
        [method] => GET
        [mtime] => 0
        [clength] => 0
        [chunked] => 0
        [content_type] => application/x-httpd-php
        [no_cache] => 0
        [no_local_copy] => 1
        [unparsed_uri] => /dir/index.php?var=value
        [uri] => /dir/index.php
        [filename] => /home/htdocs/dir/index.php
        [args] => var=value
        [allowed] => 0
        [sent_bodyct] => 0
        [bytes_sent] => 0
        [request_time] => 1074282764
    )
    ¡El fichero existe!
