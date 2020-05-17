def main():
  # print("Keep it logically awesome.")
  import random 
  f = open("/Users/rahuljain/Documents/GitHub/python-random-quote/quotes.txt")
  quotes = f.readlines()
  f.close()
  
  x=len(quotes)
  z=x-1
  y=random.randint(0,z)
  quot= quotes[y]
  print(quot)

if __name__== "__main__":
  main()
