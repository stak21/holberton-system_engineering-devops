#!/usr/bin/env ruby


regex = /hb[t]{2,5}n/i
arg = ARGV[0]
arg.scan(regex) do |match|
	puts match.to_s
end
