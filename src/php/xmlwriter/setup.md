---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/xmlwriter.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_reviewed: false
translation_revision: 765b2d6ee
order: 103540
---

## Instalación/Configuración

## Requisitos

Esta extensión requiere la extensión PHP [libxml](#book.libxml). Esto significa pasar la opción de configuración `--with-libxml`, o anterior a PHP 7.4 la opción de configuración `--enable-libxml`, aunque esto se realiza implícitamente ya que libxml está activado por defecto.

## Instalación

XMLWriter se envía con el código fuente de PHP. Esta extensión está activada por defecto. Puede ser desactivada utilizando la opción de configuración: `--disable-xmlwriter`

## Tipos de recursos

Antes de PHP 8.0.0, había un tipo de recurso utilizado por la versión procedimental de XMLWriter: el devuelto por `xmlwriter_open_memory` o `xmlwriter_open_uri`.
