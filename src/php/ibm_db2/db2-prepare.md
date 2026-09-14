---
title: db2_prepare
description: Prepara una consulta SQL para ser ejecutada
source_url: https://www.php.net/manual/es/function.db2-prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30990
---

db2_prepare

Prepara una consulta SQL para ser ejecutada

## Descripción

```php
db2_prepare(resource $connection, string $statement, [array $options]): resource
```php

`db2_prepare` crea una consulta SQL preparada que puede incluir ningún o varios marcadores (caracteres `?`) representando los argumentos de entrada, salida o entrada/salida. Se pueden pasar argumentos a la consulta preparada utilizando la función `db2_bind_param`, si solo hay entradas, se puede utilizar `db2_execute`.

Existen tres ventajas principales de utilizar consultas preparadas en la aplicación :

- *Rendimiento* : al preparar una consulta, el servidor de base de datos crea un plan de acceso optimizado para la recuperación de datos con la consulta. Posteriormente, el envío de la consulta preparada con `db2_execute` permite a la consulta reutilizar el plan de acceso y así evitar sobrecargas del procesador en cada envío de consulta que crearía dinámicamente un nuevo plan de acceso.

- *Seguridad* : al preparar una consulta, se pueden incluir marcadores para los valores de entrada. Al ejecutar una consulta preparada con estos valores de entrada, el servidor de base de datos verifica cada valor de entrada para asegurarse de que los tipos coincidan con la definición de la columna o del parámetro de definición.

- *Funcionalidad avanzada* : Los marcadores permiten no solo pasar valores de entrada en las consultas SQL preparadas, sino también recuperar parámetros de SALIDA y de ENTRADA/SALIDA de los procedimientos de registro utilizando la función `db2_bind_param`.

## Parámetros

`connection`  
Una variable recurso de conexión válida devuelta por `db2_connect` o `db2_pconnect`.

`statement`  
Una consulta SQL que puede contener uno o varios marcadores.

`options`  
Un array asociativo que contiene las opciones de la consulta. Se puede utilizar este parámetro para solicitar un cursor flotante en los servidores de base de datos que soportan esta funcionalidad.

Para una descripción de las opciones válidas, consulte la función `db2_set_option`.

## Valores devueltos

Devuelve una variable recurso si la consulta SQL fue enviada correctamente o `false` si el servidor de base de datos ha devuelto un error. Se puede determinar qué error fue devuelto llamando a la función `db2_stmt_error` o `db2_stmt_errormsg`.

## Ejemplos

Preparación y ejecución de una consulta SQL con marcadores

El siguiente ejemplo prepara una consulta INSERT que acepta cuatro marcadores, luego itera sobre el array que contiene los valores de entrada que serán pasados a la función `db2_execute`.

```
<?php
$animales = array(
    array(0, 'gato', 'Pook', 3.2),
    array(1, 'perro', 'Peaches', 12.3),
    array(2, 'caballo', 'Smarty', 350.0),
);

$insert = 'INSERT INTO animales (id, raza, nombre, peso)
    VALUES (?, ?, ?, ?)';
$stmt = db2_prepare($conn, $insert);
if ($stmt) {
    foreach ($animales as $animal) {
        $result = db2_execute($stmt, $animal);
    }
}
?>

   
```php

## Véase también

db2_bind_param

db2_execute

db2_stmt_error

db2_stmt_errormsg
