import urllib.request
import re

def GetWordsCount (url:str):
  #res = urllib.request.urlretrieve(url, 'File.txt') 
  data = urllib.request.urlopen(url)
  data = data.read().decode("utf-8").lower().replace("\'", "")
  word = re.search('(\w+(?:-\w+)+|\w+)', data)
  while word:
      yield [word.group(0), len(re.findall(r'\b'+word.group(0)+r'\b', data))]
      data = re.sub(r'\b'+word.group(0)+r'\b', '', data)
      word = re.search('(\w+(?:-\w+)+|\w+)', data)

if __name__ == "__main__":
  words = GetWordsCount("https://raw.githubusercontent.com/dscape/spell/master/test/resources/big.txt")
  data = [word for word in words]
  print(data)
