# comment - serach and replace limit cap
exec { 'sed':
  command => "/bin/sed -Ei  sed -Ei '/holberton/s/[0-9]+/20/g' /etc/security/limits.conf",
}

exec { 'restart':
  command => '/usr/sbin/service nginx restart',
}
