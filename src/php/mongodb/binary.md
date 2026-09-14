---
title: La clase MongoDB\BSON\Binary
source_url: https://www.php.net/manual/es/class.mongodb-bson-binary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/binary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47420
---

## Introducción

Tipo BSON para datos binarios (i.e. array de bytes). Los valores binarios también tienen un subtipo, que se utiliza para indicar qué tipo de datos se encuentra en el array de bytes. Los subtipos de cero a 127 están predefinidos o reservados. Los subtipos de 128-255 son definidos por el usuario.

## Sinopsis de la clase

MongoDB\BSON\Binary

final

MongoDB\BSON\Binary

MongoDB\BSON\BinaryInterface

MongoDB\BSON\Type

JsonSerializable

Stringable

Constantes

const

int

MongoDB\BSON\Binary::TYPE_GENERIC

0

const

int

MongoDB\BSON\Binary::TYPE_FUNCTION

1

const

int

MongoDB\BSON\Binary::TYPE_OLD_BINARY

2

const

int

MongoDB\BSON\Binary::TYPE_OLD_UUID

3

const

int

MongoDB\BSON\Binary::TYPE_UUID

4

const

int

MongoDB\BSON\Binary::TYPE_MD5

5

const

int

MongoDB\BSON\Binary::TYPE_ENCRYPTED

6

const

int

MongoDB\BSON\Binary::TYPE_COLUMN

7

const

int

MongoDB\BSON\Binary::TYPE_SENSITIVE

8

const

int

MongoDB\BSON\Binary::TYPE_VECTOR

9

const

int

MongoDB\BSON\Binary::TYPE_USER_DEFINED

128

Métodos

## Constantes predefinidas

`MongoDB\BSON\Binary::TYPE_GENERIC`  
Datos binarios genéricos.

`MongoDB\BSON\Binary::TYPE_FUNCTION`  
Función.

`MongoDB\BSON\Binary::TYPE_OLD_BINARY`  
Datos binarios genéricos (desaconsejados en favor de `MongoDB\BSON\Binary::TYPE_GENERIC`).

`MongoDB\BSON\Binary::TYPE_OLD_UUID`  
Identificador universalmente único (desaconsejado en favor de `MongoDB\BSON\Binary::TYPE_UUID`). Al utilizar este tipo, los datos del binario deben tener una longitud de 16 bytes.

Históricamente, otros controladores codifican valores con este tipo según sus convenciones lingüísticas (por ejemplo, variable indianness), lo que lo hace no portable. El controlador PHP no aplica ninguna manipulación especial para codificar o decodificar datos con este tipo.

`MongoDB\BSON\Binary::TYPE_UUID`  
Identificador universalmente único. Al utilizar este tipo, los datos del binario deben tener una longitud de 16 bytes y estar codificados según [RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122).

`MongoDB\BSON\Binary::TYPE_MD5`  
Hash MD5. Al utilizar este tipo, los datos del binario deben tener una longitud de 16 bytes.

`MongoDB\BSON\Binary::TYPE_ENCRYPTED`  
Valor cifrado. Este subtipo se utiliza para el cifrado del lado del cliente.

`MongoDB\BSON\Binary::TYPE_COLUMN`  
Dato de columna. Este subtipo se utiliza para las colecciones de series temporales.

`MongoDB\BSON\Binary::TYPE_SENSITIVE`  
Datos sensibles. Este subtipo se utiliza para los datos sensibles que deberían ser excluidos de los registros de eventos del lado del servidor si es posible.

`MongoDB\BSON\Binary::TYPE_VECTOR`  
Datos de vector. Este subtipo se utiliza para almacenar eficientemente datos de vector para su uso con la búsqueda de vectores de MongoDB.

`MongoDB\BSON\Binary::TYPE_USER_DEFINED`  
Tipo definido por el usuario. Mientras que los tipos entre 0 y 127 están predefinidos o reservados, los tipos entre 128 y 255 son definidos por el usuario y pueden ser utilizados para cualquier cosa.

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
<td>PECL mongodb 2.2.0</td>
<td>Adición de <code>MongoDB\BSON\Binary::TYPE_VECTOR</code>, así como las funciones MongoDB\BSON\Binary::fromVector, MongoDB\BSON\Binary::getVectorType y MongoDB\BSON\Binary::toArray.</td>
</tr>
<tr>
<td>PECL mongodb 2.0.0</td>
<td><p>Esta clase ya no implementa la interfaz Serializable.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.17.0</td>
<td>Adición de <code>MongoDB\BSON\Binary::TYPE_SENSITIVE</code>.</td>
</tr>
<tr>
<td>PECL mongodb 1.12.0</td>
<td><p>Implementa Stringable para PHP 8.0+.</p>
<p>Adición de <code>MongoDB\BSON\Binary::TYPE_COLUMN</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.7.0</td>
<td>Adición de <code>MongoDB\BSON\Binary::TYPE_ENCRYPTED</code>.</td>
</tr>
<tr>
<td>PECL mongodb 1.3.0</td>
<td>Implementa MongoDB\BSON\BinaryInterface.</td>
</tr>
<tr>
<td>PECL mongodb 1.2.0</td>
<td>Implementa Serializable y JsonSerializable.</td>
</tr>
</tbody>
</table>
