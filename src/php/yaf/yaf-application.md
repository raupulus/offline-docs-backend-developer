---
title: La clase Yaf_Application
source_url: https://www.php.net/manual/es/class.yaf-application.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf-application.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 104530
---

## Introducción

`Yaf_Application` proporciona una característica de arranque de aplicaciones que provee de recursos reusables, clases de arranque comunes y basadas en módulos y verificación de dependencia.

> [!NOTE]
> `Yaf_Application` implementa el patrón singleton, y `Yaf_Application` no puede ser serializada o deserializada, lo que causará problemas al intentar usar PHPUnit para escribir algún caso de prueba para Yaf.
>
> Se puede usar la anotación @backupGlobals de PHPUnit para controlar las operaciones de copia de respaldo y restauración de variables globales. De este modo se puede solucionar este problema.

## Sinopsis de la clase

Yaf_Application

final

Yaf_Application

Propiedades

protected

config

protected

dispatcher

protected

static

\_app

protected

\_modules

protected

\_running

protected

\_environ

Métodos

## Propiedades

`config`  

`dispatcher`  

`_app`  

`_modules`  

`_running`  

`_environ`
