# Default character shortcuts

## Normal mode

### Alphabet

`a` append - add text after coursor
`A` append - at the end of the line

`b` back - go to the beggining of previous word
`B` back - go to the beggining of previous word but ignore special characters

`c` change (delete and insert). It requires motion
`cc` deletes entire line and goes to insert mode
`C` deletes everyting till the end of the line and goes to insert mode

`d` delete. It requires motion
`dd` deletes entire line
`D` deletes everyting till the end of the line

`e` end - go to the end of the next word
`ge` end - go to the end of the previous word
`E` end - go to the end of the previous word but ignore special characters
`gE` end - go to the end of the previous word but ignore special characters

`f` forward to - go to next searched character
`;` repeats the last character searched forward
`F` forward to - go to previous searched character
`,` repeats the last character searched backward

`g` go to -
`gg` go to the first line
`G` go to the last line
`gX` used as modifier with many keys

`h` left motion
`H` high - go to the top of the current window

`i` insert - add text before the coursor
`gi` should go to last insert mode but is overwritten by coc plugin
`I` insert - at the beggining of the line

`j` down motion
`J` join - join current and next line

`k` up motion
`K` look up for the definition of the current word (may need a plugin)

`l` right motion
`L` low - go to the bottom of the current window

`mX` mark - set a mark with certain letter (lowercase letter for current buffer,)
`'X` go to mark with certain letter
`M` middle - go to the middle of the current window

`n` next - goes to next item located by search `/`
`N` previous - goes to previous item located by search `/`

`o` insert below the current line
`O` insert above the current line

`p` put/paste - paste below current line or after coursor
`P` put/paste - paste above current line or before coursor

`q` record macro
`@q` repeat macro
`Q` go to Ex mode

`r` replace - replaces single character
`R` go to replace mode

`s` substitution - like replace but goes in isert mode. replaces by easymotion key
`S` substitution - deletes entire line and goes to insert mode, like `cc`

`t` till - like `f` just goes before the searched character
`T` till - like `f` just goes before the searched character but backwards

`u` undo
`U` undos all changes on a single line

`v` visual - go to visualsual mode
`V` v-line - selects whole line

`w` word - go to beggining of next word
`W` word - go to beggining of next word but ignore special characters

`x` delete - deletes current character righ of the coursor
`X` delete - deletes current character letterft of the coursor (like backspace)

`y` yank - put in clipboard
`Y` yank - put in clipboard from coursor till the end of the line

`z` wors with combination of other characters
`zt` scrolls so the current line is at the top of the screen
`zb` scrolls so the current line is at the bottom of the screen
`z.` scrolls so the current line is at the midddle of the screen and puts coursor to the begginging
`zz` scrolls so the current line is at the midddle of the screen but leave the coursor in place
`zl` scroll right
`zl` scroll left
`ZZ` save and exit
`ZQ` force exit without saving, like `:q!`


### Numerical

`1`
`2`
`3`
`4`
`5`
`6`
`7`
`8`
`9`
`0`

### Special characters

`~` tilde - mostly case switch can be used with visual mode
`g~~` switch case on entire line

`<backtick>` backtick - jump to mark

`!` bang - in command mode allows execution of external command
`!l` in command mode allow formatting of current line by external program

`@` at - reply a macro with `@<macro_name>`
`@@` reply previously recorded macro

`#` pound - jump to the previous occurance of the current word

`$` dollar - jump to the end of the line
`g$` end of the curent line line goes to multiple rows

`%` percent sign - jumpt through matching elements
`g%` percent sign - jumpt through matching elements backwards
`:e %:h` in command mode shows the path of current file 

`^` hat or carret - go to fist non-blank sharacter of the line
`^` can be used in regex as a begginging of a line

`&` ampersand - repeats last substitution

`*` star - jump to next occurance of a word oposite of `#`

`(` parenthasie - jump back a sentance
`)` parenthasie - jump forward a sentance

`_` underscore - act on next `<count>` -1 lines

`+` plus - act on next `<count>` lines

`-` dash - act on previous `<count>` -1 lines

`+` plus - same as underscore

`=` equal sign
`==` filter the current line with vim or external app

`{` curlies - move back through paragraphs
`}` curlies - move forward through paragraphs
`]}` go to first closing curlie
`[{` go to first opening curlie

`[` brackets - navigate through a lot of things...
`]`
`ctrl]` go to tag definition
`]c` next change in a diff file
`[c` previous change in a diff file
`[I` shows number of occurencies of the current word

`;`
`'`
`\`
`,`
`.`
`<space>` save

{
  "a": 1,
  "b": 2,
  "c": 3
}
