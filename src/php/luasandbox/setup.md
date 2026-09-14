---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/luasandbox.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 44190
---

## Instalación/Configuración

## Requisitos

Para utilizar esta extensión, Lua 5.1 debe estar instalado, disponible en la [página de inicio de Lua](http://www.lua.org/).

Para utilizar las funcionalidades de temporizador, LuaSandbox debe estar instalado en Linux.

Si se utiliza FreeBSD o Mac OS X, solo se soporta el tiempo real (reloj de pared), las funciones que pretenden devolver el tiempo de CPU devolverán en realidad el tiempo del reloj de pared.

Si se utiliza Windows, ninguna función de temporizador será soportada. Los límites de tiempo serán inoperantes.

## Instalación

Esta extensión [PECL](https://pecl.php.net/) no está integrada en PHP.

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/luasandbox>.

Si el sistema operativo es Debian 10 o más reciente, o Ubuntu 18.04 o más reciente, entonces LuaSandbox debería ser típicamente instalado desde el paquete `php-luasandbox`:

    sudo apt-get install php-luasandbox
