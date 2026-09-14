---
title: SplFileInfo::getSize
description: Obtiene el tamaño de el fichero
source_url: https://www.php.net/manual/es/splfileinfo.getsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 84180
---

SplFileInfo::getSize

Obtiene el tamaño de el fichero

## Descripción

```php
public SplFileInfo::getSize(): int
```php

Devuelve el tamaño de el fichero en bytes para el fichero referenciado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El tamaño del fichero en bytes en caso de éxito, o `false` en caso de error.

## Errores/Excepciones

Lanza una `RuntimeException` si el fichero no existe o en caso de error.

## Ejemplos

SplFileInfo::getSize example

```
     
<?php
$info = new SplFileInfo('example.jpg');
echo $info->getFilename() . " " . $info->getSize();
?>

    
```php

Resultado del ejemplo anterior es similar a:

         
    example.jpg 15385

## Véase también

`filesize`
