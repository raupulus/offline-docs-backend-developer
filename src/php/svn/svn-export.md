---
title: svn_export
description: Exporta el contenido de un directorio SVN
source_url: https://www.php.net/manual/es/function.svn-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_revision: 997700a58
order: 89990
---

svn_export

Exporta el contenido de un directorio SVN

## Descripción

```php
svn_export(string $frompath, string $topath, [bool $working_copy], [int $revision_no]): bool
```php

Exporta el contenido de una copia de trabajo o un repositorio en un directorio 'limpio'.

## Parámetros

`frompath`  
La ruta del repositorio actual.

`topath`  
La ruta del nuevo repositorio.

`working_copy`  
Si es `true`, exportará ficheros no cometidos de la copia de trabajo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `svn_export`

```
<?php
$working_dir     = '../';
$new_working_dir = '/home/user/devel/foo/trunk';

svn_export($working_dir, $new_working_dir);
?>

   
```php

## Véase también

svn_import
