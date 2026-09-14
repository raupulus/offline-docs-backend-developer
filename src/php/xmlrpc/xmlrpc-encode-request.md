---
title: xmlrpc_encode_request
description: Genera el XML para un método
source_url: https://www.php.net/manual/es/function.xmlrpc-encode-request.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlrpc/functions/xmlrpc-encode-request.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlrpc
translation_status: ready
translation_reviewed: false
translation_revision: 3abd17e61
order: 103400
---

xmlrpc_encode_request

Genera el XML para un método

## Descripción

```php
xmlrpc_encode_request(string $method, mixed $params, [array $output_options]): string
```php

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Parámetros

`method`  
Nombre del método a llamar.

`params`  
Argumentos del método, compatibles con la firma del método.

`output_options`  
Array que especifica las opciones de salida que puede contener (los valores por omisión están en negrita):

- output_type: php, *xml*

- verbosity: no_white_space, newlines_only, *pretty*

- escaping: cdata, *non-ascii, non-print, markup* (puede ser una cadena con un valor o un array con varios valores)

- version: simple, *xmlrpc*, soap 1.1, auto

- encoding: *iso-8859-1*, otros juegos de caracteres soportados por iconv

## Valores devueltos

Devuelve una cadena que contiene la representación XML de la solicitud.

## Ejemplos

Ejemplo con XMLRPC

```
<?php
$request = xmlrpc_encode_request("method", [1, 2, 3]);
$context = stream_context_create([
    'http' => [
        'method'  => "POST",
        'header'  => "Content-Type: text/xml",
        'content' => $request,
    ]
]);
$file = file_get_contents("http://www.example.com/xmlrpc", false, $context);
$response = xmlrpc_decode($file);
if ($response && xmlrpc_is_fault($response)) {
    trigger_error("xmlrpc: $response[faultString] ($response[faultCode])");
} else {
    print_r($response);
}
?>

    
```php

## Véase también

`stream_context_create`, `file_get_contents`, `xmlrpc_decode`
