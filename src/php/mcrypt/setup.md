---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/mcrypt.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 46030
---

## Instalación/Configuración

## Requisitos

Estas funciones utilizan [mcrypt](http://mcrypt.sourceforge.net/). Para utilizar esta biblioteca, descargue el fichero `libmcrypt-x.x.tar.gz` desde <http://mcrypt.sourceforge.net/> y siga las instrucciones de instalación proporcionadas.

Se requiere la versión 2.5.6 o posterior de la biblioteca libmcrypt.

Los usuarios de Windows encontrarán la biblioteca en la versión Windows de PHP 5.3. La versión binaria de Windows de PHP 5.3 utiliza la versión estática de la biblioteca MCrypt, no se necesita ninguna DLL.

Si se compila PHP con la biblioteca `libmcrypt 2.4.x`, se admiten los siguientes algoritmos: `"CAST"`, `"LOKI97"`, `"RIJNDAEL"`, `"SAFERPLUS"`, `"SERPENT"` así como los siguientes cifrados: `"ENIGMA"` (cifrado), `"PANAMA"`, `"RC4"` y `"WAKE"`. Con `libmcrypt 2.4.x` otro modo de cifrado está disponible: `"nOFB"`.

## Tipos de recursos

`mcrypt_module_open` devuelve un puntero de cifrado.
