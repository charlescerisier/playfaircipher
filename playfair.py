#from tkinter import*
import random 
import sys

#Chiffrage
def keygenerator() : 
	j=0
	k=0
	alphabet=['A','B','C','D','E','F','G','H','I','J','L','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
	random.shuffle(alphabet) 
	key = [[None]*5 for i in range(5)]
	for i in range (5):
		for j in range(5):
			key[i][j] = alphabet[5*i+j]
	return key

def divide(text):
	global textMat
	textMat=[]
	for j in range (0,len(text)-1,2):
		if (text[j]==text[j+1]):
			text=text[0:j+1]+"X"+text[j+1:]
	text=text.upper()
	text=text.replace(" ","")
	lenght=len(text)
	if (lenght%2==0 and len(text)%2):
		for i in range(0,lenght,2): 
			textMat.append(text[i:i+2])
	else : 
		text+='B'
		for i in range(0,lenght,2): 
			textMat.append(text[i:i+2])
	findindex(textMat)

def findindex(text):
	global index
	p = len(textMat); n = 4 #p linges et n colonnes
	index = [[0]*n for i in range(p)]
	for w in range(0,len(textMat)):
		for i in range (0,len(mat)):
			for j in range (0,len(mat[0])): 
				if (mat[i][j]==textMat[w][0]):
					index[w][0]=i
					index[w][1]=j
				if (mat[i][j]==textMat[w][1]):
					index[w][2]=i
					index[w][3]=j
	chiffrage()

def chiffrage() : 
	global encrypted
	encrypted=[]
	for i in range (len(index)):
		if (index[i][0]==index[i][2]): 
			if (index[i][1]!=4 and index[i][3] !=4):
				newcol1=index[i][1]+1
				newcol2=index[i][3]+1
			if(index[i][1]==4):
				newcol1=0
				newcol2=index[i][3]+1
			if(index[i][3]==4):
				newcol1=index[i][1]+1
				newcol2=0
			line=index[i][0]
			encrypted.append(mat[line][newcol1])
			encrypted.append(mat[line][newcol2])
			
		elif (index[i][1]==index[i][3]): 
			if (index[i][0]!=4 and index[i][2] !=4):
				newline1=index[i][0]+1
				newline2=index[i][2]+1

			if(index[i][0]==4):
				newline1=0
				newline2=index[i][2]+1
			if(index[i][2]==4):
				newline1=index[i][0]+1
				newline2=0

			colone=index[i][1]
			encrypted.append(mat[newline1][colone])
			encrypted.append(mat[newline2][colone])
			
		else : 
			newline1=index[i][0]
			newline2=index[i][2]
			col1=index[i][3]
			col2=index[i][1]
			encrypted.append(mat[newline1][col1])
			encrypted.append(mat[newline2][col2])
	affichage(encrypted) 


#dechiffrage
def dechiffrer(mat) :
	crypted =[]
	decrypted=[]
	text.split(" ")
	for i in range(0,len(text),2): 
		crypted.append(text[i:i+2])
	p = len(crypted); n = 4 #p linges et n colonnes
	index = [[0]*n for i in range(p)]
	for w in range(0,len(crypted)):
		for i in range (0,len(mat)):
			for j in range (0,len(mat[0])): 
				if (mat[i][j]==crypted[w][0]):
					index[w][0]=i
					index[w][1]=j
				if (mat[i][j]==crypted[w][1]):
					index[w][2]=i
					index[w][3]=j
	print("index : ", index)


	for i in range (len(index)):
		if (index[i][0]==index[i][2]): 
			print("meme lignes")
			if (index[i][1]!=0 and index[i][3] !=0):
				newcol1=index[i][1]-1
				newcol2=index[i][3]-1
			if(index[i][1]==0):
				newcol1=4
				newcol2=index[i][3]-1
			if(index[i][3]==0):
				newcol1=index[i][1]-1
				newcol2=4
			line=index[i][0]
			decrypted.append(mat[line][newcol1])
			decrypted.append(mat[line][newcol2])
			
		elif (index[i][1]==index[i][3]): 
			print("meme colone")
			if (index[i][0]!=0 and index[i][2] !=0):
				newline1=index[i][0]-1
				newline2=index[i][2]-1

			if(index[i][0]==0):
				newline1=4
				newline2=index[i][2]-1
			if(index[i][2]==0):
				newline1=index[i][0]-1
				newline2=4

			colone=index[i][1]
			decrypted.append(mat[newline1][colone])
			decrypted.append(mat[newline2][colone])

		else : 
			newline1=index[i][0]
			newline2=index[i][2]
			col1=index[i][3]
			col2=index[i][1]
			decrypted.append(mat[newline1][col1])
			decrypted.append(mat[newline2][col2])

	affichage(decrypted)


#Global
def affichage(res) : 
	global mat
	resultat="".join(str(x) for x in res)	
	print("la clé de chiffrement est : " )
	afficheMat(mat)
	print("Le message chiffré est :", resultat)


def afficheMat(mat):
    nbl=len(mat)
    nbc=len(mat[0])
    for i in range (nbl):
        print("(",end="")
        for j in range (nbc):
            print("%5s" %mat[i][j],end=" ")
        print(")")


def init() : 
	global text,mat,index
	mode=str(input("Choisir le mode chiffrer '1', dechiffrer '2' ou quitter '3' : "))
	if (mode=='1'):
		text=str(input("Entrer le texte a chiffrer : "))
		choicekey=str(input("Tapez 'o' pour generer une clé aléatoire ou 'n' pour utiliser celle par défaut : "))
		if (choicekey =="o"): 
			mat=keygenerator()
			divide(text)
			init()
		else : 
			mat=[["B","Y","D","G","Z"],["J","S","F","U","P"],["L","A","R","K","X"],["C","O","I","V","E"],["Q","N","M","H","T"]]
			divide(text)
			init()
	elif (mode=='2'):
		text=str(input("Entrer le texte a dechiffrer : "))
		choicekey=str(input("Tapez 'o' pour ecrire une clé ou 'n' pour utiliser celle par défaut : "))
		if (choicekey =="o"): 
			writedkey=str(input("Entrer une clé (tout attachée) : "))
			writedkey=list(writedkey)
			key = [[None]*5 for i in range(5)]
			for i in range (5):
				for j in range(5):
					key[i][j] = writedkey[5*i+j]
			mat=key
			print(key)
			dechiffrer(mat)
			init()
		else : 
			mat=[["B","Y","D","G","Z"],["J","S","F","U","P"],["L","A","R","K","X"],["C","O","I","V","E"],["Q","N","M","H","T"]]
			dechiffrer(mat)
			init()

	elif (mode=='3'): 
		sys.exit(0)
	else : 
		print("Vous n'avez pas correctement choisi le mode ")
		init() 

init()