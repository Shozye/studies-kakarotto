package goals.heuristics

import goals.statistics.Statistics

final case class WinLoseFromFutureHeuristic() extends Heuristic {
    def getValue(statistics: Statistics): Int = {
        if(statistics.amountWinTilesCurrent >= 1) then 1
        else if(statistics.amountCurrentLoseEnemyWinTile >= 1) {-1}
        else if(statistics.amountWinTilesEnemy >= 2) {-1}
        else if(statistics.amountLoseTilesCurrent == statistics.amountFreeTiles) {-1}
        else if(statistics.amountLoseTilesEnemy == statistics.amountFreeTiles) {1}
        else 0
    }
}
