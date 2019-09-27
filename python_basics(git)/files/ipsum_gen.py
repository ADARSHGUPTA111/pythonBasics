from random import randint



ninja_words=['Adarsh','Gupta','is','a', 'very', 'talented', 'boy',
 'i', 'have' ,'ever' ,'come' ,'across' ,'he' ,'must' ,'work',
 'much' ,'harder', 'in', 'order', 'to', 'achieve', 'greater' ,
 'things', 'in', 'life', 'just', 'hunt','your', 'dream', 'and' ,
 'stop', 'not', 'until' ,'succed']

paragraphs=int(input("How many paragraphs of ninja ipsum"))

with open('ipsum.txt') as ipsum_original:
	items=ipsum_original.read().split()

def ninjarize(word):
	random_pos=randint(0,len(ninja_words)-1)
	return f'{word} {ninja_words[random_pos]}'

for n in range(paragraphs):
	ninja_text=list(map(ninjarize,items))
	with open('ninja_ipsum.txt','a') as ipsum_ninja:
		ipsum_ninja.write(' '.join(ninja_text)+'\n\n')
