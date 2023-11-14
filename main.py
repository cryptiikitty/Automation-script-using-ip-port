import os
import datetime
import argparse
import time
 
def parse_args():
    parser = argparse.ArgumentParser(description='Express bot')
    parser.add_argument('--f', type=str, help='parsing file')
    args = parser.parse_args()
 
    return args
 
def send_to_scan(text):
    lines = []
    with open(text, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    a = len(lines)
    msg = ''
    i = 0
    while i < int(a):
        c = lines[i]
        #print(c)
        arr = c.split(':')
        print('ip:', arr[0])
        print('port:', arr[1])
        print('')
        os.system("timeout 5 python3 openssl_req_client_cert.py {} {}".format(arr[0], arr[1])) # command here
        print('------------------')
        time.sleep(2)
        i += 1
 
if __name__ == '__main__':
    args = parse_args()
    if args.f:
        text = args.f
        send_to_scan(text)
