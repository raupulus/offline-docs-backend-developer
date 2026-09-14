---
title: PharData::buildFromDirectory
description: Construye un archivo tar/zip a partir de los ficheros de un directorio
source_url: https://www.php.net/manual/es/phardata.buildfromdirectory.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/buildFromDirectory.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64470
---

PharData::buildFromDirectory

Construye un archivo tar/zip a partir de los ficheros de un directorio

## Descripción

```php
public PharData::buildFromDirectory(string $directory, [string $pattern]): array
```php

Rellena un archivo tar/zip a partir del contenido de un directorio. El segundo argumento opcional es una expresión regular (pcre) utilizada para excluir ficheros. Cualquier fichero cuyo nombre cumpla la expresión será incluido, todos los demás serán excluidos. Para un control más fino, utilice `PharData::buildFromIterator`.

## Parámetros

`directory`  
La ruta relativa o absoluta hacia el directorio que contiene todos los ficheros a añadir al archivo.

`pattern`  
Una expresión regular opcional que se utiliza para filtrar la lista de ficheros. Solo los ficheros cuyos nombres cumplan la expresión serán incluidos en el archivo.

## Valores devueltos

`Phar::buildFromDirectory` devuelve un array asociativo que hace corresponder una ruta de fichero interno con una ruta completa en el sistema de ficheros, o `false` si ocurre un error.

## Errores/Excepciones

Este método lanza una excepción `BadMethodCallException` cuando no es capaz de instanciar los iteradores internos de directorio, o una excepción `PharException` si se han encontrado errores durante el registro del archivo phar.

## Historial de cambios

| Versión | Descripción                                          |
|---------|------------------------------------------------------|
| 8.1.0   | PharData::buildFromDirectory ya no devuelve `false`. |

## Ejemplos

Un ejemplo con `PharData::buildFromDirectory`

```
<?php
$phar = new PharData('projet.tar');
// añade todos los ficheros al proyecto
$phar->buildFromDirectory(dirname(__FILE__) . '/projet');

$phar2 = new PharData('projet2.zip');
// añade todos los ficheros al proyecto incluyendo solo los ficheros php
$phar2->buildFromDirectory(dirname(__FILE__) . '/projet', '/\.php$/');
?>

    
```php

## Véase también

`Phar::buildFromDirectory`, `PharData::buildFromIterator`
