set nocompatible
source $VIMRUNTIME/vimrc_example.vim
"source $VIMRUNTIME/mswin.vim
"behave mswin
set background=dark

let g:pathogen_disabled = ["minibufexpl","suround"]
if has("win32")
	call pathogen#infect()
	call pathogen#helptags()
	call pathogen#infect()
else
	execute pathogen#infect()
endif
set runtimepath^=~/.vim/bundle/ctrlp.vim
set wildignore+=*/tmp/*,*/target/*,*/dist/*,*.so,*.swp,*.zip,*.class,*.jar,*.war,*.pyc
set complete-=i
set complete-=t
nnoremap ,cd :cd %:p:h<CR>:pwd<CR>

let g:ctrlp_regexp = 1
let g:session_autosave_periodic=5
let g:session_autosave="yes"
let g:session_autosave_silent=1

"helpful command for pane navigation when uwing c-w in tmux
nnoremap <C-J> <C-W><C-J>
nnoremap <C-J> <C-W><C-K>
nnoremap <C-Q> <C-W><C-Q>

"another way to do after the fact () wrapping around visual text"
"to me this seems cleaner
:vnoremap _( <ESC>`>a)<ESC>`<i(<ESC>
:vnoremap _' <ESC>`>a'<ESC>`<i'<ESC>
:vnoremap _" <ESC>`>a"<ESC>`<i"<ESC>
:vnoremap _# <ESC>`>a#<ESC>`<i#<ESC>
:vnoremap _{ <ESC>`>a}<ESC>`<i{<ESC>
:vnoremap _[ <ESC>`>a]<ESC>`<i[<ESC>
""----------------------------------------
"au BufRead,BufNewFile *.txt		setfiletype text

:inoremap ( ()<ESC>:let leavechar=")"<CR>i
:inoremap [ []<ESC>:let leavechar="]"<CR>i
:inoremap { {}<ESC>:let leavechar="}"<CR>i
:inoremap " ""<ESC>:let leavechar="\""<CR>i
:inoremap ' ''<ESC>:let leavechar="'"<CR>i

:imap <C-j> <ESC>:exec "normal f" . leavechar<CR>a

:nnoremap j gj
:nnoremap k gk

augroup vimrc_filetype
 autocmd!
 autocmd FileType c call s:MyCSettings()
 autocmd FileType text call s:MyTxtSettings()
 autocmd FileType tex call s:MyTxtSettings()
 autocmd FileType python call s:MyPYSettings()
 autocmd FileType pig call s:MyPigSettings()
 autocmd FileType html call MyHtmlSettings()
 autocmd FileType structure call MyHtmlSettings()
 autocmd FileType css call s:MyCssSettings()
 autocmd FileType java call s:MyJavaSettings()
 autocmd FileType vim call s:MyVimSettings()
 autocmd FileType matlab call s:MyMatlabSettings()
augroup end
"autocmd VimLeavePre * call StoreHistory()
"

function! s:MyCSettings()
  " Insert comments markers
  map - :s/^/\/\//<CR>:nohlsearch<CR>
endfunction

function! s:MyTxtSettings()
  " Insert comments markers
  map <Leader>N i%%%<ESC>
  map <Leader>P i***<ESC>
  map <Leader>V i$$$<ESC>
  map <Leader>I i&&&<ESC>
  map <Leader>D i@@@<ESC>
  map <Leader>F i!!!<ESC>
  map <Leader>Q i###<ESC>
  map <Leader>R iRRR<ESC>
  map <Leader>d mz\D`m\D`z
  map <Leader>q mz\Q`m\Q`z
  map <Leader>i mz\I`m\I`z
  map <Leader>v mz\V`m\V`z
  map <Leader>f mz\F`m\F`z
  map <Leader>n mz\N`m\N`z
  map <Leader>p mz\P`m\P`z
  map <Leader>r mz\R`m\R`z
  map <Leader>c i CCC CCC<ESC>2b3la
  map <Leader>h i TTT TTT<ESC>2b3la "h is for thought


  set wrap linebreak nolist  
  :nnoremap j gj
  :nnoremap k gk
endfunction

function! s:MyJavaSettings()
  " Insert comments markers
  map - :s/\S.*/\/\/\0\/\//<CR>:noh<CR>
  map _ :s/\/\/\(.*\)\/\//\1/<CR>:noh<CR>
