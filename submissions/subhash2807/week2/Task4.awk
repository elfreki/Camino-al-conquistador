#! /bin/awk -f
BEGIN{
        FS=" - - [[]| \"| +";
        n=0;
        print "#,ip_addr,date_accessed,endpoint_accessed,useragent";
}
NR>=22 && NR<=33 && $7~/404/{

        n++;
        printf "%d,%s,%s,%s,",n,$1,$2,$5;
        gsub(/"/,"");
        for( i=10;i<=NF;i++)
        printf "%s ",$i;
        printf "\n";
}

