---
title: Data conversion
source_url: https://www.debian.org/doc/manuals/debian-reference/_data_conversion
source_repo: https://salsa.debian.org/debian/debian-reference.git
source_ref: master
source_commit: b7239e647
source_path: 11_data_conversion.rawxml
technology: debian
version: 12 (Bookworm)
license: GPL-2.0-or-later
retrieved_at: '2026-09-15'
order: 120
---

## Data conversion

Tools and tips for converting data formats on the Debian system are described.

Standard based tools are in very good shape but support for proprietary data formats are limited.

## Text data conversion tools

Following packages for the text data conversion caught my eyes.

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `libc6` | @-@popcon1@-@ | @-@psize1@-@ | charset | text encoding converter between locales by `iconv(1)` (fundamental) |
| `recode` | @-@popcon1@-@ | @-@psize1@-@ | charset+eol | text encoding converter between locales (versatile, more aliases and features) |
| `konwert` | @-@popcon1@-@ | @-@psize1@-@ | charset | text encoding converter between locales (fancy) |
| `nkf` | @-@popcon1@-@ | @-@psize1@-@ | charset | character set translator for Japanese |
| `tcs` | @-@popcon1@-@ | @-@psize1@-@ | charset | character set translator |
| `unaccent` | @-@popcon1@-@ | @-@psize1@-@ | charset | replace accented letters by their unaccented equivalent |
| `tofrodos` | @-@popcon1@-@ | @-@psize1@-@ | eol | text format converter between DOS and Unix: `fromdos(1)` and `todos(1)` |
| `macutils` | @-@popcon1@-@ | @-@psize1@-@ | eol | text format converter between Macintosh and Unix: `frommac(1)` and `tomac(1)` |

List of text data conversion tools

### Converting a text file with iconv

> [!TIP]
> `iconv(1)` is provided as a part of the `libc6` package and it is always available on practically all Unix-like systems to convert the encoding of characters.

You can convert encodings of a text file with `iconv(1)` by the following.

    $ iconv -f encoding1 -t encoding2 input.txt >output.txt

Encoding values are case insensitive and ignore "`-`" and "`_`" for matching. Supported encodings can be checked by the "`iconv -l`" command.

