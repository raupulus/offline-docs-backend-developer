---
title: rnp_dump_packets_to_json
description: Muestra la información del flujo de paquetes OpenPGP en un string JSON
source_url: https://www.php.net/manual/es/function.rnp-dump-packets-to-json.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-dump-packets-to-json.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72110
---

rnp_dump_packets_to_json

Muestra la información del flujo de paquetes OpenPGP en un string JSON

## Descripción

```php
rnp_dump_packets_to_json(string $input, int $flags): string
```php

## Parámetros

`input`  
El string de entrada que contiene los datos OpenPGP, ya sea en formato binario o en formato ASCII-armored.

`flags`  
Ver las constantes predefinidas `RNP_JSON_DUMP_*`.

## Valores devueltos

Un string JSON con la información o `false` si ocurre un error
