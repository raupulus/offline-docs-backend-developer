---
title: Instalación
source_url: https://www.php.net/manual/es/ldap.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 30dd50ff8
order: 42920
---

## Instalación

El soporte LDAP de PHP no está activado por omisión. Se debe utilizar la opción de configuración `--with-ldap[=DIR]` al compilar PHP, donde DIR es el directorio de instalación del servidor LDAP. Para activar el soporte SASL, asegúrese de que la opción de configuración `--with-ldap-sasl[=DIR]` sea utilizada y que el fichero `sasl.h` exista en el sistema.

> [!NOTE]
> Para hacer funcionar esta extensión, algunas bibliotecas DLL deben estar disponibles a través del `PATH` del sistema Windows. Lea la F.A.Q titulada "[Cómo agregar mi carpeta PHP a mi PATH de Windows](#faq.installation.addtopath)" para más información. Copiar las bibliotecas DLL desde la carpeta PHP a la carpeta del sistema de Windows también funciona (ya que la carpeta del sistema está por defecto en el `PATH` del sistema), pero este método no es recomendado. *Esta extensión requiere que los siguientes ficheros estén en el `PATH`:* `libeay32.dll` y `ssleay32.dll`, o, desde OpenSSL 1.1 `libcrypto-*.dll` y `libssl-*.dll`

Para poder utilizar las bibliotecas Oracle LDAP, un [entorno Oracle](#oci8.requirements) adecuado debe ser definido.
