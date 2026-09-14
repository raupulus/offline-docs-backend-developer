---
title: yaz_scan_result
description: Devuelve el resultado de un escaneado
source_url: https://www.php.net/manual/es/function.yaz-scan-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-scan-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 107910
---

yaz_scan_result

Devuelve el resultado de un escaneado

## Descripción

```php
yaz_scan_result(resource $id, [array $result]): array
```php

`yaz_scan_result` devuelve una tabla con los términos y la información asociada tal y como fue recibida del servidor en la última función `yaz_scan` realizada.

## Parámetros

`id`  
El recurso de conexión asociado por `yaz_connect`.

`result`  
Si se indica, este array será modificado para contener información adicional tomada de la respuesta del scan:

- `number` - Número de entradas devueltas

- `stepsize` - Tamaño del paso

- `position` - Posición del término

- `status` - Estado del escaneo

## Valores devueltos

Devuelve un array (0..n-1) donde n es el número de elementos devuetos. Cada valor es un par donde el primer elemento es el término, y el segundo es el contador de resultados.
