def ExtractSeqFromFile(filename, name):
	fi = open(filename, 'r')
	L = fi.readlines()
	i=0
	seq=""
	while L[i][0]==">" or L[i][0]=="#":    #lines are ID or comments
		if L[i][0]==">":
			if name=="":
				name=L[i][1:].strip()
		i+=1

	while i<len(L) and L[i][0]!=">" and L[i][0]!="#":
		seq+=L[i].strip()	#remove '\n' if there is one
		i+=1

	if name=="":
		name="Unnamed"

	return seq, name


class NucleicAcid:
	"""countNT : count the number of nucleotids of a DNA sequence
	DNA2RNA : transcribe a DNA sequence to a RNA sequence (T->U)
	RevCompl : Give the complement strand of a DNA sequence"""

	#A,C,G,T,U(RNA),W,S,M,K,R,Y,B,D,H,V,N,Z
	dicCompl={"C":"G", "G":"C", "T":"A", "U":"A",             #static var
		"W":"W", "S":"S", "M":"K", "K":"M", "R":"Y", 
		"B":"V", "D":"H", "H":"D", "V":"B",
		"N":"N", "Z":"Z"} 


	def VerifSeqANDGiveType(self):
		for j in self.seq:
			if j!="A" and j not in NucleicAcid.dicCompl.keys():
				print("ERROR : The sequence contains unaccepted characters.")
				return False
			if self.type=="undefined":
				if j=="T":
					self.type="DNA"
				elif j=="U":
					self.type="RNA"		
		return self.seq, self.type


	def __init__(self, seq, seqname, seqtype):

		self.type=seqtype		
		self.seq=seq

		verif = NucleicAcid.VerifSeqANDGiveType(self)

		if not verif:
			print("Please make sure your file follows the following rules:\n * Only one sequence by file (if more than one, only the first sequence will be treated).\n * Any line that does not correspond to a nucleic sequence must be preceded by a '>' or a '#'.\n * The sequence cannot contain any spaces or any characters that arent in the following list:\n     A,C,G,T,U,W,S,M,K,R,Y,B,D,H,V,N,Z\n")
			del self
			raise ValueError('sequence contains unaccepted characters')


		self.name=seqname	

			

	# output : a dictionnary with the count of each nucleotids. Print results for A,C,G and either T or U depending on the type of the sequence
	def countNT(self):
		self.NucleotidCount={"A":0, "C":0, "G":0}
		if self.type=="DNA":
			self.NucleotidCount["T"]=0
		if self.type=="RNA":
			self.NucleotidCount["U"]=0
		for i in self.seq:
			if i not in self.NucleotidCount.keys():
				self.NucleotidCount[i]=1
			else:
				self.NucleotidCount[i]+=1
		
		if self.type=="DNA":
			print(str(self.NucleotidCount["A"])+" "+str(self.NucleotidCount["C"])+" "+str(self.NucleotidCount["G"])+" "+str(self.NucleotidCount["T"]))


		if self.type=="RNA":
			print(str(self.NucleotidCount["A"])+" "+str(self.NucleotidCount["C"])+" "+str(self.NucleotidCount["G"])+" "+str(self.NucleotidCount["U"]))


	# output : another instance called RNA which contains the sequence of the RNA, its type and its name. Works only for DNA sequence
	def DNA2RNA(self):
		if self.type=="DNA":
			RNAname=self.name+"-RNA"
			RNAseq=self.seq.replace('T','U')
			RNAtype="RNA"
			self.RNA=self.__class__(RNAseq, RNAname, RNAtype)
		else:
			print("The nucleic sequence is already a RNA sequence")


	# output : another instance called ComplementedStrand which contains the sequence of the complemented strand, its type and its name. Works for DNA and RNA sequence.
	def RevCompl(self):
		i=len(self.seq)-1
		CSseq=''
		CSname=self.name+"-ComplementedStrand"
		CStype=self.type

		if self.type=="undefined":
			print("sequence type (DNA or RNA) undefined. By default, it is interpreted as a DNA sequence")

		while i>=0:
			if self.seq[i]=='A':
				if self.type=="RNA":
					CSseq+="U"
				else :
					CSseq+="T"
			else :
				CSseq+=NucleicAcid.dicCompl[self.seq[i]]
			i-=1

		self.ComplementedStrand=self.__class__(CSseq, CSname, CStype)


				


