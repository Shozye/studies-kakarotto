package goals.heuristics

import goals.statistics.Statistics


final case class LosingXX_PatternHeuristic() extends Heuristic {
    def getValue(statistics: Statistics): Int = {
        -statistics.patternInfo.current.typeXX_3
    }
}

final case class LosingX__PatternHeuristic() extends Heuristic {
    def getValue(statistics: Statistics): Int = {
        -statistics.patternInfo.current.typeX__3
    }
}
final case class Losing_X_PatternHeuristic() extends Heuristic {
    def getValue(statistics: Statistics): Int = {
        -statistics.patternInfo.current.type_X_3
    }
}
