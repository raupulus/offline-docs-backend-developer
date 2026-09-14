---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/mongodb.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51760
---

## Instalación/Configuración

## Requisitos

A partir de la versión 1.21.0, la extensión requiere PHP 8.1 o superior. Las versiones anteriores de la extensión permiten la compatibilidad con versiones más antiguas de PHP.

La extensión requiere [libbson](https://github.com/mongodb/mongo-c-driver/tree/master/src/libbson) y [libmongoc](https://github.com/mongodb/mongo-c-driver), y usará por omisión las versiones incluidas de ambas bibliotecas. También se pueden usar bibliotecas del sistema, como se explica en la documentación de [instalación manual](#mongodb.installation.manual).

La extensión, a través de libmongoc, depende opcionalmente de una biblioteca TLS (por ejemplo, OpenSSL) y la usará si está disponible. Si el proceso de compilación no logra encontrar una biblioteca TLS, los usuarios deben verificar que el paquete de desarrollo apropiado (por ejemplo, `libssl-dev`) y [pkg-config](https://en.wikipedia.org/wiki/Pkg-config) estén instalados. El proceso para detectar y configurar bibliotecas TLS se explica con más detalle en la documentación de [instalación manual](#mongodb.installation.manual).

[Cyrus SASL](http://cyrusimap.org/) es una dependencia opcional para admitir la autenticación Kerberos y se usará si está disponible.

> [!NOTE]
> Debido a posibles problemas para representar enteros de 64 bits en plataformas de 32 bits, se recomienda a los usuarios emplear entornos de 64 bits. Al usar una plataforma de 32 bits, tenga en cuenta que cualquier entero de 64 bits leído desde la base de datos se devolverá como una instancia de `MongoDB\BSON\Int64` en lugar de un tipo entero de PHP.
