---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/mysql.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_reviewed: true
translation_revision: 15d88bef8
order: 52520
---

## Instalación/Configuración

## Requisitos

Para poder utilizarlos, es necesario compilar PHP con el soporte MySQL.

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:

## Tipos de recursos

Existen dos tipos de recursos utilizados por el módulo MySQL. El primero es un identificador de conexión al servidor, denominado `mysql link`, y el segundo es un identificador de resultado de consulta, denominado `mysql result`.
