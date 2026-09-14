---
title: Phar::running
description: Devuelve la ruta completa en el disco o la URL phar completa del archivo
  phar actualmente ejecutado
source_url: https://www.php.net/manual/es/phar.running.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/running.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64330
---

Phar::running

Devuelve la ruta completa en el disco o la URL phar completa del archivo phar actualmente ejecutado

## Descripción

```php
final public static Phar::running([bool $returnPhar]): string
```php

Devuelve la ruta completa del archivo phar ejecutado. Esto es utilizado de manera similar a la constante mágica `__FILE__` y tiene efectos únicamente dentro de un archivo phar que está siendo ejecutado.

Dentro de un contenedor de carga de un archivo, `Phar::running` devuelve `""`. Utilice simplemente `__FILE__` para acceder al phar actual dentro de un contenedor de carga.

## Parámetros

`returnPhar`  
Si `false`, se devuelve la ruta completa en el disco hacia el phar. Si `true`, se devuelve una URL phar completa.

## Valores devueltos

Devuelve la ruta del fichero si es válida, de lo contrario una cadena vacía.

## Ejemplos

Un ejemplo con `Phar::running`

Para el ejemplo siguiente, se asume que el archivo phar es `/ruta/al/archivo.phar`.

```
<?php
$a = Phar::running(); // $a vale "phar:///ruta/al/archivo.phar"
$b = Phar::running(false); // $b vale "/ruta/al/archivo.phar"
?>

    
```php
