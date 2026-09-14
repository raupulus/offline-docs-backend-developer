---
title: imap_mailboxmsginfo
description: Lee la información sobre el buzón de correo actual
source_url: https://www.php.net/manual/es/function.imap-mailboxmsginfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-mailboxmsginfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 848fab73a
order: 38340
---

imap_mailboxmsginfo

Lee la información sobre el buzón de correo actual

## Descripción

```php
imap_mailboxmsginfo(IMAP\Connection $imap): stdClass
```php

`imap_mailboxmsginfo` verifica el estado actual del buzón de correo en el servidor. Es similar al uso de la función `imap_status`, pero también proporciona el tamaño total de los mensajes del buzón de correo, lo que requiere un poco más de tiempo de ejecución.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

## Valores devueltos

Devuelve un objeto con las siguientes propiedades:

|  |  |
|----|----|
| Date | Fecha de la última modificación del contenido del buzón de correo (fecha y hora actuales) |
| Driver | Controlador |
| Mailbox | Nombre del buzón de correo |
| Nmsgs | Número de mensajes |
| Recent | Número de mensajes recientes |
| Unread | Número de mensajes no leídos |
| Deleted | Número de mensajes eliminados |
| Size | Tamaño del buzón de correo |

Propiedades del buzón de correo

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_mailboxmsginfo`

```
<?php

$mbox = imap_open("{imap.example.org}INBOX", "username", "password")
      or die("Conexión imposible: " . imap_last_error());

$check = imap_mailboxmsginfo($mbox);

if ($check) {
    echo "Fecha : "     . $check->Date    . "<br />\n" ;
    echo "Controlador : "   . $check->Driver  . "<br />\n" ;
    echo "Buzón de correo : "  . $check->Mailbox . "<br />\n" ;
    echo "Mensajes : " . $check->Nmsgs   . "<br />\n" ;
    echo "Reciente : "   . $check->Recent  . "<br />\n" ;
    echo "No leído : "   . $check->Unread  . "<br />\n" ;
    echo "Eliminado : "  . $check->Deleted . "<br />\n" ;
    echo "Tamaño : "     . $check->Size    . "<br />\n" ;
} else {
    echo "imap_mailboxmsginfo() ha fallado: " . imap_last_error() . "<br />\n";
}

imap_close($mbox);

?>

    
```php
