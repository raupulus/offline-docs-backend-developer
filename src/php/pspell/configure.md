---
title: Instalación
source_url: https://www.php.net/manual/es/pspell.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 86177fa03
order: 66330
---

## Instalación

## PHP 8.4

Esta extensión ha sido movida al módulo [PECL](https://pecl.php.net/) y no será integrada en PHP a partir de PHP 8.4.0

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/pspell>.

## PHP \< 8.4

Para activar esta extensión, compílese PHP con la opción `--with-pspell[=dir]`.

> [!NOTE]
> Para hacer funcionar esta extensión, algunas bibliotecas DLL deben estar disponibles a través del `PATH` del sistema Windows. Lea la F.A.Q titulada "[Cómo agregar mi carpeta PHP a mi PATH de Windows](#faq.installation.addtopath)" para más información. Copiar las bibliotecas DLL desde la carpeta PHP a la carpeta del sistema de Windows también funciona (ya que la carpeta del sistema está por defecto en el `PATH` del sistema), pero este método no es recomendado. *Esta extensión requiere que los siguientes ficheros estén en el `PATH`:* `aspell-15.dll` desde la `carpeta bin` de la instalación de aspell.
>
> El soporte Win32 requiere al menos la versión 0.50 de aspell.
