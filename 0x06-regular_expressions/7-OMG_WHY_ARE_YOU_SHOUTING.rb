#!/usr/bin/env ruby


regex = /[[:upper:]]/

last = ""
arg = ARGV[0]
arg.scan(regex) do |match|
	last += match
end
puts last.to_s
