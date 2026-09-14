---
title: stream_context_get_options
description: Recuperar las opciones para un flujo/envoltura/contexto
source_url: https://www.php.net/manual/es/function.stream-context-get-options.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-context-get-options.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: dcdd9c608
order: 87840
---

stream_context_get_options

Recuperar las opciones para un flujo/envoltura/contexto

## Descripción

```php
stream_context_get_options(resource $stream_or_context): array
```php

Devuelve una matriz de opciones del el flujo o contexto especificados.

## Parámetros

`stream_or_context`  
El `stream` (flujo) o `context` (contexto) de donde se van a obtener las opciones

## Valores devueltos

Devuelve una matriz asociativa con las opciones.

## Ejemplos

Ejemplo de `stream_context_get_options`

```
<?php
$params = array("método" => "POST");

stream_context_set_default(array("http" => $params));

var_dump(stream_context_get_options(stream_context_get_default()));

?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      ["http"]=>
      array(1) {
        ["método"]=>
        string(4) "POST"
      }
    }
