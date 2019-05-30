# comment - serach and replace limit cap
exec { 'sed':
  command => -i 's/15/15000/g' /etc/default/nginx",
}
