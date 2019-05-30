# comment - serach and replace limit cap
exec { 'sed':
  command => "/bin/sed -i 's/.*holberton soft.*/holberton soft nofile 20/' /etc/security/limits.conf && /bin/sed -i 's/.*holberton hard.*/holberton hard nofile 20/' /etc/security/limits.conf && /usr/sbin/service nginx restart",
}
