---
title: Yaf_Route_Interface::assemble
description: Ensamblar una petición
source_url: https://www.php.net/manual/es/yaf-route-interface.assemble.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_route_interface/assemble.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 7418592d8
order: 106720
---

Yaf_Route_Interface::assemble

Ensamblar una petición

## Descripción

```php
abstract public Yaf_Route_Interface::assemble(array $info, [array $query]): string
```php

Este método devuelve un URL según el argumento info info, y pospone los string de consultas al URL según el argumento query.

Una ruta debería implementar este método según sus propias reglas de ruta, y realizar un progreso inverso.

## Parámetros

`info`  

`query`  

## Valores devueltos
