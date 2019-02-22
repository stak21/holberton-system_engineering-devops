#!/usr/bin/env ruby


regex = /Holberton/i
arg = ARGV[0]
arg.scan(regex) do |match|
	puts match.to_s
end
