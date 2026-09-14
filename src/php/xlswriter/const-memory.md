---
title: Vtiful\Kernel\Excel::constMemory
description: Vtiful\Kernel\Excel constMemory
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.constMemory.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/const-memory.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 102460
---

Vtiful\Kernel\Excel::constMemory

Vtiful\Kernel\Excel constMemory

## Descripción

```php
public Vtiful\Kernel\Excel::constMemory(string $fileName, [string $sheetName])
```php

Escribe un archivo grande con un uso constante de la memoria.

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

$file = $fileObject->constMemory('tutorial.xlsx', 'sheet');
?>

   
```php
