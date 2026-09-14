---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/ldap.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43620
---

## Instalación/Configuración

## Requisitos

Es necesario descargar y compilar las bibliotecas clientes LDAP desde [OpenLDAP](https://www.openldap.org/software/download/) o [Bind9.net](http://www.bind9.net/download-openldap/) para asegurar el soporte LDAP. Para PHP 5.6 o versiones posteriores, se requiere OpenLDAP 2.4 o versiones posteriores.

## Tipos de recursos

Antes de PHP 8.1.0, la mayoría de las funciones LDAP operan sobre recursos devueltos por las funciones LDAP (por ejemplo, `ldap_connect` devuelve un identificador de enlace LDAP positivo requerido por varias funciones LDAP).
