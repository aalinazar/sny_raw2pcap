#!/usr/bin/python
####################################################################
#  raw2pcap version 1.0
#           2016-02-10 17:35 
#
#  Author: Alfred Alinazar
####################################################################
#
#  this script should be executed on cron
#  PLEASE MODIFY src_dir and dst_dir prior to execute the script
#
####################################################################

import os

case_list = "caselist.txt"
dst_dir = "/pcap"
src_dir="/unprocessed"

def get_case_list(case_list):
	with open(case_list) as f:
		case_names = f.read().split()
	return case_names
	
def get_date_dir(case_name):
	date_dir = list()
	for dir in os.listdir(case_name):
		dir_full = os.path.join(case_name,dir)
		if os.path.isdir(dir_full):
			date_dir.append(dir)
	return date_dir
	
def sync_raw_and_pcap(src_dir,dst_dir,case_names):	
	for case_name in case_names:
		src_case = src_dir+'/'+case_name
		if os.path.exists(src_case):
			date_dirs = get_date_dir(src_case)
			for date_dir in date_dirs:
				source = src_case+"/"+date_dir
				destination = dst_dir+"/"+case_name
				if not os.path.exists(destination):
					os.makedirs(destination)
				destination_date = destination+"/"+date_dir
				if not os.path.exists(destination_date):
					# both lines should be replaced with raw2pcap command later
					os.makedirs(destination_date)
					command = "echo " + "raw2pcap "+source+" "+ destination
					os.system(command) 
				
		else:
			print case_name," doesn't exists"
	
#print get_date_dir("\unprocessed\T1-IMAP-102")

case_names = get_case_list(case_list)
sync_raw_and_pcap(src_dir,dst_dir,case_names)