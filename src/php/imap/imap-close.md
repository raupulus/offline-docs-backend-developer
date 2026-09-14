---
title: imap_close
description: Termina un flujo IMAP
source_url: https://www.php.net/manual/es/function.imap-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 6054b3697
order: 38010
---

imap_close

Termina un flujo IMAP

## Descripción

```php
imap_close(IMAP\Connection $imap, [int $flags]): true
```php

Termina un flujo IMAP.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`flags`  
Si se establece en `CL_EXPUNGE`, la función realizará una purga automática del buzón antes de cerrarlo, eliminando todos los mensajes marcados para su eliminación. Se puede lograr lo mismo con la función `imap_expunge`

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Lanza una excepción `ValueError` si el argumento `flags` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |
| 8.0.0 | Ahora se lanza una excepción `ValueError` para valores de argumento `flags` inválidos. Anteriormente, se emitía una advertencia y la función devolvía `false`. |

## Véase también

`imap_open`
