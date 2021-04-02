# 0x0B-ssh

## Learning Objectives
    * What is a server
    * Where servers usually live
    * What is SSH
    * How to create an SSH RSA key pair
    * How to connect to a remote host using an SSH RSA key pair
    * The advantage of using #!/usr/bin/env bash instead of /bin/bash

## File Descriptions

* 0-use_a_private_key - Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.
    * Requirements:
        * Only use ssh single-character flags
        * You cannot use -l
        * You do not need to handle the case of a private key protected by a passphrase
* 1-create_ssh_key_pair - Write a Bash script that creates an RSA key pair.
    * Requirements:
        * Name of the created private key must be holberton
        * Number of bits in the created key to be created 4096
        * The created key must be protected by the passphrase betty
* 2-ssh_config - configures vagrant so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.
    * Requirements:
        * Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
        * Your SSH client configuration must be configured to refuse to authenticate using a password
* (Task 3 of project is) - Add the SSH public key below to your server so that we can connect using the ubuntu user.
* 100-puppet_ssh_config.pp -  sets up your client SSH configuration file so that you can connect to a server without typing a password.
    * Requirements:
    * Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
    * Your SSH client configuration must be configured to refuse to authenticate using a password
