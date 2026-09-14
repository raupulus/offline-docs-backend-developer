---
title: Phar::mungServer
description: Define una lista de un máximo de 4 variables $_SERVER que deben ser modificadas
  durante la ejecución
source_url: https://www.php.net/manual/es/phar.mungserver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/mungServer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: a634e78ae
order: 64280
---

Phar::mungServer

Define una lista de un máximo de 4 variables \$\_SERVER que deben ser modificadas durante la ejecución

## Descripción

```php
final public static Phar::mungServer(array $variables): void
```php

`Phar::mungServer` debe ser llamada solo en el contenedor de carga de un archivo phar.

Define una lista de un máximo de 4 variables `$_SERVER` que deben ser modificadas durante la ejecución. Las variables que pueden ser modificadas para borrar los rastros de la ejecución phar son `REQUEST_URI`, `PHP_SELF`, `SCRIPT_NAME` y `SCRIPT_FILENAME`.

Por sí sola, esta método no hace nada. Toma efecto solo cuando se combina con `Phar::webPhar` y solo si el archivo solicitado es un archivo PHP a parsear. Tenga en cuenta que las variables `PATH_INFO` y `PATH_TRANSLATED` siempre son modificadas.

Los valores iniciales de las variables que son modificadas son almacenados en el array SERVER con el prefijo `PHAR_` y por ejemplo `SCRIPT_NAME` será almacenada como `PHAR_SCRIPT_NAME`.

## Parámetros

`variables`  
un array que contiene cualquiera de estas strings. `REQUEST_URI`, `PHP_SELF`, `SCRIPT_NAME` y `SCRIPT_FILENAME` como índices de strings. Otros valores desencadenan una excepción y `Phar::mungServer` es sensible a mayúsculas/minúsculas.

## Valores devueltos

No devuelve ningún valor.

## Errores/Excepciones

Levanta una excepción `UnexpectedValueException` si se encuentra algún problema en los datos pasados.

## Ejemplos

Un ejemplo con `Phar::mungServer`

```
<?php
// ejemplo de contenedor
Phar::mungServer(array('REQUEST_URI'));
Phar::webPhar();
__HALT_COMPILER();
?>

    
```php

## Véase también

`Phar::webPhar`, `Phar::setStub`
