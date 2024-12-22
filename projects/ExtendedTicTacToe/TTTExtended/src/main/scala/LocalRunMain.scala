import game.{Player, PlayerUtils}
import strategies.{MinimaxABStrategy, RandomLegalStrategy, TTTStrategy, MinimaxABFastStrategy}
import bot.LocalBot
import scala.util.Random

object LocalRunMain {

    def runTests(strategy1: TTTStrategy, strategy2: TTTStrategy, amountGames: Int): Unit = {
        val start = System.currentTimeMillis()

        val results = (0 until amountGames)
            .map(index => {
                val currentTimestamp = System.currentTimeMillis()
                val winner = LocalBot.run(strategy1 = strategy1, strategy2 = strategy2)
                println(s"[$index] winner: $winner in ${System.currentTimeMillis() - currentTimestamp}ms")
                winner
            }
        )
        val interval = System.currentTimeMillis() - start
        println(s"all time: ${interval}ms, ${amountGames/(interval./(1000.0))}g/s")

        val strategy1_wins = results.count(x => x == Player.X)
        println(s"strategy1 wins: $strategy1_wins, strategy2 wins: ${amountGames - strategy1_wins}")

    }


    def runTournament(population: IndexedSeq[Vector[Double]]): Array[Int] = {
        val results = (0 until population.size).map(_ => 0).toArray
        for weights1 <- (0 until population.size)  do {
            for weights2 <- (weights1 + 1 until population.size) do {
                val fighter1_1st = MinimaxABFastStrategy(goals.HeurMinimaxGoal2(population(weights1).toList, Player.X, 4), 4)
                val fighter2_2nd = MinimaxABFastStrategy(goals.HeurMinimaxGoal2(population(weights2).toList, Player.O, 4), 4)
                val winner1 = LocalBot.run(strategy1 = fighter1_1st, strategy2 = fighter2_2nd)

                val fighter1_2nd = MinimaxABFastStrategy(goals.HeurMinimaxGoal2(population(weights1).toList, Player.O, 4), 4)
                val fighter2_1st = MinimaxABFastStrategy(goals.HeurMinimaxGoal2(population(weights2).toList, Player.X, 4), 4)
                val winner2 = LocalBot.run(strategy1 = fighter2_1st, strategy2 = fighter1_2nd)

                winner1 match
                    case Player.X => results(weights1) += 10
                    case Player.O => results(weights2) += 10
                    case Player.NONE => results(weights2) += 1; results(weights1) += 1; 

                winner2 match
                    case Player.X => results(weights2) += 10
                    case Player.O => results(weights1) += 10
                    case Player.NONE => results(weights2) += 1; results(weights1) += 1; 
            }
        }

        results
    }

    def mutate(elems: Vector[Double]): Vector[Double] = {
        elems
            .map(
                elem => elem*(1-(Random.nextDouble()-0.5)/10) + Random.nextDouble() - 0.5
            )
    } 

    def genetyk(): Unit = {
        var population = (0 until 10).map(_ => Vector.from((0 until 9).map(_ => Random.nextDouble()*99 + 1)))
        println(s"Starting population: $population")
        var generation_counter = 0
        while generation_counter < 50 do {          
            val results = runTournament(population)
            val sortedResults = results.toList.zipWithIndex.sortBy(x => x._1)      
            val betterResults = sortedResults.filter(x => x._1 >= sortedResults(sortedResults.size/2)._1)
            val best = betterResults.maxBy(x => x._1)
            println(s"Najlepszy w generacji wtf${generation_counter}wtf: $best, jest to ${population(best._2)}")

            val newPopulationRaw = betterResults.map((power, index) => population(index))
            val newPopulation = newPopulationRaw ++ newPopulationRaw.map(vectordouble => mutate(vectordouble))
            population = newPopulation.toIndexedSeq
            generation_counter += 1
        }
    }

    def main(args: Array[String]): Unit = {
    
        val amountGames = 100
        val strategyBaseStart = MinimaxABFastStrategy(goals.MinimaxGoal(Player.X, 4), 4)
        val strategyBaseEnd = MinimaxABFastStrategy(goals.MinimaxGoal(Player.O, 4), 4)

        val strategyHeur1Start = MinimaxABFastStrategy(goals.HeurMinimaxGoal(List(1), Player.X, 4), 4)
        val strategyHeur1End = MinimaxABFastStrategy(goals.HeurMinimaxGoal(List(1), Player.O, 4), 4)

        val strategyHeur2Start = MinimaxABFastStrategy(goals.HeurMinimaxGoal2(List(1,0.1,1,0.1,1,1,1,0.1,0.1), Player.X, 5), 5)
        val strategyHeur2End = MinimaxABFastStrategy(goals.HeurMinimaxGoal2(List(1,0.1,1,0.1,1,1,1,0.1,0.1), Player.O, 5), 5)

        runTests(
            strategyHeur2Start, 
            strategyHeur2End, 
            amountGames
        )
        

    }

}

