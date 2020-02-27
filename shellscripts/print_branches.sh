
## this macro can be run using source print_branches.sh > log ;; yes must be directed to log
## feed the rootfile name and tree name before running else it will not be able to see the rootfile you want to print 


rootfilename=EcalTPGParam.root
treename=tpgmap



root -l $rootfilename <<EOF
$treename->Print()
EOF



cat log | grep "*Br" | awk '{print $3}' > log_branchnames.txt

