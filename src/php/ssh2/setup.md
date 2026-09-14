---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/ssh2.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_revision: 12f0e7220
order: 86770
---

## Instalación/Configuración

## Requisitos

Las librerías [OpenSSL](http://www.openssl.org/) y [libssh2](http://libssh2.org/) son obligatorias. Asegúrese que las librerías de desarrollo estan instaladas, donde el nombre típico del paquete podría ser `openssl-dev`.

Es necesaria la versión 1.2 o posterior de libssh2 , aunque es posible que nuevos lanzamientos de pecl/ssh2 pueden requerir versiones posteriores (consultar las notas de lanzamiento)

La función `ssh2_auth_agent` estará disponible únicamente con libssh \>= 1.2.3.

El soporte para `stream_set_timeout` para canalizar secuencias sólo estará disponible con libssh \>= 1.2.9.

libssh2 viene en dos versiones: gcrypt y openssl. Algunas distribuciones de Linux compilan libssh2 contra la librería gcrypt, y otras utilizan openssl. libssh2 tiene algunos problemas cuando se compila contra gcrypt, por favor, utilice openssl.

## Tipos de recursos

Esta extensión define los siguientes tipos de recursos: SSH2 Session, SSH2 Listener, SSH2 SFTP, SSH2 Publickey Subsystem (disponible a partir de ssh2 0.10)
