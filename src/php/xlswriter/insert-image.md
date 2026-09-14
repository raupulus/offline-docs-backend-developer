---
title: Vtiful\Kernel\Excel::insertImage
description: Vtiful\Kernel\Excel insertImage
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.insertImage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/insert-image.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: '469121548'
order: 102530
---

Vtiful\Kernel\Excel::insertImage

Vtiful\Kernel\Excel insertImage

## Descripción

```php
public Vtiful\Kernel\Excel::insertImage(int $row, int $column, string $localImagePath)
```php

Inserta una imagen local en la celda.

## Parámetros

`row`  
fila de celdas

`column`  
columna de celdas

`localImagePath`  
ruta de la imagen local

## Valores devueltos

instancia `Vtiful\Kernel\Excel`

## Ejemplos

ejemplo

```
<?php
$config = [
    'path' => './tests'
];

$excel = new \Vtiful\Kernel\Excel($config);

$file = $excel->fileName("free.xlsx");

$file->insertImage(5, 0, '/vagrant/ASW-G-66.jpg');

$file->output();

   
```php
