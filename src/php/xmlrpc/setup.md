---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/xmlrpc.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlrpc/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlrpc
translation_status: ready
translation_reviewed: false
translation_revision: 765b2d6ee
order: 103520
---

## Instalación/Configuración

## Requisitos

Esta extensión requiere la extensión PHP [libxml](#book.libxml). Esto significa pasar la opción de configuración `--with-libxml`, o anterior a PHP 7.4 la opción de configuración `--enable-libxml`, aunque esto se realiza implícitamente ya que libxml está activado por defecto.

## Tipos de recursos

Ésta extensión define un recurso de servicio de XML-RPC devuelto por `xmlrpc_server_create`.
