#!/usr/bin/env ruby

# Collect all arguments
results = ARGV.map { |arg| arg }

# Sort arguments: integers numerically, others lexicographically
sorted_results = results.sort do |a, b|
  # Check if both can be converted to integers
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

sorted_results.each do |result|
  puts result
end
