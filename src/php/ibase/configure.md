---
title: Instalación
source_url: https://www.php.net/manual/es/ibase.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 29600
---

## Instalación

Esta extensión ha sido movida al módulo [PECL](https://pecl.php.net/) y no será integrada en PHP a partir de PHP 7.4.0

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://github.com/FirebirdSQL/php-firebird>.

Para activar el soporte de Firebird/InterBase, es necesario compilar PHP con la opción `--with-interbase[=DIR]`, donde DIR es el directorio de instalación de Firebird/InterBase (que por omisión es `/usr`).

> [!NOTE]
> Para hacer funcionar esta extensión, algunas bibliotecas DLL deben estar disponibles a través del `PATH` del sistema Windows. Lea la F.A.Q titulada "[Cómo agregar mi carpeta PHP a mi PATH de Windows](#faq.installation.addtopath)" para más información. Copiar las bibliotecas DLL desde la carpeta PHP a la carpeta del sistema de Windows también funciona (ya que la carpeta del sistema está por defecto en el `PATH` del sistema), pero este método no es recomendado. *Esta extensión requiere que los siguientes ficheros estén en el `PATH`:* `fbclient.dll,gds32.dll`
>
> Si se instala un servidor Firebird/InterBase en la misma máquina que la que ejecuta PHP, ya se tendrá esta biblioteca y `fbclient.dll,gds32.dll` (gds32.dll se genera desde el instalador) debería estar ya en su `PATH`.
