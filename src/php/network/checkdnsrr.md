---
title: checkdnsrr
description: Resolución DNS de una dirección IP
source_url: https://www.php.net/manual/es/function.checkdnsrr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/checkdnsrr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 56220
---

checkdnsrr

Resolución DNS de una dirección IP

## Descripción

```php
checkdnsrr(string $hostname, [string $type]): bool
```php

Busca el registro DNS de tipo `type` correspondiente al host `hostname`.

## Parámetros

`hostname`  
`hostname` puede ser una dirección IP en formato numérico o un nombre de host.

`type`  
`type` puede ser uno de los siguientes valores: A, MX, NS, SOA, PTR, CNAME, AAAA, A6, SRV, NAPTR, TXT o ANY.

## Valores devueltos

Devuelve `true` si se ha encontrado un registro, y `false` en caso de error o si no se ha encontrado ningún registro.

## Notas

> [!NOTE]
> Para compatibilidad con Windows antes de su implementación, pruebe la clase [PEAR](https://pear.php.net/): [Net_DNS](https://pear.php.net/package/Net_DNS).

## Véase también

`dns_get_record`, `getmxrr`, `gethostbyaddr`, `gethostbyname`, `gethostbynamel`, la página del manual man named(8)
