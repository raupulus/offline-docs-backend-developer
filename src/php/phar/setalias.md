---
title: Phar::setAlias
description: Establece el alias del archivo Phar
source_url: https://www.php.net/manual/es/phar.setalias.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/setAlias.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: 661e08a17
order: 64340
---

Phar::setAlias

Establece el alias del archivo Phar

## Descripción

```php
public Phar::setAlias(string $alias): true
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Establece el alias del archivo Phar y lo escribe como alias permanente de este archivo phar. Un alias puede ser utilizado dentro de un archivo phar para asegurar que el uso del flujo `phar` para acceder a ficheros internos funcione siempre independientemente de la ubicación del archivo phar en el sistema de ficheros. Una alternativa consiste en confiar en la intercepción de `include` realizada por Phar o en utilizar `Phar::interceptFileFuncs` y usar rutas relativas.

## Parámetros

`alias`  
Una pequeña cadena con la que se referirá a este archivo durante los accesos con el flujo `phar`.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Se lanza una excepción `UnexpectedValueException` cuando el acceso en escritura está desactivado y se lanza una excepción `PharException` si el alias ya está en uso o si se ha encontrado un problema al escribir los cambios en el disco.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Phar::setAlias ahora tiene un tipo de retorno provisional de tipo `true`. |

## Ejemplos

Un ejemplo con `Phar::setAlias`

```
<?php
try {
    $phar = new Phar('monphar.phar');
    $phar->setAlias('monp.phar');
} catch (Exception $e) {
    // trata los errores
}
?>

    
```php

## Véase también

`Phar::__construct`, `Phar::interceptFileFuncs`
