---
title: Phar::buildFromDirectory
description: Construye un archivo phar a partir de los ficheros de un directorio
source_url: https://www.php.net/manual/es/phar.buildfromdirectory.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/buildFromDirectory.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 63910
---

Phar::buildFromDirectory

Construye un archivo phar a partir de los ficheros de un directorio

## Descripción

```php
public Phar::buildFromDirectory(string $directory, [string $pattern]): array
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Rellena un archivo phar a partir del contenido de un directorio. El segundo parámetro, opcional, es una expresión regular (pcre) utilizada para excluir ficheros. Todo fichero cuyo nombre cumpla la expresión regular será incluido, los demás serán excluidos. Para un control más fino, utilice `Phar::buildFromIterator`.

## Parámetros

`directory`  
La ruta absoluta o relativa hacia el directorio que contiene todos los ficheros a añadir al archivo.

`pattern`  
Una expresión regular opcional utilizada para filtrar la lista de ficheros. Solo los ficheros cuyo nombre cumpla la expresión regular serán incluidos en el archivo.

## Valores devueltos

`Phar::buildFromDirectory` devuelve un array asociativo que hace corresponder la ruta interna del fichero con la ruta completa en el sistema de ficheros.

## Errores/Excepciones

Este método lanza una excepción `BadMethodCallException` cuando no es capaz de instanciar el iterador de directorio interno, o una excepción `PharException` si ha habido errores durante el guardado del archivo.

## Historial de cambios

| Versión | Descripción                                      |
|---------|--------------------------------------------------|
| 8.1.0   | Phar::buildFromDirectory ya no devuelve `false`. |

## Ejemplos

Un ejemplo con `Phar::buildFromDirectory`

```
<?php
// crea con el alias "proyecto.phar"
$phar = new Phar('proyecto.phar', 0, 'proyecto.phar');
// añade ficheros en el proyecto
$phar->buildFromDirectory(dirname(__FILE__) . '/proyecto');
$phar->setStub($phar->createDefaultWebStub('cli/index.php', 'www/index.php'));

$phar2 = new Phar('proyecto2.phar', 0, 'proyecto2.phar');
// añade todos los ficheros en el proyecto, pero solo los ficheros .php
$phar->buildFromDirectory(dirname(__FILE__) . '/proyecto', '/\.php$/');
$phar->setStub($phar->createDefaultStub('cli/index.php', 'www/index.php'));
?>

   
```php

## Véase también

`Phar::buildFromIterator`
