#!/usr/bin/expect
set timeout 5
spawn "./EnergyPlus-8.7.0-78a111df4a-Linux-x86_64.sh"
expect "Do you accept the license? \\\[yN\\\]: " {send "y\r"}
expect "EnergyPlus install directory \\\[/usr/local\\\]:" { send "\n" }
expect "Symbolic link location (enter \\\"n\\\" for no links) \\\[/usr/local/bin\\\]:" { send "\n" }
expect "Symbolic links were successful."
