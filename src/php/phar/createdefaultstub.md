---
title: Phar::createDefaultStub
description: Crea un contenedor de carga de un archivo Phar
source_url: https://www.php.net/manual/es/phar.createdefaultstub.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/createDefaultStub.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64020
---

Phar::createDefaultStub

Crea un contenedor de carga de un archivo Phar

## Descripción

```php
final public static Phar::createDefaultStub([string $index], [string $webIndex]): string
```php

Este método está destinado a la creación de contenedores específicos del formato de archivo phar y no está diseñado para ser utilizado con archivos phar basados en tar o zip.

Los archivos Phar contienen un cargador o contenedor escrito en PHP que se ejecuta cuando el archivo es ejecutado ya sea mediante una inclusión

```
    
<?php
include 'monphar.phar';
?>
    
   
```php

o mediante una simple ejecución:

        
    php monphar.phar
        
       

Este método proporciona un medio simple y fácil de crear un contenedor que lanzará un archivo de inicio desde el archivo phar. Además, se pueden especificar archivos diferentes para ejecutar el archivo desde la línea de comandos o desde un servidor web. El contenedor de carga llama entonces a `Phar::interceptFileFuncs` para permitir el empaquetado fácil de aplicaciones PHP que acceden al sistema de archivos. Si la extensión phar no está presente, el contenedor de carga extraerá el archivo phar a un directorio temporal y tratará los archivos. Una función de apagado eliminará los archivos temporales al final.

## Parámetros

`index`  
Ruta relativa dentro del archivo phar a ejecutar en caso de acceso desde la línea de comandos

`webIndex`  
Ruta relativa dentro del archivo phar a ejecutar en caso de acceso desde un navegador

## Valores devueltos

Devuelve un string que contiene un contenedor de carga personalizado que permite que el archivo Phar creado funcione con o sin la extensión Phar activada.

## Errores/Excepciones

Lanza una excepción `UnexpectedValueException` si uno de los argumentos es más largo de 400 bytes.

## Historial de cambios

| Versión | Descripción                              |
|---------|------------------------------------------|
| 8.0.0   | `index` y `webIndex` ahora son nullable. |

## Ejemplos

Ejemplo con `Phar::createDefaultStub`

```
<?php
try {
    $phar = new Phar('monphar.phar');
    $phar->setStub($phar->createDefaultStub('cli.php', 'web/index.php'));
} catch (Exception $e) {
    // trata los errores
}
?>

    
```php

## Véase también

`Phar::setStub`, `Phar::getStub`
