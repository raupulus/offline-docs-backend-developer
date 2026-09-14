---
title: RarArchive::__toString
description: Obtener representación de texto
source_url: https://www.php.net/manual/es/rararchive.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rararchive/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68480
---

RarArchive::\_\_toString

Obtener representación de texto

## Descripción

```php
public RarArchive::__toString(): string
```php

Proporciona una representación de cadena para este objeto `RarArchive`. Esta actualmente muestra la ruta completa del volumen de archivo que fue abierto y si el recurso es válido o ya estaba cerrado a través de una llamada a RarArchive::close.

Este método debe ser utilizado sólo para propósitos de depuración, ya que no existen garantías en cuanto a la información que contiene el resultado o cómo esta es formateada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una representación textual de este objeto `RarArchive`. El contenido de esta representación no es especificado.

## Ejemplos

Ejemplo de RarArchive::\_\_toString

```
<?php
$rar_arch = RarArchive::open('latest_winrar.rar');
echo $rar_arch."\n";
$rar_arch->close();
echo $rar_arch."\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    RAR Archive "D:\php_rar\trunk\tests\latest_winrar.rar"
    RAR Archive "D:\php_rar\trunk\tests\latest_winrar.rar" (closed)
