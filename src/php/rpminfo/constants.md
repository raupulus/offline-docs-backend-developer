---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/rpminfo.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rpminfo/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rpminfo
translation_status: ready
translation_reviewed: true
translation_revision: 1177b7275
order: 72420
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`RPMVERSION` (`string`)  
La versión de la biblioteca RPM.

<!-- -->

`RPMSENSE_ANY` (`int`)  

`RPMSENSE_LESS` (`int`)  

`RPMSENSE_GREATER` (`int`)  

`RPMSENSE_EQUAL` (`int`)  

`RPMSENSE_POSTTRANS` (`int`)  

`RPMSENSE_PREREQ` (`int`)  

`RPMSENSE_PRETRANS` (`int`)  

`RPMSENSE_INTERP` (`int`)  

`RPMSENSE_SCRIPT_PRE` (`int`)  

`RPMSENSE_SCRIPT_POST` (`int`)  

`RPMSENSE_SCRIPT_PREUN` (`int`)  

`RPMSENSE_SCRIPT_POSTUN` (`int`)  

`RPMSENSE_SCRIPT_VERIFY` (`int`)  

`RPMSENSE_FIND_REQUIRES` (`int`)  

`RPMSENSE_FIND_PROVIDES` (`int`)  

`RPMSENSE_TRIGGERIN` (`int`)  

`RPMSENSE_TRIGGERUN` (`int`)  

`RPMSENSE_TRIGGERPOSTUN` (`int`)  

`RPMSENSE_MISSINGOK` (`int`)  

`RPMSENSE_RPMLIB` (`int`)  

`RPMSENSE_TRIGGERPREIN` (`int`)  

`RPMSENSE_KEYRING` (`int`)  

`RPMSENSE_CONFIG` (`int`)  

<!-- -->

`RPMMIRE_DEFAULT` (`int`)  
Modelo de búsqueda en una expresión regular con `\.`, `.*`, y `^...$` añadidos.

`RPMMIRE_STRCMP` (`int`)  
El modelo de búsqueda es una `string`, utilizando `strcmp(3)`.

`RPMMIRE_REGEX` (`int`)  
El modelo de búsqueda es una expresión regular, utilizando `regcomp(3)`.

`RPMMIRE_GLOB` (`int`)  
El modelo de búsqueda es una expresión global, utilizando `fnmatch(3)`.

<!-- -->

`RPMTAG_ARCH` (`int`)  

`RPMTAG_ARCHSUFFIX` (`int`)  
Requiere librpm \>= 4.18

`RPMTAG_ARCHIVESIZE` (`int`)  

`RPMTAG_BASENAMES` (`int`)  
El nombre (no la ruta) de los ficheros, con el índice de la base de datos.

`RPMTAG_BUGURL` (`int`)  

`RPMTAG_BUILDARCHS` (`int`)  

`RPMTAG_BUILDHOST` (`int`)  

`RPMTAG_BUILDTIME` (`int`)  

`RPMTAG_C` (`int`)  

`RPMTAG_CHANGELOGNAME` (`int`)  

`RPMTAG_CHANGELOGTEXT` (`int`)  

`RPMTAG_CHANGELOGTIME` (`int`)  

`RPMTAG_CLASSDICT` (`int`)  

`RPMTAG_CONFLICTFLAGS` (`int`)  

`RPMTAG_CONFLICTNAME` (`int`)  
Dependencias conflictivas, con el índice de la base de datos.

`RPMTAG_CONFLICTNEVRS` (`int`)  

`RPMTAG_CONFLICTS` (`int`)  

`RPMTAG_CONFLICTVERSION` (`int`)  

`RPMTAG_COOKIE` (`int`)  

`RPMTAG_DBINSTANCE` (`int`)  

`RPMTAG_DEPENDSDICT` (`int`)  

`RPMTAG_DESCRIPTION` (`int`)  

`RPMTAG_DIRINDEXES` (`int`)  

`RPMTAG_DIRNAMES` (`int`)  
El directorio de los ficheros, con el índice de la base de datos.

`RPMTAG_DISTRIBUTION` (`int`)  

