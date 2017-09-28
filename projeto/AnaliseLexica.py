#!/usr/bin/python
# coding: utf-8

import ply.lex as lex

class Lexer:
	def __init__(self):
		self.lexer = lex.lex(debug=False, module=self, optimize=False)

	#palavras reservadas
	keywords = {
		'repita': 'REPITA',
		'fim': 'FIM',
		'se': 'SE',
		'então': 'ENTAO',
		'senão': 'SENAO',
		'flutuante': 'FLUTUANTE',
		'retorna': 'RETORNA',
		'até': 'ATE',
		'leia': 'LEIA',
		'escreva': 'ESCREVA',
		'inteiro': 'INTEIRO',        
	}

	tokens = ['SOMA', 'SUB', 'MUL', 'DIV', 'EQ', 'VIRG', 'ATRIB', 'MENOR', 'MAIOR',
				'MENOREQ', 'MAIOREQ', 'APAR', 'FPAR', 'DPON', 'NUM_FLU', 'NUM_INT',
				'ID', 'ACOL', 'ELOG', 'OULOG', 'NEG', 'FCOL'] + list(keywords.values())

	t_SOMA = r'\+'
	t_SUB = r'\-'
	t_MUL = r'\*'
	t_DIV = r'/'
	t_EQ = r'='
	t_VIRG = r','
	t_ATRIB = r':='
	t_MENOR = r'<'
	t_MAIOR = r'>'
	t_MENOREQ = r'<='
	t_MAIOREQ = r'>='
	t_APAR = r'\('
	t_FPAR = r'\)'
	t_DPON = r':'
	t_NUM_INT = r'\d+'
	t_ACOL = r'\[' 
	t_FCOL = r'\]'
	t_ELOG = r'\&\&'
	t_OULOG = r'\|\|'
	t_NEG = r'\!'
	t_NUM_FLU = r'([0-9]+(\.[0-9]*)(e(\+|\-)?(\d+))?)|([0-9]+(e(\+|\-)(\d+)))' #expressão regular numero flutuante
                
	def t_ID(self, t):
		r'[a-zA-Zá-ñÁ-Ñà-źÀ-Ź][a-zA-Zá-ñÁ-Ñà-źÀ-Ź0-9_à-ú]*'
		t.type = self.keywords.get(t.value, 'ID')
		return t

	def t_COMMENT(self, t):
		#r'\{(.|\s)*?\}'
		#r'\{[^}]*[^{]*\}'
		r'\{.*\}'

	def t_NEWLINE(self, t):
		r'\n+'
		t.lexer.lineno += len(t.value)

	t_ignore = ' \t'

	def t_error(self, t):
		print("Item ilegal: '%s', linha %d, coluna %d" % (t.value[0], t.lineno, t.lexpos))
		t.lexer.skip(1)

	def test(self, code):
		lex.input(code)
		while True:
			t = lex.token()
			if not t:
				break
			print(t)

if __name__ == '__main__':
	from sys import argv
	lexer = Lexer()
	f = open(argv[1])
	lexer.test(f.read())
