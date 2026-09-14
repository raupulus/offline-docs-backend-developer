---
title: imap_getmailboxes
description: Lista los buzones de correo y devuelve los detalles de cada uno
source_url: https://www.php.net/manual/es/function.imap-getmailboxes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-getmailboxes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38180
---

imap_getmailboxes

Lista los buzones de correo y devuelve los detalles de cada uno

## Descripción

```php
imap_getmailboxes(IMAP\Connection $imap, string $reference, string $pattern): array
```php

Lista los buzones de correo.

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

Devuelve un array de objetos que contienen información sobre los buzones de correo. Cada objeto posee un atributo de `name`, que contiene el nombre completo del buzón de correo, `delimiter` que es el delimitador jerárquico y `attributes`. `attributes` es una máscara de bits, que contiene :

- `LATT_NOINFERIORS` - Este buzón de correo no tiene "hijos" (no hay más buzones de correo debajo de este) y no puede contener ninguno. Una llamada a la función `imap_createmailbox` no funcionará en este buzón.

- `LATT_NOSELECT` - Esto es solo un contenedor, no un buzón de correo (no se puede abrir).

- `LATT_MARKED` - Este buzón de correo está marcado. Esto significa que puede contener nuevos mensajes desde la última vez que fue verificado. Este marcador no se proporciona con todos los servidores IMAP.

- `LATT_UNMARKED` - Este buzón de correo no está marcado y no contiene nuevos mensajes. Si `MARKED` o `UNMARKED` se proporciona, se puede asumir que el servidor IMAP soporta esta funcionalidad para este buzón de correo.

- `LATT_REFERRAL` - Este contenedor tiene una referencia a un buzón de correo remoto.

- `LATT_HASCHILDREN` - Este buzón de correo tiene inferiores seleccionables.

- `LATT_HASNOCHILDREN` - Este buzón de correo no tiene inferiores seleccionables.

Devuelve `false` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_getmailboxes`

```
<?php
$mbox = imap_open("{imap.example.org}", "username", "password", OP_HALFOPEN)
      or die("Conexión imposible: " . imap_last_error());

$list = imap_getmailboxes($mbox, "{imap.example.org}", "*");
if (is_array($list)) {
    foreach ($list as $key => $val) {
        echo "($key) ";
        echo imap_utf7_decode($val->name) . ",";
        echo "'" . $val->delimiter . "',";
        echo $val->attributes . "<br />\n";
    }
} else {
    echo "imap_getmailboxes ha fallado: " . imap_last_error() . "\n";
}

imap_close($mbox);
?>

    
```php

## Véase también

`imap_getsubscribed`
