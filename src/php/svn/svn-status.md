---
title: svn_status
description: Obtiene el estado de los ficheros y directorios de la copia de trabajo
source_url: https://www.php.net/manual/es/function.svn-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: true
translation_revision: 997700a58
order: 90340
---

svn_status

Obtiene el estado de los ficheros y directorios de la copia de trabajo

## Descripción

```php
svn_status(string $path, [int $flags]): array
```php

Devuelve el estado de los ficheros y directorios de la copia de trabajo, proporcionando las modificaciones, adiciones, eliminaciones, así como otros cambios de los elementos de la copia de trabajo.

## Parámetros

`path`  
Ruta local al fichero o directorio del que se desea obtener el estado.

> [!NOTE]
> Los caminos relativos pueden ser resueltos si el directorio de trabajo actual es uno de los que contienen el binario PHP. Para utilizar el directorio de trabajo, utilice la función `realpath`, o la instrucción dirname(\_\_FILE\_\_).

`flags`  
Cualquier combinación de `Svn::NON_RECURSIVE`, `Svn::ALL` (independientemente del estado de modificación), `Svn::SHOW_UPDATES` (se añadirán entradas para elementos que no están actualizados), `Svn::NO_IGNORE` (ignora las propiedades `svn:ignore` al analizar nuevos ficheros) y `Svn::IGNORE_EXTERNALS`.

## Valores devueltos

Devuelve un array indexado numéricamente de arrays asociativos que detallan el estado de los elementos del repositorio:

    Array (
        [0] => Array (
            // información sobre el elemento
        )
        [1] => ...
    )

      

La información sobre un elemento es un array asociativo que puede contener las siguientes claves:

`path`  
Ruta al fichero/directorio de esta entrada en el sistema de ficheros local.

`text_status`  
Estado del texto del elemento. Refiérase a las [constantes de estado](#svn.constants.status) para los valores posibles.

`repos_text_status`  
Estado del texto del elemento en el repositorio. Solo ocurre si `update` está definido como `true`. Refiérase a las [constantes de estado](#svn.constants.status) para los valores posibles.

`prop_status`  
Estado de la propiedad del elemento. Refiérase a las [constantes de estado](#svn.constants.status) para los valores posibles.

`repos_prop_status`  
Estado de la propiedad del elemento en el repositorio. Solo ocurre si `update` está definido como `true`. Refiérase a las [constantes de estado](#svn.constants.status) para los valores posibles.

`locked`  
Si el elemento está bloqueado. (Definido solo si `true`.)

`copied`  
Si el elemento ha sido copiado o no (previsto para añadir con el registro). (Definido solo si `true`.)

`switched`  
Si el elemento ha cambiado de repositorio de referencia, utilizando el comando switch. (Definido solo si `true`)

Estas claves solo están definidas si el elemento está versionado:

`name`  
Nombre base del elemento en el repositorio.

`url`  
URL del elemento en el repositorio.

`repos`  
URL base del repositorio.

`revision`  
Revisión del elemento en la copia de trabajo.

`kind`  
Tipo del elemento, es decir, fichero o directorio. Refiérase a las [constantes de tipo](#svn.constants.type) para los valores posibles.

`schedule`  
Acción prevista para el elemento, es decir, adición o eliminación. Las constantes para estos números mágicos no están disponibles, pueden ser emuladas utilizando:

```
<?php
if (!defined('svn_wc_schedule_normal')) {
    define('svn_wc_schedule_normal',  0); // nada especial
    define('svn_wc_schedule_add',     1); // elemento a añadir
    define('svn_wc_schedule_delete',  2); // elemento a eliminar
    define('svn_wc_schedule_replace', 3); // elemento a añadir y eliminar
}
?>

      
```php

`deleted`  
Si el elemento ha sido eliminado, pero las revisiones padre aún existen (Definido solo si `true`.)

`absent`  
Si el elemento está ausente, pero Subversion sabe que debería estar aquí. (Definido solo si `true`.)

`incomplete`  
Si la entrada del fichero para un directorio está incompleta. (Definido solo si `true`.)

`cmt_date`  
Timestamp Unix de la fecha del último commit. (No afectado por el parámetro `update`).

`cmt_rev`  
Revisión del último commit. (No afectado por el parámetro `update`).

`cmt_author`  
Nombre del autor del último commit. (No afectado por el parámetro `update`).

`prop_time`  
Timestamp Unix que representa la fecha/hora de la última actualización de las propiedades.

`text_time`  
Timestamp Unix que representa la fecha/hora de la última actualización del texto.

## Ejemplos

Ejemplo de uso

Este ejemplo muestra un uso básico de esta función.

```
<?php
print_r(svn_status(realpath('wc')));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array (
        [0] => Array (
            [path] => /home/bob/wc/sandwich.txt
            [text_status] => 8 // el elemento ha sido modificado
            [repos_text_status] => 1 // Ninguna información disponible, use update
            [prop_status] => 3 // ningún cambio
            [repos_prop_status] => 1 // Ninguna información disponible, use update
            [name] => sandwich.txt
            [url] => http://www.example.com/svnroot/deli/trunk/sandwich.txt
            [repos] => http://www.example.com/svnroot/
            [revision] => 123
            [kind] => 1 // fichero
            [schedule] => 0 // ninguna acción prevista
            [cmt_date] => 1165543135
            [cmt_rev] => 120
            [cmt_author] => Alice
            [prop_time] => 1180201728
            [text_time] => 1180201729
        )
    )

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

svn_update

svn_log

Documentación SVN del comando

"svn status"
