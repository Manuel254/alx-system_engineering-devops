# Puppet script that replaces a line

file { '/var/www/html/wp-settings.php'
  ensure => present,
}

exec { 'replace_text':
  path    => ['/bin','/usr/bin'],
  command => "sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'",
}
