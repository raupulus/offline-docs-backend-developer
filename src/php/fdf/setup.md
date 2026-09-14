---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/fdf.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22700
---

## Instalación/Configuración

## Requisitos

Se necesitará el SDK de FDF toolkit, disponible en el sitio <http://www.adobe.com/devnet/acrobat/fdftoolkit.html>. Desde PHP 4.3.0, se necesitará la versión 5.0 del SDK. La biblioteca FDF toolkit está disponible como una biblioteca compilada, editada por Adobe, en los sistemas operativos Win32, Linux, Solaris y AIX.

## Tipos de recursos

La mayoría de las funciones FDF requieren un recurso de tipo `fdf` como primer argumento. Un recurso `fdf` es una estructura que representa un fichero FDF abierto. Se pueden crear recursos `fdf` con las funciones `fdf_create`, `fdf_open` y `fdf_open_string`.
