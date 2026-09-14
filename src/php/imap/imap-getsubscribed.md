---
title: imap_getsubscribed
description: Lista todas las carpetas de correo suscritas
source_url: https://www.php.net/manual/es/function.imap-getsubscribed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-getsubscribed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38190
---

imap_getsubscribed

Lista todas las carpetas de correo suscritas

## Descripción

```php
imap_getsubscribed(IMAP\Connection $imap, string $reference, string $pattern): array
```php

Lista todas las carpetas de correo suscritas.

`imap_getsubscribed` es idéntico a `imap_getmailboxes`, pero solo devuelve las carpetas de correo a las que el usuario está suscrito.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`reference`  
`reference` debe ser solo el servidor en la forma descrita en `imap_open`

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

`pattern`  
Especifica en qué parte de la jerarquía del buzón comenzar la búsqueda.

Hay dos caracteres especiales que se pueden pasar como parte del `pattern`: '`*`' y '`%`'. '`*`' significa devolver todos los buzones. Si se pasa `pattern` como '`*`', se obtendrá una lista de toda la jerarquía del buzón. '`%`' significa devolver solo el nivel actual. '`%`' como parámetro `pattern` devolverá solo los buzones de nivel superior; '`~/mail/%`' en `UW_IMAPD` devolverá cada buzón en el directorio `~/mail`, pero ninguno en las subcarpetas de ese directorio.

## Valores devueltos

Devuelve un array de objetos que contienen información sobre las carpetas de correo. Cada objeto posee un atributo de `name`, que contiene el nombre completo de la carpeta de correo, `delimiter` que es el delimitador jerárquico y `attributes`. `attributes` es una máscara de bits, que contiene :

- `LATT_NOINFERIORS` - Esta carpeta de correo no tiene "hijos" (no hay más carpetas de correo debajo de esta).

- `LATT_NOSELECT` - Esto es solo un contenedor, no una carpeta de correo (no se puede abrir).

- `LATT_MARKED` - Esta carpeta de correo está marcada. Utilizado únicamente con UW-IMAPD.

- `LATT_UNMARKED` - Esta carpeta de correo no está marcada. Utilizado únicamente con UW-IMAPD.

- `LATT_REFERRAL` - Este contenedor tiene una referencia a una carpeta de correo remota.

- `LATT_HASCHILDREN` - Esta carpeta de correo tiene inferiores seleccionables.

- `LATT_HASNOCHILDREN` - Esta carpeta de correo no tiene inferiores seleccionables.

La función devuelve `false` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |
