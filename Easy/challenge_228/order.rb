# See if inputted words are lexicographically in order.

def check_words(arr)
    arr.each do |item|
        jumbled = false
        counter = 0
        print "#{item}"
        while counter < item.length - 1
           if item[counter+1] - item[counter] < 0
               if check_reverse(item)
                   puts " REVERSE ORDER"
               else 
                   puts " NOT IN ORDER"
               end
               jumbled = true
               break
           end
           counter += 1
        end
        if !jumbled
            puts " IN ORDER"
        end
    end
end

def check_reverse(word)
    counter = word.length - 1
    while counter > 0
        if word[counter] - word[counter - 1] > 0
            return false
        end
        counter += -1
    end
    return true
end

def get_words()
    raw = File.open("words.in", "r") { |file| file.read }
    return raw.split("\n")
end

word_arr = get_words()
check_words(word_arr)
