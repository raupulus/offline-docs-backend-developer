---
title: svn_import
description: Importa una ruta no versionada en un repositorio
source_url: https://www.php.net/manual/es/function.svn-import.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-import.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: true
translation_revision: 997700a58
order: 90220
---

svn_import

Importa una ruta no versionada en un repositorio

## Descripción

```php
svn_import(string $path, string $url, bool $nonrecursive): bool
```php

Entrega una ruta `path` no versionada en el repositorio a la URL `url`. Si `path` es un directorio y `nonrecursive` es `false`, el directorio será importado recursivamente.

## Parámetros

`path`  
Ruta hacia el fichero o directorio a importar.

> [!NOTE]
> Los caminos relativos pueden ser resueltos si el directorio de trabajo actual es uno de los que contienen el binario PHP. Para utilizar el directorio de trabajo, utilice la función `realpath`, o la instrucción dirname(\_\_FILE\_\_).

`url`  
URL del repositorio en el cual se importa.

`nonrecursive`  
Si se debe o no realizar una importación recursiva.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de uso

Este ejemplo muestra un uso clásico de esta función. Para importar un directorio llamado `"new-files"` en el repositorio a la URL `"http://www.example.com/svnroot/incoming/abc"`, se utiliza:

```
<?php
svn_import(realpath('new-files'), 'http://www.example.com/svnroot/incoming/abc', false);
?>

   
```php

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

svn_add

Documentación SVN sobre el comando

"svn import"
