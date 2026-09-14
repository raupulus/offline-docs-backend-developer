---
title: svn_cleanup
description: Limpia, de forma recursiva, un directorio de trabajo, finalizando las
  operaciones incompletas y eliminando los bloqueos
source_url: https://www.php.net/manual/es/function.svn-cleanup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-cleanup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: true
translation_revision: 997700a58
order: 89940
---

svn_cleanup

Limpia, de forma recursiva, un directorio de trabajo, finalizando las operaciones incompletas y eliminando los bloqueos

## Descripción

```php
svn_cleanup(string $workingdir): bool
```php

Limpia, de forma recursiva, un directorio de trabajo `workingdir`, finalizando las operaciones incompletas y eliminando los bloqueos. Se debe utilizar cuando la copia de trabajo ya no es funcional.

## Parámetros

`workingdir`  
Ruta al directorio local de trabajo a limpiar.

> [!NOTE]
> Los caminos relativos pueden ser resueltos si el directorio de trabajo actual es uno de los que contienen el binario PHP. Para utilizar el directorio de trabajo, utilice la función `realpath`, o la instrucción dirname(\_\_FILE\_\_).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de uso

Este ejemplo muestra cómo limpiar una copia de trabajo de un directorio llamado `"help-me"`:

```
<?php
svn_cleanup(realpath('help-me'));
?>

   
```php

La función `realpath` debe ser llamada, debido a la mala gestión de las rutas relativas por parte de SVN.

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

update

Documentación SVN sobre el comando

"svn cleanup"
