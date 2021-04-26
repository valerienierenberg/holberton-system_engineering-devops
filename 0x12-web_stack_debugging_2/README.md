# 0x12-web_stack_debugging_2

## Learning Objectives
- Web stack debugging
- User privileges
- Running commands as another user


## File Descriptions
- 0-iamsomeoneelse:
    - write a Bash script that accepts one argument
    - the script should run the whoami command under the user passed as an argument
- 1-run_nginx_as_nginx:
    - nginx must be running as nginx user
    - nginx must be listening on all active IPs on port 8080
    - You cannot use apt-get remove
    - Write a Bash script that configures the container to fit the above requirements
- 100-fix_in_7_lines_or_less:
    - Using what you did for task #1, make your fix short and sweet.
    - Requirements:
        - Your Bash script must be 7 lines long or less
        - There must be a new line at the end of the file
        - You respect Bash script requirements
        - You cannot use ;
        - You cannot use &&
        - You cannot use wget
        - You cannot execute your previous answer file (Do not include the name of the previous script in this one)
