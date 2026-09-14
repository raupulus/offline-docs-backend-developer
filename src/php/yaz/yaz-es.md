---
title: yaz_es
description: Prepara para una solicitud de servicio extendido
source_url: https://www.php.net/manual/es/function.yaz-es.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-es.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: dfd68fd22
order: 107840
---

yaz_es

Prepara para una solicitud de servicio extendido

## Descripción

```php
yaz_es(resource $id, string $type, array $args): void
```php

Esta función prepara para una solicitud de servicio extendido. Los servicios extendidos son una familia de diversas facilidades Z39.50, tales como actualización de registros, ordenado de ítem, administración de base de datos, etc.

> [!NOTE]
> Muchos servidores Z39.50 no soportan servicios extendidos.

La `yaz_es` crea un paquete de solicitud de servicio extendido y la pone en una cola de operaciones. Se utiliza `yaz_wait` para enviar la(s) solicitud(es) al servidor. Después de completar `yaz_wait` el resultado de la operación del servicio extendido se debe esperar con una llamada a `yaz_es_result`.

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

`type`  
Un string que representa el tipo de servicio extendido: `itemorder` (Ordenado de ítem), `create` (Crear base de datos), `drop` (Descartar base de datos), `commit` (Operación de cometer), `update` (Actualizar registro), `xmlupdate` (Actualizar XML). Cada tipo se especifica en la sección siguiente.

`args`  
Un array con las opciones de servicio extendido, más opciones específicas del paquete. Las opciones son idénticas a las ofrecidas en la API C de ZOOM C. Consulte a los [servicios extendidos](https://software.indexdata.com/yaz/doc/zoom.html) de ZOOM.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Actualizar registro

```
<?php
$con = yaz_connect("myhost/database");
$args = array (
    "record" => "<gils><title>some title</title></gils>",
    "syntax" => "xml",
    "action" => "specialUpdate"
);
yaz_es($con, "update", $args);
yaz_wait();
$result = yaz_es_result($id);
?>

   
```php

## Véase también

`yaz_es_result`
