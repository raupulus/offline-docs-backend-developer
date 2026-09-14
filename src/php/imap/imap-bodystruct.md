---
title: imap_bodystruct
description: Lee la estructura de una sección del cuerpo de un correo electrónico
source_url: https://www.php.net/manual/es/function.imap-bodystruct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-bodystruct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 37980
---

imap_bodystruct

Lee la estructura de una sección del cuerpo de un correo electrónico

## Descripción

```php
imap_bodystruct(IMAP\Connection $imap, int $message_num, string $section): stdClass
```php

Lee la estructura de una sección especificada del cuerpo de un correo electrónico.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`message_num`  
El número del mensaje

`section`  
La sección del cuerpo a leer

## Valores devueltos

Devuelve la información en un objeto, o `false` si ocurre un error. Para una descripción detallada de la estructura del objeto así como de sus propiedades, consulte la función `imap_fetchstructure`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Véase también

`imap_fetchstructure`
