exec { 'sed':
  command => '/bin/sed -i 's/phpp/php/' /var/www/html/wp-settings.php'

}
