---
title: pathinfo
description: Devuelve información sobre una ruta del sistema
source_url: https://www.php.net/manual/es/function.pathinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/pathinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: d0cc084a9
order: 23910
---

pathinfo

Devuelve información sobre una ruta del sistema

## Descripción

```php
pathinfo(string $path, [int $flags]): array
```php

`pathinfo` devuelve información sobre la ruta `path`, en forma de string o array asociativo, dependiendo del argumento `flags`.

> [!NOTE]
> Para más información sobre la lectura de la ruta actual, consulte la sección sobre las [variables predefinidas](#language.variables.predefined).

> [!NOTE]
> `pathinfo` opera de manera ingenua sobre la cadena de entrada, y no es consciente de los sistemas de archivos actuales, o de los componentes de rutas como "`..`".

> [!NOTE]
> Solo en sistemas Windows, el carácter `\` será interpretado como separador de directorio. En otros sistemas, será tratado como cualquier otro carácter.

> [!CAUTION]
> La función `pathinfo` es sensible a la configuración local, por lo tanto, si se desea que analice correctamente una ruta que contenga caracteres de varios bytes, la configuración local correspondiente debe ser definida utilizando la función `setlocale`.

## Parámetros

`path`  
La ruta a analizar.

`flags`  
Especifica qué elemento será devuelto. Puede pasar una de las constantes `PATHINFO_DIRNAME`, `PATHINFO_BASENAME`, `PATHINFO_EXTENSION` y `PATHINFO_FILENAME`.

Si `flags` no es especificado, todos los elementos son devueltos.

## Valores devueltos

Si `flags` no es utilizado, esta función devolverá un array asociativo que contiene los siguientes elementos : `dirname`, `basename`, `extension` (si existe), y `filename`.

> [!NOTE]
> Si `path` contiene más de una extensión, `PATHINFO_EXTENSION` devuelve únicamente la última y `PATHINFO_FILENAME` eliminará únicamente la última también (ver el primer ejemplo a continuación).

> [!NOTE]
> Si `path` no tiene extensión, el elemento `extension` no será devuelto (ver el segundo ejemplo a continuación).

> [!NOTE]
> Si `basename` del argumento `path` comienza con un punto, los caracteres siguientes son interpretados como la `extension`, y el `filename` estará vacío (ver el tercer ejemplo a continuación).

Si `flags` es utilizado, esta función devolverá una `string` que contiene los elementos.

## Ejemplos

Ejemplo con `pathinfo`

```
<?php
$path_parts = pathinfo('/www/htdocs/inc/lib.inc.php');

echo $path_parts['dirname'], "\n";
echo $path_parts['basename'], "\n";
echo $path_parts['extension'], "\n";
echo $path_parts['filename'], "\n";
?>

    
```php

El ejemplo anterior mostrará:

    /www/htdocs/inc
    lib.inc.php
    php
    lib.inc

Ejemplo `pathinfo` sin extensión

```
<?php
$path_parts = pathinfo('/path/emptyextension.');
var_dump($path_parts['extension']);

$path_parts = pathinfo('/path/noextension');
var_dump($path_parts['extension']);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(0) ""

    Notice: Undefined index: extension in test.php on line 6
    NULL

Ejemplo con `pathinfo`

```
<?php
print_r(pathinfo('/some/path/.test'));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [dirname] => /some/path
        [basename] => .test
        [extension] => test
        [filename] =>
    )

Ejemplo de `pathinfo` con desestructuración de array

El argumento `flags` no es una máscara de bits. Solo un valor puede ser proporcionado. Para seleccionar únicamente un conjunto limitado de valores analizados, utilice la desestructuración de array como se muestra a continuación:

```
     
     <?php
     ['basename' => $basename, 'dirname' => $dirname] = pathinfo('/www/htdocs/inc/lib.inc.php');
     var_dump($basename, $dirname);
     ?>
     
    
```php

Resultado del ejemplo anterior es similar a:

         
         string(11) "lib.inc.php"
         string(15) "/www/htdocs/inc"

## Véase también

`dirname`, `basename`, `parse_url`, `realpath`
