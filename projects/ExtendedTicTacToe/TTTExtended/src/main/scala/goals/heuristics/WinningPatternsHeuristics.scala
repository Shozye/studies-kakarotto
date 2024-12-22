package goals.heuristics

import goals.statistics.Statistics


final case class WinningX___PatternHeuristic() extends Heuristic {
    def getValue(statistics: Statistics): Int = {
        statistics.patternInfo.current.typeX___4
    }
}

final case class WinningXX__PatternHeuristic() extends Heuristic {
    def getValue(statistics: Statistics): Int = {
        statistics.patternInfo.current.typeXX__4
    }
}
final case class WinningX_X_PatternHeuristic() extends Heuristic {
    def getValue(statistics: Statistics): Int = {
        statistics.patternInfo.current.typeX_X_4
    }
}
final case class Winning_X__PatternHeuristic() extends Heuristic {
    def getValue(statistics: Statistics): Int = {
        statistics.patternInfo.current.type_X__4
    }
}
final case class WinningX__XPatternHeuristic() extends Heuristic {
    def getValue(statistics: Statistics): Int = {
        statistics.patternInfo.current.typeX__X4
    }
}