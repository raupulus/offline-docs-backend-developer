---
title: imap_status
description: Devuelve la información de estado sobre un buzón de correo
source_url: https://www.php.net/manual/es/function.imap-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38570
---

imap_status

Devuelve la información de estado sobre un buzón de correo

## Descripción

```php
imap_status(IMAP\Connection $imap, string $mailbox, int $flags): stdClass
```php

Devuelve la información de estado sobre el buzón de correo `mailbox`.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`mailbox`  
El nombre del buzón de correo, ver la documentación de la función `imap_open` para más detalles

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

`flags`  
Los flags válidos son:

- `SA_MESSAGES` - establece el valor de `$status->messages` al número de mensajes en el buzón de correo.

- `SA_RECENT` - establece el valor de `$status->recent` al número de mensajes recientes en el buzón de correo.

- `SA_UNSEEN` - establece el valor de `$status->unseen` al número de mensajes no leídos en el buzón de correo.

- `SA_UIDNEXT` - establece el valor de `$status->uidnext` al siguiente valor de uid que será utilizado.

- `SA_UIDVALIDITY` - establece el valor de `$status->uidvalidity` a una constante, que cambia cuando el uid del buzón de correo ya no es válido.

- `SA_ALL` - establece todos los valores anteriores.

## Valores devueltos

Esta función devuelve un objeto que contiene la información de estado, o `false` si ocurre un error. El objeto tiene las siguientes propiedades: `messages`, `recent`, `unseen`, `uidnext`, y `uidvalidity`.

`flags` también está definido, que contiene una máscara con una de las constantes anteriores.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_status`

```
<?php
$mbox = imap_open("{imap.example.com}", "username", "password", OP_HALFOPEN)
      or die("Conexión imposible : " . imap_last_error());

$status = imap_status($mbox, "{imap.example.org}INBOX", SA_ALL);
if ($status) {
  echo "Mensajes :   " . $status->messages    . "<br />\n";
  echo "Reciente :   " . $status->recent      . "<br />\n";
  echo "No leído :   " . $status->unseen      . "<br />\n";
  echo "Próximo UID: " . $status->uidnext     . "<br />\n";
  echo "Validez del UID: " . $status->uidvalidity . "<br />\n";
} else {
  echo "imap_status ha fallado : " . imap_last_error() . "\n";
}

imap_close($mbox);
?>

    
```php
