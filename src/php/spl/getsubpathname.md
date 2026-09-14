---
title: RecursiveDirectoryIterator::getSubPathname
description: Obtiene el subcamino y el nombre del fichero
source_url: https://www.php.net/manual/es/recursivedirectoryiterator.getsubpathname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursivedirectoryiterator/getsubpathname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: c03200d4f
order: 83090
---

RecursiveDirectoryIterator::getSubPathname

Obtiene el subcamino y el nombre del fichero

## Descripción

```php
public RecursiveDirectoryIterator::getSubPathname(): string
```php

Obtiene el subcamino y el nombre del fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El subcamino (subdirectorio) y el nombre del fichero.

## Ejemplos

Ejemplo `getSubPathname`

```
    
      $directory = '/tmp';

      $it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory));

      foreach ($it as $file) {
          echo 'SubPathName: ' . $it->getSubPathname() . "\n";
          echo 'SubPath:     ' . $it->getSubPath() . "\n\n";
      }
    
    
```php

Resultado del ejemplo anterior es similar a:

        
         SubPathName: fruit/apple.xml
         SubPath:     fruit

         SubPathName: stuff.xml
         SubPath:

         SubPathName: veggies/carrot.xml
         SubPath:     veggies

## Véase también

RecursiveDirectoryIterator::getSubPath, RecursiveDirectoryIterator::key
