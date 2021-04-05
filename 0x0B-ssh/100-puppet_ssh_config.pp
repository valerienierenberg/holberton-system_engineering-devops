# Using Puppet, configures SSH config file so that you can connect...
# ...to a server without typing a password.
# SSH client configuration configured to use the private key ~/.ssh/holberton
# SSH client configuration configured to refuse to authenticate using a passwd

file_line { 'holbie private key':
    ensure => present
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'remove pwd authentication':
    ensure => present
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}
