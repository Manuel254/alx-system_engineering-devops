# Kills a process named killmenow
exec { 'killmenow':
  command => '/usr/bin/pkill -9 killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
}
