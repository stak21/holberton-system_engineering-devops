# comment - serach and replace limit cap
exec { 'sed':
  command => "/bin/sed -i '/holberton soft/c\holberton soft nofile 20' /etc/security/limits.conf && /bin/sed -i '/holberton hard/c\holberton hard nofile 20' /etc/security/limits.conf",
}
