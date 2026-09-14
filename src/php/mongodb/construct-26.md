---
title: MongoDB\Driver\ReadPreference::__construct
description: Crear una nueva ReadPreference
source_url: https://www.php.net/manual/es/mongodb-driver-readpreference.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/readpreference/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50870
---

MongoDB\Driver\ReadPreference::\_\_construct

Crear una nueva ReadPreference

## Descripción

```php
final public MongoDB\Driver\ReadPreference::__construct(string $mode, [array $tagSets], [array $options])
```php

Construye un nuevo `MongoDB\Driver\ReadPreference`, que es un objeto de valor inmutable.

## Parámetros

`mode`  
| Valor | Descripción |
|----|----|
| `"primary"` | Todas las operaciones leídas desde el conjunto de réplicas actual primario. Este es el modo de preferencia de lectura por omisión para MongoDB. |
| `"primaryPreferred"` | En la mayoría de las situaciones, las operaciones son leídas desde el primario, pero si no está disponible, las operaciones son leídas desde un miembro secundario. |
| `"secondary"` | Todas las operaciones son leídas desde los miembros secundarios del conjunto de réplicas. |
| `"secondaryPreferred"` | En la mayoría de los casos, las operaciones son leídas por miembros secundarios, pero si ningún miembro secundario está disponible, las operaciones son leídas desde el primario. |
| `"nearest"` | Operaciones leídas desde el miembro del conjunto de réplicas con la latencia de red más baja, independientemente del tipo de miembro. |

Modo de preferencia de lectura

`tagSets`  
Los conjuntos de etiquetas permiten dirigir las operaciones de lectura a miembros específicos de un conjunto de réplicas. Este parámetro debe ser un array de arrays asociativos, que contienen cada uno cero o más pares clave/valor. Al seleccionar un servidor para una operación de lectura, el controlador intenta seleccionar un nodo que contenga todas las etiquetas de un conjunto (es decir, el array asociativo de pares clave/valor). Si la selección falla, el controlador intentará con los siguientes conjuntos. Un conjunto de etiquetas vacío (`array()`) corresponde a cualquier nodo y puede ser utilizado como respaldo.

Las etiquetas no son compatibles con el modo `"primary"` y, en general, solo se aplican cuando se selecciona un miembro secundario de un conjunto para una operación de lectura. Sin embargo, el modo `"nearest"`, cuando se combina con un conjunto de etiquetas, selecciona el miembro correspondiente con la latencia de red más baja. Este miembro puede ser primario o secundario.

`options`  
<table>
<caption>options</caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>hedge</td>
<td><code>objectarray</code></td>
<td><p>Especifica si se debe utilizar o no <a href="https://www.mongodb.com/docs/manual/core/sharded-cluster-query-router/#mongos-hedged-reads">las lecturas cruzadas</a>, que son soportadas desde MongoDB 4.4+ para las consultas compartidas.</p>
<p>El servidor de lecturas cruzadas está disponible para todas las lecturas de referencias no primarias, y está activado por omisión al utilizar el modo <code>"nearest"</code>. Esta opción permite activar explícitamente el servidor de lecturas cruzadas para las lecturas de referencias no primarias especificando <code>['enabled' =&gt; true]</code>, o desactivar explícitamente el servidor de lecturas cruzadas para las lecturas de referencias <code>"nearest"</code> especificando <code>['enabled' =&gt; false]</code>.</p></td>
</tr>
<tr>
<td>maxStalenessSeconds</td>
<td><code>int</code></td>
<td><p>Especifica un desfase de replicación máximo, o "obsolescencia", para las lecturas de los secundarios. Cuando la obsolescencia estimada de un secundario supera este valor, el controlador deja de utilizarlo para las operaciones de lectura.</p>
<p>Si se especifica, la obsolescencia máxima debe ser un entero signado de 32 bits mayor o igual a <code>MongoDB\Driver\ReadPreference::SMALLEST_MAX_STALENESS_SECONDS</code>.</p>
<p>Por omisión, <code>MongoDB\Driver\ReadPreference::NO_MAX_STALENESS</code>, lo que significa que el controlador no tendrá en cuenta el desfase de un secundario al elegir dónde dirigir una operación de lectura.</p>
<p>Esta opción no es compatible con el modo <code>"primary"</code>. La especificación de una obsolescencia máxima requiere asimismo que todas las instancias de MongoDB del despliegue utilicen MongoDB 3.4+. Se lanzará una excepción en tiempo de ejecución si todas las instancias de MongoDB en el despliegue son de una versión de servidor más antigua.</p></td>
</tr>
</tbody>
</table>

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si

mode

es incorrecto.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si

tagSets

es proporcionado para una preferencia de lectura primaria o es incorrecto (es decir, no es un array de cero o más documentos).

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si la opción

"maxStalenessSeconds"

es proporcionada para una preferencia de lectura primaria o está fuera de rango.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | Pasar un `int` para el argumento `mode` ya no es soportado. |
| PECL mongodb 1.20.0 | Pasar un `int` para el argumento `mode` está *DEPRECADO*. |
| PECL mongodb 1.8.0 | Añadida la opción `"hedge"`. |
| PECL mongodb 1.3.0 | El argumento `mode` acepta ahora un valor de string, que es compatible con la opción URI `"readPreference"` para `MongoDB\Driver\Manager::__construct` |
| PECL mongodb 1.2.0 | Añadido un tercer argumento de `options`, que soporta la opción `"maxStalenessSeconds"`. |

## Ejemplos

Ejemplo con `MongoDB\Driver\ReadPreference::__construct`

```
<?php

/* Prefiera un nodo secundario pero recurra a un primario. */
var_dump(new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::SECONDARY_PREFERRED));

/* Prefiera un nodo en el centro de datos de Nueva York con la latencia más baja. */
var_dump(new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::NEAREST, [['dc' => 'ny']]));

/* Requiere un nodo secundario cuyo desfase de replicación se encuentre dentro de los dos minutos */
var_dump(new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::SECONDARY, null, ['maxStalenessSeconds' => 120]));

/* Activa explícitamente el servidor de lecturas cruzadas */
var_dump(new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::SECONDARY, null, ['hedge' => ['enabled' => true]]));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\Driver\ReadPreference)#1 (1) {
      ["mode"]=>
      string(18) "secondaryPreferred"
    }
    object(MongoDB\Driver\ReadPreference)#1 (2) {
      ["mode"]=>
      string(7) "nearest"
      ["tags"]=>
      array(1) {
        [0]=>
        object(stdClass)#2 (1) {
          ["dc"]=>
          string(2) "ny"
        }
      }
    }
    object(MongoDB\Driver\ReadPreference)#1 (2) {
      ["mode"]=>
      string(9) "secondary"
      ["maxStalenessSeconds"]=>
      int(120)
    }
    object(MongoDB\Driver\ReadPreference)#1 (2) {
      ["mode"]=>
      string(9) "secondary"
      ["hedge"]=>
      object(stdClass)#1 (1) {
        ["enabled"]=>
        bool(true)
      }
    }

## Véase también

Read Preference reference
