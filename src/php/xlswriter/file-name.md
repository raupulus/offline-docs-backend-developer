---
title: Vtiful\Kernel\Excel::fileName
description: Vtiful\Kernel\Excel fileName
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.filename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/file-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 102490
---

Vtiful\Kernel\Excel::fileName

Vtiful\Kernel\Excel fileName

## Descripción

```php
public Vtiful\Kernel\Excel::fileName(string $fileName, [string $sheetName])
```php

Crear un nuevo archivo xlsx y crea una hoja de trabajo.

## Parámetros

`fileName`  
Nombre del archivo XLSX

`sheetName`  
Nombre de la hoja de trabajo

## Valores devueltos

instancia `Vtiful\Kernel\Excel`

## Ejemplos

ejemplo

```
<?php
$config = [
  'path' => '/home/viest'
];

$fileObject = new \Vtiful\Kernel\Excel($config);

$file = $fileObject->fileName('tutorial.xlsx', 'sheet');
?>

   
```php
