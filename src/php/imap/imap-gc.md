---
title: imap_gc
description: Borra la caché IMAP
source_url: https://www.php.net/manual/es/function.imap-gc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-gc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 673d373ed
order: 38140
---

imap_gc

Borra la caché IMAP

## Descripción

```php
imap_gc(IMAP\Connection $imap, int $flags): true
```php

Elimina todas las entradas de un tipo dado en la caché IMAP.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`flags`  
Indica el tipo de caché a purgar. Puede ser una combinación de las siguientes constantes: `IMAP_GC_ELT` (caché de los elementos de mensaje), `IMAP_GC_ENV` (sobre y cuerpo), `IMAP_GC_TEXTS` (textos).

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Lanza una excepción `ValueError` si el argumento `flags` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |
| 8.0.0 | Una excepción `ValueError` es ahora lanzada para valores de argumento `flags` inválidos. Anteriormente, se emitía una advertencia y la función devolvía `false`. |

## Ejemplos

Ejemplo con`imap_gc`

```
<?php

$mbox = imap_open("{imap.example.org:143}", "username", "password");

imap_gc($mbox, IMAP_GC_ELT);

?>

    
```php
