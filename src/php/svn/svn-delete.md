---
title: svn_delete
description: Elimina un elemento de un directorio de trabajo o de un repositorio
source_url: https://www.php.net/manual/es/function.svn-delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: false
translation_revision: 997700a58
order: 89970
---

svn_delete

Elimina un elemento de un directorio de trabajo o de un repositorio

## Descripción

```php
svn_delete(string $path, [bool $force]): bool
```php

Elimina un fichero, un directorio o un enlace simbólico, según el `path` utilizado, desde un directorio de trabajo. El elemento será eliminado del repositorio en la próxima llamada a la función `svn_commit` en el directorio de trabajo.

## Parámetros

`path`  
Ruta hacia el elemento a eliminar.

> [!NOTE]
> Los caminos relativos pueden ser resueltos si el directorio de trabajo actual es uno de los que contienen el binario PHP. Para utilizar el directorio de trabajo, utilice la función `realpath`, o la instrucción dirname(\_\_FILE\_\_).

`force`  
Si vale `true`, el fichero será eliminado incluso si tiene modificaciones locales. De lo contrario, las modificaciones locales harán fallar la función. Por omisión, vale `false`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

Documentación SVN sobre la eliminación
