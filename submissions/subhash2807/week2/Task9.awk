#! /bin/awk -f

BEGIN {
	#12 May 08 : 00 : 00
	start=12080000;
	#12 May 09 : 00 : 00
	end=12090000;
	objectSize=0;
}
{
	n=int(substr($4,2,2)substr($4,14,2)substr($4,17,2)substr($4,20,2));
        if(n >= start && n <=end ){
		objectSize=objectSize+$10
	}
}
END{
	print objectSize " is the  total requested size bw 8:00 am to 9:am on 12 May";
}
