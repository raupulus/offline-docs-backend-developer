---
title: Phar::mapPhar
description: Lee el phar ejecutado y carga su manifiesto
source_url: https://www.php.net/manual/es/phar.mapphar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/mapPhar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64260
---

Phar::mapPhar

Lee el phar ejecutado y carga su manifiesto

## Descripción

```php
final public static Phar::mapPhar([string $alias], [int $offset]): bool
```php

Este método estático puede ser utilizado únicamente dentro del contenedor de carga de un archivo Phar para inicializar el phar cuando es ejecutado directamente o cuando es incluido en otro script.

## Parámetros

`alias`  
El alias que puede ser utilizado en la URL `phar://` para referirse al archivo en lugar de utilizar su ruta completa.

`offset`  
Variable no utilizada, presente por motivos de compatibilidad con la biblioteca PHP_Archive de PEAR.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se lanza una excepción `PharException` si el método no es llamado directamente dentro de la ejecución de PHP, si no se encuentra ningún token \_\_HALT_COMPILER(); en el archivo fuente actual o si el archivo no puede ser abierto en lectura.

## Ejemplos

Ejemplo con `Phar::mapPhar`

mapPhar debe ser utilizado únicamente dentro del contenedor de carga de un phar. Utilice loadPhar para cargar un phar externo en memoria.

A continuación se muestra un ejemplo de contenedor de carga Phar que utiliza mapPhar.

```
<?php
function __autoload($class)
{
    include 'phar://mon.phar/' . str_replace('_', '/', $class) . '.php';
}
try {
    Phar::mapPhar('mon.phar');
    include 'phar://mon.phar/demarrage.php';
} catch (PharException $e) {
    echo $e->getMessage();
    die('No puede inicializar el Phar');
}
__HALT_COMPILER();

    
```php

## Véase también

`Phar::loadPhar`
