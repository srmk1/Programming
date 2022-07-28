LCT is a tool that was designed to find clusters in logfile(s), so that each cluster corresponds to a certain line pattern that occurs frequently enough. Here are some examples of the clusters that SLCT is able to detect:
Dec 18 * myhost.mydomain sshd[*]: log: Connection from * port *
Dec 18 * myhost.mydomain sshd[*]: log: Password authentication for * accepted.

With the help of SLCT, one can quickly build a model of logfile(s), and also identify rare lines that do not fit the model (and are possibly anomalous).

SLCT has been tested on Linux and Solaris (compiled with gcc), but is likely to compile and work on other platforms as well.

For more information, read the man page. There is also a paper about SLCT (published at IPOM 2003).

Papers about the application of SLCT for log mining and IDS alert classification have been published at NOMS 2008 and CNSM 2010.

Also, you might be interested in the LogCluster algorithm that is designed as an improvement over SLCT.
