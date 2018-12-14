spath = 'C:/py/data.txt'
outpath='C:/py/result.csv'
buff=''
scheme =( 'Lead #'
			,'Application posted:'
			,'Prospect information:'
			,'First name:'
			,'Last name:'
			,'E-mail: '
			,'Home phone number:'
			,'Cell phone number:'
			,'Best time to call:'
			,'City'
			,'Area code'
			,'State'
			,'Zip'
			,'Credit rating'
			,'Gross yearly income'
			,'Mortgage information:'
			,'Loan purpose'
			,'Home value'
			,'Loan amount'
			,'Property type'
			,'Preferred loan type'
			,'Loan close period'
			,'Services requested:'
			,'Comments, goals:'#select the line start with
			)


def rwtocsv(rpath,wpath):
#write
	with open(wpath,'w') as fw:

#read
		with open(rpath, 'r') as fp:
			print ("Name of the file: ", fp.name)
			line = fp.readline()
			while line:
					for sch in scheme:
						if line.startswith(sch):
							buff =line.strip(sch)
							buff = buff.replace("\r","")
							buff = buff.replace("\n","")
							buff = '"'+buff+'"'
							if sch=='Lead #':
								buff='\n'+buff+','
							else:
								buff=buff+','					
							fw.write(buff)
							print(buff,end='')
						buff=''
					line=fp.readline()



rwtocsv(spath,outpath)