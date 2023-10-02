blank_board = """
  1   2   3
1   |   |  
 --- --- ---
2   |   | 
 --- --- ---
3   |   |  
"""

name   = input("What is your name? ")
print("Welcome to Tic Tac Toe, " + name + ". Here is our playing board:")
print(blank_board)

# tic-tac-toe positions
b = [
  [" "," "," "],
  [" "," "," "],
  [" "," "," "]
]


player = "X"
played = [] #to save already occupied positions

# Loop for each turn
play_on = True
while play_on:
  print("It's " + player + "'s turn")
  position = input("Enter a position (i.e., 1,1): ")
    
  # Check the position is valid
  if len(position) == 3:
    valid = position[0].isnumeric() and position[1] == "," and position[2].isnumeric()
  else:
    print("invalid position")
    continue
  if valid:
    row = int(position[0])
    col = int(position[2])
    if row <= 3 and col <= 3:
      valid = True
    else:
      print("invalid position")
      continue
  else:
    print("invalid position")
    continue
  # Update the correct variable based on the position entered
  if position not in played: #check if the position is already taken
    b[row - 1][col - 1] = player
  else:
      print("already taken position")
      continue
  
  new_board = f"""
    1   2   3
  1 {b[0][0]} | {b[0][1]} | {b[0][2]}
   --- --- ---
  2 {b[1][0]} | {b[1][1]} | {b[1][2]}
   --- --- ---
  3 {b[2][0]} | {b[2][1]} | {b[2][2]}
  """
  
  print(new_board)
  #check the rows
  for i in b:
    if i[0] == i[1] == i[2] == player:
      print('The Winner is ', player)
      play_on = False
    
    
# Check the columns

  for i in range(3):
    if b[0][i] == b[1][i] == b[2][i] == player:
      print('The Winner is ', player)
      play_on = False
  
# Check the diagonals
  if b[0][0] == b[1][1] == b[2][2] == player:
    print('The Winner is ', player)
    play_on = False
  elif b[0][2] == b[1][1] == b[2][0] == player:
    print('The Winner is ', player)
    play_on = False
#check full board
  counter = 0
  for list in b:
    counter += 1
    if list[0] == ' ':
      break
    elif list[1] == ' ':
      break
    elif list[2] == ' ':
      break
    else:
      if counter == 3:
        play_on = False
        print("Game Over. It is a draw!!!")
  
      
          
  # Update Player
  if player == "X":
    player = "O"
  else:
    player = "X"