`RPMTAG_DISTTAG` (`int`)  

`RPMTAG_DISTURL` (`int`)  

`RPMTAG_DSAHEADER` (`int`)  

`RPMTAG_E` (`int`)  

`RPMTAG_ENCODING` (`int`)  

`RPMTAG_ENHANCEFLAGS` (`int`)  

`RPMTAG_ENHANCENAME` (`int`)  
Dependencia débil, con el índice de la base de datos, requiere librpm \>= 4.13.

`RPMTAG_ENHANCENEVRS` (`int`)  

`RPMTAG_ENHANCES` (`int`)  

`RPMTAG_ENHANCEVERSION` (`int`)  

`RPMTAG_EPOCH` (`int`)  

`RPMTAG_EPOCHNUM` (`int`)  

`RPMTAG_EVR` (`int`)  

`RPMTAG_EXCLUDEARCH` (`int`)  

`RPMTAG_EXCLUDEOS` (`int`)  

`RPMTAG_EXCLUSIVEARCH` (`int`)  

`RPMTAG_EXCLUSIVEOS` (`int`)  

`RPMTAG_FILECAPS` (`int`)  

`RPMTAG_FILECLASS` (`int`)  

`RPMTAG_FILECOLORS` (`int`)  

`RPMTAG_FILECONTEXTS` (`int`)  

`RPMTAG_FILEDEPENDSN` (`int`)  

`RPMTAG_FILEDEPENDSX` (`int`)  

`RPMTAG_FILEDEVICES` (`int`)  

`RPMTAG_FILEDIGESTALGO` (`int`)  

`RPMTAG_FILEDIGESTS` (`int`)  

`RPMTAG_FILEFLAGS` (`int`)  

`RPMTAG_FILEGROUPNAME` (`int`)  

`RPMTAG_FILEINODES` (`int`)  

`RPMTAG_FILELANGS` (`int`)  

`RPMTAG_FILELINKTOS` (`int`)  

`RPMTAG_FILEMD5S` (`int`)  

`RPMTAG_FILEMODES` (`int`)  

`RPMTAG_FILEMTIMES` (`int`)  

`RPMTAG_FILENAMES` (`int`)  

`RPMTAG_FILENLINKS` (`int`)  

`RPMTAG_FILEPROVIDE` (`int`)  

`RPMTAG_FILERDEVS` (`int`)  

`RPMTAG_FILEREQUIRE` (`int`)  

`RPMTAG_FILESIGNATURELENGTH` (`int`)  

`RPMTAG_FILESIGNATURES` (`int`)  

`RPMTAG_FILESIZES` (`int`)  

`RPMTAG_FILESTATES` (`int`)  

`RPMTAG_FILETRIGGERCONDS` (`int`)  

`RPMTAG_FILETRIGGERFLAGS` (`int`)  

`RPMTAG_FILETRIGGERINDEX` (`int`)  

`RPMTAG_FILETRIGGERNAME` (`int`)  
El nombre del fichero desencadenante, con el índice de la base de datos, requiere librpm \>= 4.13.

`RPMTAG_FILETRIGGERPRIORITIES` (`int`)  

`RPMTAG_FILETRIGGERSCRIPTFLAGS` (`int`)  

`RPMTAG_FILETRIGGERSCRIPTPROG` (`int`)  

`RPMTAG_FILETRIGGERSCRIPTS` (`int`)  

`RPMTAG_FILETRIGGERTYPE` (`int`)  

`RPMTAG_FILETRIGGERVERSION` (`int`)  

`RPMTAG_FILEUSERNAME` (`int`)  

`RPMTAG_FILEVERIFYFLAGS` (`int`)  

`RPMTAG_FSCONTEXTS` (`int`)  

`RPMTAG_GIF` (`int`)  

`RPMTAG_GROUP` (`int`)  
El grupo de paquete, con el índice de la base de datos.

`RPMTAG_HDRID` (`int`)  
Obsoleto, utilizar `RPMTAG_SHA1HEADER` en su lugar. Eliminado en librpm 6.

`RPMTAG_HEADERCOLOR` (`int`)  

