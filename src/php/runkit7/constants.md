---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/runkit7.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: 3a826d03c
order: 72830
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`RUNKIT7_IMPORT_FUNCTIONS` (`int`)  
El flag `runkit7_import` indica que las funciones normales deben ser importadas del archivo especificado.

`RUNKIT7_IMPORT_CLASS_METHODS` (`int`)  
El flag `runkit7_import` indica que los métodos de clase deben ser importados del archivo especificado.

`RUNKIT7_IMPORT_CLASS_CONSTS` (`int`)  
El flag `runkit7_import` indica que las constantes de clase deben ser importadas del archivo especificado.

`RUNKIT7_IMPORT_CLASS_PROPS` (`int`)  
El flag `runkit7_import` indica que las propiedades de clase estándar deben ser importadas del archivo especificado.

`RUNKIT7_IMPORT_CLASS_STATIC_PROPS` (`int`)  
El flag `runkit7_import` indica que las propiedades estáticas de clase deben ser importadas del archivo especificado. Disponible a partir de Runkit 1.0.1.

`RUNKIT7_IMPORT_CLASSES` (`int`)  
El flag `runkit7_import` representa un OU a nivel de bits de las constantes `RUNKIT7_IMPORT_CLASS_*`.

`RUNKIT7_IMPORT_OVERRIDE` (`int`)  
El flag `runkit7_import` indica que si alguna de las funciones, métodos, constantes o propiedades importados ya existen, deben ser sobrescritos por las nuevas definiciones. Si este flag no está definido, entonces todas las definiciones importadas que ya existan serán ignoradas.

`RUNKIT7_ACC_RETURN_REFERENCE` (`int`)  
Incluir este flag para hacer que la función o método creado o redefinido devuelva una referencia.

`RUNKIT7_ACC_PUBLIC` (`int`)  
El flag para `runkit7_method_add` y `runkit7_method_redefine` para hacer que el método sea público.

`RUNKIT7_ACC_PROTECTED` (`int`)  
El flag para `runkit7_method_add` y `runkit7_method_redefine` para hacer que el método sea protegido.

`RUNKIT7_ACC_PRIVATE` (`int`)  
El flag para `runkit7_method_add` y `runkit7_method_redefine` para hacer que el método sea privado.

`RUNKIT7_ACC_STATIC` (`int`)  
El flag para `runkit7_method_add` y `runkit7_method_redefine` para hacer que el método sea estático.

`RUNKIT7_FEATURE_MANIPULATION` (`int`)  
Igual a 1 si la manipulación en tiempo de ejecución está activada, y 0 en caso contrario.

`RUNKIT7_FEATURE_SUPERGLOBALS` (`int`)  
Igual a 1 si las superglobales personalizadas están activadas, y 0 en caso contrario.

`RUNKIT7_FEATURE_SANDBOX` (`int`)  
Siempre 0, es impracticable implementar la funcionalidad de entorno de pruebas en php 7.
