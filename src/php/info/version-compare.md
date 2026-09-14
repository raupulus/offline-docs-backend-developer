---
title: version_compare
description: Comparar dos strings de versión en el formato de versiones de PHP
source_url: https://www.php.net/manual/es/function.version-compare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/version-compare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: 4e6f0774f
order: 39240
---

version_compare

Comparar dos strings de versión en el formato de versiones de PHP

## Descripción

```php
version_compare(string $version1, string $version2, [string $operator]): int
```php

`version_compare` compara dos versiones de PHP estandarizadas.

`version_compare` reemplaza inicialmente `_`, `-` y `+` por un punto (`.`) en los strings de versión y también inserta puntos antes y después de cualquier carácter no numérico para que, por ejemplo, '4.3.5RC1' se convierta en '4.3.5.RC.1'. Luego, compara los fragmentos de izquierda a derecha. Si una parte contiene caracteres alfabéticos, estos son gestionados en el siguiente orden: `any string not found in this list` \< `dev` \< `alpha` = `a` \< `beta` = `b` \< `RC` = `rc` \< `#` \< `pl` = `p`. De esta manera, es posible comparar no solo versiones de diferentes niveles, como '4.1' y '4.1.2', sino también versiones de desarrollo de PHP, en cualquier etapa.

## Parámetros

`version1`  
Primer número de versión.

`version2`  
Segundo número de versión.

`operator`  
Un operador opcional. Los operadores posibles son: `<`, `lt`, `<=`, `le`, `>`, `gt`, `>=`, `ge`, `==`, `=`, `eq`, `!=`, `<>`, `ne` respectivamente.

Este parámetro es sensible a mayúsculas/minúsculas, por lo que los valores deben estar en minúsculas.

## Valores devueltos

Por omisión, `version_compare` devuelve `-1` si la primera versión es inferior a la segunda, `0` si son iguales, y `1` si la segunda es inferior a la primera.

Cuando se utiliza el parámetro opcional `operator`, la función devuelve `true` si la relación es la especificada por el operador, `false` en caso contrario.

## Ejemplos

Los ejemplos siguientes utilizan la constante `PHP_VERSION`, sabiendo que contiene el valor de la versión de PHP utilizada para ejecutar el código.

Ejemplo con `version_compare`

```
<?php
if (version_compare(PHP_VERSION, '7.0.0') >= 0) {
    echo 'Tengo al menos la versión 7.0.0 de PHP; mi versión: ' . PHP_VERSION . "\n";
}

if (version_compare(PHP_VERSION, '5.3.0') >= 0) {
    echo 'Tengo al menos la versión 5.3.0 de PHP; mi versión: ' . PHP_VERSION . "\n";
}

if (version_compare(PHP_VERSION, '5.0.0', '>=')) {
    echo 'Tengo al menos la versión 5.0.0 de PHP; mi versión: ' . PHP_VERSION . "\n";
}

if (version_compare(PHP_VERSION, '5.0.0', '<')) {
    echo 'Aún utilizo PHP 4; mi versión: ' . PHP_VERSION . "\n";
}
?>

    
```php

## Notas

> [!NOTE]
> La constante `PHP_VERSION` contiene la versión actual de PHP.

> [!NOTE]
> Tenga en cuenta que las versiones intermedias, como `5.3.0-dev`, son consideradas inferiores a sus versiones finales (como 5.3.0).

> [!NOTE]
> Los strings especiales de versión como `alpha` y `beta` son sensibles a mayúsculas/minúsculas. Los strings de versión provenientes de fuentes arbitrarias que no siguen el estándar de PHP deben ser convertidos a minúsculas utilizando la función `strtolower` antes de llamar a la función `version_compare`.

## Véase también

`phpversion`, `php_uname`, `function_exists`
