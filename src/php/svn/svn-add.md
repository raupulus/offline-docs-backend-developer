---
title: svn_add
description: Prevé la adición de un elemento en el directorio de trabajo
source_url: https://www.php.net/manual/es/function.svn-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: true
translation_revision: 997700a58
order: 89880
---

svn_add

Prevé la adición de un elemento en el directorio de trabajo

## Descripción

```php
svn_add(string $path, [bool $recursive], [bool $force]): bool
```php

Añade un fichero, un directorio o un enlace simbólico, utilizando la ruta `path` en el directorio de trabajo. El elemento será añadido al repositorio en la próxima llamada a la función `svn_commit` sobre la copia de trabajo.

## Parámetros

`path`  
Ruta del elemento a añadir.

> [!NOTE]
> Los caminos relativos pueden ser resueltos si el directorio de trabajo actual es uno de los que contienen el binario PHP. Para utilizar el directorio de trabajo, utilice la función `realpath`, o la instrucción dirname(\_\_FILE\_\_).

`recursive`  
Si el elemento es un directorio, si se debe o no añadir recursivamente todo su contenido. Por omisión, vale `true`

`force`  
Si vale `true`, Subversion buscará recursivamente en los directorios versionados existentes para añadir todos los ficheros que actualmente no están versionados. Por omisión, vale `false`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `svn_add`

En un directorio de trabajo donde el comando `svn status` devuelve:

    $ svn status
    ?      foobar.txt

       

...este código:

```
<?php
svn_add('foobar.txt');
?>

   
```php

...marcará el fichero `foobar.txt` como fichero a añadir en el directorio.

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

Documentación SVN sobre el comando

"svn add"
