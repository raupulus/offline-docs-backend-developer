---
title: getprotobyname
description: Devuelve el número de protocolo asociado a un nombre de protocolo
source_url: https://www.php.net/manual/es/function.getprotobyname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/getprotobyname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 56330
---

getprotobyname

Devuelve el número de protocolo asociado a un nombre de protocolo

## Descripción

```php
getprotobyname(string $protocol): int
```php

`getprotobyname` devuelve el número de protocolo asociado con el nombre de protocolo `protocol`, como en `/etc/protocols`.

## Parámetros

`protocol`  
El nombre del protocolo.

## Valores devueltos

Devuelve el número del protocolo, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `getprotobyname`

```
<?php
$protocol = 'tcp';
$get_prot = getprotobyname($protocol);
if ($get_prot === FALSE) {
    echo 'Protocolo inválido';
} else {
    echo 'Protocolo #' . $get_prot;
}
?>

    
```php

## Véase también

`getprotobynumber`
