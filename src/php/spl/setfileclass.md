---
title: SplFileInfo::setFileClass
description: Establece la clase empleada con SplFileInfo::openFile
source_url: https://www.php.net/manual/es/splfileinfo.setfileclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/setfileclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: c142be811
order: 84270
---

SplFileInfo::setFileClass

Establece la clase empleada con

SplFileInfo::openFile

## Descripción

```php
public SplFileInfo::setFileClass([string $class]): void
```php

Este método se emplea para establecer una clase propia que será utilizada cuando se invoque a SplFileInfo::openFile. El nombre de la clase pasado a este método debe ser `SplFileObject` o una clase derivada de `SplFileObject`.

## Parámetros

`class`  
El nombre de la clase a emplear cuando se invoca a SplFileInfo::openFile.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `SplFileInfo::setFileClass`

```
<?php
// Crear una clase que extiende a SplFileObject
class MiFoo extends SplFileObject {}

$info = new SplFileInfo(__FILE__);
// Establecer la clase a usar
$info->setFileClass('MiFoo');
var_dump($info->openFile());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    object(MiFoo)#2 (0) { }

## Véase también

SplFileInfo::openFile
