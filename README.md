# ciscomac
The script will query "macaddress.io" for the MAC address provided as its first argument and provide Vendor name (if found) as the output.
Script will validate input for incorrect characters and minimal length of the MAC address (given the address can be provided in a number of different formats it only validates that much).

"macaddress.io" requires an API key which is hardcoded into the script and can be changed (MY_KEY variable)

It can be containerized into Docker and run from an image, requires 'python:2'.

EXAMPLE:

./macquery.py 00:0000111111
Vendor: Xerox Corp

DOCKER EXAMPLE:

#docker build -t cisco-mac .

Sending build context to Docker daemon  18.43kB
Step 1/4 : FROM python:2
 ---> 37093962fbf5
 Step 2/4 : ADD macquery.py /
 ---> Using cache
 ---> 630a0283697f
 Step 3/4 : ENTRYPOINT [ "python" ,"/macquery.py" ]
 ---> Using cache
 ---> 9a2cc14cfcfc
 Step 4/4 : CMD []
 ---> Using cache
 ---> 89bcffcfab64
 Successfully built 89bcffcfab64
 Successfully tagged cisco-mac:latest

# docker run  cisco-mac 000000112233
Vendor: Xerox Corp

