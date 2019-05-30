# comment - serach and replace limit cap
exec { 'sed':
  command => "/bin/sed -i '55,56s/4/15/g' /etc/security/limits.conf"
}

  exec { 'restart':
	command => '/usr/sbin/service nginx restart',
}
