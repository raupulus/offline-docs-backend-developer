---
title: Shell Syntax
source_url: https://www.gnu.org/software/bash/manual
source_path: 006-shell-syntax.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 60
---

## Shell Syntax

When the shell reads input, it proceeds through a sequence of operations. If the input indicates the beginning of a comment, the shell ignores the comment symbol (‘`#`’), and the rest of that line.

Otherwise, roughly speaking, the shell reads its input and divides the input into words and operators, employing the quoting rules to select which meanings to assign various words and characters.

The shell then parses these tokens into commands and other constructs, removes the special meaning of certain words or characters, expands others, redirects input and output as needed, executes the specified command, waits for the command’s exit status, and makes that exit status available for further inspection or processing.

### Shell Operation

The following is a brief description of the shell’s operation when it reads and executes a command. Basically, the shell does the following:

1.  Reads its input from a file (see [Shell Scripts](#Shell-Scripts)), from a string supplied as an argument to the `-c` invocation option (see [Invoking Bash](#Invoking-Bash)), or from the user’s terminal.

2.  Breaks the input into words and operators, obeying the quoting rules described in [Quoting](#Quoting). These tokens are separated by `metacharacters`. This step performs alias expansion (see [Aliases](#Aliases)).

3.  Parses the tokens into simple and compound commands (see [Shell Commands](#Shell-Commands)).

4.  Performs the various shell expansions (see [Shell Expansions](#Shell-Expansions)), breaking the expanded tokens into lists of filenames (see [Filename Expansion](#Filename-Expansion)) and commands and arguments.

5.  Performs any necessary redirections (see [Redirections](#Redirections)) and removes the redirection operators and their operands from the argument list.

6.  Executes the command (see [Executing Commands](#Executing-Commands)).

7.  Optionally waits for the command to complete and collects its exit status (see [Exit Status](#Exit-Status)).

### Quoting

quoting

Quoting is used to remove the special meaning of certain characters or words to the shell. Quoting can be used to disable special treatment for special characters, to prevent reserved words from being recognized as such, and to prevent parameter expansion.

Each of the shell metacharacters (see [Definitions](#Definitions)) has special meaning to the shell and must be quoted if it is to represent itself.

When the command history expansion facilities are being used (see [History Interaction](#History-Interaction)), the history expansion character, usually ‘`!`’, must be quoted to prevent history expansion. See [Bash History Facilities](#Bash-History-Facilities), for more details concerning history expansion.

There are four quoting mechanisms: the escape character, single quotes, double quotes, and dollar-single quotes.

#### Escape Character

A non-quoted backslash ‘`\`’ is the Bash escape character. It preserves the literal value of the next character that follows, removing any special meaning it has, with the exception of `newline`. If a `\newline` pair appears, and the backslash itself is not quoted, the `\newline` is treated as a line continuation (that is, it is removed from the input stream and effectively ignored).

#### Single Quotes

Enclosing characters in single quotes (‘`'`’) preserves the literal value of each character within the quotes. A single quote may not occur between single quotes, even when preceded by a backslash.

#### Double Quotes

Enclosing characters in double quotes (‘`"`’) preserves the literal value of all characters within the quotes, with the exception of ‘`$`’, ‘`` ` ``’, ‘`\`’, and, when history expansion is enabled, ‘`!`’. When the shell is in POSIX mode (see [Bash POSIX Mode](#Bash-POSIX-Mode)), the ‘`!`’ has no special meaning within double quotes, even when history expansion is enabled. The characters ‘`$`’ and ‘`` ` ``’ retain their special meaning within double quotes (see [Shell Expansions](#Shell-Expansions)). The backslash retains its special meaning only when followed by one of the following characters: ‘`$`’, ‘`` ` ``’, ‘`"`’, ‘`\`’, or `newline`. Within double quotes, backslashes that are followed by one of these characters are removed. Backslashes preceding characters without a special meaning are left unmodified.

A double quote may be quoted within double quotes by preceding it with a backslash. If enabled, history expansion will be performed unless an ‘`!`’ appearing in double quotes is escaped using a backslash. The backslash preceding the ‘`!`’ is not removed.

The special parameters ‘`*`’ and ‘`@`’ have special meaning when in double quotes (see [Shell Parameter Expansion](#Shell-Parameter-Expansion)).

#### ANSI-C Quoting

quoting, ANSI

dollar-single quote quoting

Character sequences of the form `$'string'` are treated as a special kind of single quotes. The sequence expands to \<string\>, with backslash-escaped characters in \<string\> replaced as specified by the ANSI C standard. Backslash escape sequences, if present, are decoded as follows:

`\a`  
alert (bell)

`\b`  
backspace

`\e`; `\E`  
An escape character (not in ANSI C).

`\f`  
form feed

`\n`  
newline

`\r`  
carriage return

`\t`  
horizontal tab

`\v`  
vertical tab

`\\`  
backslash

`\'`  
single quote

`\"`  
double quote

`\?`  
question mark

`\nnn`  
The eight-bit character whose value is the octal value \<nnn\> (one to three octal digits).

`\xHH`  
The eight-bit character whose value is the hexadecimal value \<HH\> (one or two hex digits).

`\uHHHH`  
The Unicode (ISO/IEC 10646) character whose value is the hexadecimal value \<HHHH\> (one to four hex digits).

`\UHHHHHHHH`  
The Unicode (ISO/IEC 10646) character whose value is the hexadecimal value \<HHHHHHHH\> (one to eight hex digits).

`\cx`  
A control-\<x\> character.

The expanded result is single-quoted, as if the dollar sign had not been present.

#### Locale-Specific Translation

localization

internationalization

native languages

translation, native languages

Prefixing a double-quoted string with a dollar sign (‘`$`’), such as `$"hello, world"`, causes the string to be translated according to the current locale. The `gettext` infrastructure performs the lookup and translation, using the `LC_MESSAGES`, `TEXTDOMAINDIR`, and `TEXTDOMAIN` shell variables, as explained below. See the gettext documentation for additional details not covered here. If the current locale is `C` or `POSIX`, if there are no translations available, or if the string is not translated, the dollar sign is ignored, and the string is treated as double-quoted as described above. Since this is a form of double quoting, the string remains double-quoted by default, whether or not it is translated and replaced. If the `noexpand_translation` option is enabled using the `shopt` builtin (see [The Shopt Builtin](#The-Shopt-Builtin)), translated strings are single-quoted instead of double-quoted.

The rest of this section is a brief overview of how you use gettext to create translations for strings in a shell script named \<scriptname\>. There are more details in the gettext documentation.

internationalized scripts

string translations

Once you’ve marked the strings in your script that you want to translate using \$"…", you create a gettext "template" file using the command

    bash --dump-po-strings scriptname > domain.pot

The \<domain\> is your message domain. It’s just an arbitrary string that’s used to identify the files gettext needs, like a package or script name. It needs to be unique among all the message domains on systems where you install the translations, so gettext knows which translations correspond to your script. You’ll use the template file to create translations for each target language. The template file conventionally has the suffix ‘`.pot`’.

You copy this template file to a separate file for each target language you want to support (called "PO" files, which use the suffix ‘`.po`’). PO files use various naming conventions, but when you are working to translate a template file into a particular language, you first copy the template file to a file whose name is the language you want to target, with the ‘`.po`’ suffix. For instance, the Spanish translations of your strings would be in a file named ‘`es.po`’, and to get started using a message domain named "example," you would run

    cp example.pot es.po

Ultimately, PO files are often named \<domain\>.po and installed in directories that contain multiple translation files for a particular language.

Whichever naming convention you choose, you will need to translate the strings in the PO files into the appropriate languages. This has to be done manually.

When you have the translations and PO files complete, you’ll use the gettext tools to produce what are called "MO" files, which are compiled versions of the PO files the gettext tools use to look up translations efficiently. MO files are also called "message catalog" files. You use the `msgfmt` program to do this. For instance, if you had a file with Spanish translations, you could run

    msgfmt -o es.mo es.po

to produce the corresponding MO file.

Once you have the MO files, you decide where to install them and use the `TEXTDOMAINDIR` shell variable to tell the gettext tools where they are. Make sure to use the same message domain to name the MO files as you did for the PO files when you install them.

LANG

LC_MESSAGES

TEXTDOMAIN

TEXTDOMAINDIR

Your users will use the `LANG` or `LC_MESSAGES` shell variables to select the desired language.

You set the `TEXTDOMAIN` variable to the script’s message domain. As above, you use the message domain to name your translation files.

You, or possibly your users, set the `TEXTDOMAINDIR` variable to the name of a directory where the message catalog files are stored. If you install the message files into the system’s standard message catalog directory, you don’t need to worry about this variable.

The directory where the message catalog files are stored varies between systems. Some use the message catalog selected by the `LC_MESSAGES` shell variable. Others create the name of the message catalog from the value of the `TEXTDOMAIN` shell variable, possibly adding the ‘`.mo`’ suffix. If you use the `TEXTDOMAIN` variable, you may need to set the `TEXTDOMAINDIR` variable to the location of the message catalog files, as above. It’s common to use both variables in this fashion: `$TEXTDOMAINDIR`/`$LC_MESSAGES`/LC_MESSAGES/`$TEXTDOMAIN`.mo.

If you used that last convention, and you wanted to store the message catalog files with Spanish (es) and Esperanto (eo) translations into a local directory you use for custom translation files, you could run

    TEXTDOMAIN=example
    TEXTDOMAINDIR=/usr/local/share/locale

    cp es.mo ${TEXTDOMAINDIR}/es/LC_MESSAGES/${TEXTDOMAIN}.mo
    cp eo.mo ${TEXTDOMAINDIR}/eo/LC_MESSAGES/${TEXTDOMAIN}.mo

When all of this is done, and the message catalog files containing the compiled translations are installed in the correct location, your users will be able to see translated strings in any of the supported languages by setting the `LANG` or `LC_MESSAGES` environment variables before running your script.

### Comments

comments, shell

In a non-interactive shell, or an interactive shell in which the `interactive_comments` option to the `shopt` builtin is enabled (see [The Shopt Builtin](#The-Shopt-Builtin)), a word beginning with ‘`#`’ introduces a comment. A word begins at the beginning of a line, after unquoted whitespace, or after an operator. The comment causes that word and all remaining characters on that line to be ignored. An interactive shell without the `interactive_comments` option enabled does not allow comments. The `interactive_comments` option is enabled by default in interactive shells. See [Interactive Shells](#Interactive-Shells), for a description of what makes a shell interactive.
