---
title: rpmvercmp
description: Comparación de versiones RPM
source_url: https://www.php.net/manual/es/function.rpmvercmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rpminfo/functions/rpmvercmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rpminfo
translation_status: ready
translation_reviewed: true
translation_revision: 1d4f5d151
order: 72510
---

rpmvercmp

Comparación de versiones RPM

## Descripción

```php
rpmvercmp(string $evr1, string $evr2, [string $operator]): int
```php

Compara dos versiones de paquetes RPM.

## Parámetros

`evr1`  
La primera cadena `epoch:version-release`.

`evr2`  
La segunda cadena `epoch:version-release`.

`operator`  
Un operador opcional. Los operadores posibles son: `<`, `lt`, `<=`, `le`, `>`, `gt`, `>=`, `ge`, `==`, `=`, `eq`, `!=`, `<>`, `ne`.

Este parámetro distingue mayúsculas y minúsculas, los valores deben estar en minúsculas.

## Valores devueltos

Devuelve `-1` si `evr1` es inferior a `evr2`, `1` si `evr1` es superior a `evr2`, y `0` si son iguales.

Cuando se utiliza el argumento opcional `operator`, la función devolverá `true` si la relación es la especificada por el operador, en caso contrario `false`.

## Historial de cambios

| Versión            | Descripción                             |
|--------------------|-----------------------------------------|
| PECL rpminfo 0.7.0 | El `operator` opcional ha sido añadido. |
