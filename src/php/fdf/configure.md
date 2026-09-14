---
title: Instalación
source_url: https://www.php.net/manual/es/fdf.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22320
---

## Instalación

Esta extensión es considerada no mantenida y muerta. Sin embargo, el código fuente sigue disponible desde el SVN de PECL aquí: <https://svn.php.net/viewvc/pecl/fdf>.

Esta extensión ya no se proporciona con PHP.

> [!NOTE]
> Si se encuentran problemas durante la configuración de FDF con soporte fdftk, verifique que el fichero de encabezado `fdftk.h` y la biblioteca `libfdftk.so` estén en su lugar. El script `configure` soporta la jerarquía de directorios de la distribución FDF SDK y la organización clásica `DIR/include` y `DIR/lib`: por lo tanto, se puede utilizar uno u otro directamente con la distribución descomprimida, o bien incluyendo el fichero de encabezado y la biblioteca apropiada en su sistema, es decir, en `/usr/local/include` y `/usr/local/lib`. Solo queda configurar con `--with-fdftk=/usr/local`.

> [!NOTE]
> Para hacer funcionar esta extensión, algunas bibliotecas DLL deben estar disponibles a través del `PATH` del sistema Windows. Lea la F.A.Q titulada "[Cómo agregar mi carpeta PHP a mi PATH de Windows](#faq.installation.addtopath)" para más información. Copiar las bibliotecas DLL desde la carpeta PHP a la carpeta del sistema de Windows también funciona (ya que la carpeta del sistema está por defecto en el `PATH` del sistema), pero este método no es recomendado. *Esta extensión requiere que los siguientes ficheros estén en el `PATH`:* `fdftk.dll`
