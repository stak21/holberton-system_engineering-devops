#comment - serach and replace limit cap
exec { 'sed':
  command => "/bin/sed -i 's/15/15000/g' /etc/default/nginx && /usr/sbin/service nginx restart",
  }
