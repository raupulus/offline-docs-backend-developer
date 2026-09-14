---
title: La interfaz MongoDB\Driver\CursorInterface
source_url: https://www.php.net/manual/es/class.mongodb-driver-cursorinterface.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursorinterface.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49440
---

## Introducción

Esta interfaz es implementada por `MongoDB\Driver\Cursor` para ser usada como un parámetro, retorno, o tipo de propiedad en clases de usuario.

## Sinopsis de la clase

MongoDB\Driver\CursorInterface

MongoDB\Driver\CursorInterface

Iterator

Métodos

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
<td>PECL mongodb 2.0.0</td>
<td><p>Esta interfaz ahora extiende Iterator.</p>
<p>Los tipos de retorno declarados previamente como provisionales ahora están obligados.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.15.0</td>
<td>Los tipos de retorno de los métodos son declarados como provisionales en PHP 8.0 y posteriores, lo que desencadena avisos de depreciación en el código que implementa esta interfaz sin declarar los tipos de retorno apropiados. El atributo <code>#[ReturnTypeWillChange]</code> puede ser añadido para ignorar la notificación de depreciación.</td>
</tr>
</tbody>
</table>
