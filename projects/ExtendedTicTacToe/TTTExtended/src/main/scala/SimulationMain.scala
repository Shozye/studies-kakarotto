import game.{Player, PlayerUtils}
import strategies.{MinimaxABStrategy, RandomLegalStrategy, TTTStrategy}

object SimulationMain {
  private def getStrategy(args: Array[String], player: Player, start_depth: Int): TTTStrategy = {
    args(0) match {
      case "random-legal" => RandomLegalStrategy()
      case "minimax" =>
        MinimaxABStrategy(goals.MinimaxGoal(player, start_depth), start_depth, true)
      case "onemove" =>
        MinimaxABStrategy(goals.HeurMinimaxGoal(List(), player, start_depth), start_depth, true)
    }
  }

  def main(args: Array[String]): Unit = {
    val ip = args(0)
    val port = args(1).toInt
    val player = args(2).toInt
    val depth = args(3).toInt

    Runner.runSingleBot(
      ip,
      port,
      player,
      depth,
      getStrategy(
        args.slice(4, args.length),
        PlayerUtils.fromInt(player),
        depth
      )
    )
  }

}
