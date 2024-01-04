
# Valid Anagram 
class Anagram(object):
    def anagramm(self, s, t):
        self.s = s
        self.t = t
        
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) #if key is not present
        print(countS.get(s[i])) 
        print(s[i])
    
anagram = Anagram()
anagram.anagramm('anagram', 'nagaram')

#Group Anagram

