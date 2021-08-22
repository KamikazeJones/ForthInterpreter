import sys



class Tokenizer:
  
  def __init__(self):
    pass

  def start(self):
    return self.getKey()

  def isEOF(self):
    return self.ch == ''

  def isEnter(self):
    return self.ch == '\n'

  def isTab(self):
    return self.ch == '\t'

  def isSpace(self):
    return self.ch == ' '


  def isWhiteSpace(self):
    return self.isSpace() or self.isTab() or self.isEnter()     

  def getKey(self):
    self.ch = sys.stdin.read(1)
    # print(ord(self.ch))
    # print(self.isWhiteSpace())
    return self.ch

  def getWord(self):
    # A first character must have already been read.
    self.word = ''
    while not self.isEOF() and self.isWhiteSpace():
      self.getKey()

    while not self.isEOF() and not self.isWhiteSpace():
      self.word += self.ch
      self.getKey()

    return self.word

class Forth:

  def __init__(self):
      # Mapping from names to functions
      self.words = dict()
      self.tokenizer = Tokenizer() 

  def outer_interpreter(self):
    return True 

def test():
  testKey()
  testWord()

def testKey():
    print("-- testKey --")
    f = Forth()
    ch = f.tokenizer.start()
    while not f.tokenizer.isEOF():
      print(ch, end='');
      ch=f.tokenizer.getKey()

def testWord():
    print("-- testWord --")
    f = Forth()
    f.tokenizer.start()
    while not f.tokenizer.isEOF():
      word = f.tokenizer.getWord()
      print(word);

if __name__ == "__main__":
  test()