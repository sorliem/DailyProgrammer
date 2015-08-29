# Divisible by 7 challenge

def isDivisible(num)
    return num % 7 == 0
end

def reverseInt(num)
    return num.to_s.split("").reverse.join.to_i
end

def main(lim)
    total = 0
    (0..lim).step(7) do |num|
       if isDivisible(reverseInt(num))
           # puts num
           total += num
       end
    end
    puts "total = #{total}"
end


# invoke stuff
# puts isDivisible(18)
upperLimit = 10000000

main(upperLimit)
