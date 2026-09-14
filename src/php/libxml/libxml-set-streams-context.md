---
title: libxml_set_streams_context
description: Configura el contexto de flujos para la próxima operación libxml
source_url: https://www.php.net/manual/es/function.libxml-set-streams-context.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/libxml/functions/libxml-set-streams-context.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: libxml
translation_status: ready
translation_reviewed: false
translation_revision: 3abd17e61
order: 43710
---

libxml_set_streams_context

Configura el contexto de flujos para la próxima operación libxml

## Descripción

```php
libxml_set_streams_context(resource $context): void
```php

`libxml_set_streams_context` configura el contexto de flujos para la próxima operación libxml.

## Parámetros

`context`  
El recurso de contexto de flujos, creado con la función `stream_context_create`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Genera una `TypeError` cuando se pasa un recurso no flujo al `context`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `libxml_set_streams_context` genera ahora una TypeError cuando se pasa un recurso no flujo al `context`, en lugar de generarla más tarde cuando el contexto es utilizado. |

## Ejemplos

Ejemplo con `libxml_set_streams_context`

```
<?php
$opts = [
    'http' => [
        'user_agent' => 'PHP libxml agent',
    ]
];

$context = stream_context_create($opts);
libxml_set_streams_context($context);

// lee un fichero vía HTTP
$dom = new DOMDocument;
$doc = $dom->load('http://www.example.com/file.xml');

?>

    
```php

## Véase también

`stream_context_create`
