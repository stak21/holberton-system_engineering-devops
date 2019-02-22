#!/usr/bin/env ruby


regex = /h[b]{0,1}tn/i
arg = ARGV[0]
arg.scan(regex) do |match|
	puts match.to_s
end
