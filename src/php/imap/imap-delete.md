---
title: imap_delete
description: Marca el fichero para el borrado, en el buzón de correo actual
source_url: https://www.php.net/manual/es/function.imap-delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 673d373ed
order: 38040
---

imap_delete

Marca el fichero para el borrado, en el buzón de correo actual

## Descripción

```php
imap_delete(IMAP\Connection $imap, string $message_nums, [int $flags]): true
```php

Marca los mensajes `message_nums` para el borrado. El borrado real no intervendrá hasta la llamada de la función `imap_expunge` o de `imap_close` con el parámetro opcional `CL_EXPUNGE`.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_nums`  
Un string representando uno o varios mensajes en un estilo de formato de una secuencia IMAP4 (`"n"`, `"n:m"`, o una combinación de esto, delimitado por comas).

`flags`  
Puede ser definido a `FT_UID` que solicita a la función tratar el argumento `message_nums` como un `UID`.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Lanza una excepción `ValueError` si el parámetro `flags` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |
| 8.0.0 | Una excepción `ValueError` es ahora lanzada para valores de parámetro `flags` inválidos. Anteriormente, una advertencia era emitida y la función retornaba `false`. |

## Ejemplos

Ejemplo con `imap_delete`

```
<?php

$mbox = imap_open("{imap.example.org}INBOX", "username", "password")
    or die("Conexión imposible : " . imap_last_error());

$check = imap_mailboxmsginfo($mbox);
echo "Número de mensajes antes del borrado : " . $check->Nmsgs . "<br />\n";

imap_delete($mbox, 1);

$check = imap_mailboxmsginfo($mbox);
echo "Número de mensajes después del borrado : " . $check->Nmsgs . "<br />\n";

imap_expunge($mbox);

$check = imap_mailboxmsginfo($mbox);
echo "Número de mensajes después de imap_expunge : " . $check->Nmsgs . "<br />\n";

imap_close($mbox);
?>

    
```php

## Notas

> [!NOTE]
> Los buzones de correo IMAP no tienen los flags de sus mensajes guardados entre las conexiones, por lo que la función `imap_expunge` debe ser llamada durante la misma conexión para que los mensajes marcados para el borrado sean realmente purgados.

## Véase también

`imap_undelete`, `imap_expunge`, `imap_close`
