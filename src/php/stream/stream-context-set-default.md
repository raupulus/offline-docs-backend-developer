---
title: stream_context_set_default
description: Configura el contexto predeterminado de los flujos
source_url: https://www.php.net/manual/es/function.stream-context-set-default.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-context-set-default.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: 3abd17e61
order: 87860
---

stream_context_set_default

Configura el contexto predeterminado de los flujos

## Descripción

```php
stream_context_set_default(array $options): resource
```php

Configura el contexto predeterminado de los flujos que será utilizado cada vez que un fichero sea manipulado (`fopen`, `file_get_contents`, etc.) sin parámetro de contexto. Utiliza la misma sintaxis que `stream_context_create`.

## Parámetros

`options`  
Las opciones a configurar para el contexto predeterminado.

> [!NOTE]
> `options` debe ser un array asociativo de arrays asociativos, en el formato `$arr['gestor']['opción'] = $valor`.

## Valores devueltos

Devuelve el contexto de flujo predeterminado.

## Ejemplos

Ejemplo con `stream_context_set_default`

```
<?php
$default_opts = [
  'http' => [
    'method' => "GET",
    'header' => "Accept-language: en\r\n" .
                "Cookie: foo=bar",
    'proxy'  => "tcp://10.54.1.39:8000",
  ]
];

$default = stream_context_set_default($default_opts);

/* Envía una petición GET al servidor proxy 10.54.1.39
 * para www.example.com, utilizando las opciones de contexto especificadas en $default_opts
 */
readfile('http://www.example.com');
?>

    
```php

## Véase también

`stream_context_create`, `stream_context_get_default`, Lista de gestores de flujos con sus opciones de contexto ([???](#wrappers)).
