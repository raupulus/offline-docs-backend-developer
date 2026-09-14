---
title: svn_diff
description: Comparar dos rutas de forma recursiva
source_url: https://www.php.net/manual/es/function.svn-diff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-diff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: false
translation_revision: 997700a58
order: 89980
---

svn_diff

Comparar dos rutas de forma recursiva

## Descripción

```php
svn_diff(string $path1, int $rev1, string $path2, int $rev2): array
```php

Compara dos rutas, `path1` y `path2`, de forma recursiva.

> [!NOTE]
> No es una utilidad de comparación real. Solo los ficheros locales que están versionados pueden ser comparados: otros ficheros fallarán.

## Parámetros

`path1`  
Primera ruta. Puede ser una URL hacia un fichero/directorio de un repositorio SVN o una ruta hacia un fichero/directorio local.

> [!NOTE]
> Los caminos relativos pueden ser resueltos si el directorio de trabajo actual es uno de los que contienen el binario PHP. Para utilizar el directorio de trabajo, utilice la función `realpath`, o la instrucción dirname(\_\_FILE\_\_).

> [!WARNING]
> Si una ruta hacia un fichero local solo tiene barras invertidas y ninguna barra, esta extensión fallará. Reemplace siempre todas las barras invertidas con barras al utilizar esta función.

`rev1`  
Número de revisión de la primera ruta. Utilice la constante `SVN_REVISON_HEAD` para especificar la revisión más reciente.

`path2`  
Segunda ruta a comparar. Ver el argumento `path1` para la descripción.

`rev2`  
Número de revisión de la segunda ruta. Ver el argumento `rev1` para la descripción.

## Valores devueltos

Devuelve un array que contiene 2 flujos: el primero representa la salida de la comparación, y el segundo contiene los errores. Los flujos pueden ser leídos utilizando la función `fread`. Devuelve `false` o `null` si ocurre un error.

La salida del comparador puede, por omisión, estar en formato de comparación unificado Subversion, pero un [motor externo de comparación](http://svnbook.red-bean.com/en/1.2/svn.advanced.externaldifftools.html) puede ser utilizado, según la configuración SVN.

## Ejemplos

Ejemplo de uso

Este ejemplo muestra un uso básico de esta función y recupera el contenido desde los flujos:

```
<?php
list($diff, $errors) = svn_diff(
    'http://www.example.com/svnroot/trunk/foo', SVN_REVISION_HEAD,
    'http://www.example.com/svnroot/branches/dev/foo', SVN_REVISION_HEAD
);
if (!$diff) exit;
$contents = '';
while (!feof($diff)) {
  $contents .= fread($diff, 8192);
}
fclose($diff);
fclose($errors);
var_dump($contents);
?>

   
```php

El ejemplo anterior mostrará:

    Index: http://www.example.com/svnroot/trunk/foo
    ===================================================================
    --- http://www.example.com/svnroot/trunk/foo        (.../foo) (revision 23)
    +++ http://www.example.com/svnroot/branches/dev/foo (.../foo) (revision 27)
     // further diff output

Comparación de dos revisiones de una ruta del repositorio

Este ejemplo implementa un gestor que permite a un usuario comparar fácilmente dos revisiones de un elemento utilizando una ruta de repositorio externa (la sintaxis por omisión es verbosa):

```
<?php
function svn_diff_same_item($path, $rev1, $rev2) {
    return svn_diff($path, $rev1, $path, $rev2);
}
?>

   
```php

Comparación, más portable, de dos ficheros locales

Este ejemplo implementa un gestor para comparar dos ficheros locales, de forma más portable gestionando el problema de `realpath` y el error con las barras invertidas:

```
<?php
function svn_diff_local($path1, $rev1, $path2, $rev2) {
    $path1 = str_replace('\\', '/', realpath($path1));
    $path2 = str_replace('\\', '/', realpath($path2));
    return svn_diff($path1, $rev1, $path2, $rev2);
}
?>

   
```php

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

Documentación SVN sobre la orden

"svn diff"
