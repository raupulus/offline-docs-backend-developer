---
title: Instalación
source_url: https://www.php.net/manual/es/mysqlnd.install.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqlnd/install.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqlnd
translation_status: ready
translation_reviewed: false
translation_revision: 9598935f2
order: 56140
---

## Instalación

**Instalación bajo Unix**

Para utilizar el controlador nativo MySQL, PHP debe ser compilado especificando explícitamente que las extensiones de base de datos MySQL deben ser compiladas en relación con él. Esto se realiza mediante las opciones de configuración anteriores a la compilación de PHP en sí.

Por ejemplo, para compilar la extensión MySQL, `mysqli` y PDO MySQL utilizando el controlador nativo MySQL, la siguiente orden debe ser ejecutada:

```php
 ./configure --with-mysql=mysqlnd \
--with-mysqli=mysqlnd \
--with-pdo-mysql=mysqlnd \
[otras opciones]

 
```

**Instalación bajo Windows**

En las distribuciones oficiales de PHP para Windows, el controlador nativo MySQL está activado por defecto y no se requiere configuración adicional para su uso. Todas las extensiones de base de datos MySQL lo utilizarán entonces.

**Soporte del plugin de autenticación SHA-256**

El driver nativo MySQL requiere la carga de la funcionalidad OpenSSL de PHP, y la activación de la conexión a MySQL mediante cuentas que utilizan el plugin de autenticación MySQL SHA-256. Por ejemplo, PHP podría ser configurado utilizando la siguiente orden:

```php
./configure --with-mysql=mysqlnd \
--with-mysqli=mysqlnd \
--with-pdo-mysql=mysqlnd \
--with-openssl
[otras opciones]

 
```

En Autotools, el soporte SSL extendido en `mysqlnd` es activado implícitamente durante la compilación con la extensión `openssl` utilizando la opción de configuración `--with-openssl`. Durante la compilación sin la extensión `openssl`, la opción de configuración `--with-mysqlnd-ssl` puede ser utilizada para activar explícitamente el soporte SSL extendido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | La opción de configuración Autotools `--with-mysqlnd-ssl` fue añadida para activar explícitamente el soporte SSL extendido durante la compilación sin la extensión `openssl`. |
