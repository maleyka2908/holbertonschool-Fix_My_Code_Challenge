#!/usr/bin/ruby

result = []
ARGV.each do |arg|
  next if arg !~ /^-?[0-9]+$/
  result << arg.to_i
end

result.sort.each do |n|
  puts n
end
