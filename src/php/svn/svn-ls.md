---
title: svn_ls
description: Devuelve la lista del contenido de un directorio de un repositorio, opcionalmente
  en la revisión proporcionada
source_url: https://www.php.net/manual/es/function.svn-ls.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-ls.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: true
translation_revision: 997700a58
order: 90240
---

svn_ls

Devuelve la lista del contenido de un directorio de un repositorio, opcionalmente en la revisión proporcionada

## Descripción

```php
svn_ls(string $repos_url, [int $revision_no], [bool $recurse], [bool $peg]): array
```php

Esta función consulta la URL del repositorio y devuelve una lista de los ficheros y directorios, opcionalmente desde una revisión específica. Es el equivalente al comando `svn list $repos_url[@$revision_no]`.

> [!NOTE]
> Esta función no funciona con copias de trabajo. `repos_url` *DEBE* ser una URL de repositorio.

## Parámetros

`url`  
URL del repositorio, por ejemplo `http://www.example.com/svnroot`. Para acceder a un repositorio local Subversion a través del sistema de ficheros, utilice el siguiente URI: `file:///home/user/svn-repos`.

`revision`  
Número de revisión a utilizar. Si se omite, se utilizará HEAD.

`recurse`  
Activa la recursividad.

## Valores devueltos

En caso de éxito, esta función devuelve un array de ficheros, listados de la siguiente forma:

    [0] => Array
        (
            [created_rev] => número de revisión de la última edición
            [last_author] => nombre del autor de la última edición
            [size] => tamaño del fichero
            [time] => fecha y hora de la última edición, en formato 'M d H:i' o 'M d Y', según la antigüedad del fichero
            [time_t] => timestamp Unix de la última edición
            [name] => nombre del fichero o directorio
            [type] => tipo, puede ser 'file' o 'dir'
        )
    [1] => ...

        

## Ejemplos

Ejemplo con `svn_ls`

```
<?php
print_r( svn_ls('http://www.example.com/svnroot/') );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
            (
                [created_rev] => 20
                [last_author] => Joe
                [size] => 0
                [time] => Apr 02 09:28
                [time_t] => 1175520529
                [name] => tags
                [type] => dir
            )
        [1] => Array
            (
                [created_rev] => 23
                [last_author] => Bob
                [size] => 0
                [time] => Apr 02 15:15
                [time_t] => 1175541322
                [name] => trunk
                [type] => dir
            )
    )

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

Documentación SVN sobre el comando

"svn list"
