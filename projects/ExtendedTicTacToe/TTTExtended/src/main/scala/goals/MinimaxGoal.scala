
package goals

import game.{Game, Player}

class MinimaxGoal(maximizingPlayer: Player, max_depth: Int) extends Goal {
  def calculate(game: Game): Double = 0

  def calculateTerminal(winner: Player, depth: Int): Int = 
   (2137_000_000 + 1_000*(depth) + (max_depth - depth)) * (if (maximizingPlayer == winner) 1 else -1)
}
