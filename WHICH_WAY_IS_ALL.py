# -*- coding: utf-8 -*-

def Help():
	print("!!:gs/foo/bar/  allows global serach and replace of the 2nd to last command")
	print("find . -name \"*.undo\" -ls | awk '{total += $7} END {print total}'")
	print("find . 2>/dev/null -type f -user pasmith -exec ls -ls {} \\;")
	print("find . -name \"*.cpp\" -exec grep  \"html\" '{}' \\;")
	print("find . -amin -1  #finds files read in last minute")
	print("find . -atime -1  #finds files read within last 1*(24 hours)")
	print("find . -mtime +1  #finds files modified more than 1*(24 hours ago)")
	print("find . -newer  backup.tar.gz  find files edited more recently than given file")
	print("find . -size +100[ckGM] b has a weird definition")
	print("find / -name art  2>&1 | grep -v \"Permission denied\"")
	print("find . -type d \( -path ./.ipython -o -path ./netbeans-7.4 -o -path ./Downloads/rstudio-0.98.1103 \) -prune -o  -name \"*tomc*\" -print")
	print("du -c *  prints summary at end of output")
	print("tar -[zj]cvf tarballname.tar.gz itemtocompress")
	print("tar -[zj]xvf tarballname.tar.gz   [-C /dir]")
	print("ln -s ACTUAL_FILE_NAME SYMBOLIC_FILE_NAME ")
	print("ls -tlr *nofilter*  *y_try* |  awk '{for(i=1;i<6;i++) $i=\"\";print}' will exclude columns 1-5 and print the rest")
	print("ls -tlr *nofilter*  *y_try* | awk '{for(i=4;i<=13;i++) printf $i\" \"}'")
	print("ls -tlr *nofilter*  *y_try* |  awk '{ for (i=1; i<8; i++) $i=\"\"; print $0 }")
	print("grep -i phish * | awk '{FS=\"\\t\"; print $3}'")
	print("grep -i phish * | awk -F\"\\t\" '{ print $3}'")
	print('to grep a variable number of lines')
	print("sed -n '/3039ac1dc14d533c69252cc9/,/NEW_/p' data_20140402")
	print("tail -f file.txt | grep -E --line-buffered -v  \"\-1 0 0 0 0\"")
	print("sort du output by adding leading zeros to awk output then piping through lexographic sort")
	print("du -bS * | awk '{FS=\"\\t\"; print sprintf(\"%015d %s\", $1, $2)}' | sort")
	print("sed -r 's/\\b([a-z][a-z]*)\\b/\\n*\\1*\\n/gi'  < data.txt | sed -nr 's/\*(.*)\*/\\1/p' > out")
	print("sed -n 1,10p  #prints the first n lines of a file or pipe")
	print("sed -n '1p;0~3p'  #prints first line or line % N == 0")
	print("echo \"From use@your.net  Mon Jan 21 13:49:47 2013 abc\" | sed -rne 's/([[:alpha:]][[:alpha:]]*)[ ]/\\n*\\1*\\n/gip'  -e 's/[ ]([[:alpha:]][[:alpha:]]*)/\\n*\\1*\\n/gip'")
	print("awk 'NR == 1 || NR % 3 == 0' yourfile  #prints first line or line % N == 0")
	print("hadoop fs -du -s   /user/hive/warehouse/paul* | awk '{FS=\" \"; sum+=$1} END {print sum/1000000000}'")

	print('careful when passing a %s to awk and also have a %s string formatter in python')
	print("o1 = Utilities.GrabResult(\"cd hive;du -bS * | awk '{FS=\\\\\\\"\\t\\\\\\\"; print sprintf(\\\\\\\"%015d %s\\\\\\\", \\$1, \\$2)}' | sort\", **kwargsGrabResult)")
	print("o1 = Utilities.GrabResult(\"cd hive;du -bS %s | awk '{FS=\\\\\\\"\\t\\\\\\\"; print sprintf(\\\\\\\"%%015d %%s\\\\\\\", \\$1, \\$2)}' | sort\"%('stringhere or other formatter only for the percent s that python will be mapping'), **kwargsGrabResult)")
	print('some multiline commands grabbing file names from grep/cut and bash loop to call easliy do etc... or another grep');
	print('for eml in `grep -i opentable * | cut -d: -f1`; do echo $eml; curl --insecure -F timezone="America/Los_Angeles" -F api_key= -F locale="" -F "email=<$eml" \'https://host.com/v1/discovery\'; done')
	print('exec 3<&0; grep "^2016-03-08 12:50:06.*completed" tc.time | awk \'{print $6}\' | uniq | sed \'s/\[R:\(.*\);\]/\1/\' | while read -r rid; do grep "$rid" tc.log > "${rid}_out"; done')
	print("for eml in `grep -i opentable * | cut -d: -f1`; do grep -iH confirm $eml; done")
	print("for eml in `grep -i opentable * | awk '{print $2}'`; do grep -iH confirm $eml; done")

	s1 = """
END=5
for ((i=1;i<=END;i++)); do
	echo $i
done
	"""
	print(s1)

	s1 = """
for ((i=1;i<=3;i++)); do TABLE_SRC=`date +header_data_%Y%m%d -d "$i days ago"`; echo $TABLE_SRC ; done
	"""
	print(s1)

	s1 = """
while true; do /data/servers/Genericscripts/mail_cicd2.sh -p tc -a jmeter -environment development; done	"""
	print(s1)

	s1 = """for elem in `ls`; do   new=$(echo $elem | sed -e 's/tc/tc-feedback-handler/'); echo $new;  mv -v "$elem" "$new"; done	"""

	print(s1)

	print('command that runs locust uses time for walltime and parses locust report to generate a metareport on multiple locust runs')
	s1 = """> ReportProcess3; for elem in {1..15}; do { { echo $elem; time { z1=$(locust -f /home/pasmith/sandboxa/myrepo/locust_shscls.py --host=https://host.com  --no-web --clients=$elem  --hatch-rate=10 --num-request=150 2>&1); }  }; echo $z1 | sed 's/POST/POST\\n/g' | sed 's/Total/Total\\n/g' | sed 's/-//g' | grep 'predict/v2 .*Total' | tail -1  ; } >> ReportProcess3  2>&1; done"""

	print(s1)
	print('directory looping')
	s1 = """for elem in */; do echo $elem; done"""
	print(s1)
	s1 = """for elem in `find . -maxdepth 1 -mindepth 1 -type d -printf '%P\n'`; do echo $elem; done"""
	print(s1)


if __name__=="__main__":
	Help()
