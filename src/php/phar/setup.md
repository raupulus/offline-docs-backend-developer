---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/phar.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: 184f3f7bd
order: 64920
---

## Instalación/Configuración

## Requisitos

Puede ser deseable activar las extensiones [zlib](#book.zlib) y [bzip2](#book.bzip2) para aprovechar el soporte de archivos phar comprimidos. Asimismo, para utilizar las firmas OpenSSL, la extensión [OpenSSL](#book.openssl) debe ser activada.

Si [zend.multibyte](#ini.zend.multibyte) está activado, [zend.detect_unicode](#ini.zend.detect-unicode) también debe estar activado.

## Tipos de recursos

La extensión Phar proporciona el flujo `phar`, que permite el acceso de forma transparente a los ficheros contenidos en un phar. Para más información, consulte [el formato de archivo Phar](#phar.fileformat)
