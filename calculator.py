import sys

def multip(a, b):
  return a * b

def main(a, b):
  result = multip(a, b)
  print(result)
  return result

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]), int(sys.argv[2]))
