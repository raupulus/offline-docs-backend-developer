---
title: stream_context_get_params
description: Lee los parámetros de un contexto
source_url: https://www.php.net/manual/es/function.stream-context-get-params.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-context-get-params.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 6a5b22785
order: 87850
---

stream_context_get_params

Lee los parámetros de un contexto

## Descripción

```php
stream_context_get_params(resource $context): array
```php

`stream_context_get_params` lee los parámetros del contexto o del flujo `stream_or_context`.

## Parámetros

`context`  
Un `resource` de flujo o de [contexto](#context).

## Valores devueltos

Devuelve un array asociativo que contiene las opciones de contexto y su valor.

## Ejemplos

Ejemplo con `stream_context_get_params`

Ejemplo simple.

```
<?php
$ctx = stream_context_create();
$params = array("notification" => "stream_notification_callback");
stream_context_set_params($ctx, $params);

var_dump(stream_context_get_params($ctx));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      ["notification"]=>
      string(28) "stream_notification_callback"
      ["options"]=>
      array(0) {
      }
    }

## Véase también

`stream_context_set_option`, `stream_context_set_params`
