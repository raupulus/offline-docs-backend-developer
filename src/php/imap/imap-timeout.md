---
title: imap_timeout
description: Configura o devuelve el timeout
source_url: https://www.php.net/manual/es/function.imap-timeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-timeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: e2f50c240
order: 38600
---

imap_timeout

Configura o devuelve el timeout

## Descripción

```php
imap_timeout(int $timeout_type, [int $timeout]): int
```php

Define o devuelve el timeout imap.

## Parámetros

`timeout_type`  
Un valor entre los siguientes: `IMAP_OPENTIMEOUT`, `IMAP_READTIMEOUT`, `IMAP_WRITETIMEOUT`, o `IMAP_CLOSETIMEOUT`.

`timeout`  
El timeout, en segundos.

## Valores devueltos

Si el argumento `timeout` está definido, esta función devuelve `true` en caso de éxito y `false` si ocurre un error.

Si `timeout` no se proporciona o si se evalúa a -1, el timeout actual será devuelto como un `int`.

## Ejemplos

Ejemplo con `imap_timeout`

```
<?php

echo "El timeout actual es " . imap_timeout(IMAP_READTIMEOUT) . "\n";

?>

    
```php
