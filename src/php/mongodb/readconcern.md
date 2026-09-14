---
title: La clase MongoDB\Driver\ReadConcern
source_url: https://www.php.net/manual/es/class.mongodb-driver-readconcern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/readconcern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50850
---

## Introducción

`MongoDB\Driver\ReadConcern` controla el nivel de aislamiento para las operaciones de lectura para los conjuntos de réplicas y las réplicas de réplicas. Esta opción requiere MongoDB 3.2 o posterior.

## Sinopsis de la clase

MongoDB\Driver\ReadConcern

final

MongoDB\Driver\ReadConcern

MongoDB\BSON\Serializable

Serializable

Propiedades

public

readonly

string

null

level

Constantes

const

string

MongoDB\Driver\ReadConcern::AVAILABLE

"available"

const

string

MongoDB\Driver\ReadConcern::LINEARIZABLE

"linearizable"

const

string

MongoDB\Driver\ReadConcern::LOCAL

"local"

const

string

MongoDB\Driver\ReadConcern::MAJORITY

"majority"

const

string

MongoDB\Driver\ReadConcern::SNAPSHOT

"snapshot"

Métodos

## Propiedades

`level`  
El nivel del read concern. `null` si no se especificó ningún nivel.

## Constantes predefinidas

`MongoDB\Driver\ReadConcern::AVAILABLE`  
Por omisión para las lecturas en los secundarios cuando `afterClusterTime` y `level` no están especificados.

La consulta devuelve los datos más recientes de la instancia. No garantiza que los datos hayan sido escritos en la mayoría de los miembros del conjunto de réplicas (es decir, que puedan ser anulados).

Para las colecciones no fragmentadas (incluyendo las colecciones en un despliegue autónomo o un despliegue de réplicas), las lecturas `"local"` y `"available"` se comportan de manera idéntica.

Para un clúster compartido, la lectura `"available"` proporciona una mayor tolerancia a las particiones ya que no espera para garantizar garantías de coherencia. Sin embargo, una consulta con una lectura `"available"` puede devolver documentos huérfanos si el fragmento está en proceso de migración de piezas ya que la lectura `"available"`, a diferencia de la lectura `"local"`, no contacta al primario del fragmento ni a los servidores de configuración para obtener metadatos actualizados.

`MongoDB\Driver\ReadConcern::LINEARIZABLE`  
La consulta devuelve los datos que reflejan todas las escrituras exitosas emitidas con un nivel de escritura de `"majority"` *y* reconocido antes del inicio de la operación de lectura. Para los conjuntos de réplicas que funcionan con `writeConcernMajorityJournalDefault` definido en `true`, la lectura linealizable devuelve datos que nunca serán anulados.

Con `writeConcernMajorityJournalDefault` definido en `false`, MongoDB no esperará que las escrituras `w: "majority"` sean durables antes de acusar recibo de las escrituras. En consecuencia, las operaciones de escritura `"majority"` podrían eventualmente ser anuladas en caso de pérdida de un miembro del conjunto de réplicas.

Se puede especificar un nivel de lectura linealizable para las operaciones de lectura en el primario únicamente.

La lectura linealizable garantiza que las operaciones de lectura especifiquen un filtro de consulta que identifique de manera única un solo documento.

> [!TIP]
> Siempre utilizar `maxTimeMS` con una lectura linealizable en caso de no disponibilidad de la mayoría de los miembros portadores de datos. `maxTimeMS` garantiza que la operación no bloquee indefinidamente y garantiza que la operación devuelva un error si el nivel de lectura no puede ser satisfecho.

La lectura linealizable requiere MongoDB 3.4.

`MongoDB\Driver\ReadConcern::LOCAL`  
Por omisión para las lecturas en el primario si `level` no está especificado y para las lecturas en los secundarios si `level` no está especificado pero `afterClusterTime` está especificado.

La consulta devuelve los datos más recientes de la instancia. No garantiza que los datos hayan sido escritos en la mayoría de los miembros del conjunto de réplicas (es decir, que puedan ser anulados).

`MongoDB\Driver\ReadConcern::MAJORITY`  
La consulta devuelve los datos más recientes reconocidos como haber sido escritos en la mayoría de los miembros del conjunto de réplicas.

Para utilizar el nivel de lectura `"majority"`, los conjuntos de réplicas deben utilizar el motor de almacenamiento WiredTiger y el protocolo de elección versión 1.

`MongoDB\Driver\ReadConcern::SNAPSHOT`  
La lectura `"snapshot"` está disponible para las transacciones multi-documentos, y a partir de MongoDB 5.0, para ciertas operaciones de lectura fuera de las transacciones multi-documentos.

Si la transacción no forma parte de una sesión coherente, al validar la transacción con un nivel de escritura `"majority"`, las operaciones de transacción están garantizadas de haber leído desde una instantánea de datos mayoritariamente comprometidos.

Si la transacción forma parte de una sesión coherente, al validar la transacción con un nivel de escritura `"majority"`, las operaciones de transacción están garantizadas de haber leído desde una instantánea de datos mayoritariamente comprometidos que aseguran la coherencia causal con la operación inmediatamente anterior al inicio de la transacción.

Fuera de las transacciones multi-documentos, el nivel de lectura `"snapshot"` está disponible en los primarios y los secundarios para las siguientes operaciones de lectura: `find`, `aggregate` y `distinct` (en colecciones no fragmentadas). Todas las demás órdenes de lectura prohíben `"snapshot"`.

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
<td>PECL mongodb 1.11.0</td>
<td><p>Adición de la constante <code>MongoDB\Driver\ReadConcern::SNAPSHOT</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.7.0</td>
<td>Implementa Serializable.</td>
</tr>
<tr>
<td>PECL mongodb 1.4.0</td>
<td><p>Adición de la constante <code>MongoDB\Driver\ReadConcern::MAJORITY</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.2.0</td>
<td><p>Adición de la constante <code>MongoDB\Driver\ReadConcern::LINEARIZABLE</code></p>
<p>Implementa MongoDB\BSON\Serializable.</p></td>
</tr>
</tbody>
</table>

## Véase también

Referencia de lectura
