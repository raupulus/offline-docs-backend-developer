---
title: stream_context_create
description: Crea un contexto de flujo
source_url: https://www.php.net/manual/es/function.stream-context-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-context-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: c49274b06
order: 87820
---

stream_context_create

Crea un contexto de flujo

## Descripción

```php
stream_context_create([array $options], [array $params]): resource
```php

Crea y devuelve un contexto de flujo, con los parámetros proporcionados por `options`.

## Parámetros

`options`  
Debe ser un array asociativo, en el formato `$arr['wrapper']['option'] = $value` o `null`. Consulte las [opciones de contexto](#context) para obtener una lista de las envolturas y opciones disponibles.

Por omisión `null`.

`params`  
Debe ser un array asociativo de formato `$arr['parameter'] = $value` o `null`. Consulte la documentación sobre los [parámetros de contexto](#context.params) para obtener una lista de los parámetros de flujo estándar.

## Valores devueltos

Un recurso que representa el contexto del flujo.

## Historial de cambios

| Versión | Descripción                              |
|---------|------------------------------------------|
| 8.0.0   | `options` y `params` ahora son nullable. |

## Ejemplos

Ejemplo con `stream_context_create`

```
<?php

$opts = [
  'http' => [
    'method' => "GET",
    // Utilice CRLF \r\n para separar múltiples encabezados
    'header' => "Accept-language: en\r\n" .
            "Cookie: foo=bar",
  ]
];

$context = stream_context_create($opts);

/* Envía una petición HTTP a www.example.com
   con los encabezados adicionales anteriores */
$fp = fopen('http://www.example.com', 'r', false, $context);
fpassthru($fp);
fclose($fp);
?>

   
```php

## Véase también

stream_context_set_option

La lista de gestores (

)

Las opciones de contexto (

)
