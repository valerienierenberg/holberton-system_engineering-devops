#  0x05-processes_and_signals

## Project Description:
This project covers management of processes, including the following commands and signals:
* ps
* pgrep
* pkill
* kill
* exit
* trap

## Learning Objectives
* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

## Requirements:
* Allowed editors: vi, vim, emacs
* All files will be interpreted on Ubuntu 14.04 LTS
* All files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All Bash script files must be executable
* Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
* The first line of all Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all Bash scripts should be a comment explaining what is the script doing

## File Descriptions:
* 0-what-is-my-pid - Bash script that displays its own PID
* 1-list_your_processes - Bash script that displays a list of currently running processes (including for users who might not have a TTY, in user format, shows process heirarchy)
* 2-show_your_bash_pid - (Using previous exercise command) Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
* 3-show_your_bash_pid_made_easy - Bash script that displays the PID, along with the process name, of processes whose name contain the word bash. (not allowed to use ps)
* 4-to_infinity_and_beyond - Bash script that displays To infinity and beyond indefinitely. (sleep 2 added in between each iteration)
* 5-dont_stop_me_now - Bash script that stops 4-to_infinity_and_beyond process (using kill)
* 6-stop_me_if_you_can - Bash script that stops 4-to_infinity_and_beyond process. (without using kill or killall)
* 7-highlander - Bash script that displays: "To infinity and beyond" indefinitely, with a sleep 2 in between each iteration. And "I am invincible!!!" when receiving a SIGTERM signal
* 8-beheaded_process - Bash script that kills the process 7-highlander.
* 100-process_and_pid_file - Bash script that:
    * Creates the file /var/run/holbertonscript.pid containing its PID
    * Displays To infinity and beyond indefinitely
    * Displays I hate the kill command when receiving a SIGTERM signal
    * Displays Y U no love me?! when receiving a SIGINT signal
    * Deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
* 101-manage_my_process manage_my_process - Bash (init) script 101-manage_my_process that manages manage_my_process.
    * When passing the argument start:
        * Starts manage_my_process
        * Creates a file containing its PID in /var/run/my_process.pid
        * Displays manage_my_process started
    * When passing the argument stop:
        * Stops manage_my_process
        * Deletes the file /var/run/my_process.pid
        * Displays manage_my_process stopped
    * When passing the argument restart
        * Stops manage_my_process
        * Deletes the file /var/run/my_process.pid
        * Starts manage_my_process
        * Creates a file containing its PID in /var/run/my_process.pid
        * Displays manage_my_process restarted
* 102-zombie.c - C program that creates 5 zombie processes
* 103-screencast_unix_signal - screencast where you live-code/demo something related to Unix signals.