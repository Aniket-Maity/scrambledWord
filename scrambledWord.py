def main():
   
    words = [
            'acceptable',
            'tacit',
            'chunky',
            'racial',
            'difficult',
            'unadvised',
            'spurious',
            'familiar',
            'fuzzy',
            'fast',
            'rightful',
            'disgusted',
            'maker',
            'joyful',
            'data',
            'ambition',
            'windows',
            'pancakes',
            'passion',
            'dedicate'
            ]
   
    new_words = [''.join(sorted(w)) for w in words]
   
    n = int(input())
   
    test_words = []
   
    for _ in range(n):
#        test_words.append(input())
        test_words = input().split(" ")
       
    #    test_words = ['mafriali', 'ticat', 'tyoji']
#        results = []
        for word in test_words:
            if ''.join(sorted(word)) in new_words:
                print("true")
#                results.append("true")
            else:
                print("false")
#                results.append("false")
    #    print("".join(results))
       
if __name__ == "__main__":
    main()