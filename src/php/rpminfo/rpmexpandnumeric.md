---
title: rpmexpandnumeric
description: Obtiene el valor numérico de una macro RPM
source_url: https://www.php.net/manual/es/function.rpmexpandnumeric.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rpminfo/functions/rpmexpandnumeric.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rpminfo
translation_status: ready
translation_reviewed: true
translation_revision: 1d4f5d151
order: 72480
---

rpmexpandnumeric

Obtiene el valor numérico de una macro RPM

## Descripción

```php
rpmexpandnumeric(string $text): int
```php

Obtiene el valor numérico de una macro RPM.

## Parámetros

`text`  
El texto con las macros RPM a expandir.

## Valores devueltos

La expansión de la macro como `int`. Los valores booleanos (`Y` o `y` retorna 1, `N` o `n` retorna `0`) también están permitidos. Una macro no definida retorna `0`.

## Ejemplos

Un ejemplo `rpmexpandnumeric`

```
<?php
$bits = rpmexpandnumeric("%__isa_bits");
print_r($bits);
?>

   
```php

El ejemplo anterior mostrará:

    64

## Véase también

rpmexpand
