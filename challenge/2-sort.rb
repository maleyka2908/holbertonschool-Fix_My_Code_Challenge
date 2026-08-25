#!/usr/bin/env ruby

results = ARGV.map { |arg| arg }

sorted_results = results.sort do |a, b|
  a_is_int = a =~ /\A-?\d+\z/
  b_is_int = b =~ /\A-?\d+\z/

  if a_is_int && b_is_int
    a.to_i <=> b.to_i
  elsif a_is_int
    -1
  elsif b_is_int
    1
  else
    a <=> b
  end
end

puts sorted_results.join(' ')
