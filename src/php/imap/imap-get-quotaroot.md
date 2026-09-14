---
title: imap_get_quotaroot
description: Lee los cuotas de cada usuario
source_url: https://www.php.net/manual/es/function.imap-get-quotaroot.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-get-quotaroot.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38160
---

imap_get_quotaroot

Lee los cuotas de cada usuario

## Descripción

```php
imap_get_quotaroot(IMAP\Connection $imap, string $mailbox): array
```php

Recupera los cuotas de cada usuario. El valor límite representa el espacio límite asignado para este usuario para el uso de su buzón de correo. El valor de uso representa el tamaño actual del buzón de correo.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`mailbox`  
`mailbox` debe ser un nombre de buzón de correo (i.e. INBOX).

## Valores devueltos

Devuelve un array de enteros, conteniendo los cuotas del buzón de correo del usuario. Todos los valores son representados por una clave basada en el nombre del buzón, y por un array representando el nivel de uso y los límites.

Esta función devolverá `false` si ocurre un error, y un array de datos si la respuesta del servidor no pudo ser comprendida.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_get_quotaroot`

```
<?php
$mbox = imap_open("{imap.example.org}", "kalowsky", "password", OP_HALFOPEN)
      or die("Conexión imposible : " . imap_last_error());

$quota = imap_get_quotaroot($mbox, "INBOX");
if (is_array($quota)) {
   $storage = $quota['STORAGE'];
   echo "STORAGE nivel de uso : " .  $storage['usage'];
   echo "STORAGE tamaño límite : " .  $storage['limit'];

   $message = $quota['MESSAGE'];
   echo "MESSAGE nivel de uso : " .  $message['usage'];
   echo "MESSAGE tamaño límite : " .  $message['limit'];

   /* ...  */

}

imap_close($mbox);
?>

    
```php

## Notas

Esta función es accesible únicamente a los usuarios de la biblioteca c-client2000 o más reciente.

`imap` debería ser abierto como el usuario cuyo buzón de correo se desea verificar.

## Véase también

`imap_open`, `imap_set_quota`, `imap_get_quota`
