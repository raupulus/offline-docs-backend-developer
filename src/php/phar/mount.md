---
title: Phar::mount
description: Monta un camino o un fichero externo a una ubicación virtual dentro del
  archivo phar
source_url: https://www.php.net/manual/es/phar.mount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/mount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64270
---

Phar::mount

Monta un camino o un fichero externo a una ubicación virtual dentro del archivo phar

## Descripción

```php
final public static Phar::mount(string $pharPath, string $externalPath): void
```php

Al igual que el concepto unix de montar un dispositivo externo en un punto de la jerarquía, `Phar::mount` permite referirse a ficheros y directorios externos como si estuvieran dentro del archivo.

## Parámetros

`pharPath`  
El camino interno dentro del archivo phar a utilizar como punto de montaje. Debe ser un camino relativo dentro del archivo phar, y no debe existir ya.

`externalPath`  
Un camino o URL hacia un fichero o directorio externo a montar dentro del archivo

## Valores devueltos

No devuelve valor. Se lanza una excepción `PharException` en caso de fallo.

## Errores/Excepciones

Se lanza una excepción `PharException` si se encuentra un problema durante el montaje.

## Ejemplos

Un ejemplo con `Phar::mount`

El siguiente ejemplo muestra el acceso a un fichero de configuración externo como si fuera un camino dentro del archivo phar.

Primero, el código dentro del archivo phar:

```
<?php
$configuration = simplexml_load_string(file_get_contents(
    Phar::running(false) . '/config.xml'));
?>

    
```php

Luego el código externo utilizado para montar el fichero de configuración:

```
<?php
// se comienza configurando la asociación entre el fichero config.xml abstracto
// y el que está en el disco
Phar::mount('phar://config.xml', '/home/example/config.xml');
// ahora se lanza la aplicación
include '/ruta/al/archivo.phar';
?>

    
```php

Otro método es colocar el código de montaje dentro del contenedor de carga del archivo phar. Aquí hay un ejemplo para configurar un fichero de configuración por defecto si no se hace ninguna configuración de usuario:

```
<?php
// se comienza configurando la asociación entre el fichero config.xml abstracto
// y el que está en el disco
if (defined('EXTERNAL_CONFIG')) {
    Phar::mount('config.xml', EXTERNAL_CONFIG);
    if (file_exists(__DIR__ . '/extra_config.xml')) {
        Phar::mount('extra.xml', __DIR__ . '/extra_config.xml');
    }
} else {
    Phar::mount('config.xml', 'phar://' . __FILE__ . '/default_config.xml');
    Phar::mount('extra.xml', 'phar://' . __FILE__ . '/default_extra.xml');
}
// ahora se lanza la aplicación
include 'phar://' . __FILE__ . '/index.php';
__HALT_COMPILER();
?>

    
```php

... y el código externo para cargar este archivo phar:

```
<?php
define('EXTERNAL_CONFIG', '/home/ejemplo/config.xml');
// ahora se lanza la aplicación
include '/ruta/al/archivo.phar';
?>

    
```php
