#!/usr/bin/expect -f
log_user 0
adress=$1
loginname=$2
password=$3
spawn telnet adress 10011
send "login $loginname $password\n"
expect "error id=0 msg=ok"
send "use 1\n"
expect "error id=0 msg=ok"
log_user 1
send "clientlist\n"
expect "error id=0 msg=ok"