`RPMTAG_HEADERI18NTABLE` (`int`)  

`RPMTAG_HEADERIMAGE` (`int`)  

`RPMTAG_HEADERIMMUTABLE` (`int`)  

`RPMTAG_HEADERREGIONS` (`int`)  

`RPMTAG_HEADERSIGNATURES` (`int`)  

`RPMTAG_ICON` (`int`)  

`RPMTAG_INSTALLCOLOR` (`int`)  

`RPMTAG_INSTALLTID` (`int`)  
El identificador de transacción de instalación, con el índice de la base de datos.

`RPMTAG_INSTALLTIME` (`int`)  

`RPMTAG_INSTFILENAMES` (`int`)  
La ruta de los ficheros, con el índice de la base de datos.

`RPMTAG_INSTPREFIXES` (`int`)  

`RPMTAG_LICENSE` (`int`)  

`RPMTAG_LONGARCHIVESIZE` (`int`)  

`RPMTAG_LONGFILESIZES` (`int`)  

`RPMTAG_LONGSIGSIZE` (`int`)  

`RPMTAG_LONGSIZE` (`int`)  

`RPMTAG_MODULARITYLABEL` (`int`)  

`RPMTAG_N` (`int`)  

`RPMTAG_NAME` (`int`)  
El nombre del paquete, con el índice de la base de datos.

`RPMTAG_NEVR` (`int`)  

`RPMTAG_NEVRA` (`int`)  

`RPMTAG_NOPATCH` (`int`)  

`RPMTAG_NOSOURCE` (`int`)  

`RPMTAG_NVR` (`int`)  

`RPMTAG_NVRA` (`int`)  

`RPMTAG_O` (`int`)  

`RPMTAG_OBSOLETEFLAGS` (`int`)  

`RPMTAG_OBSOLETENAME` (`int`)  
Paquete obsoleto, con el índice de la base de datos.

`RPMTAG_OBSOLETENEVRS` (`int`)  

`RPMTAG_OBSOLETES` (`int`)  

`RPMTAG_OBSOLETEVERSION` (`int`)  

`RPMTAG_OLDENHANCES` (`int`)  

`RPMTAG_OLDENHANCESFLAGS` (`int`)  

`RPMTAG_OLDENHANCESNAME` (`int`)  

`RPMTAG_OLDENHANCESVERSION` (`int`)  

`RPMTAG_OLDFILENAMES` (`int`)  

`RPMTAG_OLDSUGGESTS` (`int`)  

`RPMTAG_OLDSUGGESTSFLAGS` (`int`)  

`RPMTAG_OLDSUGGESTSNAME` (`int`)  

`RPMTAG_OLDSUGGESTSVERSION` (`int`)  

`RPMTAG_OPTFLAGS` (`int`)  

`RPMTAG_ORDERFLAGS` (`int`)  

`RPMTAG_ORDERNAME` (`int`)  

`RPMTAG_ORDERVERSION` (`int`)  

`RPMTAG_ORIGBASENAMES` (`int`)  

`RPMTAG_ORIGDIRINDEXES` (`int`)  

`RPMTAG_ORIGDIRNAMES` (`int`)  

`RPMTAG_ORIGFILENAMES` (`int`)  

`RPMTAG_OS` (`int`)  

`RPMTAG_P` (`int`)  

`RPMTAG_PACKAGER` (`int`)  

`RPMTAG_PATCH` (`int`)  

`RPMTAG_PATCHESFLAGS` (`int`)  

`RPMTAG_PATCHESNAME` (`int`)  

`RPMTAG_PATCHESVERSION` (`int`)  

`RPMTAG_PAYLOADCOMPRESSOR` (`int`)  

`RPMTAG_PAYLOADDIGEST` (`int`)  

`RPMTAG_PAYLOADDIGESTALT` (`int`)  
Con librpm \>= 4.16.

`RPMTAG_PAYLOADDIGESTALGO` (`int`)  

`RPMTAG_PAYLOADFLAGS` (`int`)  

`RPMTAG_PAYLOADFORMAT` (`int`)  

`RPMTAG_PKGID` (`int`)  
Obsoleto, utilizar `RPMTAG_SIGMD5` en su lugar. Eliminado en librpm 6.

