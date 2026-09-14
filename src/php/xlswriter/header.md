---
title: Vtiful\Kernel\Excel::header
description: Vtiful\Kernel\Excel header
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.header.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/header.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: '469121548'
order: 102510
---

Vtiful\Kernel\Excel::header

Vtiful\Kernel\Excel header

## Descripción

```php
public Vtiful\Kernel\Excel::header(array $headerData)
```php

Escribe un encabezado en la hoja de trabajo.

## Parámetros

`headerData`  
datos de la cabecera de la hoja de trabajo

## Valores devueltos

instancia `Vtiful\Kernel\Excel`

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
?>

   
```php
