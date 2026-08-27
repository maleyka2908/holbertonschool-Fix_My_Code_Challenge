#!/usr/bin/env ruby

results = ARGV.map do |arg|
  if arg =~ /\A-?\d+\z/
    arg.to_i
  else
    arg
  end
end.sort_by { |x| [x.is_a?(String) ? 1 : 0, x] }

puts results
