"""
Medium Translator Lambda Function

Given a word, convert all vowels and Y into the NATO phonetic alphabet

A -> Alpha
E -> Echo
I -> India
O -> Oscar
U -> Uniform
Y -> Yankee

Note that conversion is not case sensitive, also note that consonants do not need to be converted.

Expected input: {"word": "alpha"}
Expected output: {"statusCode": 200, "body": "AlphalphAlpha"}

Expected input: {"word": "harlem"}
Expected output: {"statusCode": 200, "body": "hAlpharlEchom"}
"""
import json

def lambda_handler(event, context=None):

    word = event['word']
    res = []

    if word == None:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: word field does not exist')
        }

    nato_map = {
        "a": "Alpha",
        "e": "Echo",
        "i": "India",
        "o": "Oscar",
        "u": "Uniform",
        "y": "Yankee"
    }

    result = []
    for char in word:
        lower_char = char.lower()
        if lower_char in nato_map:
            result.append(nato_map[lower_char])
        else:
            result.append(char)

    res = "".join(result)

    return {
        'statusCode': 200,
        'body': res
    }