"  map z :s/^/\/\*/|:s/$/\*\//|:nohlsearch
  let @a='^i/*0$a*/'
  set foldmethod=indent
  set foldlevel=99
  ""set foldnestmax=2
"  set viminfo+=n$HOME/_viminfo_css"
endfunction


"good for pig navigation
function! s:MyPigSettings()
  " Insert comments markers
  map - :s/\S.*/--\0\--/<CR>:noh<CR>
  map _ :s/--\(.*\)--/\1/<CR>:noh<CR>
"  map z :s/^/\/\*/|:s/$/\*\//|:nohlsearch
  let @a='^i/*0$a*/'
  set foldmethod=indent
  set foldlevel=99
  ""set foldnestmax=2
"  set viminfo+=n$HOME/_viminfo_css"
endfunction

"good for python navigation
function! s:MyPYSettings()
  " Insert comments markers
  map - :s/\S.*/\#\0\#/<CR>:noh<CR>
  map _ :s/\#\(.*\)\#/\1/<CR>:noh<CR>
"  map z :s/^/\/\*/|:s/$/\*\//|:nohlsearch
  let @a='^i/*0$a*/'
  set foldmethod=indent
  set foldlevel=99
  ""set foldnestmax=2
"  set viminfo+=n$HOME/_viminfo_css"
endfunction

function! s:MyCssSettings()
  " Insert comments markers
  let @a='^i/*0$a*/'
  map - :s/.*/\/\*\0\*\//<CR>:noh<CR>
  map _ :s/\/\*\(.*\)\*\//\1/<CR>:noh<CR>
"  set viminfo+=n$HOME/_viminfo_css"
endfunction

function! MyHtmlSettings()
  " Insert comments markers
