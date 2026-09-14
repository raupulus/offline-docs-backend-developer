---
title: Vtiful\Kernel\Excel::getHandle
description: Vtiful\Kernel\Excel getHandle
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.getHandle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/get-handle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: '469121548'
order: 102500
---

Vtiful\Kernel\Excel::getHandle

Vtiful\Kernel\Excel getHandle

## Descripción

```php
public Vtiful\Kernel\Excel::getHandle()
```php

Consigue el manejo de los recursos de texto xlsx.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Recurso

## Ejemplos

ejemplo

```
<?php
$config = [
    'path' => './tests'
];

$fileObject  = new \Vtiful\Kernel\Excel($config);

$file = $fileObject->fileName('tutorial.xlsx', 'sheet_one')
    ->header(['name', 'age']);

$handle = $file->getHandle();
?>

   
```php
