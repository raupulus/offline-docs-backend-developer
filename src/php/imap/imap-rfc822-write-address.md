---
title: imap_rfc822_write_address
description: Devuelve una dirección de correo electrónico formateada correctamente
source_url: https://www.php.net/manual/es/function.imap-rfc822-write-address.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-rfc822-write-address.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: e2f50c240
order: 38480
---

imap_rfc822_write_address

Devuelve una dirección de correo electrónico formateada correctamente

## Descripción

```php
imap_rfc822_write_address(string $mailbox, string $hostname, string $personal): string
```php

Devuelve una dirección de correo electrónico formateada correctamente según la [RFC2822](https://datatracker.ietf.org/doc/html/rfc2822).

## Parámetros

`mailbox`  
El nombre del buzón de correo, consulte la documentación de la función `imap_open` para más detalles

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

`hostname`  
La parte del host del correo electrónico

`personal`  
El nombre del propietario de la cuenta

## Valores devueltos

Devuelve una dirección de correo electrónico formateada correctamente según la [RFC2822](https://datatracker.ietf.org/doc/html/rfc2822), o `false` si ocurre un error.

## Ejemplos

Ejemplo con `imap_rfc822_write_address`

```
<?php
echo imap_rfc822_write_address("hartmut", "example.com", "Hartmut Holzgraefe");
?>

    
```php

El ejemplo anterior mostrará:

    Hartmut Holzgraefe <hartmut@example.com>
