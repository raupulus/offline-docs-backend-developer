---
title: SplFileObject::fscanf
description: Analiza la entrada de un fichero de acuerdo a un formato
source_url: https://www.php.net/manual/es/splfileobject.fscanf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/fscanf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 9947012f7
order: 84430
---

SplFileObject::fscanf

Analiza la entrada de un fichero de acuerdo a un formato

## Descripción

```php
public SplFileObject::fscanf(string $format, mixed ...$vars): array
```php

Lee una línea de el fichero e interpreta este de acuerdo a el `format`.

Cualquier espacio en blanco en el `format` string coincide con cualquier espacio en blanco en la línea de el fichero. Esto significa que incluso un (`\t`) en el formato string puede coincidir con un sólo caracter de espacio en la secuencia de entrada.

## Parámetros

`format`  
El formato interpretado para `string` se describe en la documentación de la `sprintf` con las siguientes diferencias: La función no tiene en cuenta el contexto local., `F`, `g`, `G` y `b` no son soportados., `D` representa un número decimal., `i` representa un número entero con detección de base., `n` representa el número de caracteres tratados hasta este punto., `s` detiene la lectura en cada carácter de espacio., `*` en lugar de `argnum$` elimina la asignación de esta especificación de conversión.

`vars`  
Los valores opcionales asignados.

## Valores devueltos

Si sólo se pasa un parámetro a este método, los valores analizados serán devueltos como un `array`. De lo contrario, si se pasan los parámetros opcionales, el método devolverá el número de valores asignados. Los parámetros opcionales deben ser pasados por referencia.

Si se esperan más subcadenas en el `format` de las disponibles en la línea leída del fichero, se devuelve `null`.

Cuando se usan parámetros opcionales y se alcanza el final de la línea leída del fichero antes de que se haya analizado ningún valor, se devuelve `-1`.

## Ejemplos

Ejemplo de SplFileObject::fscanf

```
<?php
$file = new SplFileObject("usuarios.txt");
while ($usuarioinfo = $file->fscanf("%s %s %s")) {
   list ($nombre, $profesion, $codigopais) = $usuarioinfo;
   // Operar con  $name $profession $countrycode
}
?>

   
```php

Contenido de usuarios.txt

```
javier   argonaut    pe
hiroshi  sculptor    jp
robert   slacker     us
luigi    florist     it

   
```php

## Véase también

fscanf

sscanf

printf

sprintf
