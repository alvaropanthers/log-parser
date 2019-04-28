# log-parser
-Make a program that parses auth.log and displays the information clearly in a interface.  
-The interface will be a html document that uses javascript and html to display this information.  

-Information about auth.log  
	     -File location: /var/log/auth.log  
	     -All authentication related events in Debian and Ubuntu server are logged here.  
	     -If you're looking for anything involving the user authorization mechanism,
	     you can find it in this log file.  
	     -Useful for:  
	     	     -Investigating failed login attempts  
		     	 -Investigating brute-force attacks and other vulnerabilities related to  
				  user authorization mechanism.  

Feb 25 07:03:52 dailyprog sshd[12430]: Failed password for postgres from 213.234.26.179 port 53065 ssh2  
Feb 25 07:08:16 dailyprog sshd[12636]: Failed password for invalid user vk from 140.143.93.31 port 57698  

Feb 25 09:05:42 dailyprog sshd[19567]: Failed password for invalid user teste from 217.61.14.223 port 59054 ssh2  
Feb 25 08:55:07 dailyprog sshd[18944]: Failed password for invalid user user from 217.61.14.223 port 60092 ssh2  
