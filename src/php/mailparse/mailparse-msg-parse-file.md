---
title: mailparse_msg_parse_file
description: Procesa un archivo
source_url: https://www.php.net/manual/es/function.mailparse-msg-parse-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mailparse/functions/mailparse-msg-parse-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mailparse
translation_status: ready
translation_revision: 01bd007b0
order: 44400
---

mailparse_msg_parse_file

Procesa un archivo

## Descripción

```php
mailparse_msg_parse_file(string $filename): resource
```php

Procesa un archivo. Este es el modo óptimo de interpretar un archivo que tenga en disco.

## Parámetros

`filename`  
Ruta al archivo que contiene el mensaje. El archivo es abierto y secuenciado a través del analizador sintáctico.

> [!NOTE]
> El mensaje contenido en `filename` debe terminar con una nueva línea (`CRLF`); de lo contrario, no se analizará la última línea del mensaje.

## Valores devueltos

Devuelve un recurso `MIME` que representa la estructura, o `false` en caso de error.

## Notas

> [!NOTE]
> Se recomienda llamar a `mailparse_msg_free` en el resultado de esta función, cuando ya no sea necesaria, para evitar fugas de memoria

## Véase también

mailparse_msg_free

mailparse_msg_create
