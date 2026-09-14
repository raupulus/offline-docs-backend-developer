---
title: SplFileInfo::setInfoClass
description: Establece la clase empleada con SplFileInfo::getFileInfo y SplFileInfo::getPathInfo
source_url: https://www.php.net/manual/es/splfileinfo.setinfoclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/setinfoclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: c142be811
order: 84280
---

SplFileInfo::setInfoClass

Establece la clase empleada con

SplFileInfo::getFileInfo

y

SplFileInfo::getPathInfo

## Descripción

```php
public SplFileInfo::setInfoClass([string $class]): void
```php

Este método se emplea para establecer una clase propia que será utilizada cuando se invoque a SplFileInfo::getFileInfo y SplFileInfo::getPathInfo. El nombre de la clase pasado a este método debe ser `SplFileInfo` o una clase derivada de `SplFileInfo`.

## Parámetros

`class`  
El nombre de la clase a emplear cuando se invoca a SplFileInfo::getFileInfo y SplFileInfo::getPathInfo.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `SplFileInfo::setFileClass`

```
<?php
// Crear una clase que extiende a SplFileInfo
class MiFoo extends SplFileInfo {}

$info = new SplFileInfo('foo');
// Establecer el nombre de clase a usar
$info->setInfoClass('MiFoo');
var_dump($info->getFileInfo());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    object(MiFoo)#2 (0) { }

## Véase también

SplFileInfo::getFileInfo
