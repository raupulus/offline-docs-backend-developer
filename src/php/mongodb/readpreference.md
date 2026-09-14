---
title: La clase MongoDB\Driver\ReadPreference
source_url: https://www.php.net/manual/es/class.mongodb-driver-readpreference.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/readpreference.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50930
---

## Introducción

## Sinopsis de la clase

MongoDB\Driver\ReadPreference

final

MongoDB\Driver\ReadPreference

MongoDB\BSON\Serializable

Serializable

Propiedades

public

readonly

string

mode

public

readonly

array

null

tags

public

readonly

int

maxStalenessSeconds

public

readonly

object

null

hedge

Constantes

const

string

MongoDB\Driver\ReadPreference::PRIMARY

primary

const

string

MongoDB\Driver\ReadPreference::PRIMARY_PREFERRED

primaryPreferred

const

string

MongoDB\Driver\ReadPreference::SECONDARY

secondary

const

string

MongoDB\Driver\ReadPreference::SECONDARY_PREFERRED

secondaryPreferred

const

string

MongoDB\Driver\ReadPreference::NEAREST

nearest

const

int

MongoDB\Driver\ReadPreference::NO_MAX_STALENESS

-1

const

int

MongoDB\Driver\ReadPreference::SMALLEST_MAX_STALENESS_SECONDS

90

Métodos

## Propiedades

`mode`  
El modo de preferencia de lectura como cadena (por ejemplo `"primary"`, `"secondary"`).

`tags`  
La lista de conjuntos de tags utilizada por la preferencia de lectura, o `null` si no se especificó ningún conjunto de tags.

`maxStalenessSeconds`  
La duración máxima de obsolescencia en segundos para las lecturas, o `MongoDB\Driver\ReadPreference::NO_MAX_STALENESS` si no se especificó ninguna duración máxima de obsolescencia.

`hedge`  
Un documento que especifica las opciones de hedge para la preferencia de lectura, o `null` si no se especificó ninguna opción de hedge.

> [!WARNING]
> Esta propiedad está obsoleta ya que las lecturas con hedge están obsoletas en MongoDB 8.0.

## Constantes predefinidas

`MongoDB\Driver\ReadPreference::PRIMARY`  
Todas las operaciones se leen desde el primario actual del conjunto de réplicas. Esta es la preferencia de lectura por omisión para MongoDB.

`MongoDB\Driver\ReadPreference::PRIMARY_PREFERRED`  
En la mayoría de las situaciones, las operaciones se leen desde el primario, pero si no está disponible, las operaciones se leen desde los miembros secundarios.

`MongoDB\Driver\ReadPreference::SECONDARY`  
Todas las operaciones se leen desde los miembros secundarios del conjunto de réplicas.

`MongoDB\Driver\ReadPreference::SECONDARY_PREFERRED`  
En la mayoría de los casos, las operaciones se leen desde los miembros secundarios, pero si ningún miembro secundario está disponible, las operaciones se leen desde el primario.

`MongoDB\Driver\ReadPreference::NEAREST`  
Las operaciones se leen desde el miembro del conjunto de réplicas con la menor latencia de red, independientemente del tipo de miembro.

`MongoDB\Driver\ReadPreference::NO_MAX_STALENESS`  
El valor por omisión de la opción `"maxStalenessSeconds"` es no especificar ningún límite sobre la obsolescencia máxima, lo que significa que el controlador no tendrá en cuenta el desfase de un secundario al elegir dónde dirigir una operación de lectura.

`MongoDB\Driver\ReadPreference::SMALLEST_MAX_STALENESS_SECONDS`  
El valor mínimo de la opción `"maxStalenessSeconds"` es de 90 segundos. El controlador estima la obsolescencia de los segundos verificando periódicamente la última fecha de escritura de cada miembro del conjunto de réplicas. Como estos controles son poco frecuentes, la estimación de la obsolescencia es aproximada. Por lo tanto, el controlador no puede aplicar un valor de obsolescencia máxima inferior a 90 segundos.

## Historial de cambios

<table role="class">
<thead>
<tr>
<th>Versión</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>PECL mongodb 2.3.0</td>
<td>Se añadieron las propiedades públicas readonly.</td>
</tr>
<tr>
<td>PECL mongodb 2.0.0</td>
<td><p>Eliminar las constantes <code>MongoDB\Driver\ReadPreference::RP_PRIMARY</code>, <code>MongoDB\Driver\ReadPreference::RP_PRIMARY_PREFERRED</code>, <code>MongoDB\Driver\ReadPreference::RP_SECONDARY</code>, <code>MongoDB\Driver\ReadPreference::RP_SECONDARY_PREFERRED</code>, y <code>MongoDB\Driver\ReadPreference::RP_NEAREST</code>. El método getMode también fue eliminado.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.7.0</td>
<td><p>Añadir las constantes <code>MongoDB\Driver\ReadPreference::PRIMARY</code>, <code>MongoDB\Driver\ReadPreference::PRIMARY_PREFERRED</code>, <code>MongoDB\Driver\ReadPreference::SECONDARY</code>, <code>MongoDB\Driver\ReadPreference::SECONDARY_PREFERRED</code>, <code>MongoDB\Driver\ReadPreference::NEAREST</code>.</p>
<p>Implementa Serializable.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.2.0</td>
<td><p>Añadir las constantes <code>MongoDB\Driver\ReadPreference::NO_MAX_STALENESS</code> y <code>MongoDB\Driver\ReadPreference::SMALLEST_MAX_STALENESS_SECONDS</code>.</p>
<p>Implementa MongoDB\BSON\Serializable.</p></td>
</tr>
</tbody>
</table>
