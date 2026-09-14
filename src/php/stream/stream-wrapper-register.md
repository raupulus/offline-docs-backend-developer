---
title: stream_wrapper_register
description: Registra un gestor de URL
source_url: https://www.php.net/manual/es/function.stream-wrapper-register.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-wrapper-register.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: b6c8a19a3
order: 88220
---

stream_wrapper_register

Registra un gestor de URL

## Descripción

```php
stream_wrapper_register(string $protocol, string $class, [int $flags]): bool
```php

`stream_wrapper_register` permite implementar gestores de protocolo y flujo, para ser utilizados con todas las otras funciones de ficheros, como `fopen`, `fread`, etc.

## Parámetros

`protocol`  
El nombre del gestor a registrar. Los nombres de protocolo válidos deben contener únicamente caracteres alfanuméricos, puntos (.), más (+) o guiones (-).

`class`  
La clase que implementa el protocolo `protocol`.

`flags`  
Debe ser configurado a `STREAM_IS_URL` si `protocol` es un protocolo de URL. Por omisión, esta opción vale 0, y es válida para flujos locales.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

`stream_wrapper_register` retorna `false` si el protocolo `protocol` ya tiene un gestor.

## Ejemplos

Cómo registrar un gestor de flujo

```
<?php
$existed = in_array("var", stream_get_wrappers());
if ($existed) {
    stream_wrapper_unregister("var");
}
stream_wrapper_register("var", "VariableStream");
$myvar = "";

$fp = fopen("var://myvar", "r+");

fwrite($fp, "line1\n");
fwrite($fp, "line2\n");
fwrite($fp, "line3\n");

rewind($fp);
while (!feof($fp)) {
    echo fgets($fp);
}
fclose($fp);
var_dump($myvar);

if ($existed) {
    stream_wrapper_restore("var");
}

?>

    
```php

El ejemplo anterior mostrará:

    line1
    line2
    line3
    string(18) "line1
    line2
    line3
    "

## Véase también

El prototipo de clase [???](#class.streamwrapper), [???](#stream.streamwrapper.example-1), `stream_wrapper_unregister`, `stream_wrapper_restore`, `stream_get_wrappers`
