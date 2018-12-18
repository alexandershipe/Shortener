######## Shortener

# Given two strings s, t, determine if string s can be changed into string t using the following rule:

# Remove any number of lowercase letters from s (or none at all), then capitalize all remaining letters of s.

# Example of the rule:
# s = AAbcD
# Possible outputs using the rule:
# Remove none, capitalize -> AABCD
# Remove c, capitalize -> AABD
# Remove b, capitalize -> AACD
# Remove b and c, capitalize -> AAD

# If it is possible to create the string t by processing s using the rule, then the function should return True, otherwise return False.

def shortener(s, t):

    # The amount of chars in s
    s_size = len(s)
    # The amount of chars in t
    t_size = len(t)

    # If t is larger than s the rule will always fail
    if t_size > s_size:
        return False

    # Current t index for comparison initialized to zero
    t_index = 0

    # Loop through all the chars in the s string to compare to t string
    for s_index in range(s_size):

        # If finished checking all t chars and there are still uppercase s chars left then false
        if t_index >= t_size:
            if s[s_index].isupper() == True:
                return False
        else:
            # Check if t has a lowercase character. If it does, function automatically is false because of rule.
            if t[t_index].islower() == True:
                return False
            # Check if s char matches t char with either case
            if (s[s_index] == t[t_index]) or (s[s_index].upper() == t[t_index]):
                t_index = t_index+1
            # If s char doesn't match and s char is uppercase, the function is false since you can't get rid of it.
            elif s[s_index].isupper() == True:
                return False
    # If all s and t values were checked and rule doesn't fail, the function is true
    if t_index >= t_size:
        return True

    return False

# Test Cases
test_cases = [
    ("daBccd", "ABC", True),
    ("sYOCa", "YOCN", False),
    ("aaaaaa", "AAAAAAA", False),
    ("SVAHHHMVIIDYIcOSHMDUAVJRIBxBZQSUBIVEBHfVTZVSHATUYDJGDRRUBQFHEEEUZLQGXTNKFWUYBAeFKUHSFLZEUINBZYRIXOPYYXAEZZWELUPIEIWGZHEIYIROLQLAVHhMKRDSOQTJYYLTCTSIXIDAnPIHNXENWFFZFJASRZRDAPVYPAViVBLVGRHObnwlcyprcfhdpfjkyvgyzpovsgvlqbhtwrucvszaqinbgeafuswkjrcexvyzq","SVAHHHMVIIDYIOSHMDUAVJRIBBZQSUBIVEBHVTZVSHATUYDJGDRRUBQFHEEEUZLQGXTNKFWUYBAFKUHSFLZEUINBZYRIXOPYYXAEZZWELUPIEIWGZHEIYIROLQLAVHMKRDSOQTJYYLTCTSIXIDAPIHNXENWFFZFJASRZRDAPVYPAVVBLVGRHO", True),
    ("a", "AA", False),("UZJMUCYHpfeoqrqeodznwkxfqvzktyomkrVyzgtorqefcmffauqhufkpptaupcpxguscmsbvolhorxnjrheqhxlgukjmgncwyastmtgnwhrvvfgbhybeicaudklkyrwvghpxbtpyqioouttqqrdhbinvbywkjwjkdiynvultxxxmwxztglbqitxmcgiusfewmsvxchkryzxipbmgrnqhfmlghomfbsKjglimxuobomfwutwfcmklzcphbbfohnaxgbaqbgocghaaizyhlctupndmlhwwlxxvighhjjrctcjBvxtagxbhrbrWwsyiiyebdgyfrlztoycxpjcvmzdvfeYqaxitkfkkxwybydcwsbdiovrqwkwzbgammwslwmdesygopzndedsbdixvi","UZJMUCYH", False)
]

for case in test_cases:
    s, t, output = case
    print(shortener(s, t) == output)
