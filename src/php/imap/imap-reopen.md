---
title: imap_reopen
description: Reabre un flujo IMAP hacia una nueva caja de correo
source_url: https://www.php.net/manual/es/function.imap-reopen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-reopen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38450
---

imap_reopen

Reabre un flujo

IMAP

hacia una nueva caja de correo

## Descripción

```php
imap_reopen(IMAP\Connection $imap, string $mailbox, [int $flags], [int $retries]): bool
```php

Reabre la conexión especificada al servidor IMAP o NNTP, con una nueva caja de correo.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`mailbox`  
El nombre de la caja de correo, ver la documentación de la función `imap_open` para más detalles

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

`flags`  
`flags` es una máscara de bits, que puede contener los siguientes valores:

- `OP_READONLY` - Abre una caja de correo en modo de solo lectura

- `OP_ANONYMOUS` - No utilizar, o modificar el fichero `.newsrc` para las noticias (NNTP únicamente)

- `OP_HALFOPEN` - Para los nombres IMAP y NNTP, abre una conexión pero no abre una caja de correo.

- `OP_EXPUNGE` - Elimina silenciosamente el flujo reciclado

- `CL_EXPUNGE` - Elimina automáticamente la caja de correo de la lista, al finalizar el flujo. (ver `imap_delete` y `imap_expunge`).

`retries`  
El número máximo de intentos de conexión

## Valores devueltos

Devuelve `true` si el flujo es reabierto, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_reopen`

```
<?php
$mbox = imap_open("{imap.example.org:143}INBOX", "username", "password") or die(implode(", ", imap_errors()));
// ...
imap_reopen($mbox, "{imap.example.org:143}INBOX.Sent") or die(implode(", ", imap_errors()));
// ..
?>

    
```php
