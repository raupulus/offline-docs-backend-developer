---
title: mailparse_msg_extract_part_file
description: Extrae/decodifica una sección de mensaje
source_url: https://www.php.net/manual/es/function.mailparse-msg-extract-part-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mailparse/functions/mailparse-msg-extract-part-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mailparse
translation_status: ready
translation_revision: 01bd007b0
order: 44330
---

mailparse_msg_extract_part_file

Extrae/decodifica una sección de mensaje

## Descripción

```php
mailparse_msg_extract_part_file(resource $mimemail, mixed $filename, [callable $callbackfunc]): string
```php

Extrae/decodifica una sección de mensaje del archivo indicado.

Los contenidos de la sección serán decodificados de acuerdo a su codificación de transferencia - se soportan base64, imprimible-con-comillas y texto uuencode.

## Parámetros

`mimemail`  
Un recurso `MIME` válido, creado con `mailparse_msg_create`.

`filename`  
Puede ser un nombre de archivo o un recurso de secuencia válido.

`callbackfunc`  
Si se define, este parámetro debe ser una llamada de retorno válida, a la cual le será pasada la sección extraída, o `null` para asegurarse de que esta función devuelva la sección extraída.

Si no se especifica, los contenidos serán enviados a "stdout".

## Valores devueltos

Si `callbackfunc` es diferente de `null` devuelve `true` en caso de éxito.

Si `callbackfunc` es `null`, devuelve la sección extraída como una cadena.

Devuelve `false` en caso de fallo.

## Véase también

mailparse_msg_extract_part

mailparse_msg_extract_whole_part_file
