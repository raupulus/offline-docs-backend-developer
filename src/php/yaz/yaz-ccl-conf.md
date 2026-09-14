---
title: yaz_ccl_conf
description: Configura el analizador CCL
source_url: https://www.php.net/manual/es/function.yaz-ccl-conf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-ccl-conf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107750
---

yaz_ccl_conf

Configura el analizador CCL

## Descripción

```php
yaz_ccl_conf(resource $id, array $config): void
```php

Ésta función configura la consulta analizadora CCL para un servidor con definiciones de puntos de acceso (Calificadores CCL) y su asignación al RPN.

Para asignar una consulta especifica CCL al RPN después se llama la función `yaz_ccl_parse`.

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

`config`  
Un arreglo de configuración. Cada clave del arreglo es el nombre de un campo CCL y el correspondiente valor que mantiene una cadena que especifica una asignación al RPN.

La asignación es una secuencia de el tipo de atributo, de los valores de los atributos pares. El tipo de atributo y el valor del atributo están separados por un signo (`=`). Cada par es separado por un espacio en blanco.

La información adicional la puede encontrar en la página [CCL](https://software.indexdata.com/yaz/doc/tools.html#CCL).

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

En cada ejemplo a continuación, el analizador CCL está configurado para soportar el árbol de los campos CCL: `ti`, `au` y `isbn`. Cada campo es asignado a su equivalente BIB-1. Es asumida que la variable `$id` es la conexión ID.

Configuración del CCL

```
<?php
$fields = array(
  "ti" => "1=4",
  "au"   => "1=1",
  "isbn" => "1=7"
);
yaz_ccl_conf($id, $fields);
?>

   
```php

## Véase también

`yaz_ccl_parse`
