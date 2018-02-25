import HW5_P1P2 as simcode
import scr.FigureSupport as FigureSupport
import scr.StatisticalClasses as Statistics

PROB_HEAD = 0.5
N_GAMES = 1000

# simulate the designated number of trials
myGame = simcode.SetOfGames(prob_head=PROB_HEAD, n_games=N_GAMES)

# create histogram of rewards
FigureSupport.graph_histogram(
    observations=myGame.get_game_rewards(),
    title='Histogram of rewards',
    x_label='Payout',
    y_label='Count')

# indicate min and max expected reward
myGameStats = Statistics.SummaryStat('1000 games', myGame.get_game_rewards())
print('Maximum Reward: $',myGameStats.get_max())
print('Minimum Reward: $',myGameStats.get_min())

# calculate probability of loss
print('Probability of losing money: ', myGame.get_prob_losing())
