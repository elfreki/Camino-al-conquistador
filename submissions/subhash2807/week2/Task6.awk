#! /bin/awk -f
BEGIN {
        OFS="\t";
        FS=" ";
	line=0;
	#13 May 12 : 00 : 00
	start=13120000;
	#13 May 14 : 52 : 50
	end=13145250;
}

{
	#[13/May/2018:13:50:13
	n=int(substr($4,2,2)substr($4,14,2)substr($4,17,2)substr($4,20,2));
        if(n >= start && n <=end ){
		print $0;
	}
}

