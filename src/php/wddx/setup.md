---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/wddx.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wddx/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wddx
translation_status: ready
translation_revision: 765b2d6ee
order: 101260
---

## Instalación/Configuración

## Requisitos

Esta extensión requiere la extensión PHP [libxml](#book.libxml). Esto significa pasar la opción de configuración `--with-libxml`, o anterior a PHP 7.4 la opción de configuración `--enable-libxml`, aunque esto se realiza implícitamente ya que libxml está activado por defecto.

Para utilizar WDDX, es necesario instalar la biblioteca expat (que se proporciona con Apache 1.3.7 o superior).

## Tipos de recursos

Esta extensión define un identificador de paquete WDDX, devuelto por la función `wddx_packet_start`.
