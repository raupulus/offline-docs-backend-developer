---
title: fscanf
description: Analiza un archivo según un formato
source_url: https://www.php.net/manual/es/function.fscanf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fscanf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 9947012f7
order: 23660
---

fscanf

Analiza un archivo según un formato

## Descripción

```php
fscanf(resource $stream, string $format, mixed ...$vars): array
```php

La función `fscanf` es similar a la función `sscanf`, excepto que toma un archivo como entrada, representado por el recurso `stream` e interpreta la entrada según el formato `format` especificado.

Todos los caracteres en blanco de la cadena de formato corresponden a tantos espacios en el flujo de entrada. Esto significa que una tabulación (`\t`) en la cadena de formato puede reemplazar un espacio simple en el flujo de entrada.

Cada llamada a la función `fscanf` lee una línea del archivo.

## Parámetros

`stream`  
Un puntero al sistema de ficheros de tipo `resource` que típicamente se crea utilizando `fopen`.

`format`  
El formato interpretado para `string` se describe en la documentación de la `sprintf` con las siguientes diferencias: La función no tiene en cuenta el contexto local., `F`, `g`, `G` y `b` no son soportados., `D` representa un número decimal., `i` representa un número entero con detección de base., `n` representa el número de caracteres tratados hasta este punto., `s` detiene la lectura en cada carácter de espacio., `*` en lugar de `argnum$` elimina la asignación de esta especificación de conversión.

`vars`  
Los valores opcionales a asignar.

## Valores devueltos

Si solo se pasan 2 argumentos a la función, el valor analizado será devuelto como un `array`. Si se pasan argumentos opcionales, la función devolverá el número de valores asignados. Los argumentos opcionales deben ser pasados por referencia.

Si se esperan más subcadenas en el `format` de las disponibles en `string`, `null` será devuelto. En otros casos de error, `false` será devuelto.

Cuando se usan parámetros opcionales y se alcanza el final de la entrada leída de `stream` antes de que se haya analizado ningún valor, se devuelve `-1`.

## Ejemplos

Ejemplo con `fscanf`

```
<?php
$handle = fopen("users.txt", "r");
while ($userinfo = fscanf($handle, "%s\t%s\t%s\n")) {
    list ($name, $profession, $countrycode) = $userinfo;
    //... procesamiento de datos
}
fclose($handle);
?>

   
```php

Contenido del archivo users.txt

```
javier  argonaut        pe
hiroshi sculptor        jp
robert  slacker us
luigi   florist it

   
```php

## Véase también

fread

fgets

fgetss

sscanf

printf

sprintf
