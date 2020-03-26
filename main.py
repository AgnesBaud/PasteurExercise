from code import *
import sys

if __name__=="__main__":

	"""-i : sequence file
	-n : [optional] name of the sequence
	-t : [optional] type of the sequence (DNA or RNA)"""

	dicARG={"-i":"NA", "-n":"", "-t":"undefined"}
	argc=len(sys.argv)

	i=1
	while i<argc:
		dicARG[sys.argv[i]]=sys.argv[i+1]
		i+=2

	if dicARG['-i']=='NA':
		print("use argument -i to give the name of a file.")
		raise ValueError('no sequence file given')


	S,dicARG['-n']=ExtractSeqFromFile(dicARG['-i'],dicARG['-n'])

	s = NucleicAcid(S,dicARG['-n'],dicARG['-t'])
	print("name : "+s.name)
	print("type : "+s.type)

	print("sequence :\n"+s.seq+"\n")

	s.countNT()

	s.DNA2RNA()
	if s.type=="DNA":
		print("\nRNA sequence :\n"+s.RNA.seq+"\n")

	s.RevCompl()
	print("Complemented Strand :\n"+s.ComplementedStrand.seq+"\n")
