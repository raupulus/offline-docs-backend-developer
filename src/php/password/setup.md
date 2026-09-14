---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/password.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/password/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: password
translation_status: ready
translation_revision: 2417d61a2
order: 61140
---

## Instalación/Configuración

## Requisitos

No se requiere ninguna biblioteca externa para compilar esta extensión.

Para el hachado de contraseñas Argon2, debe estar disponible [libargon2](https://github.com/P-H-C/phc-winner-argon2) o, a partir de PHP 8.4.0, la versión OpenSSL 3.2 o superior. A partir de PHP 7.3.0, se requiere la versión 20161029 o superior de libargon2 si se utiliza libargon2.

## Instalación

No hay instalación necesaria para usar estas funciones, son parte del núcleo de PHP.

Sin embargo, para activar el hachado de contraseñas Argon2, PHP debe ser compilado con soporte para libargon2 utilizando la opción de configuración `--with-password-argon2` o, a partir de PHP 8.4.0, con OpenSSL utilizando `--with-openssl` y `--with-openssl-argon2`.

Anterior a PHP 8.1.0, era posible especificar el directorio argon2 con `--with-password-argon2[=DIR]`.
