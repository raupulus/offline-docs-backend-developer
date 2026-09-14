---
title: Phar::setDefaultStub
description: Utilizado para establecer el cargador PHP o el contenedor de carga de
  un archivo Phar como cargador por defecto
source_url: https://www.php.net/manual/es/phar.setdefaultstub.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/setDefaultStub.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: 661e08a17
order: 64350
---

Phar::setDefaultStub

Utilizado para establecer el cargador PHP o el contenedor de carga de un archivo Phar como cargador por defecto

## Descripción

```php
public Phar::setDefaultStub([string $index], [string $webIndex]): true
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Este método es un atajo que combina las funcionalidades de `Phar::createDefaultStub` y `Phar::setStub`.

## Parámetros

`index`  
Ruta relativa dentro del archivo phar a ejecutar si se lanza desde la línea de comandos

`webIndex`  
Ruta relativa dentro del archivo phar a ejecutar si se lanza desde un navegador

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Se lanza una excepción `UnexpectedValueException` si [phar.readonly](#ini.phar.readonly) está activada en el php.ini. Se lanza una excepción `PharException` si se encuentran problemas al escribir los cambios en el disco.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Phar::setDefaultStub ahora tiene un tipo de retorno provisional de `true`. |
| 8.0.0 | `webIndex` ahora es nullable. |

## Ejemplos

Un ejemplo con `Phar::setDefaultStub`

```
<?php
try {
    $phar = new Phar('monphar.phar');
    $phar->setDefaultStub('cli.php', 'web/index.php');
    // es equivalente a:
    // $phar->setStub($phar->createDefaultStub('cli.php', 'web/index.php'));
} catch (Exception $e) {
    // manejo de errores
}
?>

    
```php

## Véase también

`Phar::setStub`, `Phar::createDefaultStub`
