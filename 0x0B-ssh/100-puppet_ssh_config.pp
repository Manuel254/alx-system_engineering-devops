# Puppet file to make configurations to the SSH client configuration

file_line { 'key':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#?\\s*IdentityFile\\s+',
  require => Package['openssh-client'],
  notify  => Service['ssh'],
}

file_line { 'password':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^#?\\s*PasswordAuthentication\\s+',
  require => Package['openssh-client'],
  notify  => Service['ssh'],
}
