---
title: svn_blame
description: Obtiene las acusaciones SVN de un archivo
source_url: https://www.php.net/manual/es/function.svn-blame.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-blame.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_revision: 997700a58
order: 89910
---

svn_blame

Obtiene las acusaciones SVN de un archivo

## Descripción

```php
svn_blame(string $repository_url, [int $revision_no]): array
```php

Obtiene las acusaciones SVN de un archivo desde una URL de repositorio.

## Parámetros

`repository_url`  
La URL del repositorio.

`revision_no`  
El número de revisión.

## Valores devueltos

Un `array` con la información de acuses SVN separados por línea incluyendo los números de revisión, número de línea, línea de codigo, autor, y fecha.

## Ejemplos

Ejemplo de `svn_blame`

```
<?php
$svnurl = 'http://svn.example.org/svnroot/foo/trunk/index.php';

print_r( svn_blame($svnurl) );

?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] = Array
              (
               [rev] = 1
               [line_no] = 1
               [line] = Hello World
               [author] = joesmith
               [date] = 2007-07-02T05:51:26.628396Z
              )
        [1] = Array
              ...

## Véase también

svn_diff

svn_logs

svn_status
