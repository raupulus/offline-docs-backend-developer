---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/solr.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: f79fac8b3
order: 77110
---

## Instalación/Configuración

## Requisitos

Las extensiones libxml y curl deben activarse asimismo para disponibilizar la extensión Apache Solr.

Se requiere libxml2 en versión 2.6.31 y posteriores.

Se requiere libcurl en versión 7.18.0 y posteriores.

Las versiones de biblioteca mencionadas son necesarias y intentar modificar el código para compilar esta extensión con bibliotecas de versión diferente no se recomienda. Esto podría fallar con errores que podrían ser muy difíciles de depurar.

## Instalación

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/solr>.

Para obtener ayuda y soporte, visite el grupo google de la extensión. [Extensión Apache Solr PHP](https://groups.google.com/forum/#!forum/php-solr)

Los binarios Windows (los ficheros DLL) para esta extensión PECL están disponibles en el sitio web PECL.

> [!NOTE]
> El módulo Solr puede ser compilado en modo de depuración pasando la opción de configuración `--enable-solr-debug`.
>
> Durante una compilación manual, asegúrese de incluir el soporte curl y libxml.
