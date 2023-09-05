#!/bin/bash
echo "enter username"
read username
echo "enter password"
read password
if [[ ( $username == "srikanth"  &&  $password == "srikanth90" )]] then
echo "valid user"
else
echo "invalid user"
fi
