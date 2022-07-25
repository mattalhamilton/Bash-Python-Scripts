#! /bin/sh

#This is the destructive write to the alert_data.csv file

echo "Date,Time,Priority,Classification,Description,Source_IP,Destination_IP" > ~/alert_data.csv


#first echo to tell user the file is being processed

echo -e "Processing the pcap file...\n"



#Here is where all the beautiful magic happens

input=fast_short.pcap
while IFS= read -r line
do
	
	date=$(echo $line | cut -d "-" -f 1)
	time=$(echo $line | cut -d "." -f 1)
	time=$(echo $time | cut -d "-" -f 2)
	description=$(echo $line | cut -d "]" -f 3)
	description=$(echo $description | cut -d "[" -f 1)
	classification=$(echo $line | cut -d "[" -f 5)
	classification=$(echo $classification | cut -d "]" -f 1)
	classification=$(echo $classification | cut -d ":" -f 2)
	priority=$(echo $line | cut -d "[" -f 6)
	priority=$(echo $priority | cut -d "]" -f 1)
	priority=$(echo $priority | cut -d ":" -f 2)
	source_ip=$(echo $line | tr "}" "|")
	source_ip=$(echo $source_ip | cut -d "|" -f 2)
	source_ip=$(echo $source_ip | cut -d "-" -f 1)
	dest_ip=$(echo $line | tr "}" "|")
	dest_ip=$(echo $dest_ip | cut -d "|" -f 2)
	dest_ip=$(echo $dest_ip | cut -d ">" -f 2)
	
	line_out=$date,$time,$priority,$classification,$description,$source_ip,$dest_ip
	
	echo $line_out >> ~/alert_data.csv	

done < $input


#This is the second echo to tell the user it is done

echo "The pcap file has been processed"

#This sends it back to the home directory

cd ~
