---
title: Yaf_Route_Interface::route
description: Enruta una petición
source_url: https://www.php.net/manual/es/yaf-route-interface.route.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_interface/route.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 7418592d8
order: 106730
---

Yaf_Route_Interface::route

Enruta una petición

## Descripción

```php
abstract public Yaf_Route_Interface::route(Yaf_Request_Abstract $request): bool
```php

Yaf_Route_Interface::route es el único método que debería implementar un enrutamiento personalizado.

> [!NOTE]
> Desde la 2.3.0, hay otro método que también debería ser implementado, ver Yaf_Route_Interface::assemble.

Si este método devuelve `true`, el proceso de enrutamiento terminará, de otro modo `Yaf_Router` llamará a la siguiente ruta de la pila de enrutamiento para enrutar la petición.

Este método establecería el resultado del enrutamiento al parámetro request, llamando a los métodos Yaf_Request_Abstract::setControllerName, Yaf_Request_Abstract::setActionName y Yaf_Request_Abstract::setModuleName.

Este método debería también llamar al método Yaf_Request_Abstract::setRouted para realizar al fin la petición enrutada.

## Parámetros

`request`  
Una instancia de la clase `Yaf_Request_Abstract`.

## Valores devueltos
