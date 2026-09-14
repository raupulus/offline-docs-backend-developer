---
title: stream_context_get_default
description: Lee el contexto por defecto de los flujos
source_url: https://www.php.net/manual/es/function.stream-context-get-default.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-context-get-default.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: 3abd17e61
order: 87830
---

stream_context_get_default

Lee el contexto por defecto de los flujos

## Descripción

```php
stream_context_get_default([array $options]): resource
```php

`stream_context_get_default` devuelve el contexto por defecto que se utiliza con las funciones de ficheros como `fopen`, `file_get_contents`, etc, cuando se utilizan sin parámetro de contexto. Las opciones del contexto por defecto pueden especificarse opcionalmente con la misma sintaxis que para `stream_context_create`.

## Parámetros

`options`  
`options` debe ser un array asociativo de arrays asociativos, en el formato `$arr['wrapper']['option'] = $value` o `null`.

## Valores devueltos

Un `resource` de contexto de flujo.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | `options` es ahora nullable. |

## Ejemplos

Ejemplo con `stream_context_get_default`

```
<?php
$default_opts = [
  'http' => [
    'method' => "GET",
    'header' => "Accept-language: en\r\n" .
                "Cookie: foo=bar",
    'proxy' =>  "tcp://10.54.1.39:8000",
  ]
];

$alternate_opts = [
  'http' => [
    'method'  => "POST",
    'header'  => "Content-type: application/x-www-form-urlencoded\r\n" .
                 "Content-length: " . strlen("baz=bomb"),
    'content' => "baz=bomb",
  ]
];

$default = stream_context_get_default($default_opts);
$alternate = stream_context_create($alternate_opts);

/* Envía una petición GET clásica a un servidor proxy 10.54.1.39
 * hacia www.example.com, utilizando las opciones de contexto especificadas
 * en $default_opts
 */
readfile('http://www.example.com');

/* Envía una petición POST directamente a www.example.com
 * Utiliza las opciones de contexto de $alternate_opts
 */
readfile('http://www.example.com', false, $alternate);

?>

    
```php

## Véase también

`stream_context_create`, `stream_context_set_default`, Lista de gestores soportados con las opciones de contexto ([???](#wrappers)).
