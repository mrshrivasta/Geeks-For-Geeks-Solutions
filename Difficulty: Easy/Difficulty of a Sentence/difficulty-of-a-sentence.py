class Solution:
    def calcDiff(self, s):
        vowels = set('aeiou')
        words = s.lower().split()
        score = 0
        
        for word in words:
            consonant_count = 0
            vowel_count = 0
            max_consecutive_consonants = 0
            current_consecutive = 0
            
            for c in word:
                if c.isalpha():
                    if c in vowels:
                        vowel_count += 1
                        current_consecutive = 0
                    else:
                        consonant_count += 1
                        current_consecutive += 1
                        max_consecutive_consonants = max(max_consecutive_consonants, current_consecutive)
            
            if max_consecutive_consonants >= 4 or consonant_count > vowel_count:
                score += 5
            else:
                score += 3
        
        return score