`RPMTAG_PLATFORM` (`int`)  

`RPMTAG_POLICIES` (`int`)  

`RPMTAG_POLICYFLAGS` (`int`)  

`RPMTAG_POLICYNAMES` (`int`)  

`RPMTAG_POLICYTYPES` (`int`)  

`RPMTAG_POLICYTYPESINDEXES` (`int`)  

`RPMTAG_POSTIN` (`int`)  

`RPMTAG_POSTINFLAGS` (`int`)  

`RPMTAG_POSTINPROG` (`int`)  

`RPMTAG_POSTTRANS` (`int`)  

`RPMTAG_POSTTRANSFLAGS` (`int`)  

`RPMTAG_POSTTRANSPROG` (`int`)  

`RPMTAG_POSTUN` (`int`)  

`RPMTAG_POSTUNFLAGS` (`int`)  

`RPMTAG_POSTUNPROG` (`int`)  

`RPMTAG_POSTUNTRANS` (`int`)  
Requiere librpm \>= 4.19

`RPMTAG_POSTUNTRANSFLAGS` (`int`)  
Requiere librpm \>= 4.19

`RPMTAG_POSTUNTRANSPROG` (`int`)  
Requiere librpm \>= 4.19

`RPMTAG_PREFIXES` (`int`)  

`RPMTAG_PREIN` (`int`)  

`RPMTAG_PREINFLAGS` (`int`)  

`RPMTAG_PREINPROG` (`int`)  

`RPMTAG_PRETRANS` (`int`)  

`RPMTAG_PRETRANSFLAGS` (`int`)  

`RPMTAG_PRETRANSPROG` (`int`)  

`RPMTAG_PREUN` (`int`)  

`RPMTAG_PREUNFLAGS` (`int`)  

`RPMTAG_PREUNPROG` (`int`)  

`RPMTAG_PREUNTRANS` (`int`)  
Requiere librpm \>= 4.19

`RPMTAG_PREUNTRANSFLAGS` (`int`)  
Requiere librpm \>= 4.19

`RPMTAG_PREUNTRANSPROG` (`int`)  
Requiere librpm \>= 4.19

`RPMTAG_PROVIDEFLAGS` (`int`)  

`RPMTAG_PROVIDENAME` (`int`)  
Las dependencias proporcionadas, con el índice de la base de datos.

`RPMTAG_PROVIDENEVRS` (`int`)  

`RPMTAG_PROVIDES` (`int`)  

`RPMTAG_PROVIDEVERSION` (`int`)  

`RPMTAG_PUBKEYS` (`int`)  

`RPMTAG_R` (`int`)  

`RPMTAG_RECOMMENDFLAGS` (`int`)  

`RPMTAG_RECOMMENDNAME` (`int`)  
Las dependencias débiles recomendadas, con el índice de la base de datos, requiere librpm \>= 4.13.

`RPMTAG_RECOMMENDNEVRS` (`int`)  

`RPMTAG_RECOMMENDS` (`int`)  

`RPMTAG_RECOMMENDVERSION` (`int`)  

`RPMTAG_RECONTEXTS` (`int`)  

`RPMTAG_RELEASE` (`int`)  

`RPMTAG_REMOVETID` (`int`)  

`RPMTAG_REQUIREFLAGS` (`int`)  

`RPMTAG_REQUIRENAME` (`int`)  
Las dependencias requeridas, con el índice de la base de datos.

`RPMTAG_REQUIRENEVRS` (`int`)  

`RPMTAG_REQUIRES` (`int`)  

`RPMTAG_REQUIREVERSION` (`int`)  

`RPMTAG_RPMVERSION` (`int`)  

`RPMTAG_RSAHEADER` (`int`)  

`RPMTAG_SHA1HEADER` (`int`)  
La firma SHA1, con el índice de la base de datos.

`RPMTAG_SHA256HEADER` (`int`)  

`RPMTAG_SIGGPG` (`int`)  

`RPMTAG_SIGMD5` (`int`)  
La firma MD5, con el índice de la base de datos.

