# Source
YouTube:
    Matering the Vim Language
    How to do 90% of What Plugins do (with just vim)

# Normal mode

All commands work as a word + noun (dw = delete word)

## Words:
`d` delete
`D` delete till the end of a line
`c` change (delete + insert)
`C` change till the end of a line
`>` indenti (works with hjkl operators)
`<` outdent 
`v` visually select
`V` visuall select lines
`y` yank/copy
`Y` yank whole line

## Nouns:
`w` word forward
`b` word backward
`2j` jump 2 ammount of lines
`f_` go to first appearance of character _ in that line
`F_` same thing but backwards
`t_` go to a character before the first appearance of character _ in that line
`T_` same thing but backwards
`/` search for any character, word
`?` same thing but backwards
`m` set mark, eg. mq sets q mark on place where the cursor is
`{}` beggining/end of paragraph
`%` goes to next paren of brackets
`.` repeats the last command executed (whatever it is)
`diw` delete the whole word on which the coursor is on
`di"` delete everything inside the ""
`di]` delete everything inside of []
`dip` delete everythins indside of paragraph
`dit` delete everything inside of a tag eg `<html>___ </html>`
`d'q` delete everyting until the marker q
 same operations work with c, v, y
`daw|"|]` same as diw but with a it captures also the space that follows i
`~` replace case upper --> lower
`gUw` change whole word to uppecrase
`guw` change whole word to lowercase
`gUU` whole line uppercase

## Registers
`"` used to name a registry
`"cyy` yank whole line to registry named "c"
`"cp` paste from "c" registry

## Commands:
`:find <file_name>` finds a file name in the current directory
`:read <file_name>` adds the content of the file to this document
`:ls` lists all files which are currently opened in vim
`:b <part_of_the_filename>` opens that file if it is already opened in vim
`:echo expand(%)` get the name of the currently opened file
`g` at the end of the command means it applies to the whole document
`v` means an NOT to match the given pattern

## Control commands

### Normal Mode 

`ctrl + ]` jump to a definition of a tag
`ctrl + g]` will show all the occurencies of this defined tag 
`ctrl + t` jump back up the tag stack
`ctrl + n` autocompletes a word, n is for next
`ctrl + p` autocompletes a word, p is for previous
`ctrl + w + s` split window horizontally
`ctrl + w + v` split window vertical
`ctrl + w + q` remove split
`ctrl + w + w` move to next window

### Insert Mode

`ctrl + x ctrl + n` autocomplete but with words only within this file
`ctrl + x ctrl + f` fzf complete path
`ctrl + x ctrl + k` fzf complete word (from whole dictionary)
`ctrl + x ctrl + j` fzf complete file with Ag (silver-searcher)
`ctrl + x ctrl + l` fzf complete line
`ctrl + x ctrl + ]` autocompletes a tag 

### Buffers

Buffers are used when more that one files are open within the same Vim
`:ls` show available files in buffer
`:bn` go to next file in buffed
`:bp` go to previous file in buffer
`:b<number>` go to specific buffer
`:b#` go to previous active buffer
`:bd` close current buffer

## Plugin commands

### surround plugin
`ysiwX` surround word with X (.,[]{} whatever)
`cs"'` replace surrunding " with ' if text is already surrounded
`dsX` delete exisitng X surrundings

### comment plugin
`gcc` comment out a line
`gc2j` comment N number of lines below
`gcgc` uncomment adjacent commented lines

### vim-system-copy
`cpiw` copy word to system plugin
`cpi'` copy content inside of '' to system plugin
`cvi'` paste content of system clipboard inside of ''

### vim folding

`zi` switch folding on or off
`za` toggle current fold open/closed
`zc` close current fold
`zR` open all folds
`zM` close all folds
`zv` expand folds to reveal coursor

### FZF
`:FZF` starts a regular fuzzyfinder  
`:Files` searches for files in current git dir and shows preview
`:Rg` initiates ripgrep search, searches also for phrases within files
`:Ag` initiates silverSearcher, simlar to ripgrep
`:Blines` something like find (`/` ) in vim but it will show lines where it found it and you can jumb to that line
`:Lines` does search in all opened buffers
`:History:` command history
`:Buffers` serach opened buffers

## Leader shortcuts

### Normal mode

`-` split horizontal
`q` quit
`q!` quit without saving
`w` save
`e` FZF 
`r` FZF buffers
`t` FZF git files (shows all git files)
`y` NERDTree find
`u`
`i`
`o`
`p`
`[`
`]`
`a`
`s` FZF git modified files
`d`
`f`
`g` FZF ripgrep
`h` move to left split
`j` move to lower split
`k` move to upper split
`l` move to right split
`;`
`'`
`\` split vertical
`z`
`x` save and close
`c`
`v` toggle paste
`b`
`n` NERDTree open
`m`
`,` save
`.` switch between current and last buffer
`<space>` clear whitespace at the end of the line

### Insert mode

`-`
`q` quit current file
`q!` quit current file without saving
`w` save current file
`e`
`r` 
`t`
`y`
`u`
`i`
`o`
`p`
`[`
`]`
`a`
`s`
`d`
`f`
`g`
`h`
`j`
`jk` go to normal mode
`k`
`l`
`;`
`'`
`\`
`z`
`x` save and exit
`c`
`v`
`b`
`n`
`m`
`,`
`.`
`<space>` 





















