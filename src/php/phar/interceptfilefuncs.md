---
title: Phar::interceptFileFuncs
description: Indica a phar que debe interceptar las funciones de archivos
source_url: https://www.php.net/manual/es/phar.interceptfilefuncs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/interceptFileFuncs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64190
---

Phar::interceptFileFuncs

Indica a phar que debe interceptar las funciones de archivos

## Descripción

```php
final public static Phar::interceptFileFuncs(): void
```php

Indica a phar que debe interceptar `fopen`, `readfile`, `file_get_contents`, `opendir` y todas las funciones relativas a stat. Si cualquiera de estas funciones es llamada desde el archivo phar con una ruta relativa, la llamada es modificada para acceder a un archivo dentro del archivo. Las rutas absolutas se asumen como intentos de carga de archivos externos desde el sistema de archivos.

Esta función permite la ejecución de aplicaciones PHP diseñadas para ser lanzadas fuera de un disco duro, como aplicación phar.

## Parámetros

No se proporcionan argumentos.

## Valores devueltos

## Ejemplos

Ejemplo con `Phar::interceptFileFuncs`

```
<?php
Phar::interceptFileFuncs();
include 'phar://' . __FILE__ . '/fichero.php';
?>

    
```php

Suponiendo que este phar se llama `/ruta/hacia/miphar.phar` y contiene `fichero.php` y `fichero2.txt`, si `fichero.php` contiene este código:

Un ejemplo con `Phar::interceptFileFuncs`

```
<?php
echo file_get_contents('fichero2.txt');
?>

    
```php

Normalmente, PHP buscaría en el directorio actual el archivo llamado `file2.txt`, es decir, en el directorio de fichero.php o el directorio actual del usuario de la línea de comandos. `Phar::interceptFileFuncs` indica a PHP que considere `phar:///ruta/hacia/miphar.phar/` como directorio actual y así abre en el ejemplo anterior el archivo `phar:///ruta/hacia/miphar.phar/fichero2.txt`.
