---
title: mailparse_stream_encode
description: Secuencia datos desde un apuntador de archivo, codifica y escribe a fp_destino
source_url: https://www.php.net/manual/es/function.mailparse-stream-encode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mailparse/functions/mailparse-stream-encode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mailparse
translation_status: ready
translation_revision: 01bd007b0
order: 44430
---

mailparse_stream_encode

Secuencia datos desde un apuntador de archivo, codifica y escribe a fp_destino

## Descripción

```php
mailparse_stream_encode(resource $sourcefp, resource $destfp, string $encoding): bool
```php

Secuencia datos del apuntador de archivo fuente, aplica la `codificacion` y escribe al apuntador de archivo de destino.

## Parámetros

`sourcefp`  
Un gestor de archivo válido. El archivo es secuenciado a través del procesador.

`destfp`  
El gestor de archivo de destino, en el cual los datos codificados serán escritos.

`encoding`  
Una de las codificaciones de caracteres soportadas por el módulo [mbstring](#ref.mbstring).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `mailparse_stream_encode`

```
<?php

// Contenido de email.eml: hola, este es un trozo de texto=hola.
$aa = fopen('email.eml', 'r');

$dest = tmpfile();

mailparse_stream_encode($aa, $dest, "quoted-printable");

rewind($dest);

// Mostrar el contenido del nuevo archivo
fpassthru($dest);

?>

   
```php

El ejemplo anterior mostrará:

    hola, este es un trozo de texto=3Dhola.
