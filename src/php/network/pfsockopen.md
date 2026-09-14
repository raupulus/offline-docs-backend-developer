---
title: pfsockopen
description: Se abre un socket de conexión Internet o Unix persistente
source_url: https://www.php.net/manual/es/function.pfsockopen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/pfsockopen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: false
translation_revision: 4e6f0774f
order: 56510
---

pfsockopen

Se abre un socket de conexión Internet o Unix persistente

## Descripción

```php
pfsockopen(string $hostname, [int $port], [int $error_code], [string $error_message], [float $timeout]): resource
```php

`pfsockopen` se comporta exactamente como `fsockopen` pero la conexión abierta permanece abierta, incluso después de finalizar el script. Es la versión persistente de `fsockopen`.

## Parámetros

Para más información sobre los argumentos, consúltese la documentación sobre la función `fsockopen`.

## Valores devueltos

`pfsockopen` devuelve un puntero de fichero que puede ser utilizado con otras funciones de fichero (como `fgets`, `fgetss`, `fwrite`, `fclose`, y `feof`), o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | `timeout` ahora es nullable. |

## Véase también

`fsockopen`
