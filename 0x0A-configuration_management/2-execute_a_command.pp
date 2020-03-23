# Using Puppet, create a manifest that kills a process named killmenow
exec { 'pkill':
  provider => shell,
  command => 'pkill -f killmenow',
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}
