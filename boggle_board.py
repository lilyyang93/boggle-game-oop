import random
class BoggleBoard:
  def __init__(self):
    print('____\n____\n____\n____')
  
  def shake():
    board = ''
    length = 0
    boggle_dice = ['AAEEGN'],['ELRTTY'],['AOOTTW'],['ABBJOO'],['EHRTVW'],['CIMOTU'],['DISTTY'],['EIOSST'],['DELRVY'],['ACHOPS'],['HIMNQU'],['EEINSU'],['EEGHNW'],['AFFKPS'],['HLNNRZ'],['DEILRX']

    while(length < 16):
      for dice in boggle_dice:
        for letter in dice:
          l = random.choice(letter)
          if l == 'Q':
            board += 'Qu '
            length += 1
          else:
            board += l + '  '
            length += 1
        if length == 4 or length == 8 or length == 12:
          board += '\n'
    return board
print(BoggleBoard.shake())
