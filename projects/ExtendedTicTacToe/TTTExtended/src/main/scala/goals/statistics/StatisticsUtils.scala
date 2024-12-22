package goals.statistics
import game.{Game, PlayerUtils}
import game.Player
import scala.collection.immutable.ArraySeq
import scala.annotation.tailrec

enum Result {
    case WIN
    case LOSE
    case NONE
    case NOT_POSSIBLE
}

object StatisticsUtils {
  def getAmountWinLose(game: Game, player: Player):(Int, Int) = {
        val terminals = 
            for move <- game.children() yield {
                game.makeMove(move)
                val terminal = game.isTerminalBest(move)
                game.removeMove(move)
                terminal
            }
        val amountWin = terminals.count(p => p == player)
        val amountLose = terminals.length - amountWin - terminals.count(p => p == Player.NONE)
        (amountWin,amountLose)
    }

    def getWinLoseTable(game: Game): ArraySeq[(Result, Result)] = {
        val winLoseTable = (0 until 25).map(_=>(Result.NOT_POSSIBLE, Result.NOT_POSSIBLE)).toArray
        
        for move <- game.children() yield {
            game.makeMove(move)
            val terminal = game.isTerminalBest(move)
            game.removeMove(move)
            winLoseTable(move) = 
                ((if terminal == game.player then Result.WIN 
                else if terminal == Player.NONE then Result.NONE 
                else Result.LOSE), winLoseTable(move)(1))
        }
        game.swapPlayer()
        for move <- game.children() yield {
            game.makeMove(move)
            val terminal = game.isTerminalBest(move)
            game.removeMove(move)
            winLoseTable(move) = 
                (winLoseTable(move)(0),(if terminal == game.player then Result.WIN 
                else if terminal == Player.NONE then Result.NONE 
                else Result.LOSE))
        }
        game.swapPlayer()
        ArraySeq.from(winLoseTable)
    }




    def getBigPatternInfo(game: Game): BigPatternInfo = {
        val bigPatternInfo = BigPatternInfo()
        for {
            winstate <- Game.winStatesInt
        } do {
            val newwinstate = (
                game.get(winstate(0)),
                game.get(winstate(1)),
                game.get(winstate(2)),
                game.get(winstate(3))
            )
            val A = game.player
            val B = PlayerUtils.opposite(game.player)
            val N = Player.NONE
            
            newwinstate match {
                case (A, N, N, A) =>  bigPatternInfo.current.typeX__X4 += 1
                case (B, N, N, B) =>  bigPatternInfo.enemy.typeX__X4 += 1

                case (A, A, N, N) | (N, N, A, A) => bigPatternInfo.current.typeXX__4 += 1
                case (B, B, N, N) | (N, N, B, B) => bigPatternInfo.enemy.typeXX__4 += 1

                case (A, N, A, N) | (N, A, N, A) => bigPatternInfo.current.typeX_X_4 += 1
                case (B, N, B, N) | (N, B, N, B) => bigPatternInfo.enemy.typeX_X_4 += 1

                case (A, N, N, N) | (N, N, N, A) => bigPatternInfo.current.typeX___4 += 1
                case (B, N, N, N) | (N, N, N, B) => bigPatternInfo.enemy.typeX___4 += 1

                case (N, A, N, N) | (N, N, A, N) => bigPatternInfo.current.type_X__4 += 1
                case (N, B, N, N) | (N, N, B, N) => bigPatternInfo.enemy.type_X__4 += 1

                case (A, A, N, A) | (A, N, A, A) => bigPatternInfo.current.typeXX_X4 += 1
                case (B, B, N, B) | (B, N, B, B) => bigPatternInfo.enemy.typeXX_X4 += 1

                case (_, _, _ ,_) => 
            }
        }

        for {
            loseState <- Game.loseStatesInt
        } do {
            val newlosestate = (
                game.get(loseState(0)),
                game.get(loseState(1)),
                game.get(loseState(2))
            )
            val A = game.player
            val B = PlayerUtils.opposite(game.player)
            val N = Player.NONE
            
            newlosestate match {
                case (A, N, N) | (N, N, A) =>  bigPatternInfo.current.typeX__3 += 1
                case (B, N, N) | (N, N, B) =>  bigPatternInfo.enemy.typeX__3 += 1
                
                case (A, A, N) | (N, A, A) => bigPatternInfo.current.typeXX_3 += 1
                case (B, B, N) | (N, B, B) => bigPatternInfo.enemy.typeXX_3 += 1

                case (N, A, N)  => bigPatternInfo.current.type_X_3 += 1
                case (N, B, N)  => bigPatternInfo.enemy.type_X_3 += 1

                case (_, _, _) => 
            }
        }

        bigPatternInfo
    }
}
