# Turn off password authentication
exec { 'Turn off passwd auth':
  command => '/bin/sed -i "s/^#?\\s*PasswordAuthentication\\s.*/PasswordAuthentication no/g" /etc/ssh/sshd_config',
  unless  => '/bin/grep -q "^\\s*PasswordAuthentication\\s*no\\s*$" /etc/ssh/sshd_config',
}

# Declare identity file
exec { 'Declare identity file':
  command => '/bin/echo -e "\nIdentityFile /path/to/identity/file" >> /etc/ssh/ssh_config',
  unless  => '/bin/grep -q "^\\s*IdentityFile\\s*/path/to/identity/file\\s*$" /etc/ssh/ssh_config',
}
