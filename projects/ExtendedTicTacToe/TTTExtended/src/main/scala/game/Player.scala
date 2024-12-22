
package game

enum Player(val name: String) {
  case X extends Player("X")
  case O extends Player("O")
  case NONE extends Player("-")
}

