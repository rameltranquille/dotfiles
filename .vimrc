let mapleader = ","

" =================================
" Plugins 
" =================================

call plug#begin('~/.vim/plugged')

" Plug 'junegunn/vim-easy-align'
Plug 'preservim/nerdtree'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'jiangmiao/auto-pairs'
Plug 'tpope/vim-sensible'
Plug 'tpope/vim-surround'
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-repeat'
Plug 'tpope/vim-markdown'
Plug 'dracula/vim',{'as':'dracula'}
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'lervag/vimtex'
Plug 'vim-syntastic/syntastic'
Plug 'kassio/neoterm'
Plug 'ycm-core/YouCompleteMe'

call plug#end()

colorscheme dracula

" Neoterm
nnoremap <F1> :Tnew<CR>
nnoremap <F2> :Tclose<CR>  
nnoremap <F3> :Tclear<CR>  
nnoremap <F4> :Tkill<CR>
nnoremap <F5> :Ttoggle<CR>

let g:neoterm_default_mod="botright"
" let g:neoterm_size=":res -10"
" let g:neoterm_keep_term_open=0



" Airline
let g:airline_theme='molokai'

let g:airline#extensions#syntastic#enabled=1
let g:airline#extensions#fzf#enabled=1

" Syntastic
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

" Vim Markdown
let g:markdown_fenced_languages = ['html', 'python', 'bash=sh']

" fzf
let g:fzf_preview_window = ['right:40%:hidden', 'ctrl-/']

" Easy Align
nmap ga <Plug>(EasyAlign)

" Nerdtree
nnoremap <C-n> :NERDTreeToggle<CR>
nnoremap <leader>n :NERDTreeFocus<CR>
" autocmd VimEnter * NERDTree | wincmd p

autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() |
    \ quit | endif

" Vimtex
let g:tex_flavor='latex'
let g:vimtex_view_method='zathura'
let g:vimtex_quickfix_mode=0
set conceallevel=1
let g:tex_conceal='abdmg'


" =================================
" Programming Language Specific
" =================================

autocmd Filetype tex nnoremap <buffer> <F12> :update<bar>VimtexCompile<CR>
autocmd Filetype html nnoremap <buffer> <F12> :update<bar>!firefox %<CR>
autocmd Filetype python nnoremap <buffer> <F12> :update<bar>:T 'python %'<CR>
autocmd Filetype cpp nnoremap <buffer> <F10> :update<bar>:T % && T ./a.out<CR>

au Filetype python set 
	\ tabstop=4
	\ softtabstop=4
	\ shiftwidth=4
	\ textwidth=79

au Filetype html set
	\ tabstop=2
	\ softtabstop=4
	\ shiftwidth=2

au Filetype css set 
	\ tabstop=2
	\ softtabstop=2
	\ shiftwidth=2 

au Filetype cpp set 
	\ textwidth=79
	\ tabstop=4
	\ shiftwidth=4


" =================================
" Basics
" =================================

set title
set clipboard+=unnamedplus
set encoding=UTF-8
set nocompatible
set number
set relativenumber
set incsearch
set hlsearch
set showcmd
set smarttab
set ignorecase
set smartcase
set ruler 
set wrap
set splitbelow splitright
filetype plugin indent on 
syntax on


" Disables automatic commenting on newline
autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

" =================================
" Mappings
" =================================

imap jk <Esc>

map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l
