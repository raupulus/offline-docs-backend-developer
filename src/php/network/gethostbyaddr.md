---
title: gethostbyaddr
description: Devuelve el nombre de host correspondiente a una IP
source_url: https://www.php.net/manual/es/function.gethostbyaddr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/gethostbyaddr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 56280
---

gethostbyaddr

Devuelve el nombre de host correspondiente a una IP

## Descripción

```php
gethostbyaddr(string $ip): string
```php

`gethostbyaddr` devuelve el nombre de host correspondiente a la IP `ip`.

## Parámetros

`ip`  
La dirección IP del host.

## Valores devueltos

Devuelve el nombre del host en caso de éxito, la `ip` sin modificar en caso de fallo o `false` si se proporciona una entrada mal formada.

## Ejemplos

Ejemplo con `gethostbyaddr`

```
<?php
$hostname = gethostbyaddr($_SERVER['REMOTE_ADDR']);

echo $hostname;
?>

    
```php

## Véase también

`gethostbyname`, `gethostbynamel`
