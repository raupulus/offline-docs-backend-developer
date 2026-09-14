---
title: rrdc_disconnect
description: Cierra todas las conexiones al demonio de caché rrd
source_url: https://www.php.net/manual/es/function.rrdc-disconnect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/functions/rrdc-disconnect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72680
---

rrdc_disconnect

Cierra todas las conexiones al demonio de caché rrd

## Descripción

```php
rrdc_disconnect(): void
```php

Cierra todas las conexiones al demonio de caché rrd.

Esta función es llamada automáticamente cuando el proceso global PHP finaliza. Esto depende de la API utilizada. Por ejemplo, esta función es llamada automáticamente al final de un script de línea de comandos.

Depende del usuario decidir si llamar a esta función al final de cada petición o no.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.
