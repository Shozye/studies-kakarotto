package goals

import game.Player
import game.Game
import heuristics.*
import statistics.*


class HeurMinimaxGoal2(
    weights: List[Double], maximizingPlayer: Player, max_depth: Int, debug: Boolean = false
) extends MinimaxGoal(maximizingPlayer: Player, max_depth: Int) {

    val constantHeuristics: List[Heuristic] = List (
        WinLoseFromFutureHeuristic()
    )

    val constantWeights: List[Double] = List (
        1e8.toInt
    )

    val heuristics: List[Heuristic] = List(
        DifferenceLoseMovesHeuristic(),
        WinningX___PatternHeuristic(),
        WinningXX__PatternHeuristic(),
        WinningX_X_PatternHeuristic(),
        Winning_X__PatternHeuristic(),
        WinningX__XPatternHeuristic(),
        LosingXX_PatternHeuristic(),
        LosingX__PatternHeuristic(),
        Losing_X_PatternHeuristic()
    )

    def calculateFromWeightsHeuristics(_weights: List[Double], _heuristics: List[Heuristic], statistics: Statistics): Double = {
        _weights
            .zip(_heuristics)
            .map(
                (weight, heuristic) => weight * heuristic.getValue(statistics)
            ).sum
    }

    override def calculate(game: Game): Double = 
        val statistics = Statistics.from(game)
        val eval = calculateFromWeightsHeuristics(weights, heuristics, statistics)
        val constantEval = calculateFromWeightsHeuristics(constantWeights, constantHeuristics, statistics)
        if debug then println(s"eval: $eval   constanteval: $constantEval")
        (eval + constantEval) * ( if maximizingPlayer == game.player then 1 else -1 )

        

}
