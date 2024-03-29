let mapleader = ","
set nocompatible
filetype off
filetype plugin indent on
syntax on
execute pathogen#infect()
execute pathogen#helptags()
set number
set relativenumber
set ruler
set vb
set nocp
set autoindent
set expandtab
set softtabstop=2
set shiftwidth=2
set cindent
set ts=2
set scrolloff=2
set clipboard=unnamedplus
let g:SuperTabDefaultCompletionType = "context"
let g:jedi#popup_on_dot = 0  " disables the autocomplete to popup whenever you press .

set cursorline
set colorcolumn=81
highlight ColorColumn ctermbg=darkgrey
highlight SpellBad ctermbg=darkred
"execute "set colorcolumn=" . join(range(80,335), ',')

au BufRead /tmp/mutt-* set tw=72
au BufRead /tmp/mutt-* set spell
au BufRead /tmp/mutt-* set cursorline
au BufRead /tmp/mutt-* set colorcolumn=73
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

let g:syntastic_tex_checkers = []

set grepprg=grep\ -nH\ $*
let g:tex_flavor = "latex"
" use pdflatex
let g:Tex_DefaultTargetFormat='pdf'
let g:Tex_MultipleCompileFormats='pdf,dvi'
let g:Tex_CompileRule_pdf = 'mkdir -p tmp; pdflatex -output-directory tmp -interaction=nonstopmode $*; cp tmp/*.pdf .'

map <F6> :setlocal spell! spelllang=en_us<CR>
map <F8> :setlocal spell! spelllang=es<CR>
autocmd BufNewFile,BufRead *.tex set spell
autocmd BufNewFile,BufRead *.tex let g:indentLine_enabled=0
autocmd BufNewFile,BufRead *.md let g:indentLine_enabled=0
autocmd BufNewFile,BufRead *.java set ts=4
autocmd BufNewFile,BufRead *.java set softtabstop=4
autocmd BufNewFile,BufRead *.java set shiftwidth=4

autocmd BufNewFile,BufRead *.c set ts=2
autocmd BufNewFile,BufRead *.c set softtabstop=2
autocmd BufNewFile,BufRead *.c set shiftwidth=2
set incsearch
set hlsearch

syntax enable


autocmd StdinReadPre * let s:std_in=1

set undofile
set undodir=~/.vim/undodir


set backspace=indent,eol,start
set complete-=i
set smarttab

if &t_Co == 8 && $TERM !~# '^linux'
  set t_Co=16
endif

let g:ycm_semantic_triggers = {
\  'tex'  : ['\ref{', '\cref{', '\Cref{', '\cite{', '\autocite{', '\mlacite{', '\nocite{',],
\ }

let g:jedi#force_py_version = 3
let g:calendar_google_calendar = 1
let g:calendar_google_task = 1

" vertical line indentation
let g:indentLine_color_term = 239
let g:indentLine_color_gui = '#09AA08'
let g:indentLine_char = '│'
let g:tex_comment_nospell= 1

python3 from powerline.vim import setup as powerline_setup
python3 powerline_setup()
python3 del powerline_setup

let g:powerline_pycmd = 'py3'
set laststatus=2 " Always display the statusline in all windows
set showtabline=2 " Always display the tabline, even if there is only one tab
set noshowmode " Hide the default mode text (e.g. -- INSERT -- below the statusline)
set smartcase
" Run the current file with rspec
map <Leader>rb :call VimuxRunCommand("clear; rspec " . bufname("%"))<CR>

" Prompt for a command to run
map <Leader>vp :VimuxPromptCommand<CR>

" Run last command executed by VimuxRunCommand
map <Leader>vl :VimuxRunLastCommand<CR>

" Inspect runner pane
map <Leader>vi :VimuxInspectRunner<CR>

" Close vim tmux runner opened by VimuxRunCommand
map <Leader>vq :VimuxCloseRunner<CR>

" Interrupt any command running in the runner pane
map <Leader>vx :VimuxInterruptRunner<CR>

" Zoom the runner pane (use <bind-key> z to restore runner pane)
map <Leader>vz :call VimuxZoomRunner()<CR>

let g:ycm_extra_conf_globlist = ['~/Code/UCSD-Extensions/CCppProgrammingOne/*']

let g:languagetool_jar = '/usr/share/java/languagetool/languagetool-commandline.jar'

set mouse=a
source /usr/share/vim/vim82/macros/matchit.vim

" autocmd bufnewfile *.c so ~/.vim/c_header.txt
" autocmd bufnewfile *.h so ~/.vim/h_header.txt
" autocmd bufnewfile *.cpp so ~/.vim/cpp_header.txt
" autocmd bufnewfile *_Quiz.txt so ~/.vim/_Quiz.txt_header.txt
" autocmd bufnewfile *.c exe "1," . 10 . "g/FILE_NAME.*/s//" .expand("%")
" autocmd bufnewfile *.c exe "1," . 10 . "g/DATE.*/s//" .strftime("%B %e, %Y")
" autocmd bufnewfile *.h exe "1," . 10 . "g/FILE_NAME.*/s//" .expand("%")
" autocmd bufnewfile *.h exe "1," . 10 . "g/DATE.*/s//" .strftime("%B %e, %Y")
" autocmd bufnewfile *.cpp exe "1," . 10 . "g/FILE_NAME.*/s//" .expand("%")
" autocmd bufnewfile *.cpp exe "1," . 10 . "g/DATE.*/s//" .strftime("%B %e, %Y")
" autocmd bufnewfile *_Quiz.txt exe "1," . 10 . "g/FILE_NAME.*/s//" .expand("%")
" autocmd bufnewfile *_Quiz.txt exe "1," . 10 . "g/DATE.*/s//" .strftime("%B %e, %Y")
"
set tabstop=4 expandtab shiftwidth=4 smarttab
set grepprg=ag\ --vimgrep\ $*
set grepformat=%f:%l:%c:%m
let g:syntastic_rust_checkers = ['cargo'] 

let g:ycm_language_server =
\ [
\   {
\     'name': 'rust',
\     'cmdline': ['rust-analyzer'],
\     'filetypes': ['rust'],
\     'project_root_files': ['Cargo.toml']
\   }
\ ]

let g:syntastic_python_checkers = ['pyflakes'] 

" Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
let g:UltiSnipsExpandTrigger="<c-tab>"
let g:UltiSnipsJumpForwardTrigger="<c-shift-tab>"
let g:UltiSnipsJumpBackwardTrigger="<c-tab>"

let delimitMate_expand_cr = 1

syntax enable
set background=dark
colorscheme solarized

set backupdir=~/.cache/vim/backup/

