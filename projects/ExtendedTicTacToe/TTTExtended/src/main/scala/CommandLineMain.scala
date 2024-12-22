import strategies.MinimaxABFastStrategy
import game.{Player, PlayerUtils}

object CommandLineMain {
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
            MinimaxABFastStrategy(goals.HeurMinimaxGoal2(List(1,0.1,1,0.1,1,1,1,0.1,0.1), PlayerUtils.fromInt(player), depth), depth, true)
        )
    }

}


