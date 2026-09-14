---
title: History Expansion
source_url: https://www.gnu.org/software/bash/manual
source_path: 051-history-expansion.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 510
---

## History Expansion

history expansion

The shell provides a history expansion feature that is similar to the history expansion provided by `csh` (also referred to as history substitution where appropriate). This section describes the syntax used to manipulate the history information.

History expansion is enabled by default for interactive shells, and can be disabled using the `+H` option to the `set` builtin command (see [The Set Builtin](#The-Set-Builtin)). Non-interactive shells do not perform history expansion by default, but it can be enabled with `set -H`.

History expansions introduce words from the history list into the input stream, making it easy to repeat commands, insert the arguments to a previous command into the current input line, or fix errors in previous commands quickly.

History expansion is performed immediately after a complete line is read, before the shell breaks it into words, and is performed on each line individually. Bash attempts to inform the history expansion functions about quoting still in effect from previous lines.

History expansion takes place in two parts. The first is to determine which entry from the history list should be used during substitution. The second is to select portions of that entry to include into the current one.

The entry selected from the history is called the event, and the portions of that entry that are acted upon are words. Various modifiers are available to manipulate the selected words. The entry is split into words in the same fashion that Bash does when reading input, so that several words surrounded by quotes are considered one word. The event designator selects the event, the optional word designator selects words from the event, and various optional modifiers are available to manipulate the selected words.

History expansions are introduced by the appearance of the history expansion character, which is ‘`!`’ by default. History expansions may appear anywhere in the input, but do not nest.

History expansion implements shell-like quoting conventions: a backslash can be used to remove the special handling for the next character; single quotes enclose verbatim sequences of characters, and can be used to inhibit history expansion; and characters enclosed within double quotes may be subject to history expansion, since backslash can escape the history expansion character, but single quotes may not, since they are not treated specially within double quotes.

When using the shell, only ‘`\`’ and ‘`'`’ may be used to escape the history expansion character, but the history expansion character is also treated as quoted if it immediately precedes the closing double quote in a double-quoted string.

Several characters inhibit history expansion if found immediately following the history expansion character, even if it is unquoted: space, tab, newline, carriage return, ‘`=`’, and the other shell metacharacters.

There is a special abbreviation for substitution, active when the \<quick substitution\> character (described above under `histchars`) is the first character on the line. It selects the previous history list entry, using an event designator equivalent to `!!`, and substitutes one string for another in that entry. It is described below (see [Event Designators](#Event-Designators)). This is the only history expansion that does not begin with the history expansion character.

Several shell options settable with the `shopt` builtin (see [The Shopt Builtin](#The-Shopt-Builtin)) modify history expansion behavior If the `histverify` shell option is enabled, and Readline is being used, history substitutions are not immediately passed to the shell parser. Instead, the expanded line is reloaded into the Readline editing buffer for further modification. If Readline is being used, and the `histreedit` shell option is enabled, a failed history expansion is reloaded into the Readline editing buffer for correction.

The `-p` option to the `history` builtin command shows what a history expansion will do before using it. The `-s` option to the `history` builtin may be used to add commands to the end of the history list without actually executing them, so that they are available for subsequent recall. This is most useful in conjunction with Readline.

The shell allows control of the various characters used by the history expansion mechanism with the `histchars` variable, as explained above (see [Bash Variables](#Bash-Variables)). The shell uses the history comment character to mark history timestamps when writing the history file.

### Event Designators

event designators

An event designator is a reference to an entry in the history list. The event designator consists of the portion of the word beginning with the history expansion character, and ending with the word designator if one is present, or the end of the word. Unless the reference is absolute, events are relative to the current position in the history list. <span class="indexterm cp" role="cp"></span>

`!`  
Start a history substitution, except when followed by a space, tab, the end of the line, ‘`=`’, or the rest of the shell metacharacters defined above (see [Definitions](#Definitions)).

`!n`  
Refer to history list entry \<n\>.

`!-n`  
Refer to the history entry minus \<n\>.

`!!`  
Refer to the previous entry. This is a synonym for ‘`!-1`’.

`!string`  
Refer to the most recent command preceding the current position in the history list starting with \<string\>.

`!?string[?]`  
Refer to the most recent command preceding the current position in the history list containing \<string\>. The trailing ‘`?`’ may be omitted if the \<string\> is followed immediately by a newline. If \<string\> is missing, this uses the string from the most recent search; it is an error if there is no previous search string.

`^string1^string2^`  
Quick Substitution. Repeat the last command, replacing \<string1\> with \<string2\>. Equivalent to `!!:s^string1^string2^`.

`!#`  
The entire command line typed so far.

### Word Designators

Word designators are used to select desired words from the event. They are optional; if the word designator isn’t supplied, the history expansion uses the entire event. A ‘`:`’ separates the event specification from the word designator. It may be omitted if the word designator begins with a ‘`^`’, ‘`$`’, ‘`*`’, ‘`-`’, or ‘`%`’. Words are numbered from the beginning of the line, with the first word being denoted by 0 (zero). That first word is usually the command word, and the arguments begin with the second word. Words are inserted into the current line separated by single spaces.

For example,

`!!`  
designates the preceding command. When you type this, the preceding command is repeated in toto.

`!!:$`  
designates the last word of the preceding command. This may be shortened to `!$`.

`!fi:2`  
designates the second argument of the most recent command starting with the letters `fi`.

Here are the word designators:

`0 (zero)`  
The `0`th word. For the shell, and many other, applications, this is the command word.

`n`  
The \<n\>th word.

`^`  
The first argument: word 1.

`$`  
The last word. This is usually the last argument, but expands to the zeroth word if there is only one word in the line.

`%`  
The first word matched by the most recent ‘`?string?`’ search, if the search string begins with a character that is part of a word. By default, searches begin at the end of each line and proceed to the beginning, so the first word matched is the one closest to the end of the line.

`x-y`  
A range of words; ‘`-y`’ abbreviates ‘`0-y`’.

`*`  
All of the words, except the `0`th. This is a synonym for ‘`1-$`’. It is not an error to use ‘`*`’ if there is just one word in the event; it expands to the empty string in that case.

`x*`  
Abbreviates ‘`x-$`’.

`x-`  
Abbreviates ‘`x-$`’ like ‘`x*`’, but omits the last word. If ‘`x`’ is missing, it defaults to 0.

If a word designator is supplied without an event specification, the previous command is used as the event, equivalent to `!!`.

### Modifiers

After the optional word designator, you can add a sequence of one or more of the following modifiers, each preceded by a ‘`:`’. These modify, or edit, the word or words selected from the history event.

`h`  
Remove a trailing filename component, leaving only the head.

`t`  
Remove all leading filename components, leaving the tail.

`r`  
Remove a trailing suffix of the form ‘`.suffix`’, leaving the basename.

`e`  
Remove all but the trailing suffix.

`p`  
Print the new command but do not execute it.

`q`  
Quote the substituted words, escaping further substitutions.

`x`  
Quote the substituted words as with ‘`q`’, but break into words at spaces, tabs, and newlines. The ‘`q`’ and ‘`x`’ modifiers are mutually exclusive; expansion uses the last one supplied.

`s/old/new/`  
Substitute \<new\> for the first occurrence of \<old\> in the event line. Any character may be used as the delimiter in place of ‘`/`’. The delimiter may be quoted in \<old\> and \<new\> with a single backslash. If ‘`&`’ appears in \<new\>, it is replaced with \<old\>. A single backslash quotes the ‘`&`’ in \<old\> and \<new\>. If \<old\> is null, it is set to the last \<old\> substituted, or, if no previous history substitutions took place, the last \<string\> in a !?\<string\>`[?]` search. If \<new\> is null, each matching \<old\> is deleted. The final delimiter is optional if it is the last character on the input line.

`&`  
Repeat the previous substitution.

`g`; `a`  
Cause changes to be applied over the entire event line. This is used in conjunction with ‘`s`’, as in `gs/old/new/`, or with ‘`&`’.

`G`  
Apply the following ‘`s`’ or ‘`&`’ modifier once to each word in the event.
