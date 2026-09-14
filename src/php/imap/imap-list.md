---
title: imap_list
description: Lee la lista de buzones de correo
source_url: https://www.php.net/manual/es/function.imap-list.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-list.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38250
---

imap_list

Lee la lista de buzones de correo

## Descripción

```php
imap_list(IMAP\Connection $imap, string $reference, string $pattern): array
```php

Lee la lista de buzones de correo.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`reference`  
`reference` debería ser solo el servidor en la forma descrita en `imap_open`

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

`pattern`  
Especifica en qué parte de la jerarquía del buzón comenzar la búsqueda.

Hay dos caracteres especiales que se pueden pasar como parte del `pattern`: '`*`' y '`%`'. '`*`' significa devolver todos los buzones. Si se pasa `pattern` como '`*`', se obtendrá una lista de toda la jerarquía del buzón. '`%`' significa devolver solo el nivel actual. '`%`' como parámetro `pattern` devolverá solo los buzones de nivel superior; '`~/mail/%`' en `UW_IMAPD` devolverá cada buzón en el directorio `~/mail`, pero ninguno en las subcarpetas de ese directorio.

## Valores devueltos

Devuelve un array que contiene los nombres de los buzones de correo, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_list`

```
<?php
$mbox = imap_open("{imap.example.org}", "username", "password", OP_HALFOPEN)
      or die("Conexión imposible: " . imap_last_error());

$list = imap_list($mbox, "{imap.example.org}", "*");
if (is_array($list)) {
    foreach ($list as $val) {
        echo imap_utf7_decode($val) . "\n";
    }
} else {
    echo "imap_list ha fallado: " . imap_last_error() . "\n";
}

imap_close($mbox);
?>

    
```php

## Véase también

`imap_getmailboxes`, `imap_lsub`
