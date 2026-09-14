---
title: svn_update
description: Actualiza la copia de trabajo
source_url: https://www.php.net/manual/es/function.svn-update.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-update.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: true
translation_revision: 997700a58
order: 90350
---

svn_update

Actualiza la copia de trabajo

## Descripción

```php
svn_update(string $path, [int $revno], [bool $recurse]): int
```php

Actualiza la copia de trabajo apuntada por la ruta `path` a la revisión `revno`. Si `recurse` vale `true`, los directorios se actualizarán recursivamente.

## Parámetros

`path`  
Ruta hacia la copia de trabajo local.

> [!NOTE]
> Los caminos relativos pueden ser resueltos si el directorio de trabajo actual es uno de los que contienen el binario PHP. Para utilizar el directorio de trabajo, utilice la función `realpath`, o la instrucción dirname(\_\_FILE\_\_).

`revno`  
Número de revisión hacia el cual actualizar; por omisión vale `SVN_REVISION_HEAD`.

`recurse`  
Si se deben o no actualizar los directorios recursivamente.

## Valores devueltos

Devuelve el nuevo número de revisión en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de uso

Este ejemplo muestra un uso básico de esta función:

```
<?php
echo svn_update(realpath('working-copy'));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    234

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

svn_checkout

svn_commit

Documentación SVN para el comando

"svn update"
