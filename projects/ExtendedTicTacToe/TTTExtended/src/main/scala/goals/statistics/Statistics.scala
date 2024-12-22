package goals.statistics
import game.{Game, PlayerUtils}
import game.Player
import StatisticsUtils.*
import scala.collection.immutable.ArraySeq

case class Statistics(
    amountFreeTiles: Int = 0,
    amountWinTilesCurrent: Int = 0,
    amountLoseTilesCurrent: Int = 0,
    amountWinTilesEnemy: Int = 0,
    amountLoseTilesEnemy: Int = 0,
    amountCurrentLoseEnemyWinTile: Int = 0,
    winLoseFutureTable: ArraySeq[(Result, Result)] = ArraySeq(),
    patternInfo: BigPatternInfo = BigPatternInfo()
)

object Statistics {
    def from(game: Game): Statistics = {

        val winLoseFutureTable = StatisticsUtils.getWinLoseTable(game)
        val patternInfo = StatisticsUtils.getBigPatternInfo(game)
        val amountWinTilesCurrent = winLoseFutureTable.count((result, _) => result == Result.WIN)
        val amountLoseTilesCurrent = winLoseFutureTable.count((result, _) => result == Result.LOSE)
        val amountWinTilesEnemy = winLoseFutureTable.count((_, result) => result == Result.WIN)
        val amountLoseTilesEnemy = winLoseFutureTable.count((_, result) => result == Result.LOSE)
        val amountCurrentLoseEnemyWinTile = winLoseFutureTable.count((result1, result2) => result1 == Result.LOSE && result2 == Result.WIN)
        
        Statistics(
            amountFreeTiles = 25 - game.amountMoves,
            amountWinTilesCurrent = amountWinTilesCurrent,
            amountLoseTilesCurrent = amountLoseTilesCurrent,
            amountWinTilesEnemy = amountWinTilesEnemy,
            amountLoseTilesEnemy = amountLoseTilesEnemy,
            amountCurrentLoseEnemyWinTile = amountCurrentLoseEnemyWinTile,
            winLoseFutureTable = winLoseFutureTable,
            patternInfo = patternInfo
        )
    }
}
