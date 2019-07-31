from investment_machine import InvestmentMachine

my_investment_machines = InvestmentMachine()
import numpy as np

y = 1  # y is the amount to invest
n = 10  # n is the number of instances

totalmoneylist = []
gains = []


def machine50percent():
	# a list where i add all the winnings and losings
	global totalmoneylist
	global gains
	totalmoney = 100  # starting money

	win_count1 = 0
	win_count2 = 0
	instancecount = 0
	total_reward_machine_x = 0
	totalreward = 0
	for times_machine_x in range(5):
		total_reward_machine_x = (my_investment_machines.invest(1, y) - 1)  # -1 is for te cost of investment
		if total_reward_machine_x > 0:
			win_count1 += 1
		instancecount += 1
		totalmoney += total_reward_machine_x
		gains.append(totalmoney - 100)
		total_reward_machine_x = 0  # reset rewards
	if win_count1 >= 0.5:
		m = 1
	else:
		for times_machine_x in range(5):
			total_reward_machine_x = (my_investment_machines.invest(2, y) - 1)
			if total_reward_machine_x > 0:
				win_count2 += 1
			instancecount += 1
			totalmoney += total_reward_machine_x
			gains.append(totalmoney - 100)
			total_reward_machine_x = 0  # reset rewards

		if win_count1 > win_count2:
			m = 1
		else:
			m = 2
	while instancecount < 30:
		u = 40  # by how much the totalmoney will be divided
		if win_count1/instancecount > win_count2/instancecount: 
			for times_machine_x in range(1):
				b = (totalmoney // u)  # just an invariable placeholder making sure the flooring doesn't remove $ 1
				totalmoney -= (totalmoney // u)  # removing investment amount
				total_reward_machine_x = my_investment_machines.invest(1, b)
				totalmoney += total_reward_machine_x
				gains.append(totalmoney - 100)
				if total_reward_machine_x > 0:
					win_count1 += 1
		else:
			for times_machine_x in range(1):
				b = (totalmoney // u)  # just an invariable placeholder making sure the flooring doesn't remove $ 1
				totalmoney -= (totalmoney // u)  # removing investment amount
				total_reward_machine_x = my_investment_machines.invest(2, b)
				totalmoney += total_reward_machine_x
				gains.append(totalmoney - 100)
				if total_reward_machine_x > 0:
					win_count2 += 1
		instancecount += 1
	totalmoneylist.append(totalmoney)


def main():
	gcounter = 1

	while gcounter <= 100000:
		machine50percent()

		gcounter += 1


main()

print("average profit is", (sum(totalmoneylist) / (len(totalmoneylist))) - 100)

print("average standard deviation is", ((np.std(totalmoneylist))))

print("average sharpe ratio is", ((sum(totalmoneylist) / (len(totalmoneylist))) - 100) / (np.std(totalmoneylist) + 1))

print(totalmoneylist)
