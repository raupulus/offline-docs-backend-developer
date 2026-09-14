---
title: SplFixedArray::__wakeup
description: Reinicializa el array después de su deserialización
source_url: https://www.php.net/manual/es/splfixedarray.wakeup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfixedarray/wakeup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 84840
---

SplFixedArray::\_\_wakeup

Reinicializa el array después de su deserialización

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.4.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] public SplFixedArray::__wakeup(): void
```php

Reinicializa el array después de su deserialización.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Este método es ahora obsoleto, utilice SplFixedArray::\_\_unserialize en su lugar. |
