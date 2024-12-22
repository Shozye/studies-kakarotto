package goals.heuristics

import goals.statistics.Statistics

final case class DifferenceLoseMovesHeuristic() extends Heuristic {
    def getValue(statistics: Statistics): Int = {
        -1*(statistics.amountLoseTilesCurrent - statistics.amountLoseTilesEnemy)
    }
}