| encoding value | usage |
|:---|:---|
| [ASCII](https://en.wikipedia.org/wiki/ASCII) | [American Standard Code for Information Interchange](https://en.wikipedia.org/wiki/ASCII), 7 bit code w/o accented characters |
| [UTF-8](https://en.wikipedia.org/wiki/UTF-8) | current multilingual standard for all modern OSs |
| [ISO-8859-1](https://en.wikipedia.org/wiki/ISO/IEC_8859-1) | old standard for western European languages, ASCII + accented characters |
| [ISO-8859-2](https://en.wikipedia.org/wiki/ISO/IEC_8859-2) | old standard for eastern European languages, ASCII + accented characters |
| [ISO-8859-15](https://en.wikipedia.org/wiki/ISO/IEC_8859-15) | old standard for western European languages, [ISO-8859-1](https://en.wikipedia.org/wiki/ISO/IEC_8859-1) with euro sign |
| [CP850](https://en.wikipedia.org/wiki/Code_page_850) | code page 850, Microsoft DOS characters with graphics for western European languages, [ISO-8859-1](https://en.wikipedia.org/wiki/ISO/IEC_8859-1) variant |
| [CP932](https://en.wikipedia.org/wiki/Code_page_932) | code page 932, Microsoft Windows style [Shift-JIS](https://en.wikipedia.org/wiki/Shift_JIS) variant for Japanese |
| [CP936](https://en.wikipedia.org/wiki/Code_page_936) | code page 936, Microsoft Windows style [GB2312](https://en.wikipedia.org/wiki/GB2312), [GBK](https://en.wikipedia.org/wiki/GBK) or [GB18030](https://en.wikipedia.org/wiki/GB18030) variant for Simplified Chinese |
| [CP949](https://en.wikipedia.org/wiki/Code_page_949) | code page 949, Microsoft Windows style [EUC-KR](https://en.wikipedia.org/wiki/Extended_Unix_Code#EUC-KR) or Unified Hangul Code variant for Korean |
| [CP950](https://en.wikipedia.org/wiki/Code_page_950) | code page 950, Microsoft Windows style [Big5](https://en.wikipedia.org/wiki/Big5) variant for Traditional Chinese |
| [CP1251](https://en.wikipedia.org/wiki/Windows-1251) | code page 1251, Microsoft Windows style encoding for the Cyrillic alphabet |
| [CP1252](https://en.wikipedia.org/wiki/Windows-1252) | code page 1252, Microsoft Windows style [ISO-8859-15](https://en.wikipedia.org/wiki/ISO/IEC_8859-15) variant for western European languages |
| [KOI8-R](https://en.wikipedia.org/wiki/KOI8-R) | old Russian UNIX standard for the Cyrillic alphabet |
| [ISO-2022-JP](https://en.wikipedia.org/wiki/ISO/IEC_2022) | standard encoding for Japanese email which uses only 7 bit codes |
| [eucJP](https://en.wikipedia.org/wiki/Extended_Unix_Code) | old Japanese UNIX standard 8 bit code and completely different from [Shift-JIS](https://en.wikipedia.org/wiki/Shift_JIS) |
| [Shift-JIS](https://en.wikipedia.org/wiki/Shift_JIS) | JIS X 0208 Appendix 1 standard for Japanese (see [CP932](https://en.wikipedia.org/wiki/Code_page_932)) |

List of encoding values and their usage {#list-of-encoding-values}

> [!NOTE]
> Some encodings are only supported for the data conversion and are not used as locale values ([???](#_basics_of_encoding)).

For character sets which fit in single byte such as [ASCII](https://en.wikipedia.org/wiki/ASCII) and [ISO-8859](https://en.wikipedia.org/wiki/ISO/IEC_8859) character sets, the [character encoding](https://en.wikipedia.org/wiki/Character_encoding) means almost the same thing as the character set.

For character sets with many characters such as [JIS X 0213](https://en.wikipedia.org/wiki/JIS_X_0213) for Japanese or [Universal Character Set (UCS, Unicode, ISO-10646-1)](https://en.wikipedia.org/wiki/Universal_Character_Set) for practically all languages, there are many encoding schemes to fit them into the sequence of the byte data.

- [EUC](https://en.wikipedia.org/wiki/Extended_Unix_Code) and [ISO/IEC 2022 (also known as JIS X 0202)](https://en.wikipedia.org/wiki/ISO/IEC_2022) for Japanese

- [UTF-8](https://en.wikipedia.org/wiki/UTF-8), [UTF-16/UCS-2](https://en.wikipedia.org/wiki/UTF-16/UCS-2) and [UTF-32/UCS-4](https://en.wikipedia.org/wiki/UTF-32/UCS-4) for Unicode

For these, there are clear differentiations between the character set and the character encoding.

The [code page](https://en.wikipedia.org/wiki/Code_page) is used as the synonym to the character encoding tables for some vendor specific ones.

> [!NOTE]
> Please note most encoding systems share the same code with ASCII for the 7 bit characters. But there are some exceptions. If you are converting old Japanese C programs and URLs data from the casually-called shift-JIS encoding format to UTF-8 format, use "`CP932`" as the encoding name instead of "`shift-JIS`" to get the expected results: `0x5C` → "`\`" and `0x7E` → "`~`". Otherwise, these are converted to wrong characters.

> [!TIP]
> `recode(1)` may be used too and offers more than the combined functionality of `iconv(1)`, `fromdos(1)`, `todos(1)`, `frommac(1)`, and `tomac(1)`. For more, see "`info recode`".

### Checking file to be UTF-8 with iconv

You can check if a text file is encoded in UTF-8 with `iconv(1)` by the following.

    $ iconv -f utf8 -t utf8 input.txt >/dev/null || echo "non-UTF-8 found"

> [!TIP]
> Use "`--verbose`" option in the above example to find the first non-UTF-8 character.

### Converting file names with iconv

Here is an example script to convert encoding of file names from ones created under older OS to modern UTF-8 ones in a single directory.

    #!/bin/sh
    ENCDN=iso-8859-1
    for x in *;
     do
     mv "$x" "$(echo "$x" | iconv -f $ENCDN -t utf-8)"
    done

The "`$ENCDN`" variable specifies the original encoding used for file names under older OS as in [List of encoding values and their usage](#list-of-encoding-values).

For more complicated case, please mount a filesystem (e.g. a partition on a disk drive) containing such file names with proper encoding as the `mount(8)` option (see [???](#_filename_encoding)) and copy its entire contents to another filesystem mounted as UTF-8 with "`cp -a`" command.

### EOL conversion

The text file format, specifically the end-of-line (EOL) code, is dependent on the platform.

| platform          | EOL code | control | decimal | hexadecimal |
|:------------------|:---------|:--------|:--------|:------------|
| Debian (unix)     | LF       | `^J`    | 10      | 0A          |
| MSDOS and Windows | CR-LF    | `^M^J`  | 13 10   | 0D 0A       |
| Apple's Macintosh | CR       | `^M`    | 13      | 0D          |

List of EOL styles for different platforms

The EOL format conversion programs, `fromdos(1)`, `todos(1)`, `frommac(1)`, and `tomac(1)`, are quite handy. `recode(1)` is also useful.

> [!NOTE]
> Some data on the Debian system, such as the wiki page data for the `python-moinmoin` package, use MSDOS style CR-LF as the EOL code. So the above rule is just a general rule.

> [!NOTE]
> Most editors (eg. `vim`, `emacs`, `gedit`, …) can handle files in MSDOS style EOL transparently.

> [!TIP]
> The use of "`sed -e '/\r$/!s/$/\r/'`" instead of `todos(1)` is better when you want to unify the EOL style to the MSDOS style from the mixed MSDOS and Unix style. (e.g., after merging 2 MSDOS style files with `diff3(1)`.) This is because `todos` adds CR to all lines.

### TAB conversion

There are few popular specialized programs to convert the tab codes.

| function                 | `bsdmainutils` | `coreutils` |
|:-------------------------|:---------------|:------------|
| expand tab to spaces     | "`col -x`"     | `expand`    |
| unexpand tab from spaces | "`col -h`"     | `unexpand`  |

List of TAB conversion commands from `bsdmainutils` and `coreutils` packages

`indent(1)` from the `indent` package completely reformats whitespaces in the C program.

Editor programs such as `vim` and `emacs` can be used for TAB conversion, too. For example with `vim`, you can expand TAB with "`:set expandtab`" and "`:%retab`" command sequence. You can revert this with "`:set noexpandtab`" and "`:%retab!`" command sequence.

### Editors with auto-conversion

Intelligent modern editors such as the `vim` program are quite smart and copes well with any encoding systems and any file formats. You should use these editors under the UTF-8 locale in the UTF-8 capable console for the best compatibility.

An old western European Unix text file, "`u-file.txt`", stored in the latin1 (iso-8859-1) encoding can be edited simply with `vim` by the following.

    $ vim u-file.txt

This is possible since the auto detection mechanism of the file encoding in `vim` assumes the UTF-8 encoding first and, if it fails, assumes it to be latin1.

An old Polish Unix text file, "`pu-file.txt`", stored in the latin2 (iso-8859-2) encoding can be edited with `vim` by the following.

    $ vim '+e ++enc=latin2 pu-file.txt'

An old Japanese unix text file, "`ju-file.txt`", stored in the eucJP encoding can be edited with `vim` by the following.

    $ vim '+e ++enc=eucJP ju-file.txt'

An old Japanese MS-Windows text file, "`jw-file.txt`", stored in the so called shift-JIS encoding (more precisely: CP932) can be edited with `vim` by the following.

    $ vim '+e ++enc=CP932 ++ff=dos jw-file.txt'

When a file is opened with "`++enc`" and "`++ff`" options, "`:w`" in the Vim command line stores it in the original format and overwrite the original file. You can also specify the saving format and the file name in the Vim command line, e.g., "`:w ++enc=utf8 new.txt`".

Please refer to the mbyte.txt "multi-byte text support" in `vim` on-line help and [List of encoding values and their usage](#list-of-encoding-values) for locale values used with "`++enc`".

The `emacs` family of programs can perform the equivalent functions.

### Plain text extraction

The following reads a web page into a text file. This is very useful when copying configurations off the Web or applying basic Unix text tools such as `grep(1)` on the web page.

    $ w3m -dump http://www.remote-site.com/help-info.html >textfile

Similarly, you can extract plain text data from other formats using the following.

| package | popcon | size | keyword | function |
|:---|:---|:---|:---|:---|
| `w3m` | @-@popcon1@-@ | @-@psize1@-@ | html→text | HTML to text converter with the "`w3m -dump`" command |
| `html2text` | @-@popcon1@-@ | @-@psize1@-@ | html→text | advanced HTML to text converter (ISO 8859-1) |
| `lynx` | @-@popcon1@-@ | @-@psize1@-@ | html→text | HTML to text converter with the "`lynx -dump`" command |
| `elinks` | @-@popcon1@-@ | @-@psize1@-@ | html→text | HTML to text converter with the "`elinks -dump`" command |
| `links` | @-@popcon1@-@ | @-@psize1@-@ | html→text | HTML to text converter with the "`links -dump`" command |
| `links2` | @-@popcon1@-@ | @-@psize1@-@ | html→text | HTML to text converter with the "`links2 -dump`" command |
| `antiword` | @-@popcon1@-@ | @-@psize1@-@ | MSWord→text,ps | convert MSWord files to plain text or ps |
| `catdoc` | @-@popcon1@-@ | @-@psize1@-@ | MSWord→text,TeX | convert MSWord files to plain text or TeX |
| `pstotext` | @-@popcon1@-@ | @-@psize1@-@ | ps/pdf→text | extract text from PostScript and PDF files |
| `unhtml` | @-@popcon1@-@ | @-@psize1@-@ | html→text | remove the markup tags from an HTML file |
| `odt2txt` | @-@popcon1@-@ | @-@psize1@-@ | odt→text | converter from OpenDocument Text to text |

List of tools to extract plain text data

### Highlighting and formatting plain text data

You can highlight and format plain text data by the following.

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `vim-runtime` | @-@popcon1@-@ | @-@psize1@-@ | highlight | Vim MACRO to convert source code to HTML with "`:source $VIMRUNTIME/syntax/html.vim`" |
| `cxref` | @-@popcon1@-@ | @-@psize1@-@ | c→html | converter for the C program to latex and HTML (C language) |
| `src2tex` | @-@popcon1@-@ | @-@psize1@-@ | highlight | convert many source codes to TeX (C language) |
| `source-highlight` | @-@popcon1@-@ | @-@psize1@-@ | highlight | convert many source codes to HTML, XHTML, LaTeX, Texinfo, ANSI color escape sequences and DocBook files with highlight (C++) |
| `highlight` | @-@popcon1@-@ | @-@psize1@-@ | highlight | convert many source codes to HTML, XHTML, RTF, LaTeX, TeX or XSL-FO files with highlight (C++) |
| `grc` | @-@popcon1@-@ | @-@psize1@-@ | text→color | generic colouriser for everything (Python) |
| `txt2html` | @-@popcon1@-@ | @-@psize1@-@ | text→html | text to HTML converter (Perl) |
| `markdown` | @-@popcon1@-@ | @-@psize1@-@ | text→html | markdown text document formatter to (X)HTML (Perl) |
| `asciidoc` | @-@popcon1@-@ | @-@psize1@-@ | text→any | AsciiDoc text document formatter to XML/HTML (Python) |
| `pandoc` | @-@popcon1@-@ | @-@psize1@-@ | text→any | general markup converter (Haskell) |
| `python-docutils` | @-@popcon1@-@ | @-@psize1@-@ | text→any | ReStructured Text document formatter to XML (Python) |
| `txt2tags` | @-@popcon1@-@ | @-@psize1@-@ | text→any | document conversion from text to HTML, SGML, LaTeX, man page, MoinMoin, Magic Point and PageMaker (Python) |
| `udo` | @-@popcon1@-@ | @-@psize1@-@ | text→any | universal document - text processing utility (C language) |
| `stx2any` | @-@popcon1@-@ | @-@psize1@-@ | text→any | document converter from structured plain text to other formats (m4) |
| `rest2web` | @-@popcon1@-@ | @-@psize1@-@ | text→html | document converter from ReStructured Text to html (Python) |
| `aft` | @-@popcon1@-@ | @-@psize1@-@ | text→any | "free form" document preparation system (Perl) |
| `yodl` | @-@popcon1@-@ | @-@psize1@-@ | text→any | pre-document language and tools to process it (C language) |
| `sdf` | @-@popcon1@-@ | @-@psize1@-@ | text→any | simple document parser (Perl) |
| `sisu` | @-@popcon1@-@ | @-@psize1@-@ | text→any | document structuring, publishing and search framework (Ruby) |

List of tools to highlight plain text data

## XML data

[The Extensible Markup Language (XML)](https://en.wikipedia.org/wiki/XML) is a markup language for documents containing structured information.

See introductory information at [XML.COM](http://xml.com/).

- ["What is XML?"](http://www.xml.com/pub/a/98/10/guide0.html)

- ["What Is XSLT?"](http://xml.com/pub/a/2000/08/holman/index.html)

- ["What Is XSL-FO?"](http://xml.com/pub/a/2002/03/20/xsl-fo.html)

- ["What Is XLink?"](http://xml.com/pub/a/2000/09/xlink/index.html)

### Basic hints for XML

XML text looks somewhat like [HTML](https://en.wikipedia.org/wiki/HTML). It enables us to manage multiple formats of output for a document. One easy XML system is the `docbook-xsl` package, which is used here.

Each XML file starts with standard XML declaration as the following.

    <?xml version="1.0" encoding="UTF-8"?>

The basic syntax for one XML element is marked up as the following.

    <name attribute="value">content</name>

XML element with empty content is marked up in the following short form.

    <name attribute="value"/>

The "`attribute="value"`" in the above examples are optional.

The comment section in XML is marked up as the following.

    <!-- comment -->

Other than adding markups, XML requires minor conversion to the content using predefined entities for following characters.

| predefined entity | character to be converted into |
|:------------------|:-------------------------------|
| `&quot;`          | `"` : quote                    |
| `&apos;`          | `'` : apostrophe               |
| `&lt;`            | `<` : less-than                |
| `&gt;`            | `>` : greater-than             |
| `&amp;`           | `&` : ampersand                |

List of predefined entities for XML

> [!CAUTION]
> "`<`" or "`&`" can not be used in attributes or elements.

> [!NOTE]
> When SGML style user defined entities, e.g. "`&some-tag:`", are used, the first definition wins over others. The entity definition is expressed in "`<!ENTITY some-tag "entity value">`".

> [!NOTE]
> As long as the XML markup are done consistently with certain set of the tag name (either some data as content or attribute value), conversion to another XML is trivial task using [Extensible Stylesheet Language Transformations (XSLT)](https://en.wikipedia.org/wiki/XSL_Transformations).

### XML processing

There are many tools available to process XML files such as [the Extensible Stylesheet Language (XSL)](https://en.wikipedia.org/wiki/Extensible_Stylesheet_Language).

Basically, once you create well formed XML file, you can convert it to any format using [Extensible Stylesheet Language Transformations (XSLT)](https://en.wikipedia.org/wiki/XSL_Transformations).

The [Extensible Stylesheet Language for Formatting Objects (XSL-FO)](https://en.wikipedia.org/wiki/XSL_Formatting_Objects) is supposed to be solution for formatting. The `fop` package is new to the Debian `main` archive due to its dependence to the [Java programing language](https://en.wikipedia.org/wiki/Java_(programming_language)). So the LaTeX code is usually generated from XML using XSLT and the LaTeX system is used to create printable file such as DVI, PostScript, and PDF.

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `docbook-xml` | @-@popcon1@-@ | @-@psize1@-@ | xml | XML document type definition (DTD) for DocBook |
| `xsltproc` | @-@popcon1@-@ | @-@psize1@-@ | xslt | XSLT command line processor (XML→ XML, HTML, plain text, etc.) |
| `docbook-xsl` | @-@popcon1@-@ | @-@psize1@-@ | xml/xslt | XSL stylesheets for processing DocBook XML to various output formats with XSLT |
| `xmlto` | @-@popcon1@-@ | @-@psize1@-@ | xml/xslt | XML-to-any converter with XSLT |
| `dbtoepub` | @-@popcon1@-@ | @-@psize1@-@ | xml/xslt | DocBook XML to .epub converter |
| `dblatex` | @-@popcon1@-@ | @-@psize1@-@ | xml/xslt | convert Docbook files to DVI, PostScript, PDF documents with XSLT |
| `fop` | @-@popcon1@-@ | @-@psize1@-@ | xml/xsl-fo | convert Docbook XML files to PDF |

List of XML tools

Since XML is subset of [Standard Generalized Markup Language (SGML)](https://en.wikipedia.org/wiki/SGML), it can be processed by the extensive tools available for SGML, such as [Document Style Semantics and Specification Language (DSSSL)](https://en.wikipedia.org/wiki/Document_Style_Semantics_and_Specification_Language).

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `openjade` | @-@popcon1@-@ | @-@psize1@-@ | dsssl | ISO/IEC 10179:1996 standard DSSSL processor (latest) |
| `docbook-dsssl` | @-@popcon1@-@ | @-@psize1@-@ | xml/dsssl | DSSSL stylesheets for processing DocBook XML to various output formats with DSSSL |
| `docbook-utils` | @-@popcon1@-@ | @-@psize1@-@ | xml/dsssl | utilities for DocBook files including conversion to other formats (HTML, RTF, PS, man, PDF) with `docbook2*` commands with DSSSL |
| `sgml2x` | @-@popcon1@-@ | @-@psize1@-@ | SGML/dsssl | converter from SGML and XML using DSSSL stylesheets |

List of DSSSL tools

> [!TIP]
> [GNOME](https://en.wikipedia.org/wiki/GNOME)'s `yelp` is sometimes handy to read [DocBook](https://en.wikipedia.org/wiki/DocBook) XML files directly since it renders decently on X.

### The XML data extraction

You can extract HTML or XML data from other formats using followings.

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `wv` | @-@popcon1@-@ | @-@psize1@-@ | MSWord→any | document converter from Microsoft Word to HTML, LaTeX, etc. |
| `texi2html` | @-@popcon1@-@ | @-@psize1@-@ | texi→html | converter from Texinfo to HTML |
| `man2html` | @-@popcon1@-@ | @-@psize1@-@ | manpage→html | converter from manpage to HTML (CGI support) |
| `unrtf` | @-@popcon1@-@ | @-@psize1@-@ | rtf→html | document converter from RTF to HTML, etc |
| `info2www` | @-@popcon1@-@ | @-@psize1@-@ | info→html | converter from GNU info to HTML (CGI support) |
| `ooo2dbk` | @-@popcon1@-@ | @-@psize1@-@ | sxw→xml | converter from OpenOffice.org SXW documents to DocBook XML |
| `wp2x` | @-@popcon1@-@ | @-@psize1@-@ | WordPerfect→any | WordPerfect 5.0 and 5.1 files to TeX, LaTeX, troff, GML and HTML |
| `doclifter` | @-@popcon1@-@ | @-@psize1@-@ | troff→xml | converter from troff to DocBook XML |

List of XML data extraction tools

For non-XML HTML files, you can convert them to XHTML which is an instance of well formed XML. XHTML can be processed by XML tools.

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `libxml2-utils` | @-@popcon1@-@ | @-@psize1@-@ | xml↔html↔xhtml | command line XML tool with `xmllint(1)` (syntax check, reformat, lint, …) |
| `tidy` | @-@popcon1@-@ | @-@psize1@-@ | xml↔html↔xhtml | HTML syntax checker and reformatter |

List of XML pretty print tools

Once proper XML is generated, you can use XSLT technology to extract data based on the mark-up context etc.

## Type setting

The Unix [troff](https://en.wikipedia.org/wiki/Troff) program originally developed by AT&T can be used for simple typesetting. It is usually used to create manpages.

[TeX](https://en.wikipedia.org/wiki/TeX) created by Donald Knuth is a very powerful type setting tool and is the de facto standard. [LaTeX](https://en.wikipedia.org/wiki/LaTeX) originally written by Leslie Lamport enables a high-level access to the power of TeX.

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `texlive` | @-@popcon1@-@ | @-@psize1@-@ | (La)TeX | TeX system for typesetting, previewing and printing |
| `groff` | @-@popcon1@-@ | @-@psize1@-@ | troff | GNU troff text-formatting system |

List of type setting tools

### roff typesetting

Traditionally, [roff](https://en.wikipedia.org/wiki/Roff) is the main Unix text processing system. See `roff(7)`, `groff(7)`, `groff(1)`, `grotty(1)`, `troff(1)`, `groff_mdoc(7)`, `groff_man(7)`, `groff_ms(7)`, `groff_me(7)`, `groff_mm(7)`, and "`info groff`".

You can read or print a good tutorial and reference on "`-me`" [macro](https://en.wikipedia.org/wiki/Macro_(computer_science)) in "`/usr/share/doc/groff/`" by installing the `groff` package.

> [!TIP]
> "`groff -Tascii -me -`" produces plain text output with [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code). If you wish to get manpage like output with many "^H" and "\_", use "`GROFF_NO_SGR=1 groff -Tascii -me -`" instead.

> [!TIP]
> To remove "^H" and "\_" from a text file generated by `groff`, filter it by "`col -b -x`".

### TeX/LaTeX

The [TeX Live](https://en.wikipedia.org/wiki/TeX_Live) software distribution offers a complete TeX system. The `texlive` metapackage provides a decent selection of the [TeX Live](https://en.wikipedia.org/wiki/TeX_Live) packages which should suffice for the most common tasks.

There are many references available for [TeX](https://en.wikipedia.org/wiki/TeX) and [LaTeX](https://en.wikipedia.org/wiki/LaTeX).

- [The teTeX HOWTO: The Linux-teTeX Local Guide](http://www.tldp.org/HOWTO/TeTeX-HOWTO.html)

- `tex(1)`

- `latex(1)`

- `texdoc(1)`

- `texdoctk(1)`

- "The TeXbook", by Donald E. Knuth, (Addison-Wesley)

- "LaTeX - A Document Preparation System", by Leslie Lamport, (Addison-Wesley)

- "The LaTeX Companion", by Goossens, Mittelbach, Samarin, (Addison-Wesley)

This is the most powerful typesetting environment. Many [SGML](https://en.wikipedia.org/wiki/Standard_Generalized_Markup_Language) processors use this as their back end text processor. [Lyx](https://en.wikipedia.org/wiki/Lyx) provided by the `lyx` package and [GNU TeXmacs](https://en.wikipedia.org/wiki/GNU_TeXmacs) provided by the `texmacs` package offer nice [WYSIWYG](https://en.wikipedia.org/wiki/WYSIWYG) editing environment for [LaTeX](https://en.wikipedia.org/wiki/LaTeX) while many use [Emacs](https://en.wikipedia.org/wiki/Emacs) and [Vim](https://en.wikipedia.org/wiki/Vim_(text_editor)) as the choice for the source editor.

There are many online resources available.

- The TEX Live Guide - TEX Live 2007 ("`/usr/share/doc/texlive-doc-base/english/texlive-en/live.html`") (`texlive-doc-base` package)

- [A Simple Guide to Latex/Lyx](http://www.stat.rice.edu/~helpdesk/howto/lyxguide.html)

- [Word Processing Using LaTeX](http://www-h.eng.cam.ac.uk/help/tpl/textprocessing/latex_basic/latex_basic.html)

- [Local User Guide to teTeX/LaTeX](http://supportweb.cs.bham.ac.uk/documentation/LaTeX/lguide/local-guide/local-guide.html)

When documents become bigger, sometimes TeX may cause errors. You must increase pool size in "`/etc/texmf/texmf.cnf`" (or more appropriately edit "`/etc/texmf/texmf.d/95NonPath`" and run `update-texmf(8)`) to fix this.

> [!NOTE]
> The TeX source of "The TeXbook" is available at <http://tug.ctan.org/tex-archive/systems/knuth/dist/tex/texbook.tex>. This file contains most of the required macros. I heard that you can process this document with `tex(1)` after commenting lines 7 to 10 and adding "`\input manmac \proofmodefalse`". It's strongly recommended to buy this book (and all other books from Donald E. Knuth) instead of using the online version but the source is a great example of TeX input!

### Pretty print a manual page

You can print a manual page in PostScript nicely by one of the following commands.

    $ man -Tps some_manpage | lpr

### Creating a manual page

Although writing a manual page (manpage) in the plain [troff](https://en.wikipedia.org/wiki/Troff) format is possible, there are few helper packages to create it.

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `docbook-to-man` | @-@popcon1@-@ | @-@psize1@-@ | SGML→manpage | converter from DocBook SGML into roff man macros |
| `help2man` | @-@popcon1@-@ | @-@psize1@-@ | text→manpage | automatic manpage generator from --help |
| `info2man` | @-@popcon1@-@ | @-@psize1@-@ | info→manpage | converter from GNU info to POD or man pages |
| `txt2man` | @-@popcon1@-@ | @-@psize1@-@ | text→manpage | convert flat ASCII text to man page format |

List of packages to help creating the manpage

## Printable data

Printable data is expressed in the [PostScript](https://en.wikipedia.org/wiki/PostScript) format on the Debian system. [Common Unix Printing System (CUPS)](https://en.wikipedia.org/wiki/Common_Unix_Printing_System) uses Ghostscript as its rasterizer backend program for non-PostScript printers.

### Ghostscript

The core of printable data manipulation is the [Ghostscript](https://en.wikipedia.org/wiki/Ghostscript) [PostScript (PS)](https://en.wikipedia.org/wiki/PostScript) interpreter which generates raster image.

The latest upstream Ghostscript from Artifex was re-licensed from AFPL to GPL and merged all the latest ESP version changes such as CUPS related ones at 8.60 release as unified release.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `ghostscript` | @-@popcon1@-@ | @-@psize1@-@ | [The GPL Ghostscript PostScript/PDF interpreter](https://en.wikipedia.org/wiki/Ghostscript) |
| `ghostscript-x` | @-@popcon1@-@ | @-@psize1@-@ | GPL Ghostscript PostScript/PDF interpreter - X display support |
| `libpoppler95` | @-@popcon1@-@ | @-@psize1@-@ | PDF rendering library forked from the xpdf PDF viewer |
| `libpoppler-glib8` | @-@popcon1@-@ | @-@psize1@-@ | PDF rendering library (GLib-based shared library) |
| `poppler-data` | @-@popcon1@-@ | @-@psize1@-@ | CMaps for PDF rendering library (for [CJK](https://en.wikipedia.org/wiki/CJK_characters) support: Adobe-\*) |

List of Ghostscript PostScript interpreters

> [!TIP]
> "`gs -h`" can display the configuration of Ghostscript.

### Merge two PS or PDF files

You can merge two [PostScript (PS)](https://en.wikipedia.org/wiki/PostScript) or [Portable Document Format (PDF)](https://en.wikipedia.org/wiki/Portable_Document_Format) files using `gs(1)` of Ghostscript.

    $ gs -q -dNOPAUSE -dBATCH -sDEVICE=pswrite -sOutputFile=bla.ps -f foo1.ps foo2.ps
    $ gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=bla.pdf -f foo1.pdf foo2.pdf

> [!NOTE]
> The [PDF](https://en.wikipedia.org/wiki/Portable_Document_Format), which is a widely used cross-platform printable data format, is essentially the compressed [PS](https://en.wikipedia.org/wiki/PostScript) format with few additional features and extensions.

> [!TIP]
> For command line, `psmerge(1)` and other commands from the `psutils` package are useful for manipulating PostScript documents. `pdftk(1)` from the `pdftk` package is useful for manipulating PDF documents, too.

### Printable data utilities

The following packages for the printable data utilities caught my eyes.

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `poppler-utils` | @-@popcon1@-@ | @-@psize1@-@ | pdf→ps,text,… | PDF utilities: `pdftops`, `pdfinfo`, `pdfimages`, `pdftotext`, `pdffonts` |
| `psutils` | @-@popcon1@-@ | @-@psize1@-@ | ps→ps | PostScript document conversion tools |
| `poster` | @-@popcon1@-@ | @-@psize1@-@ | ps→ps | create large posters out of PostScript pages |
| `enscript` | @-@popcon1@-@ | @-@psize1@-@ | text→ps, html, rtf | convert ASCII text to PostScript, HTML, RTF or Pretty-Print |
| `a2ps` | @-@popcon1@-@ | @-@psize1@-@ | text→ps | 'Anything to PostScript' converter and pretty-printer |
| `pdftk` | @-@popcon1@-@ | @-@psize1@-@ | pdf→pdf | PDF document conversion tool: `pdftk` |
| `html2ps` | @-@popcon1@-@ | @-@psize1@-@ | html→ps | converter from HTML to PostScript |
| `gnuhtml2latex` | @-@popcon1@-@ | @-@psize1@-@ | html→latex | converter from html to latex |
| `latex2rtf` | @-@popcon1@-@ | @-@psize1@-@ | latex→rtf | convert documents from LaTeX to RTF which can be read by MS Word |
| `ps2eps` | @-@popcon1@-@ | @-@psize1@-@ | ps→eps | converter from PostScript to EPS (Encapsulated PostScript) |
| `e2ps` | @-@popcon1@-@ | @-@psize1@-@ | text→ps | Text to PostScript converter with Japanese encoding support |
| `impose+` | @-@popcon1@-@ | @-@psize1@-@ | ps→ps | PostScript utilities |
| `trueprint` | @-@popcon1@-@ | @-@psize1@-@ | text→ps | pretty print many source codes (C, C++, Java, Pascal, Perl, Pike, Sh, and Verilog) to PostScript. (C language) |
| `pdf2svg` | @-@popcon1@-@ | @-@psize1@-@ | ps→svg | converter from PDF to [Scalable vector graphics](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) format |
| `pdftoipe` | @-@popcon1@-@ | @-@psize1@-@ | ps→ipe | converter from PDF to IPE's XML format |

List of printable data utilities

### Printing with CUPS

Both `lp(1)` and `lpr(1)` commands offered by [Common Unix Printing System (CUPS)](https://en.wikipedia.org/wiki/Common_Unix_Printing_System) provides options for customized printing the printable data.

You can print 3 copies of a file collated using one of the following commands.

    $ lp -n 3 -o Collate=True filename

    $ lpr -#3 -o Collate=True filename

You can further customize printer operation by using printer option such as "`-o number-up=2`", "`-o page-set=even`", "`-o page-set=odd`", "`-o scaling=200`", "`-o natural-scaling=200`", etc., documented at [Command-Line Printing and Options](http://localhost:631/help/options.html).

## The mail data conversion

The following packages for the mail data conversion caught my eyes.

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `sharutils` | @-@popcon1@-@ | @-@psize1@-@ | mail | `shar(1)`, `unshar(1)`, `uuencode(1)`, `uudecode(1)` |
| `mpack` | @-@popcon1@-@ | @-@psize1@-@ | MIME | encoding and decoding of [MIME](https://en.wikipedia.org/wiki/MIME) messages: `mpack(1)` and `munpack(1)` |
| `tnef` | @-@popcon1@-@ | @-@psize1@-@ | ms-tnef | unpacking [MIME](https://en.wikipedia.org/wiki/MIME) attachments of type "application/ms-tnef" which is a Microsoft only format |
| `uudeview` | @-@popcon1@-@ | @-@psize1@-@ | mail | encoder and decoder for the following formats: [uuencode](https://en.wikipedia.org/wiki/Uuencoding), [xxencode](https://en.wikipedia.org/wiki/Xxencode), [BASE64](https://en.wikipedia.org/wiki/Base64), [quoted printable](https://en.wikipedia.org/wiki/Quoted-printable), and [BinHex](https://en.wikipedia.org/wiki/BinHex) |

List of packages to help mail data conversion

> [!TIP]
> The [Internet Message Access Protocol](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol) version 4 (IMAP4) server (see [???](#_pop3_imap4_server)) may be used to move mails out from proprietary mail systems if the mail client software can be configured to use IMAP4 server too.

### Mail data basics

Mail ([SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)) data should be limited to series of 7 bit data. So binary data and 8 bit text data are encoded into 7 bit format with the [Multipurpose Internet Mail Extensions (MIME)](https://en.wikipedia.org/wiki/MIME) and the selection of the charset (see [???](#_basics_of_encoding)).

The standard mail storage format is mbox formatted according to [RFC2822 (updated RFC822)](http://tools.ietf.org/html/rfc2822). See `mbox(5)` (provided by the `mutt` package).

For European languages, "`Content-Transfer-Encoding: quoted-printable`" with the ISO-8859-1 charset is usually used for mail since there are not much 8 bit characters. If European text is encoded in UTF-8, "`Content-Transfer-Encoding: quoted-printable`" is likely to be used since it is mostly 7 bit data.

For Japanese, traditionally "`Content-Type: text/plain; charset=ISO-2022-JP`" is usually used for mail to keep text in 7 bits. But older Microsoft systems may send mail data in Shift-JIS without proper declaration. If Japanese text is encoded in UTF-8, [Base64](https://en.wikipedia.org/wiki/Base64) is likely to be used since it contains many 8 bit data. The situation of other Asian languages is similar.

> [!NOTE]
> If your non-Unix mail data is accessible by a non-Debian client software which can talk to the IMAP4 server, you may be able to move them out by running your own IMAP4 server (see [???](#_pop3_imap4_server)).

> [!NOTE]
> If you use other mail storage formats, moving them to mbox format is the good first step. The versatile client program such as `mutt(1)` may be handy for this.

You can split mailbox contents to each message using `procmail(1)` and `formail(1)`.

Each mail message can be unpacked using `munpack(1)` from the `mpack` package (or other specialized tools) to obtain the MIME encoded contents.

## Graphic data tools

The following packages for the graphic data conversion, editing, and organization tools caught my eyes.

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `gimp` | @-@popcon1@-@ | @-@psize1@-@ | image(bitmap) | GNU Image Manipulation Program |
| `imagemagick` | @-@popcon1@-@ | @-@psize1@-@ | image(bitmap) | image manipulation programs |
| `graphicsmagick` | @-@popcon1@-@ | @-@psize1@-@ | image(bitmap) | image manipulation programs (fork of `imagemagick`) |
| `xsane` | @-@popcon1@-@ | @-@psize1@-@ | image(bitmap) | GTK+-based X11 frontend for SANE (Scanner Access Now Easy) |
| `netpbm` | @-@popcon1@-@ | @-@psize1@-@ | image(bitmap) | graphics conversion tools |
| `icoutils` | @-@popcon1@-@ | @-@psize1@-@ | png↔ico(bitmap) | convert [MS Windows icons and cursors to and from PNG formats](https://en.wikipedia.org/wiki/ICO_(icon_image_file_format)) ([favicon.ico](https://en.wikipedia.org/wiki/Favicon)) |
| `scribus` | @-@popcon1@-@ | @-@psize1@-@ | ps/pdf/SVG/… | [Scribus](https://en.wikipedia.org/wiki/Scribus) DTP editor |
| `libreoffice-draw` | @-@popcon1@-@ | @-@psize1@-@ | image(vector) | LibreOffice office suite - drawing |
| `inkscape` | @-@popcon1@-@ | @-@psize1@-@ | image(vector) | [SVG (Scalable Vector Graphics)](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) editor |
| `dia` | @-@popcon1@-@ | @-@psize1@-@ | image(vector) | diagram editor (Gtk) |
| `xfig` | @-@popcon1@-@ | @-@psize1@-@ | image(vector) | Facility for Interactive Generation of figures under X11 |
| `pstoedit` | @-@popcon1@-@ | @-@psize1@-@ | ps/pdf→image(vector) | PostScript and PDF files to editable vector graphics converter (SVG) |
| `libwmf-bin` | @-@popcon1@-@ | @-@psize1@-@ | Windows/image(vector) | Windows metafile (vector graphic data) conversion tools |
| `fig2sxd` | @-@popcon1@-@ | @-@psize1@-@ | fig→sxd(vector) | convert XFig files to OpenOffice.org Draw format |
| `unpaper` | @-@popcon1@-@ | @-@psize1@-@ | image→image | post-processing tool for scanned pages for [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) |
| `tesseract-ocr` | @-@popcon1@-@ | @-@psize1@-@ | image→text | free [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) software based on the HP's commercial OCR engine |
| `tesseract-ocr-eng` | @-@popcon1@-@ | @-@psize1@-@ | image→text | OCR engine data: tesseract-ocr language files for English text |
| `gocr` | @-@popcon1@-@ | @-@psize1@-@ | image→text | free OCR software |
| `ocrad` | @-@popcon1@-@ | @-@psize1@-@ | image→text | free OCR software |
| `eog` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | Eye of GNOME graphics viewer program |
| `gthumb` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | image viewer and browser (GNOME) |
| `geeqie` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | image viewer using GTK+ |
| `shotwell` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | digital photo organizer (GNOME) |
| `gtkam` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | application for retrieving media from digital cameras (GTK+) |
| `gphoto2` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | The gphoto2 digital camera command-line client |
| `gwenview` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | image viewer (KDE) |
| `kamera` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | digital camera support for KDE applications |
| `digikam` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | digital photo management application for KDE |
| `exiv2` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | EXIF/IPTC metadata manipulation tool |
| `exiftran` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | transform digital camera jpeg images |
| `jhead` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | manipulate the non-image part of Exif compliant JPEG (digital camera photo) files |
| `exif` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | command-line utility to show EXIF information in JPEG files |
| `exiftags` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | utility to read Exif tags from a digital camera JPEG file |
| `exifprobe` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif) | read metadata from digital pictures |
| `dcraw` | @-@popcon1@-@ | @-@psize1@-@ | image(Raw)→ppm | decode raw digital camera images |
| `findimagedupes` | @-@popcon1@-@ | @-@psize1@-@ | image→fingerprint | find visually similar or duplicate images |
| `ale` | @-@popcon1@-@ | @-@psize1@-@ | image→image | merge images to increase fidelity or create mosaics |
| `imageindex` | @-@popcon1@-@ | @-@psize1@-@ | image(Exif)→html | generate static HTML galleries from images |
| `outguess` | @-@popcon1@-@ | @-@psize1@-@ | jpeg,png | universal [Steganographic](https://en.wikipedia.org/wiki/Steganography) tool |
| `librecad` | @-@popcon1@-@ | @-@psize1@-@ | DXF | CAD data editor (KDE) |
| `blender` | @-@popcon1@-@ | @-@psize1@-@ | blend, TIFF, VRML, … | 3D content editor for animation etc |
| `mm3d` | @-@popcon1@-@ | @-@psize1@-@ | ms3d, obj, dxf, … | OpenGL based 3D model editor |
| `open-font-design-toolkit` | @-@popcon1@-@ | @-@psize1@-@ | ttf, ps, … | metapackage for open font design |
| `fontforge` | @-@popcon1@-@ | @-@psize1@-@ | ttf, ps, … | font editor for PS, TrueType and OpenType fonts |
| `xgridfit` | @-@popcon1@-@ | @-@psize1@-@ | ttf | program for [gridfitting and hinting](https://en.wikipedia.org/wiki/Hinting) TrueType fonts |

List of graphic data tools

> [!TIP]
> Search more image tools using regex "`~Gworks-with::image`" in `aptitude(8)` (see [???](#_search_method_options_with_aptitude)).

Although GUI programs such as `gimp(1)` are very powerful, command line tools such as `imagemagick(1)` are quite useful for automating image manipulation via scripts.

The de facto image file format of the digital camera is the [Exchangeable Image File Format](https://en.wikipedia.org/wiki/Exchangeable_image_file_format) (EXIF) which is the [JPEG](https://en.wikipedia.org/wiki/JPEG) image file format with additional metadata tags. It can hold information such as date, time, and camera settings.

[The Lempel-Ziv-Welch (LZW) lossless data compression](https://en.wikipedia.org/wiki/Lempel-Ziv-Welch) patent has been expired. [Graphics Interchange Format (GIF)](https://en.wikipedia.org/wiki/Graphics_Interchange_Format) utilities which use the LZW compression method are now freely available on the Debian system.

> [!TIP]
> Any digital camera or scanner with removable recording media works with Linux through [USB storage](https://en.wikipedia.org/wiki/USB_flash_drive) readers since it follows the [Design rule for Camera Filesystem](https://en.wikipedia.org/wiki/Design_rule_for_Camera_File_system) and uses [FAT](https://en.wikipedia.org/wiki/File_Allocation_Table) filesystem. See [???](#_removable_storage_device).

## Miscellaneous data conversion

There are many other programs for converting data. Following packages caught my eyes using regex "`~Guse::converting`" in `aptitude(8)` (see [???](#_search_method_options_with_aptitude)).

| package | popcon | size | keyword | description |
|:---|:---|:---|:---|:---|
| `alien` | @-@popcon1@-@ | @-@psize1@-@ | rpm/tgz→deb | converter for the foreign package into the Debian package |
| `freepwing` | @-@popcon1@-@ | @-@psize1@-@ | EB→EPWING | converter from "Electric Book" (popular in Japan) to a single [JIS X 4081](https://ja.wikipedia.org/wiki/JIS_X_4081) format (a subset of the [EPWING](https://ja.wikipedia.org/wiki/EPWING) V1) |
| `calibre` | @-@popcon1@-@ | @-@psize1@-@ | any→EPUB | e-book converter and library management |

List of miscellaneous data conversion tools

You can also extract data from RPM format with the following.

    $ rpm2cpio file.src.rpm | cpio --extract
