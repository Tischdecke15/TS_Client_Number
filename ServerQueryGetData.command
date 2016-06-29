#!/usr/bin/expect -f
log_user 0
loginname=$1
password=$2
spawn telnet ts.maxeengine.com 10011
send "login $loginname $password\n"
expect "error id=0 msg=ok"
send "use 1\n"
expect "error id=0 msg=ok"
log_user 1
send "clientlist\n"
expect "error id=0 msg=ok"
