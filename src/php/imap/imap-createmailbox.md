---
title: imap_createmailbox
description: Crea un nuevo buzón de correo
source_url: https://www.php.net/manual/es/function.imap-createmailbox.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-createmailbox.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38030
---

imap_createmailbox

Crea un nuevo buzón de correo

## Descripción

```php
imap_createmailbox(IMAP\Connection $imap, string $mailbox): bool
```php

Crea un nuevo buzón de correo llamado `mailbox`.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`mailbox`  
El nombre del buzón de correo, ver la documentación de la función `imap_open` para más información. Los nombres que contienen caracteres internacionales deben ser codificados por la función `imap_utf7_encode`

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_createmailbox`

```
<?php
$mbox = imap_open("{imap.example.org}", "username", "password", OP_HALFOPEN)
     or die("conexión imposible : " . imap_last_error());

$name1 = "phpnewbox";
$name2 = imap_utf7_encode("phpnewböx"); // phpnewb&w7Y-x

$newname = $name1;

echo "El nuevo nombre será '$name1'<br />\n";

// Vamos a crear ahora un nuevo buzón de correo "phptestbox"
// en su carpeta inbox, verificar su estado y, finalmente, eliminarlo
// para devolver su inbox a su estado inicial.

if (@imap_createmailbox($mbox, imap_utf7_encode("{imap.example.org}INBOX.$newname"))) {
    $status = @imap_status($mbox, "{imap.example.org}INBOX.$newname", SA_ALL);
    if ($status) {
        echo "Su nuevo buzón '$name1' está en el siguiente estado :<br />\n";
        echo "Mensajes :   " . $status->messages    . "<br />\n";
        echo "Recientes :     " . $status->recent      . "<br />\n";
        echo "No leídos :     " . $status->unseen      . "<br />\n";
        echo "UIDnext :    " . $status->uidnext     . "<br />\n";
        echo "UIDvalidity :" . $status->uidvalidity . "<br />\n";

        if (imap_renamemailbox($mbox, "{imap.example.org}INBOX.$newname", "{imap.example.org}INBOX.$name2")) {
            echo "renombrando el buzón de correo '$name1' a '$name2'<br />\n";
            $newname = $name2;
        } else {
            echo "imap_renamemailbox en el nuevo buzón de correo falló : " . imap_last_error() . "<br />\n";
        }
    } else {
        echo "imap_status en el nuevo buzón de correo falló : " . imap_last_error() . "<br />\n";
    }

    if (@imap_deletemailbox($mbox, "{imap.example.org}INBOX.$newname")) {
        echo "nuevo buzón de correo eliminado para devolver todo a su estado<br />\n";
    } else {
        echo "imap_deletemailbox en el nuevo buzón de correo falló : " . implode("<br />\n", imap_errors()) . "<br />\n";
    }

} else {
    echo "Imposible crear un nuevo buzón de correo : " . implode("<br />\n", imap_errors()) . "<br />\n";
}

imap_close($mbox);
?>

    
```php

## Véase también

`imap_renamemailbox`, `imap_deletemailbox`
