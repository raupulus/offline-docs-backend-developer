---
title: gethostname
description: Lee el nombre del host
source_url: https://www.php.net/manual/es/function.gethostname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/gethostname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: false
translation_revision: f33c30178
order: 56310
---

gethostname

Lee el nombre del host

## Descripción

```php
gethostname(): string
```php

`gethostname` lee el nombre de host estándar para la máquina host.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un string con el nombre de host, en caso de éxito y de lo contrario `false`.

## Ejemplos

Ejemplo con `gethostname`

```
<?php
echo gethostname(); // debe mostrar i.e : sandie
?>

    
```php

## Véase también

`gethostbyname`, `gethostbyaddr`, `php_uname`
