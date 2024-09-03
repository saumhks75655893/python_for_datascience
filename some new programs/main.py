from functools import reduce
import pyjokes

jokes = pyjokes.get_joke()
print(jokes)


a = [12,4,4,4,4,65,456]
sum = reduce((lambda x,y: x+y),a)
print(sum)