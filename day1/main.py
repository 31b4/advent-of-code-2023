
def part1(data):
  res = 0
  for line in data:
    digits = []
    for c in line:
      if c.isdigit():
        digits.append(c)
    res += int(digits[0] + digits[-1])
  return res

def part2(data):
  res = 0
  str_digits = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
  for line in data:
    digits = []
    for i, c in enumerate(line):
      if c.isdigit():
        digits.append(c)
        continue
      for j, digit in enumerate(str_digits):
        if line[i:].startswith(digit):
          digits.append(str(j + 1))
    res += int(digits[0] + digits[-1])
  return res

if __name__ == '__main__':
  data = open('input.txt').read().splitlines()
  print(part1(data))
  print(part2(data))