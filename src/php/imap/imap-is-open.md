---
title: imap_is_open
description: Verificar si el flujo IMAP sigue siendo válido
source_url: https://www.php.net/manual/es/function.imap-is-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-is-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 919a02eb2
order: 38230
---

imap_is_open

Verificar si el flujo

IMAP

sigue siendo válido

## Descripción

```php
imap_is_open(IMAP\Connection $imap): bool
```php

Verifica si el flujo IMAP sigue siendo válido.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

## Valores devueltos

Devuelve `true` si el flujo sigue siendo válido, `false` en caso contrario.

## Ejemplos

Ejemplo de `imap_is_open`

```
<?php
$mbox = imap_open("{imap.example.org:143}INBOX", "username", "password") or die(implode(", ", imap_errors()));
imap_is_open($mbox);
// ...
?>

    
```php
