---
title: dirname
description: Devuelve la ruta de la carpeta padre
source_url: https://www.php.net/manual/es/function.dirname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/dirname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 21cd3a942
order: 23340
---

dirname

Devuelve la ruta de la carpeta padre

## Descripción

```php
dirname(string $path, [int $levels]): string
```php

Devuelve la ruta padre de un camino que representa un fichero o una carpeta, que corresponde a `levels` nivel(es) más arriba que la carpeta actual.

> [!NOTE]
> `dirname` actúa de forma ingenua sobre la cadena de entrada y no está al tanto del sistema de archivos actual o de componentes eventuales como "`..`".

> [!CAUTION]
> En Windows, `dirname` asume que la página de código actualmente definida, por lo que para que pueda ver el nombre de carpeta correcto con caracteres multioctetos en el camino, la página de código correspondiente debe estar definida. Si `path` contiene caracteres que son inválidos para la página de código actual, el comportamiento de `dirname` es indefinido.
>
> En otros sistemas, `dirname` asume que `path` está codificado en un codificación compatible con ASCII. De lo contrario, el comportamiento de la función es indefinido.

## Parámetros

`path`  
Un camino.

En Windows, las barras (/`/`) y backslash (`\`) se utilizan como separadores de carpeta. En otros entornos, solo la barra (`/`) se utiliza.

`levels`  
El número de carpetas padres más arriba.

Debe ser un integer superior a 0.

## Valores devueltos

Devuelve la carpeta padre del camino. Si no hay ninguna barra en el camino `path`, un punto ('`.`') será devuelto, indicando la carpeta actual. De lo contrario, la cadena devuelta será el camino `path` del cual se habrán eliminado todos los `/component`.

> [!CAUTION]
> Se debe tener cuidado al utilizar esta función en un ciclo que pueda alcanzar la carpeta raíz, ya que esto puede producir un ciclo infinito.
>
> <div class="informalexample">
>
> ```
> <?php
> dirname('.');    // Devolverá '.'.
> dirname('/');    // Devolverá `\` en Windows y '/' en sistemas *nix.
> dirname('\\');   // Devolverá `\` en Windows y '.' en sistemas *nix.
> dirname('C:\\'); // Devolverá 'C:\' en Windows y '.' en sistemas *nix.
> ?>
>
>      
> ```
>
> </div>

## Ejemplos

Ejemplo con `dirname`

```
<?php
echo dirname("/etc/passwd") . PHP_EOL;
echo dirname("/etc/") . PHP_EOL;
echo dirname(".") . PHP_EOL;
echo dirname("C:\\") . PHP_EOL;
echo dirname("/usr/local/lib", 2);

    
```php

Resultado del ejemplo anterior es similar a:

    /etc
    / (o \ en Windows)
    .
    C:\
    /usr

## Véase también

`basename`, `pathinfo`, `realpath`
