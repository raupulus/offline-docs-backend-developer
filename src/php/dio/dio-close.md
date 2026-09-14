---
title: dio_close
description: Cierra el descriptor de fichero fd
source_url: https://www.php.net/manual/es/function.dio-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dio/functions/dio-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dio
translation_status: ready
translation_revision: 96c9d88ba
order: 11850
---

dio_close

Cierra el descriptor de fichero fd

## Descripción

```php
dio_close(resource $fd): void
```php

La función `dio_close` cierra el descriptor de fichero `fd`.

## Parámetros

`fd`  
Descriptor de fichero devuelto por `dio_open`.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Cerrando un descriptor de fichero

```
<?php
$fd = dio_open('/dev/ttyS0', O_RDWR);

dio_close($fd);
?>

    
```php

## Véase también

`dio_open`
