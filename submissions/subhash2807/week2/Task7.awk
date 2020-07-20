#! /bin/awk -f
BEGIN{
	FS=" ";
	OFS="\t";
}

/Version/{

	print $0;
	n++;

}
END{
	print n " lines are printed";
}
