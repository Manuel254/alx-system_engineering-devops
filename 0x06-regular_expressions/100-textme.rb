#!/usr/bin/env ruby
r1 = /(?<=from:)(\w+|\+\d{11})/
r2 = /(?<=to:)(\w+|\+\d{11})/
r3 = /(?<=flags:)[-?\d:?]{12,14}/

print ARGV[0].scan(r1).join
print ","
print ARGV[0].scan(r2).join
print ","
puts ARGV[0].scan(r3)
