---
title: imap_getacl
description: Devuelve el ACL para el buzón
source_url: https://www.php.net/manual/es/function.imap-getacl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-getacl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38170
---

imap_getacl

Devuelve el ACL para el buzón

## Descripción

```php
imap_getacl(IMAP\Connection $imap, string $mailbox): array
```php

Recupera el ACL para el buzón dado.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`mailbox`  
El nombre del buzón, ver la documentación de la función `imap_open` para más detalles.

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

## Valores devueltos

Devuelve un array asociativo en la forma "folder" =\> "acl", o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_getacl`

```
<?php

print_r(imap_getacl($imap, 'user.joecool'));

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [asubfolder] => lrswipcda
        [anothersubfolder] => lrswipcda
    )

## Notas

Esta función está actualmente disponible solo para los usuarios de la biblioteca `c-client2000` o superior.

## Véase también

`imap_setacl`
