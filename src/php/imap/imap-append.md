---
title: imap_append
description: Añade un mensaje en un buzón de correo
source_url: https://www.php.net/manual/es/function.imap-append.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-append.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 37940
---

imap_append

Añade un mensaje en un buzón de correo

## Descripción

```php
imap_append(IMAP\Connection $imap, string $folder, string $message, [string $options], [string $internal_date]): bool
```php

Añade un `message` al `folder` especificado.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`folder`  
El nombre del buzón de correo, ver la documentación de la función `imap_open` para más información

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

`message`  
El mensaje a añadir, en forma de `string`

Al intercambiar con el servidor Cyrus IMAP, se debe utilizar "\r\n" como terminación de línea, en lugar de "\n" o la operación fallará.

`options`  
Si se proporciona, el parámetro `options` será también escrito en el buzón `folder`

`internal_date`  
Si se define este parámetro, establecerá los INTERNALDATE en el mensaje adjunto. El parámetro debe ser una cadena de fecha que cumpla con las especificaciones del rfc2060 para un valor date_time.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |
| 8.0.0 | `options` y `internal_date` ahora son nullables. |

## Ejemplos

Ejemplo con `imap_append`

```
<?php
$imap = imap_open("{imap.example.org}INBOX.Drafts", "username", "password");

$check = imap_check($imap);
echo "Msg Count before append: ". $check->Nmsgs . "\n";

imap_append($imap, "{imap.example.org}INBOX.Drafts"
                   , "From: me@example.com\r\n"
                   . "To: you@example.com\r\n"
                   . "Subject: test\r\n"
                   . "\r\n"
                   . "Este es un mensaje de prueba. Ignórelo.\r\n"
                   );

$check = imap_check($imap);
echo "Número de mensajes después de añadir : ". $check->Nmsgs . "\n";

imap_close($imap);
?>

    
```php
