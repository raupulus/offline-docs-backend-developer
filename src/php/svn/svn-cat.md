---
title: svn_cat
description: Recupera el contenido de un fichero del repositorio
source_url: https://www.php.net/manual/es/function.svn-cat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-cat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: true
translation_revision: 997700a58
order: 89920
---

svn_cat

Recupera el contenido de un fichero del repositorio

## Descripción

```php
svn_cat(string $repos_url, [int $revision_no]): string
```php

Recupera el contenido del fichero apuntado por la URL `repos_url` del repositorio, opcionalmente, en la revisión `revision_no`.

## Parámetros

`repos_url`  
URL del elemento del repositorio.

`revision_no`  
Número de revisión del elemento a recuperar; por omisión, es HEAD.

## Valores devueltos

Devuelve el contenido del elemento desde el repositorio en caso de éxito, y `false` si ocurre un error.

## Ejemplos

Ejemplo de uso

Este ejemplo recupera el contenido de un fichero, en la revisión 28:

```
<?php
$contents = svn_cat('http://www.example.com/svnroot/calc/gui.c', 28)
?>

   
```php

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

svn_list

Documentación SVN sobre el comando

"svn cat"
