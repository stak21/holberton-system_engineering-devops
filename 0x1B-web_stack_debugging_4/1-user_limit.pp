
# comment - serach and replace limit cap
exec { 'sed':
  command => -i '/holberton soft/c\holberton soft nofile 20' /etc/security/limits.conf,
  command => -i '/holberton hard/c\holberton hard nofile 20' /etc/security/limits.conf,
}
