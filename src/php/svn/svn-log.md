---
title: svn_log
description: Recupera el mensaje de historial de una URL del repositorio
source_url: https://www.php.net/manual/es/function.svn-log.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-log.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: true
translation_revision: 997700a58
order: 90230
---

svn_log

Recupera el mensaje de historial de una URL del repositorio

## Descripción

```php
svn_log(string $repos_url, [int $start_revision], [int $end_revision], [int $limit], [int $flags]): array
```php

`svn_log` recupera el historial completo del elemento correspondiente a la URL `repos_url`, o el historial de una revisión específica si `start_revision` está especificado. Esta función es equivalente al comando `svn log --verbose -r $start_revision $repos_url`.

## Parámetros

`repos_url`  
URL en el repositorio del elemento del que se debe recuperar el historial.

`start_revision`  
Número de revisión del primer historial a recuperar. Utilice la constante `SVN_REVISION_HEAD` para recuperar el historial de la revisión más reciente.

`end_revision`  
Número de revisión del último historial a recuperar. Por omisión vale `start_revision` si está especificado, de lo contrario vale la constante `SVN_REVISION_INITIAL`.

`limit`  
Número de historiales a recuperar.

`flags`  
Cualquier combinación de `SVN_OMIT_MESSAGES`, `SVN_DISCOVER_CHANGED_PATHS` y `SVN_STOP_ON_COPY`.

## Valores devueltos

En caso de éxito, esta función devuelve un array de ficheros en el formato:

    [0] => Array, ordenado del número de revisión más grande al más pequeño
    (
        [rev] => número de revisión
        [author] => nombre del autor
        [msg] => mensaje de historial
        [date] => fecha, en formato ISO 8601, es decir, date('c')
        [paths] => Array, describiendo los ficheros modificados
            (
                [0] => Array
                    (
                        [action] => letra, especificando la modificación
                        [path] => ruta absoluta del repositorio al fichero modificado
                    )
                [1] => ...
            )
    )
    [1] => ...

        

> [!NOTE]
> La salida será siempre un array indexado numéricamente de arrays, incluso si no hay ninguno, o solo un mensaje de historial.

El valor de `action` es una subparte de [la salida de estado en la primera columna](http://svnbook.red-bean.com/en/1.2/svn.ref.svn.c.status.html), donde los valores posibles son:

| Letra | Descripción                     |
|-------|---------------------------------|
| M     | El elemento ha sido modificado  |
| A     | El elemento ha sido añadido     |
| D     | El elemento ha sido eliminado   |
| R     | El elemento ha sido reemplazado |

Acciones

Si no se ha realizado ninguna modificación al elemento, se devolverá un array vacío.

## Ejemplos

Ejemplo con `svn_log`

```
<?php
print_r( svn_log('http://www.example.com/', 23) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
        (
            [rev] => 23
            [author] => 'joe'
            [msg] => 'Add cheese and salami to our sandwich.'
            [date] => '2007-04-06T16:00:27-04:00'
            [paths] => Array
                (
                    [0] => Array
                        (
                            [action] => 'M'
                            [path] =>  '/sandwich.txt'
                        )
                )
        )
    )

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

Documentación SVN para el comando

"svn log"
