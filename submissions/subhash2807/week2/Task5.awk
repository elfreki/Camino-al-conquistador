#! /bin/awk -f
BEGIN{
        FS=" - - [[]| \"| +";
        n=0;
        print "#,ip_addr,date_accessed,endpoint_accessed,googlebot-useragent";
}
$7~/404/ && /Googlebot|Bot|GoogleBot|googlebot|bot/ {

        n++;
        printf "%d,%s,%s,%s,",n,$1,$2,$5;
        gsub(/"/,"");
        for( i=10;i<=NF;i++)
        printf "%s ",$i;
        printf "\n";
}

