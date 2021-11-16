"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[
                "alex@checkio.org",
                "mike@google.com",
                "lili@apple.com",
            ]],
            "answer": 3,
        },
        {
            "input": [[
                "mi.ke@google.com",
                "alex@checkio.org",
                "mike@google.com",
                "lili@apple.com",
            ]],
            "answer": 3,
        },
        {
            "input": [[
                "alex+home@checkio.org",
                "lili+work@apple.com",
                "alex@checkio.org",
                "lili@apple.com",
            ]],
            "answer": 2,
        },
        {
            "input": [[
                "l.ili+work@apple.com",
                "a.lex@checkio.org",
                "alex+home@checkio.org",
                "lili+work@apple.com",
                "alex@checkio.org",
                "lili@apple.com",
            ]],
            "answer": 2,
        },
        {
            "input": [[
                "Alex@checkIO.org",
                "alex@checkio.org",
                "alex@check.io.org",
            ]],
            "answer": 2,
        },
        {
            "input": [[]],
            "answer": 0,
        },
    ],
    "Extra": [
        {
            "input": [["name.last@domain.com", "namelast+last.name@domain.com", "namelast@domain.com"]],
            "answer": 1,
        },
    ]
}