`RPMTAG_SIGPGP` (`int`)  

`RPMTAG_SIGSIZE` (`int`)  

`RPMTAG_SIZE` (`int`)  

`RPMTAG_SOURCE` (`int`)  

`RPMTAG_SOURCEPACKAGE` (`int`)  

`RPMTAG_SOURCEPKGID` (`int`)  

`RPMTAG_SOURCERPM` (`int`)  

`RPMTAG_SPEC` (`int`)  
Requiere librpm \>= 4.18

`RPMTAG_SUGGESTFLAGS` (`int`)  

`RPMTAG_SUGGESTNAME` (`int`)  
El directorio de los ficheros, con el índice de la base de datos.

`RPMTAG_SUGGESTNEVRS` (`int`)  

`RPMTAG_SUGGESTS` (`int`)  

`RPMTAG_SUGGESTVERSION` (`int`)  

`RPMTAG_SUMMARY` (`int`)  

`RPMTAG_SUPPLEMENTFLAGS` (`int`)  

`RPMTAG_SUPPLEMENTNAME` (`int`)  
Las dependencias débiles, con el índice de la base de datos, requiere librpm \>= 4.13.

`RPMTAG_SUPPLEMENTNEVRS` (`int`)  

`RPMTAG_SUPPLEMENTS` (`int`)  

`RPMTAG_SUPPLEMENTVERSION` (`int`)  

`RPMTAG_SYSUSERS` (`int`)  
Requiere librpm \>= 4.19

`RPMTAG_TRANSFILETRIGGERCONDS` (`int`)  

`RPMTAG_TRANSFILETRIGGERFLAGS` (`int`)  

`RPMTAG_TRANSFILETRIGGERINDEX` (`int`)  

`RPMTAG_TRANSFILETRIGGERNAME` (`int`)  
El nombre del desencadenador de fichero de transacción, con el índice de la base de datos, requiere librpm \>= 4.13.

`RPMTAG_TRANSFILETRIGGERPRIORITIES` (`int`)  

`RPMTAG_TRANSFILETRIGGERSCRIPTFLAGS` (`int`)  

`RPMTAG_TRANSFILETRIGGERSCRIPTPROG` (`int`)  

`RPMTAG_TRANSFILETRIGGERSCRIPTS` (`int`)  

`RPMTAG_TRANSFILETRIGGERTYPE` (`int`)  

`RPMTAG_TRANSFILETRIGGERVERSION` (`int`)  

`RPMTAG_TRANSLATIONURL` (`int`)  
Requiere librpm \>= 4.18

`RPMTAG_TRIGGERCONDS` (`int`)  

`RPMTAG_TRIGGERFLAGS` (`int`)  

`RPMTAG_TRIGGERINDEX` (`int`)  

`RPMTAG_TRIGGERNAME` (`int`)  
El nombre del desencadenador, con el índice de la base de datos.

`RPMTAG_TRIGGERSCRIPTFLAGS` (`int`)  

`RPMTAG_TRIGGERSCRIPTPROG` (`int`)  

`RPMTAG_TRIGGERSCRIPTS` (`int`)  

`RPMTAG_TRIGGERTYPE` (`int`)  

`RPMTAG_TRIGGERVERSION` (`int`)  

`RPMTAG_UPSTREAMRELEASES` (`int`)  
Requiere librpm \>= 4.18

`RPMTAG_URL` (`int`)  

`RPMTAG_V` (`int`)  

`RPMTAG_VCS` (`int`)  

`RPMTAG_VENDOR` (`int`)  

`RPMTAG_VERBOSE` (`int`)  

`RPMTAG_VERIFYSCRIPT` (`int`)  

`RPMTAG_VERIFYSCRIPTFLAGS` (`int`)  

`RPMTAG_VERIFYSCRIPTPROG` (`int`)  

`RPMTAG_VERITYSIGNATUREALGO` (`int`)  
Con librpm \>= 4.17.

`RPMTAG_VERITYSIGNATURES` (`int`)  
Con librpm \>= 4.17.

`RPMTAG_VERSION` (`int`)  

`RPMTAG_XPM` (`int`)
