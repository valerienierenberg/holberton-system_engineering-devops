# Using Puppet, creates a manifest that kills a process named killmenow.
# Must use the exec Puppet resource
# Must use pkill

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/'
}
