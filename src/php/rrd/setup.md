---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/rrd.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72820
---

## Instalación/Configuración

## Requisitos

Es necesario instalar primero la biblioteca librrd para utilizar la extensión PECL/rrd. Verifique si su distribución favorita de Linux ofrece el paquete librrd-dev. PECL/rrd ha sido probado con librrd 1.4.3, las versiones anteriores o más recientes pueden o no funcionar.

> [!WARNING]
> Librrd y, por lo tanto, la extensión misma no son, en la mayoría de los casos, seguras para hilos. Existen muchos estados globales y compartidos en librrd. Puede ser peligroso utilizar esta extensión en entornos multihilo como Apache 2 mpm worker. Si existen varias peticiones en paralelo, una de ellas puede modificar el estado global de la biblioteca librrd, afectando así a las otras peticiones en ejecución.

## Instalación

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/rrd>.
