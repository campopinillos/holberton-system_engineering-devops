# Using Puppet, create a manifest that kills a process named killmenow
exec { 'pkill -x killmenow':
  command => 'pkill -x killmenow',
  path    => '/usr/bin/',
}
