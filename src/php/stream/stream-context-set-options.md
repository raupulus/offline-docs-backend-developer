---
title: stream_context_set_options
description: Define las opciones en el contexto especificado
source_url: https://www.php.net/manual/es/function.stream-context-set-options.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-context-set-options.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: d715365c0
order: 87880
---

stream_context_set_options

Define las opciones en el contexto especificado

## Descripción

```php
stream_context_set_options(resource $context, array $options): true
```php

Define las opciones en el contexto especificado.

## Parámetros

`context`  
El flujo o recurso de contexto en el cual aplicar las opciones.

`options`  
Las opciones a definir para `context`.

> [!NOTE]
> `options` debe ser un `array` asociativo en el formato `$array['wrapper']['option'] = $value`.
>
> Ver [opciones y parámetros de contexto](#context) para una lista de las opciones de flujo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `stream_context_set_options`

```
<?php

$context = stream_context_create();

$options = [
    'http' => [
        'protocol_version' => 1.1,
        'user_agent' => 'PHPT Agent',
    ],
];

stream_context_set_options($context, $options);
var_dump(stream_context_get_options($context));
?>

    
```php

El ejemplo anterior mostrará:

    array(1) {
      ["http"]=>
      array(2) {
        ["protocol_version"]=>
        float(1.1)
        ["user_agent"]=>
        string(10) "PHPT Agent"
      }
    }

## Véase también

`stream_context_set_option`
