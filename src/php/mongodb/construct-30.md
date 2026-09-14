---
title: MongoDB\Driver\WriteConcern::__construct
description: Construye un WriteConcern
source_url: https://www.php.net/manual/es/mongodb-driver-writeconcern.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeconcern/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51470
---

MongoDB\Driver\WriteConcern::\_\_construct

Construye un WriteConcern

## Descripción

```php
final public MongoDB\Driver\WriteConcern::__construct(string $w, [int $wtimeout], [bool $journal])
```php

Construye un nuevo `MongoDB\Driver\WriteConcern`, que es un objeto de valor inmutable.

## Parámetros

`w`  
<table>
<caption>Preocupación de escritura</caption>
<thead>
<tr>
<th>Valor</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Solicita el acuse de recibo de que la operación de escritura se ha propagado al <code>mongod</code> autónomo o al principal en un conjunto de réplicas. Es la preocupación de escritura por omisión para MongoDB.</td>
</tr>
<tr>
<td>0</td>
<td>No solicita ningún acuse de recibo de la operación de escritura. Sin embargo, puede devolver información sobre las excepciones de socket y los errores de red a la aplicación.</td>
</tr>
<tr>
<td>&lt;entero superior a 1&gt;</td>
<td>Los números superiores a 1 son válidos únicamente para los conjuntos de réplicas para solicitar el acuse de recibo del número especificado de miembros, incluyendo el principal.</td>
</tr>
<tr>
<td><code>MongoDB\Driver\WriteConcern::MAJORITY</code></td>
<td><p>Solicita el acuse de recibo de que las operaciones de escritura se han propagado a la mayoría de los nodos votantes, incluyendo el principal, y han sido escritas en el journal en disco para esos nodos.</p>
<p>Antes de MongoDB 3.0, es la mayoría de los miembros del conjunto de réplicas (y no solo de los nodos votantes).</p></td>
</tr>
<tr>
<td>string</td>
<td>Un valor de string es interpretado como un conjunto de etiquetas. Solicita el acuse de recibo de que las operaciones de escritura se han propagado a un miembro del conjunto de réplicas con la etiqueta especificada.</td>
</tr>
</tbody>
</table>

`wtimeout`  
Tiempo máximo de espera (en milisegundos) antes de que los secundarios fallen.

`wtimeout` hará que las operaciones de escritura devuelvan un error (`WriteConcernError`) después del tiempo especificado. Cuando estas operaciones de escritura devuelvan, MongoDB no cancelará los datos modificados antes de que las preocupaciones de escritura alcancen el tiempo límite `wtimeout`.

Si se especifica, `wtimeout` debe ser un entero con signo de 64 bits mayor o igual a cero.

| Valor | Descripción |
|----|----|
| 0 | Bloquea indefinidamente. Es el comportamiento por omisión. |
| \<entero superior a 0\> | Número de milisegundos a esperar antes de devolver. |

Tiempo máximo de espera de las preocupaciones de escritura

`journal`  
Espera antes de que mongod aplique la escritura al journal.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si

w

es inválido o

wtimeout

es negativo o superior a los límites de un entero con signo de 32 bits.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.7.0 | El parámetro `wTimeout` acepta ahora valores de 64 bits. |

## Ejemplos

Ejemplo con `MongoDB\Driver\WriteConcern::__construct`

```
<?php

/* Solicita una confirmación de las solicitudes de escritura para la mayoría de los nodos
   del conjunto de réplicas */
$wc = new MongoDB\Driver\WriteConcern(MongoDB\Driver\WriteConcern::MAJORITY, 500);

/* Solicita una confirmación de las solicitudes de escritura, configurada por la etiqueta
   "MultipleDC" */
$wc = new MongoDB\Driver\WriteConcern("MultipleDC", 500);

?>

   
```php

## Véase también

Write Concern reference
