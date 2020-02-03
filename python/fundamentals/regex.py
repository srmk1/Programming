import re

#https://docs.python.org/2/library/re.html
#Metacharacters
#   .   Matches any single character example:".at" matches cat, sat, mat
#  [ ]  Matches any single character contained within [] example:"[csm]at" matches cat, sat, mat
# [^ ]  Matches a single character NOT contained within [] example:"[^c]at" matches sat, mat but not cat
#  ^    Matches the expression if at the start if the string example:"^.at" matches cat, sat, mat
#  $    Matches the expression if at the end if the string example:".at$" matches cat, sat, mat
# ( )   Contains sub expressions
#  *    Matches preceding element zero or more times example:"c.*" would match any word starting with c

#Python implements search and replace using sub() method, substitute
#sub(pattern,replacement_string,original_file_or_string,max=0)

#re.compile(pattern, flags=0)
#Compile a regular expression pattern into a regular expression object, which can be used for matching using its match() and search() methods, described below.
#The expression’s behaviour can be modified by specifying a flags value. Values can be any of the following variables, combined using bitwise OR (the | operator).
#The sequence
#   prog = re.compile(pattern)
#   result = prog.match(string)
#is equivalent to
#   result = re.match(pattern, string)
#but using re.compile() and saving the resulting regular expression object for reuse 
#is more efficient when the expression will be used several times in a single program.

def Main():

    #base match
    line = "this is the text pattern"

    match_result = re.match('pattern', line, re.M|re.I)
    if match_result:
        print("Match Found: " + match_result.group())
    else:
        print("No Match was found")

    search_result = re.search('pat', line, re.M|re.I)
    if search_result:
        print("Match Found: " + search_result.group())
    else:
        print("No Match was found")


Main()
