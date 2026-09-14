---
title: imap_set_quota
description: Modifica el cupo de un buzón de correo
source_url: https://www.php.net/manual/es/function.imap-set-quota.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-set-quota.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38530
---

imap_set_quota

Modifica el cupo de un buzón de correo

## Descripción

```php
imap_set_quota(IMAP\Connection $imap, string $quota_root, int $mailbox_size): bool
```php

Modifica el cupo del buzón de correo `quota_root`.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`quota_root`  
El buzón de correo cuyo cupo debe ser modificado. Debe seguir el formato estándar IMAP para un buzón de correo: `user.name`.

`mailbox_size`  
El tamaño máximo (en KB) para el buzón `quota_root`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_set_quota`

```
<?php
$mbox = imap_open("{imap.example.org:143}", "mailadmin", "password");

if (!imap_set_quota($mbox, "user.kalowsky", 3000)) {
    echo "Fallo al definir el cupo\n";
    return;
}

imap_close($mbox);
?>

    
```php

## Notas

`imap_get_quota` actualmente solo funciona con las bibliotecas c-client2000.

`imap_set_quota` requiere que `imap` haya sido abierto con una cuenta de administrador, para tener los derechos necesarios: no funcionará con ningún otro usuario.

## Véase también

`imap_open`, `imap_get_quota`
