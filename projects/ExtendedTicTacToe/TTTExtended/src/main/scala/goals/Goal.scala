
package goals

import game.{Game, Player}

trait Goal {
  def calculate(game: Game): Double
  def calculateTerminal(winner: Player, depth: Int): Int
  def evaluateDraw(): Int = 0
}
