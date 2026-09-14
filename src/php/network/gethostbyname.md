---
title: gethostbyname
description: Obtener la dirección IPv4 que corresponde a un nombre de host de Internet
  dado
source_url: https://www.php.net/manual/es/function.gethostbyname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/gethostbyname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_revision: 96c9d88ba
order: 56290
---

gethostbyname

Obtener la dirección IPv4 que corresponde a un nombre de host de Internet dado

## Descripción

```php
gethostbyname(string $hostname): string
```php

Devuelve la dirección IPv4 del host de Internet especificado por `hostname`.

## Parámetros

`hostname`  
El nombre de host.

## Valores devueltos

Devuelve la dirección IPv4 o un string que contiene el `hostname` sin modificar en caso de error.

## Ejemplos

Ejemplo simple de `gethostbyname`

```
<?php
$ip = gethostbyname('www.example.com');

echo $ip;
?>

    
```php

## Véase también

`gethostbyaddr`, `gethostbynamel`, `inet_pton`, `inet_ntop`
