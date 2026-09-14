---
title: La clase Yaf_Action_Abstract
source_url: https://www.php.net/manual/es/class.yaf-action-abstract.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf-action-abstract.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 4d17b7b49
order: 104520
---

## Introducción

Una acción puede ser definida en un fichero aparte en Yaf (véase `Yaf_Controller_Abstract`). Es decir, un método de acción también puede ser una clase `Yaf_Action_Abstract`.

Dado que debe haber un punto de entrada que pueda ser llamado por Yaf, debe implementar el método abstracto Yaf_Action_Abstract::execute en la clase de acción personalizada.

## Sinopsis de la clase

Yaf_Action_Abstract

Yaf_Action_Abstract

extends

Yaf_Controller_Abstract

Propiedades

protected

\_controller

Métodos

Métodos heredados

## Propiedades

`_module`  

`_name`  

`_request`  

`_response`  

`_invoke_args`  

`_view`  

`_controller`
