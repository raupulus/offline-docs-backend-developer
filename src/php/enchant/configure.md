---
title: Instalación
source_url: https://www.php.net/manual/es/enchant.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17280
---

## Instalación

Partiendo del principio de que las [bibliotecas requeridas](#enchant.requirements) están instaladas, los usuarios pueden activar enchant añadiendo la opción `--with-enchant[=dir]` durante la compilación de PHP.

Los usuarios de Windows deben activar `php_enchant.dll` para poder utilizar esta extensión.

> [!NOTE]
> Para hacer funcionar esta extensión, algunas bibliotecas DLL deben estar disponibles a través del `PATH` del sistema Windows. Lea la F.A.Q titulada "[Cómo agregar mi carpeta PHP a mi PATH de Windows](#faq.installation.addtopath)" para más información. Copiar las bibliotecas DLL desde la carpeta PHP a la carpeta del sistema de Windows también funciona (ya que la carpeta del sistema está por defecto en el `PATH` del sistema), pero este método no es recomendado. *Esta extensión requiere que los siguientes ficheros estén en el `PATH`:* `libenchant.dll`, `glib-2.dll`, `gmodule-2.dll`.
>
> Además, es necesario copiar al menos uno de los proveedores proporcionados en `lib\enchant` hacia `\usr\local\lib\enchant-2`, (que es una ruta absoluta a partir de la raíz del *disco actual*). Anterior a PHP 8.0.0, es decir, utilizando Enchant v1, los proveedores debían copiarse en `C:\enchant_plugins` en su lugar, donde esta ruta podía ser personalizada creando el valor de registro `HKEY_CURRENT_USER\SOFTWARE\Enchant\Config\Module_Dir` y estableciéndola en la ruta deseada.
