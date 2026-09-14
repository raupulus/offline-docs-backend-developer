---
title: imap_savebody
description: Guarda una parte específica del cuerpo en un fichero
source_url: https://www.php.net/manual/es/function.imap-savebody.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-savebody.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38490
---

imap_savebody

Guarda una parte específica del cuerpo en un fichero

## Descripción

```php
imap_savebody(IMAP\Connection $imap, resource $file, int $message_num, [string $section], [int $flags]): bool
```php

Guarda una parte del cuerpo del mensaje especificado.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`file`  
La ruta hacia el fichero de guardado, en forma de una `string` o un descriptor de fichero válido devuelto por la función `fopen`.

`message_num`  
El número del mensaje

`section`  
El número de la sección. Es una `string` de enteros, delimitados por una coma que corresponden al índice en la lista de secciones del cuerpo, tal como se prevé en la especificación IMAP4.

`flags`  
Una máscara que contiene una o más de las siguientes valores:

- `FT_UID` - El número `message_num` es un UID

- `FT_PEEK` - No definir el flag \Seen si no está ya definido

- `FT_INTERNAL` - La `string` devuelta está en un formato interno, que no corresponde a CRLF.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_fetchbody`