"  map - :s/^/\{\#/<CR>:s/$/\#\}/<CR>:nohlsearch<CR>"
  map - :s/.*/\{\#\0\#\}/<CR>:noh<CR>
  map _ :s/{\#\(.*\)\#}/\1/<CR>:noh<CR>
  set foldmethod=indent
  set foldlevel=99
  :abbre ho <!-- 
  :abbre hc --!>
endfunction

function! s:MyVimSettings()
  " Insert comments markers
"  map - :s/^/\"/<CR>:s/$/\"/<CR>:nohlsearch<CR>"
  map - :s/.*/\"\0/<CR>:noh<CR>
  map _ :s/\"\(.*\)/\1/<CR>:noh<CR>"
endfunction
function! s:MyMatlabSettings()
  " Insert comments markers
"  map - :s/^/\"/<CR>:s/$/\"/<CR>:nohlsearch<CR>"
  map - :s/.*/\%\0/<CR>:noh<CR>
  map _ :s/\%\(.*\)/\1/<CR>:noh<CR>
endfunction

"imap <S-CR> <Esc>:w<CR>
imap  <Esc>:w<CR>
nmap  <Esc>:w<CR>
"map <S-CR> <Esc>:w<CR>


set autoindent
set noexpandtab
set tabstop=2
set shiftwidth=2
""set noexpandtab
""set tabstop=4
"set shiftwidth=4
set incsearch
set infercase
set laststatus=2
set shortmess=a
set number
set ignorecase
set smartcase

set clipboard=unnamed
set cmdheight=2
set timeoutlen=1000 ttimeoutlen=0



map sp :set paste!<CR>:set paste?<CR>



set history=1000

set backupdir=$HOME/tmp
set directory=$HOME/tmp

set autowrite
set wildchar=<Tab> wildmenu wildmode=full

:nnoremap <F9> :bnext<CR>
:nnoremap <F10> :bprevious<CR>


"nmap <leader>a <Esc>:Ack!
nmap <silent> <CR> :silent set invhls<CR>


nmap g<Space> :b#<CR>
"nmap <S-Space> :b#<CR>
nmap <Space> za

nmap ,s :source $MYVIMRC
nmap ,v :e $MYVIMRC
nmap ,t :e $HOME/.vim/vimtips/vimtips.txt<CR>
nmap ,b :e $HOME/.vim/bestofvim.txt<CR>
if has("gui_running")
 if has("win32")
    " Open the folder containing the currently open file. Double <CR> at end
    " is so you don't have to hit return after command. Double quotes are
    " not necessary in the 'explorer.exe %:p:h' section.
    :map <silent> <C-F5> :if expand("%:p:h") != ""<CR>:!start explorer.exe %:p:h<CR>:endif<CR><CR>
  endif
endif

nmap <Leader>x :call writefile(split(@@, "\n", 1), '/home/psmith/x.tmp')<CR>
nmap <Leader>p :r /home/psmith/x.tmp<CR>

function! CHANGE_CURR_DIR()
	let _dir = expand("%:p:h")
	exec "cd " . _dir
	unlet _dir
endfunction

set diffopt+=iwhite
set diffexpr=MyDiff()

function MyDiff()
   let opt = '-a --binary '
   if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
   if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
   let arg1 = v:fname_in
   if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
   let arg2 = v:fname_new
   if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
   let arg3 = v:fname_out
   if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
   if $VIMRUNTIME =~ ' '
     if &sh =~ '\<cmd'
       if empty(&shellxquote)
         let l:shxq_sav = ''
         set shellxquote&
       endif
       let cmd = '"' . $VIMRUNTIME . '\diff"'
     else
       let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
     endif
   else
     let cmd = $VIMRUNTIME . '\diff'
   endif
   silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3
   if exists('l:shxq_sav')
     let &shellxquote=l:shxq_sav
   endif
 endfunction

function MyDiffOld()
  let opt = '-a --binary '
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
  let arg1 = v:fname_in
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
  let arg2 = v:fname_new
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
  let arg3 = v:fname_out
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
  let eq = ''
  if $VIMRUNTIME =~ ' '
    if &sh =~ '\<cmd'
      let cmd = '""' . $VIMRUNTIME . '\diff"'
      let eq = '"'
    else
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
    endif
  else
    let cmd = $VIMRUNTIME . '\diff'
  endif
  silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3 . eq
endfunction


" Jump to the next or previous line that has the same level or a lower
" level of indentation than the current line.
"
" exclusive (bool): true: Motion is exclusive
" false: Motion is inclusive
" fwd (bool): true: Go to next line
" false: Go to previous line
" lowerlevel (bool): true: Go to line with lower indentation level
" false: Go to line with the same indentation level
" skipblanks (bool): true: Skip blank lines
" false: Don't skip blank lines
function! NextIndent(exclusive, fwd, lowerlevel, skipblanks)
  let line = line('.')
  let column = col('.')
  let lastline = line('$')
  let indent = indent(line)
  let stepvalue = a:fwd ? 1 : -1
  while (line > 0 && line <= lastline)
    let line = line + stepvalue
    if ( ! a:lowerlevel && indent(line) == indent ||
          \ a:lowerlevel && indent(line) < indent)
      if (! a:skipblanks || strlen(getline(line)) > 0)
        if (a:exclusive)
          let line = line - stepvalue
        endif
        exe line
        exe "normal " column . "|"
        return
      endif
    endif
  endwhile
endfunction

" Moving back and forth between lines of same or lower indentation.
nnoremap <silent> [l :call NextIndent(0, 0, 0, 1)<CR>
nnoremap <silent> ]l :call NextIndent(0, 1, 0, 1)<CR>
nnoremap <silent> [L :call NextIndent(0, 0, 1, 1)<CR>
nnoremap <silent> ]L :call NextIndent(0, 1, 1, 1)<CR>
vnoremap <silent> [l <Esc>:call NextIndent(0, 0, 0, 1)<CR>m'gv''
vnoremap <silent> ]l <Esc>:call NextIndent(0, 1, 0, 1)<CR>m'gv''
vnoremap <silent> [L <Esc>:call NextIndent(0, 0, 1, 1)<CR>m'gv''
vnoremap <silent> ]L <Esc>:call NextIndent(0, 1, 1, 1)<CR>m'gv''
onoremap <silent> [l :call NextIndent(0, 0, 0, 1)<CR>
onoremap <silent> ]l :call NextIndent(0, 1, 0, 1)<CR>
onoremap <silent> [L :call NextIndent(1, 0, 1, 1)<CR>
onoremap <silent> ]L :call NextIndent(1, 1, 1, 1)<CR>
