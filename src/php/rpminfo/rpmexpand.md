---
title: rpmexpand
description: Obtiene el valor expandido de una macro RPM
source_url: https://www.php.net/manual/es/function.rpmexpand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rpminfo/functions/rpmexpand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rpminfo
translation_status: ready
translation_reviewed: true
translation_revision: 1d4f5d151
order: 72470
---

rpmexpand

Obtiene el valor expandido de una macro RPM

## Descripción

```php
rpmexpand(string $text): string
```php

Obtiene el valor expandido de una macro RPM.

## Parámetros

`text`  
El texto con las macros RPM a expandir.

## Valores devueltos

Un `string` con la(s) macro(s) expandida(s) concatenada(s).

## Ejemplos

Un ejemplo de `rpmexpand`

```
<?php
$distro = rpmexpand("%{?fedora:Fedora %{fedora}}%{?rhel:Enterprise Linux %{rhel}}");
print_r($distro);
?>

   
```php

El ejemplo anterior mostrará:

    Fedora 41

## Véase también

rpmexpandnumeric
