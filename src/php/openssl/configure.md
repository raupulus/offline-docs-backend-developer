---
title: Instalación
source_url: https://www.php.net/manual/es/openssl.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: badd30777
order: 58970
---

## Instalación

Para utilizar el soporte OpenSSL de PHP, también debe compilarse PHP con la opción de configuración `--with-openssl`.

La biblioteca OpenSSL también posee dependencias en tiempo de ejecución. Por ejemplo, OpenSSL necesita acceder a un generador de números pseudo-aleatorios; en la mayoría de las plataformas Unix (incluyendo Linux), debe tener acceso al dispositivo `/dev/urandom` o `/dev/random`.

La opción de configuración `--with-system-ciphers` está disponible que hace que PHP utilice la lista de cifrado del sistema en lugar de los valores por omisión codificados en el programa.

> [!NOTE]
> Para hacer funcionar esta extensión, algunas bibliotecas DLL deben estar disponibles a través del `PATH` del sistema Windows. Lea la F.A.Q titulada "[Cómo agregar mi carpeta PHP a mi PATH de Windows](#faq.installation.addtopath)" para más información. Copiar las bibliotecas DLL desde la carpeta PHP a la carpeta del sistema de Windows también funciona (ya que la carpeta del sistema está por defecto en el `PATH` del sistema), pero este método no es recomendado. *Esta extensión requiere que los siguientes ficheros estén en el `PATH`:* `libeay32.dll`, o, a partir de OpenSSL 1.1, `libcrypto-*.dll`
>
> Además, si se ha previsto utilizar las funciones relativas a la generación de claves y a los certificados, debe instalarse un fichero `openssl.cnf` válido en el sistema. Un fichero de configuración básico está incluido en las distribuciones de PHP para win32 en el directorio `extras/ssl`.
>
> PHP buscará el fichero `openssl.cnf` siguiendo la siguiente táctica:
>
> - La variable de entorno `OPENSSL_CONF`, si está definida, será utilizada como ruta (incluyendo el fichero) hacia el fichero de configuración.
>
> - La variable de entorno `SSLEAY_CONF`, si está definida, será utilizada como ruta (incluyendo el fichero) hacia el fichero de configuración.
>
> - El fichero `openssl.cnf` se supondrá que se encuentra en el directorio de certificados, tal como se configuró durante la compilación de la biblioteca openssl. Esto significa generalmente `C:\Program Files\Common Files\SSL\openssl.cnf` (x64) o `C:\Program Files (x86)\Common Files\SSL\openssl.cnf` (x86), o, antes de PHP 7.4.0, `c:\usr\local\ssl\openssl.cnf`.
>
> En su instalación, deberá decidirse si se va a instalar el fichero de configuración en la ruta por omisión o si se va a hacer en otro lugar y configurar una variable de entorno (posiblemente por sitio virtual). Tenga en cuenta que es posible reemplazar la ruta por omisión utilizando el parámetro `options` de las funciones que requieren un fichero de configuración.
>
> > [!CAUTION]
> > Asegúrese de que los usuarios no privilegiados no estén autorizados a modificar `openssl.cnf`.
>
> A partir de OpenSSL 3.0.0, que se utiliza por omisión en Windows desde PHP 8.2.0, varios algoritmos han sido considerados obsoletos. Estos algoritmos suelen haber caído en desuso, han sido considerados no seguros por la comunidad criptográfica, o algo similar. Estos algoritmos siguen disponibles a través del proveedor de algoritmos legacy (`extras/ssl/legacy.dll`) ; su utilización se describe en la sección [configuración del proveedor](https://docs.openssl.org/master/man5/config/#Provider-Configuration) del manual OpenSSL.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | La opción `--with-openssl[=DIR]` ya no acepta argumentos de directorio en favor del ajuste de la variable pkg-config `PKG_CONFIG_PATH` hacia la ubicación de OpenSSL, o especificando las variables `OPENSSL_LIBS` y `OPENSSL_CFLAGS`. |
| La ruta de configuración por omisión de OpenSSL ha sido modificada de `C:\usr\local\ssl` a `C:\Program Files\Common Files\SSL` y `C:\Program Files (x86)\Common Files\SSL`, respectivamente. |  |
