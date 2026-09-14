---
title: La clase Yaf_Route_Simple
source_url: https://www.php.net/manual/es/class.yaf-route-simple.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf-route-simple.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 104830
---

## Introducción

`Yaf_Route_Simple` comparará la cadena de consulta, y buscará la información de enrutamiento.

Todo lo que se necesita es indicar a `Yaf_Route_Simple` qué clave de la variable \$\_GET es un módulo, qué clave es un controlador, y qué clave es una acción.

Yaf_Route_Simple::route siempre devuelve `true`, por lo que es importante poner `Yaf_Route_Simple` al frente de la pila de enrutamiento, de otro modo todas las otras rutas no serán llamadas.

## Sinopsis de la clase

Yaf_Route_Simple

Yaf_Route_Simple

Yaf_Route_Interface

Propiedades

protected

controller

protected

module

protected

action

Métodos

## Propiedades

`controller`  

`module`  

`action`
