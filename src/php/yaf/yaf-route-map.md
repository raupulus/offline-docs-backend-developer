---
title: La clase Yaf_Route_Map
source_url: https://www.php.net/manual/es/class.yaf-route-map.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf-route-map.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 4d17b7b49
order: 104800
---

## Introducción

`Yaf_Route_Map` es una ruta interna, simplemente convierte el extremo de un URI (la parte del URI que va después del URI base: véase Yaf_Request_Abstract::setBaseUri) a un nombre de controlador o acción (dependen del parámetro pasado a Yaf_Route_Map::\_\_construct) en la siguiente regla: A =\> controlador A. A/B/C =\> controlador A_B_C. A/B/C/D/E =\> controlador A_B_C_D_E.

Si se especifica el segundo parámetro de Yaf_Route_Map::\_\_construct, solamente la parte de antes del delimitador del URI se usará para enrutar, la parte de después se usa para enrutar parámetros de petición (véase la sección de ejemplos de Yaf_Route_Map::\_\_construct).

## Sinopsis de la clase

Yaf_Route_Map

Yaf_Route_Map

Yaf_Route_Interface

Propiedades

protected

\_ctl_router

protected

\_delimiter

Métodos

## Propiedades

`_ctl_router`  

`_delimiter`
