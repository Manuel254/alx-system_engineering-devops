# Makes nginx handle a lot of traffic

exec { 'nginx-requests-limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

exec { 'nginx_restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
