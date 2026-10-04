
"""
Regular expression is a way to identify or make my machine adapt to expressions with a certain format

using ======> r"............."


r"@" --> tells to match literal  at sign
r"[a-z]" --> Any Singular character from a to z
r"[a-z]{n}" --> the {n} is a quantifier for how many character to be looking for contiguously in the characters
                from a to z

r"[a-z]+" -->  + == Unbounded Quantifer      1 or MORE from a to z

r"[a-z]*" --> * == Unbounded Quantifer      0 or MORE from a to z

r"[a-z]?" --> ? == Unbounded Quantifer      1 or NONE from a to z

IN REGEX  a dot  .  a wild card that matches any singluar character

Using a backslach we can treat the dot as literal so in regex we can do r"\." <==> "."

in regex r"\w " <==> matches any word

r"sth$" <===> $ means the terms that accept all strings that end with sth

r"^sth" <===> ^ means the terms that accept all strings that start with sth




"""


text = """
FOUND WALLET - turned in March 3, 2026 - call 123-482-1847
Piano lessons - $35.00/hr - starting April 10, 2024
Garage sale - Saturday May 18, 2026 - items from $0.50 to $175.00
For rent: 2BR apt available June 1, 2025 - call 123-903-4621
Tech help - beginner-friendly - $20.00/hr - since January 7, 2026
Babysitter available - from February 14, 2023 - rates from $15.00/hr
"""



import re


"""
Problem 1
Write a regular expression that matches all of the phone numbers in the text.

Each phone number has the format 123-XXX-XXXX — a literal area code 123, a hyphen, three digits, a hyphen, and four digits.

Sample matches: 123-482-1847, 123-903-4621
"""
def match_phone_number(string : str) -> list :

    regex = r"123-[0-9]{3}-[0-9]{4}"

    answer = re.findall(regex, string)
    return answer



"""
Problem 2
Write a regular expression that matches all of the prices in the text.

Each price has the format $X.XX — a dollar sign, one or more digits, a dot, and exactly two digits (e.g. $35.00, $0.50, $175.00).

Sample matches: $35.00, $0.50, $175.00, $20.00, $15.00
"""

def match_price(string : str)-> list :

    expression  = r"\$[0-9]+\.[0-9]+"

    return re.findall(expression , string)

"""

Problem 3
Write a regular expression that matches all of the dates in the text.

Each date has the format Month D, YYYY — a month name, a space, one or two digits for the day, a comma and space, and a four-digit year (e.g. March 3, 2024, April 10, 2024).

Heads up: the word Saturday also matches part of your pattern. That's expected — think about why, and whether the pattern is still correct for the task.

Sample matches: March 3, 2026, April 10, 2024, May 18, 2026, June 1, 2025, January 7, 2026, February 14, 2023
"""

def match_date(string : str)-> list :
    regex = r"[A-Z][a-z]+\s[0-3][0-9],\s[0-9]{4}"

    return re.findall(regex, string)



if  __name__ == "__main__":

    print(
        "All Dates in the text " , match_date(text) ,
        "\nAll Phone Number in the text ", match_phone_number(text) ,
        "\nAll Prices in the text ", match_price(text)
    )


