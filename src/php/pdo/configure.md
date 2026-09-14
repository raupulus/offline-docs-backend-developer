---
title: Instalación
source_url: https://www.php.net/manual/es/pdo.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_revision: 78cd8f0ba
order: 61740
---

## Instalación

Esta extensión está activada por defecto. Puede ser desactivada utilizando la opción de configuración: `--disable-pdo`

1.  PDO y el controlador [PDO_SQLITE](#ref.pdo-sqlite) están activados por defecto. Se debe activar el controlador PDO de la base de datos de su elección; consulte la documentación para los [controladores específicos de su base de datos](#pdo.drivers) para obtener más información.

    > [!NOTE]
    > Tenga en cuenta que al compilar PDO como extensión compartida (*no recomendado*), entonces todos los controladores PDO *deben* ser cargados *después* de cargar PDO.

2.  Al instalar PDO como módulo compartido, el archivo php.ini debe ser actualizado para cargar la extensión PDO automáticamente cuando PHP se inicie. Asimismo, se deben activar los controladores específicos de su base de datos; asegúrese de que estos controladores estén listados después de la línea extension=pdo, ya que PDO debe ser inicializado antes de cargar las extensiones específicas de las bases de datos. Si compila PDO y las extensiones relativas a las bases de datos de forma estática, puede omitir este paso.

        extension=pdo

            

<!-- -->

1.  PDO está activado por defecto. Seleccione los otros archivos DLL específicos de su base de datos y utilice la función `dl` para cargarlos en tiempo de ejecución o actívelos en el archivo `php.ini`. Por ejemplo, esto carga el controlador [PDO_SQLITE](#ref.pdo-sqlite) pero deja el controlador [PDO_ODBC](#ref.pdo-odbc) comentado:

        ;extension=pdo_odbc
        extension=pdo_sqlite

            

    Estas librerías DLL deben existir en el directorio del sistema [extension_dir](#ini.extension-dir).

> [!NOTE]
> Tenga en cuenta que después de modificar su `php.ini`, debe reiniciar PHP para que las nuevas directivas de configuración tengan efecto.
