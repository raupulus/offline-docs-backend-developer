---
title: imap_ping
description: Verifica que el flujo IMAP sigue activo
source_url: https://www.php.net/manual/es/function.imap-ping.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-ping.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38410
---

imap_ping

Verifica que el flujo IMAP sigue activo

## Descripción

```php
imap_ping(IMAP\Connection $imap): bool
```php

Verifica que el flujo sigue activo, enviándole un ping. Esta función permite darse cuenta de que ha llegado un correo electrónico: es incluso el método recomendado para pruebas periódicas de verificación del correo. Esta función también puede servir para mantener una conexión abierta, con los servidores que tienen un tiempo de expiración.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

## Valores devueltos

Devuelve `true` si el flujo sigue activo, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_ping`

```
<?php

$imap = imap_open("{imap.example.org}", "mailadmin", "password");

// después de una pausa
if (!imap_ping($imap)) {
    // realice un proceso para reconectar
}

?>

    
```php
