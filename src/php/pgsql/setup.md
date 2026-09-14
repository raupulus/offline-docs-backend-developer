---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/pgsql.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 5f1a92089
order: 63860
---

## Instalación/Configuración

## Requisitos

Para utilizar el soporte PostgreSQL, se necesita libpq. A partir de PHP 8.0.0, se requiere libpq 9.1 o posterior. A partir de PHP 8.4.0, se requiere libpq 10.0 o posterior. PostgreSQL soporta numerosos juegos de caracteres, incluyendo los juegos multioctetos asiáticos. La versión actual y más detalles sobre PostgreSQL están disponibles en el sitio <http://www.postgresql.org/> y la [Documentación PostgreSQL](http://www.postgresql.org/docs/current/interactive/).

## Tipos de recursos

Antes de PHP 8.1.0, existían dos tipos de recursos utilizados en el módulo PostgreSQL. El primero es el identificador para la conexión a la base de datos y el segundo es un recurso que contiene el resultado de una consulta.
