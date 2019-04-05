# using puppet, kill processes
exec { 'pkill'
  command => '/usr/bin/pkill killmenow'
}

