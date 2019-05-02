import sys
count ={}

for line in open(sys.argv[1],'r'):
	if line.startswith('protein'):continue
	line =line.strip().split()
	if int(line[4])>=400:
		if line[0] not in count:
			count[line[0]]=1
		else:
			count[line[0]]+=1
		if line[1] not in count:
			count[line[1]]=1
		else:
			count[line[1]]+=1
fd={}

for line in open(sys.argv[2],'r'):
	line=line.strip().split('\t')
	fd[line[0]]=[line[1],line[2]]
wr=open(sys.argv[3],"w")

for line in count:
	wr.write( "%s\t%s\t%s\t%s\n"%(line,count[line],fd[line][0],fd[line][1]))
wr.close()
	
	
	
	
	
