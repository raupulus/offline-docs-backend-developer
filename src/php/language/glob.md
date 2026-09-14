---
title: glob://
description: Encuentra nombres de ficheros que coinciden con un patrón dado
source_url: https://www.php.net/manual/es/wrappers.glob.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers/glob.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 8bc832a46
order: 4660
---

glob://

Encuentra nombres de ficheros que coinciden con un patrón dado

## Descripción

La envoltura de flujo `glob:`.

## Uso

- `glob://`

## Opciones

| Atributo                                                    | Soportado |
|-------------------------------------------------------------|-----------|
| Restringido por [allow_url_fopen](#ini.allow-url-fopen)     | No        |
| Restringido por [allow_url_include](#ini.allow-url-include) | No        |
| Permite la lectura                                          | No        |
| Permite la escritura                                        | No        |
| Permite la adición                                          | No        |
| Permite la lectura y escritura simultáneamente              | No        |
| Soporte de la función `stat`                                | No        |
| Soporte de la función `unlink`                              | No        |
| Soporte de la función `rename`                              | No        |
| Soporte de la función `mkdir`                               | No        |
| Soporte de la función `rmdir`                               | No        |

Resumen de la envoltura {role="stream_wrapper"}

## Ejemplos

Uso simple

```php
<?php
// Recorre todos los ficheros *.php en el directorio ext/spl/examples/ y
// muestra el nombre del fichero así como su tamaño
$it = new DirectoryIterator("glob://ext/spl/examples/*.php");
foreach($it as $f) {
    printf("%s: %.1FK\n", $f->getFilename(), $f->getSize()/1024);
}
?>

   
```

    tree.php: 1.0K
    findregex.php: 0.6K
    findfile.php: 0.7K
    dba_dump.php: 0.9K
    nocvsdir.php: 1.1K
    phar_from_dir.php: 1.0K
    ini_groups.php: 0.9K
    directorytree.php: 0.9K
    dba_array.php: 1.1K
    class_tree.php: 1.8K
